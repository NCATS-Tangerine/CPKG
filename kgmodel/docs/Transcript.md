
# Class: transcript


An RNA synthesized on a DNA or RNA template by an RNA polymerase

URI: [biolink:Transcript](https://w3id.org/biolink/vocab/Transcript)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[Transcript|has_biological_sequence(i):biological_sequence%20%3F;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[ExonToTranscriptRelationship]-%20object%201..1>\[Transcript],%20\[TranscriptToGeneRelationship]-%20subject%201..1>\[Transcript],%20\[GenomicEntity]^-\[Transcript])

## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Referenced by class

 *  **[MolecularEntity](MolecularEntity.md)** *[affects splicing of](affects_splicing_of.md)*  <sub>0..*</sub>  **[Transcript](Transcript.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[decreases splicing of](decreases_splicing_of.md)*  <sub>0..*</sub>  **[Transcript](Transcript.md)**
 *  **[ExonToTranscriptRelationship](ExonToTranscriptRelationship.md)** *[object](exon_to_transcript_relationship_object.md)*  <sub>REQ</sub>  **[Transcript](Transcript.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases splicing of](increases_splicing_of.md)*  <sub>0..*</sub>  **[Transcript](Transcript.md)**
 *  **[TranscriptToGeneRelationship](TranscriptToGeneRelationship.md)** *[subject](transcript_to_gene_relationship_subject.md)*  <sub>REQ</sub>  **[Transcript](Transcript.md)**

## Attributes


### Inherited from genomic entity:

 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](BiologicalSequence.md)
    * inherited from: [GenomicEntity](GenomicEntity.md)

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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
    * in subsets: (translator_minimal)
