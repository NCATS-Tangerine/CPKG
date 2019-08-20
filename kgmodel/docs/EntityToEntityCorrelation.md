
# Class: entity to entity correlation




URI: [biolink:EntityToEntityCorrelation](https://w3id.org/biolink/vocab/EntityToEntityCorrelation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[EntityToEntityCorrelation|relation:uriorcurie;correlation_coefficient:float%20%3F;population:uri%20%3F;cohort:uri%20%3F;id(i):identifier_type;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[EntityToEntityCorrelation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[EntityToEntityCorrelation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[EntityToEntityCorrelation],%20\[NamedThing]<object(i)%201..1-%20\[EntityToEntityCorrelation],%20\[NamedThing]<subject(i)%201..1-%20\[EntityToEntityCorrelation],%20\[EntityToEntityCorrelation]^-\[LabToMedicationCorrelation],%20\[EntityToEntityCorrelation]^-\[LabToLabCorrelation],%20\[Association]^-\[EntityToEntityCorrelation])

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Children

 * [LabToLabCorrelation](LabToLabCorrelation.md) - A correlation between two laboratory tests in the context of a particular population and cohort
 * [LabToMedicationCorrelation](LabToMedicationCorrelation.md)

## Referenced by class


## Attributes


### Own

 * [cohort](cohort.md)  <sub>OPT</sub>
    * range: [Uri](Uri.md)
 * [correlation coefficient](correlation_coefficient.md)  <sub>OPT</sub>
    * range: [Float](Float.md)
 * [relation](entity_to_entity_correlation_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](Uriorcurie.md)
 * [population](population.md)  <sub>OPT</sub>
    * range: [Uri](Uri.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Association](Association.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [Uriorcurie](Uriorcurie.md)
    * inherited from: [Association](Association.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Association](Association.md)
 * [id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [Association](Association.md)
    * in subsets: (translator_minimal)
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
 * [relation](entity_to_entity_correlation_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](Uriorcurie.md)
 * [population](population.md)  <sub>OPT</sub>
    * range: [Uri](Uri.md)
