
# Class: lab to lab correlation


A correlation between two laboratory tests in the context of a particular population and cohort

URI: [biolink:LabToLabCorrelation](https://w3id.org/biolink/vocab/LabToLabCorrelation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[LabToLabCorrelation|relation:iri_type;correlation_coefficient:float%20%3F;population:uri%20%3F;cohort:uri%20%3F;id(i):identifier_type;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[LabToLabCorrelation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[LabToLabCorrelation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[LabToLabCorrelation],%20\[LaboratoryTest]<object%201..1-%20\[LabToLabCorrelation],%20\[LaboratoryTest]<subject%201..1-%20\[LabToLabCorrelation],%20\[Association]^-\[LabToLabCorrelation])

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [cohort](cohort.md)  <sub>OPT</sub>
    * range: [Uri](Uri.md)
 * [correlation coefficient](correlation_coefficient.md)  <sub>OPT</sub>
    * range: [Float](Float.md)
 * [object](lab_to_lab_correlation_object.md)  <sub>REQ</sub>
    * range: [LaboratoryTest](LaboratoryTest.md)
 * [relation](lab_to_lab_correlation_relation.md)  <sub>REQ</sub>
    * range: [IriType](IriType.md)
 * [subject](lab_to_lab_correlation_subject.md)  <sub>REQ</sub>
    * range: [LaboratoryTest](LaboratoryTest.md)
 * [population](population.md)  <sub>OPT</sub>
    * range: [Uri](Uri.md)

### Inherited from association:

 * [id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [Association](Association.md)
    * in subsets: (translator_minimal)
 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [IriType](IriType.md)
    * inherited from: [Association](Association.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [IriType](IriType.md)
    * inherited from: [Association](Association.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [IriType](IriType.md)
    * inherited from: [Association](Association.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](Boolean.md)
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
    * inherited from: [Association](Association.md)
 * [provided by](provided_by.md)  <sub>OPT</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)

### Domain for slot:

 * [cohort](cohort.md)  <sub>OPT</sub>
    * range: [Uri](Uri.md)
 * [correlation coefficient](correlation_coefficient.md)  <sub>OPT</sub>
    * range: [Float](Float.md)
 * [object](lab_to_lab_correlation_object.md)  <sub>REQ</sub>
    * range: [LaboratoryTest](LaboratoryTest.md)
 * [relation](lab_to_lab_correlation_relation.md)  <sub>REQ</sub>
    * range: [IriType](IriType.md)
 * [subject](lab_to_lab_correlation_subject.md)  <sub>REQ</sub>
    * range: [LaboratoryTest](LaboratoryTest.md)
 * [population](population.md)  <sub>OPT</sub>
    * range: [Uri](Uri.md)
