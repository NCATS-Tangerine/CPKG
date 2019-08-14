import os

from json import load

from rdflib import URIRef

from fhirclient.models.clinicalprofile import ClinicalProfile
from fhirclient.models.coding import Coding

from kgmodel.clinicalprofiles import LabToLabCorrelation

cwd = os.path.dirname(__file__)
fname = os.path.abspath(os.path.join(cwd, 'data', 'Clinical Profiles Examples', 'jh-labs-type-I-diabetes-All-All-All.json'))
with open(fname) as f:
    cprof = load(f)

def uri_for(code: Coding) -> URIRef:
    return code.system + ('' if code.system.endswith('#') or code.system.endswith('/') else '/') + code.code


p = ClinicalProfile(jsondict=cprof)

population = p.population.identifier
for lab in p.lab:
    lab_code = uri_for(lab.code[0].coding[0])
    if lab.scalarDistribution.correlatedLabs:
        for correlated_lab in lab.scalarDistribution.correlatedLabs.entry:
            print(f"LabToLabCorrelation({lab_code} {uri_for(correlated_lab.labcode[0].coding[0])}, coefficient={correlated_lab.coefficient}")
    if lab.scalarDistribution.correlatedMedications:
        for correlated_med in lab.scalarDistribution.correlatedMedications.entry:
            for med in correlated_med.meds:
                med_code = uri_for(med.medicationCodeableConcept.coding[0])
                print(f"{lab_code} {med_code} {correlated_med.coefficient}")


