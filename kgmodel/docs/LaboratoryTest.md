
# Class: laboratory test


The definition and description of a clinical laboratory test

URI: [biolink:LaboratoryTest](https://w3id.org/biolink/vocab/LaboratoryTest)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[LabToLabCorrelation]-%20object%201..1>\[LaboratoryTest|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[LabToLabCorrelation]-%20subject%201..1>\[LaboratoryTest],%20\[Procedure]^-\[LaboratoryTest])

## Parents

 *  is_a: [Procedure](Procedure.md) - A series of actions conducted in a certain order or manner

## Referenced by class

 *  **[LabToLabCorrelation](LabToLabCorrelation.md)** *[object](lab_to_lab_correlation_object.md)*  <sub>REQ</sub>  **[LaboratoryTest](LaboratoryTest.md)**
 *  **[LabToLabCorrelation](LabToLabCorrelation.md)** *[subject](lab_to_lab_correlation_subject.md)*  <sub>REQ</sub>  **[LaboratoryTest](LaboratoryTest.md)**

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
