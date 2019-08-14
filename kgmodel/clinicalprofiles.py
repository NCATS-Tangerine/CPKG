# Auto generated from clinicalprofiles.yaml by pythongen.py version: 0.2.1
# Generation date: 2019-08-14 13:35
# Schema: ClinicalProfile Biolink Model extensions
#
# id: http://clinicalprofiles.org/biolink/extension
# description: Biolink model extensions for the ClinicalProfile knowledge graphs
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolink.model import Association, AssociationId, ChemicalSubstance, ChemicalSubstanceId, ClinicalIntervention, ClinicalInterventionId, DiseaseOrPhenotypicFeatureId, DrugId, GenomicEntityId, IdentifierType, IriType, LabelType, MolecularEntityId, NamedThingId, NarrativeText, OccurrentId, OntologyClassId, OrganismTaxonId, Phenomenon, PhenomenonId, PhenotypicFeatureId, Procedure, ProcedureId, ProviderId, PublicationId, TranscriptId
from biolinkml.utils.metamodelcore import Bool, URI
from includes.types import Boolean, Float, String, Uri

metamodel_version = "1.4.0"


# Namespaces
BFO = Namespace('http://purl.obolibrary.org/obo/BFO_')
CHEBI = Namespace('http://purl.obolibrary.org/obo/CHEBI_')
CHEMBL_COMPOUND = Namespace('http://identifiers.org/chembl.compound/')
CHEMBL_TARGET = Namespace('http://identifiers.org/chembl.target/')
CIO = Namespace('http://purl.obolibrary.org/obo/CIO_')
CIVIC = Namespace('http://example.org/UNKNOWN/CIViC/')
CL = Namespace('http://purl.obolibrary.org/obo/CL_')
CLO = Namespace('http://purl.obolibrary.org/obo/CLO_')
CLINVAR = Namespace('http://www.ncbi.nlm.nih.gov/clinvar/')
ECO = Namespace('http://purl.obolibrary.org/obo/ECO_')
ECTO = Namespace('http://example.org/UNKNOWN/ECTO/')
ENSEMBL = Namespace('http://ensembl.org/id/')
FAO = Namespace('http://purl.obolibrary.org/obo/FAO_')
GENO = Namespace('http://purl.obolibrary.org/obo/GENO_')
GO = Namespace('http://purl.obolibrary.org/obo/GO_')
HANCESTRO = Namespace('http://example.org/UNKNOWN/HANCESTRO/')
HGNC = Namespace('http://www.genenames.org/cgi-bin/gene_symbol_report?hgnc_id=')
HP = Namespace('http://purl.obolibrary.org/obo/HP_')
IAO = Namespace('http://purl.obolibrary.org/obo/IAO_')
INTACT = Namespace('http://example.org/UNKNOWN/IntAct/')
MGI = Namespace('http://www.informatics.jax.org/accession/MGI:')
MIR = Namespace('http://identifiers.org/mir/')
MONDO = Namespace('http://purl.obolibrary.org/obo/MONDO_')
NCBIGENE = Namespace('http://www.ncbi.nlm.nih.gov/gene/')
NCIT = Namespace('http://purl.obolibrary.org/obo/NCIT_')
OBAN = Namespace('http://purl.org/oban/')
OGMS = Namespace('http://purl.obolibrary.org/obo/OGMS_')
PANTHER = Namespace('http://www.pantherdb.org/panther/family.do?clsAccession=')
PMID = Namespace('http://www.ncbi.nlm.nih.gov/pubmed/')
PO = Namespace('http://purl.obolibrary.org/obo/PO_')
PR = Namespace('http://purl.obolibrary.org/obo/PR_')
PW = Namespace('http://purl.obolibrary.org/obo/PW_')
POMBASE = Namespace('https://www.pombase.org/spombe/result/')
RNACENTRAL = Namespace('http://example.org/UNKNOWN/RNAcentral/')
RO = Namespace('http://purl.obolibrary.org/obo/RO_')
REACTOME = Namespace('http://example.org/UNKNOWN/Reactome/')
SEMMEDDB = Namespace('http://example.org/UNKNOWN/SEMMEDDB/')
SGD = Namespace('https://www.yeastgenome.org/locus/')
SIO = Namespace('http://semanticscience.org/resource/SIO_')
SO = Namespace('http://purl.obolibrary.org/obo/SO_')
UBERON = Namespace('http://purl.obolibrary.org/obo/UBERON_')
UMLSSC = Namespace('https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/TUI/')
UMLSSG = Namespace('https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/GROUP/')
UMLSST = Namespace('https://uts-ws.nlm.nih.gov/rest/semantic-network/semantic-network/current/STY/')
UO = Namespace('http://purl.obolibrary.org/obo/UO_')
UPHENO = Namespace('http://purl.obolibrary.org/obo/UPHENO_')
UNIPROTKB = Namespace('http://identifiers.org/uniprot/')
VMC = Namespace('http://example.org/UNKNOWN/VMC/')
WB = Namespace('http://identifiers.org/wb/')
WD = Namespace('http://example.org/UNKNOWN/WD/')
ZFIN = Namespace('http://zfin.org/')
BIOLINK = Namespace('https://w3id.org/biolink/vocab/')
DCTERMS = Namespace('http://purl.org/dc/terms/')
DICTYBASE = Namespace('http://dictybase.org/gene/')
FALDO = Namespace('http://biohackathon.org/resource/faldo#')
OBAN = Namespace('http://example.org/UNKNOWN/oban/')
OWL = Namespace('http://www.w3.org/2002/07/owl#')
PAV = Namespace('http://purl.org/pav/')
RDF = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = Namespace('http://www.w3.org/2000/01/rdf-schema#')
SHEX = Namespace('http://www.w3.org/ns/shex#')
SKOS = Namespace('https://www.w3.org/TR/skos-reference/#')
WGS = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BIOLINK


