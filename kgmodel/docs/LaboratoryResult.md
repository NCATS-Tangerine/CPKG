
# Class: laboratory result


The result of a clinical laboratory test performed on a patient

URI: [biolink:LaboratoryResult](https://w3id.org/biolink/vocab/LaboratoryResult)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Phenomenon]^-\[LaboratoryResult|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B])

## Parents

 *  is_a: [Phenomenon](Phenomenon.md) - a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question

## Referenced by class

 *  **[LaboratoryResult](LaboratoryResult.md)** *[lab has correlated lab](lab_has_correlated_lab.md)*  <sub>0..*</sub>  **[LaboratoryResult](LaboratoryResult.md)**

## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [lab has correlated lab](lab_has_correlated_lab.md)  <sub>0..*</sub>
    * Description: A correlation between two lab tests
    * range: [LaboratoryResult](LaboratoryResult.md)
