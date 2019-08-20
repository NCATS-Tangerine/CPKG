import os
import pathlib
import sys
from json import load
from typing import List, Dict, Type, Optional

from biolink.model import Association, NamedThing
from biolinkml.utils.yamlutils import YAMLRoot, as_rdf
from jsonasobj import as_json
from rdflib import Namespace, Graph, URIRef

from fhirclient.models.clinicalprofile import ClinicalProfile
from fhirclient.models.coding import Coding
from fhirterminologyserver.LOINCServer import LOINCServer, prefname
from kgmodel.clinicalprofiles import LabToLabCorrelation, LabToMedicationCorrelation, EntityToEntityCorrelation, \
    LaboratoryTest, Medication

# Constant that identifies the base URI of the Resource.  Note that this is NOT how FHIR should work in the long term
# The ID of a Group resource is not necessarily the name of the server that dispenses it
ATTR_BASE = Namespace("http://hapi.clinicalprofiles.org/baseR4/")

cwd = os.path.dirname(__file__)
context_jsonld = pathlib.Path(os.path.abspath(os.path.join(cwd, '..', 'kgmodel', 'context.jsonld'))).as_uri()

fname = os.path.abspath(os.path.join(cwd, 'data', 'Clinical Profiles Examples', 'jh-labs-type-I-diabetes-All-All-All.json'))
with open(fname) as f:
    cprof = load(f)


entityGraph: Dict[str, NamedThing] = {}
assocGraph: List[Association] = []
termserver = LOINCServer(user='hsolbrig', password='instill-geminate-tehran', show_urls=True)
if not termserver:
    print(f"Unable to connect to LOINC terminology server", file=sys.stderr)
    sys.exit(1)


def uri_for(code: Coding, typ: Type[NamedThing]) -> str:
    """ Synthesize a URI for a Coding entry and add an entry to tne entity list if necessary """
    # TODO: Determine how to make this work with SNOMED and other non-concatenation URIs
    code_uri = code.system + ('' if code.system.endswith('#') or code.system.endswith('/') else '/') + code.code
    if code_uri not in entityGraph:
        entityGraph[code_uri] = typ(id=code_uri, name=prefname(code, termserver), category=[str(typ.class_class_uri)])
    return code_uri


def add_attribution(assoc: EntityToEntityCorrelation, prof: ClinicalProfile) -> EntityToEntityCorrelation:
    assoc.population = ATTR_BASE(prof.population)
    assoc.cohort = ATTR_BASE(prof.cohort)
    return assoc


def add_to_graph(e: YAMLRoot, g: Optional[Graph] = None) -> Graph:
    return as_rdf(e, context_jsonld, g)


p = ClinicalProfile(jsondict=cprof)


# Generate
population = p.population.identifier
for lab in p.lab[0:4]:
    lab_code = uri_for(lab.code[0].coding[0], LaboratoryTest)
    if lab.scalarDistribution.correlatedLabs:
        for correlated_lab in lab.scalarDistribution.correlatedLabs.entry:
            clab_code = uri_for(correlated_lab.labcode[0].coding[0], LaboratoryTest)
            assocGraph.append(LabToLabCorrelation(subject=lab_code,
                                                  object=clab_code,
                                                  correlation_coefficient=correlated_lab.coefficient))
    if lab.scalarDistribution.correlatedMedications:
        for correlated_med in lab.scalarDistribution.correlatedMedications.entry[0:4]:
            for med in correlated_med.meds:
                med_code = uri_for(med.medicationCodeableConcept.coding[0], Medication)
                assocGraph.append(LabToMedicationCorrelation(subject=lab_code,
                                                             object=med_code,
                                                             correlation_coefficient=correlated_med.coefficient))


g = Graph()
for e in entityGraph.values():
    add_to_graph(e, g)
for e in assocGraph:
    add_to_graph(e, g)

print(g.serialize(format="turtle").decode())