# Types

# Class references
class LaboratoryResultId(PhenomenonId):
    pass


class LaboratoryTestId(ProcedureId):
    pass


class MedicationId(ClinicalInterventionId):
    pass


class MedicineId(ChemicalSubstanceId):
    pass


class LabToLabCorrelationId(AssociationId):
    pass


@dataclass
class LaboratoryResult(Phenomenon):
    """
    The result of a clinical laboratory test performed on a patient
    """
    _inherited_slots: ClassVar[List[str]] = ["correlation", "related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes", "lab_has_correlated_lab"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.LaboratoryResult
    class_class_curie: ClassVar[str] = "biolink:LaboratoryResult"
    class_name: ClassVar[str] = "laboratory result"
    class_model_uri: ClassVar[URIRef] = BIOLINK.LaboratoryResult

    id: Union[str, LaboratoryResultId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, LaboratoryResultId):
            self.id = LaboratoryResultId(self.id)
        super().__post_init__()


@dataclass
class LaboratoryTest(Procedure):
    """
    The definition and description of a clinical laboratory test
    """
    _inherited_slots: ClassVar[List[str]] = ["correlation", "related_to", "interacts_with", "regulates_process_to_process", "has_participant", "has_input", "precedes"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.LaboratoryTest
    class_class_curie: ClassVar[str] = "biolink:LaboratoryTest"
    class_name: ClassVar[str] = "laboratory test"
    class_model_uri: ClassVar[URIRef] = BIOLINK.LaboratoryTest

    id: Union[str, LaboratoryTestId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, LaboratoryTestId):
            self.id = LaboratoryTestId(self.id)
        super().__post_init__()


@dataclass
class Medication(ClinicalIntervention):
    """
    Medication that has been prescribed and (ostensibly) taken
    """
    _inherited_slots: ClassVar[List[str]] = ["correlation", "related_to", "interacts_with"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Medication
    class_class_curie: ClassVar[str] = "biolink:Medication"
    class_name: ClassVar[str] = "medication"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Medication

    id: Union[str, MedicationId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MedicationId):
            self.id = MedicationId(self.id)
        super().__post_init__()


@dataclass
class Medicine(ChemicalSubstance):
    """
    Description of the contents of a medication
    """
    _inherited_slots: ClassVar[List[str]] = ["correlation", "related_to", "interacts_with", "has_phenotype", "molecularly_interacts_with", "affects_abundance_of", "increases_abundance_of", "decreases_abundance_of", "affects_activity_of", "increases_activity_of", "decreases_activity_of", "affects_expression_of", "increases_expression_of", "decreases_expression_of", "affects_folding_of", "increases_folding_of", "decreases_folding_of", "affects_localization_of", "increases_localization_of", "decreases_localization_of", "affects_metabolic_processing_of", "increases_metabolic_processing_of", "decreases_metabolic_processing_of", "affects_molecular_modification_of", "increases_molecular_modification_of", "decreases_molecular_modification_of", "affects_synthesis_of", "increases_synthesis_of", "decreases_synthesis_of", "affects_degradation_of", "increases_degradation_of", "decreases_degradation_of", "affects_mutation_rate_of", "increases_mutation_rate_of", "decreases_mutation_rate_of", "affects_response_to", "increases_response_to", "decreases_response_to", "affects_splicing_of", "increases_splicing_of", "decreases_splicing_of", "affects_stability_of", "increases_stability_of", "decreases_stability_of", "affects_transport_of", "increases_transport_of", "decreases_transport_of", "affects_secretion_of", "increases_secretion_of", "decreases_secretion_of", "affects_uptake_of", "increases_uptake_of", "decreases_uptake_of", "regulates_entity_to_entity", "biomarker_for", "in_taxon"]

    class_class_uri: ClassVar[URIRef] = BIOLINK.Medicine
    class_class_curie: ClassVar[str] = "biolink:Medicine"
    class_name: ClassVar[str] = "medicine"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Medicine

    id: Union[str, MedicineId] = None
    name: Union[str, LabelType] = None
    category: List[Union[str, IriType]] = empty_list()
    has_active_ingredient: List[Union[str, DrugId]] = empty_list()

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, MedicineId):
            self.id = MedicineId(self.id)
        self.has_active_ingredient = [v if isinstance(v, DrugId)
                                      else DrugId(v) for v in self.has_active_ingredient]
        super().__post_init__()


class Diagnosis(YAMLRoot):
    """
    An assertion of a disease or disorder
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.Diagnosis
    class_class_curie: ClassVar[str] = "biolink:Diagnosis"
    class_name: ClassVar[str] = "diagnosis"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Diagnosis


@dataclass
class LabToLabCorrelation(Association):
    """
    A correlation between two laboratory tests in the context of a particular population and cohort
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.LabToLabCorrelation
    class_class_curie: ClassVar[str] = "biolink:LabToLabCorrelation"
    class_name: ClassVar[str] = "lab to lab correlation"
    class_model_uri: ClassVar[URIRef] = BIOLINK.LabToLabCorrelation

    id: Union[str, LabToLabCorrelationId] = None
    subject: Union[str, LaboratoryTestId] = None
    relation: Union[str, IriType] = None
    object: Union[str, LaboratoryTestId] = None
    edge_label: Union[str, LabelType] = None
    correlation_coefficient: Optional[float] = None
    population: Optional[Union[str, URI]] = None
    cohort: Optional[Union[str, URI]] = None

    def __post_init__(self):
        if self.id is not None and not isinstance(self.id, LabToLabCorrelationId):
            self.id = LabToLabCorrelationId(self.id)
        if self.subject is not None and not isinstance(self.subject, LaboratoryTestId):
            self.subject = LaboratoryTestId(self.subject)
        if self.relation is not None and not isinstance(self.relation, IriType):
            self.relation = IriType(self.relation)
        if self.object is not None and not isinstance(self.object, LaboratoryTestId):
            self.object = LaboratoryTestId(self.object)
        if self.population is not None and not isinstance(self.population, URI):
            self.population = URI(self.population)
        if self.cohort is not None and not isinstance(self.cohort, URI):
            self.cohort = URI(self.cohort)
        super().__post_init__()

