#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/MolecularSequence) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity


@dataclass
class MolecularSequenceStructureVariantOuter(BackboneElement):
    """ Structural variant outer.
    """
    resource_type: ClassVar[str] = "MolecularSequenceStructureVariantOuter"
    start: Optional[int] = None
    end: Optional[int] = None

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantOuter, self).elementProperties()
        js.extend([
            ("start", "start", int, False, None, False),
            ("end", "end", int, False, None, False),
        ])
        return js


@dataclass
class MolecularSequenceStructureVariantInner(BackboneElement):
    """ Structural variant inner.
    """
    resource_type: ClassVar[str] = "MolecularSequenceStructureVariantInner"
    start: Optional[int] = None
    end: Optional[int] = None

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantInner, self).elementProperties()
        js.extend([
            ("start", "start", int, False, None, False),
            ("end", "end", int, False, None, False),
        ])
        return js


@dataclass
class MolecularSequenceQualityRoc(BackboneElement):
    """ Receiver Operator Characteristic (ROC) Curve.

    Receiver Operator Characteristic (ROC) Curve  to give
    sensitivity/specificity tradeoff.
    """
    resource_type: ClassVar[str] = "MolecularSequenceQualityRoc"
    score: Optional[List[int]] = empty_list()
    numTP: Optional[List[int]] = empty_list()
    numFP: Optional[List[int]] = empty_list()
    numFN: Optional[List[int]] = empty_list()
    precision: Optional[List[float]] = empty_list()
    sensitivity: Optional[List[float]] = empty_list()
    fMeasure: Optional[List[float]] = empty_list()

    def elementProperties(self):
        js = super(MolecularSequenceQualityRoc, self).elementProperties()
        js.extend([
            ("score", "score", int, True, None, False),
            ("numTP", "numTP", int, True, None, False),
            ("numFP", "numFP", int, True, None, False),
            ("numFN", "numFN", int, True, None, False),
            ("precision", "precision", float, True, None, False),
            ("sensitivity", "sensitivity", float, True, None, False),
            ("fMeasure", "fMeasure", float, True, None, False),
        ])
        return js


@dataclass
class MolecularSequenceReferenceSeq(BackboneElement):
    """ A sequence used as reference.

    A sequence that is used as a reference to describe variants that are
    present in a sequence analyzed.
    """
    resource_type: ClassVar[str] = "MolecularSequenceReferenceSeq"
    chromosome: Optional[CodeableConcept] = None
    genomeBuild: Optional[str] = None
    orientation: Optional[str] = None
    referenceSeqId: Optional[CodeableConcept] = None
    referenceSeqPointer: Optional[FHIRReference] = None
    referenceSeqString: Optional[str] = None
    strand: Optional[str] = None
    windowStart: Optional[int] = None
    windowEnd: Optional[int] = None

    def elementProperties(self):
        js = super(MolecularSequenceReferenceSeq, self).elementProperties()
        js.extend([
            ("chromosome", "chromosome", CodeableConcept, False, None, False),
            ("genomeBuild", "genomeBuild", str, False, None, False),
            ("orientation", "orientation", str, False, None, False),
            ("referenceSeqId", "referenceSeqId", CodeableConcept, False, None, False),
            ("referenceSeqPointer", "referenceSeqPointer", FHIRReference, False, None, False),
            ("referenceSeqString", "referenceSeqString", str, False, None, False),
            ("strand", "strand", str, False, None, False),
            ("windowStart", "windowStart", int, False, None, False),
            ("windowEnd", "windowEnd", int, False, None, False),
        ])
        return js


@dataclass
class MolecularSequenceVariant(BackboneElement):
    """ Variant in sequence.

    The definition of variant here originates from Sequence ontology ([variant_
    of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
    This element can represent amino acid or nucleic sequence change(including
    insertion,deletion,SNP,etc.)  It can represent some complex mutation or
    segment variation with the assist of CIGAR string.
    """
    resource_type: ClassVar[str] = "MolecularSequenceVariant"
    start: Optional[int] = None
    end: Optional[int] = None
    observedAllele: Optional[str] = None
    referenceAllele: Optional[str] = None
    cigar: Optional[str] = None
    variantPointer: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(MolecularSequenceVariant, self).elementProperties()
        js.extend([
            ("start", "start", int, False, None, False),
            ("end", "end", int, False, None, False),
            ("observedAllele", "observedAllele", str, False, None, False),
            ("referenceAllele", "referenceAllele", str, False, None, False),
            ("cigar", "cigar", str, False, None, False),
            ("variantPointer", "variantPointer", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class MolecularSequenceQuality(BackboneElement):
    """ An set of value as quality of sequence.

    An experimental feature attribute that defines the quality of the feature
    in a quantitative way, such as a phred quality score ([SO:0001686](http://w
    ww.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    """
    resource_type: ClassVar[str] = "MolecularSequenceQuality"
    type: str = None
    standardSequence: Optional[CodeableConcept] = None
    start: Optional[int] = None
    end: Optional[int] = None
    score: Optional[Quantity] = None
    method: Optional[CodeableConcept] = None
    truthTP: Optional[float] = None
    queryTP: Optional[float] = None
    truthFN: Optional[float] = None
    queryFP: Optional[float] = None
    gtFP: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    fScore: Optional[float] = None
    roc: Optional[MolecularSequenceQualityRoc] = None

    def elementProperties(self):
        js = super(MolecularSequenceQuality, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("standardSequence", "standardSequence", CodeableConcept, False, None, False),
            ("start", "start", int, False, None, False),
            ("end", "end", int, False, None, False),
            ("score", "score", Quantity, False, None, False),
            ("method", "method", CodeableConcept, False, None, False),
            ("truthTP", "truthTP", float, False, None, False),
            ("queryTP", "queryTP", float, False, None, False),
            ("truthFN", "truthFN", float, False, None, False),
            ("queryFP", "queryFP", float, False, None, False),
            ("gtFP", "gtFP", float, False, None, False),
            ("precision", "precision", float, False, None, False),
            ("recall", "recall", float, False, None, False),
            ("fScore", "fScore", float, False, None, False),
            ("roc", "roc", MolecularSequenceQualityRoc, False, None, False),
        ])
        return js


@dataclass
class MolecularSequenceRepository(BackboneElement):
    """ External repository which contains detailed report related with observedSeq
    in this resource.

    Configurations of the external repository. The repository shall store
    target's observedSeq or records related with target's observedSeq.
    """
    resource_type: ClassVar[str] = "MolecularSequenceRepository"
    type: str = None
    url: Optional[str] = None
    name: Optional[str] = None
    datasetId: Optional[str] = None
    variantsetId: Optional[str] = None
    readsetId: Optional[str] = None

    def elementProperties(self):
        js = super(MolecularSequenceRepository, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("datasetId", "datasetId", str, False, None, False),
            ("variantsetId", "variantsetId", str, False, None, False),
            ("readsetId", "readsetId", str, False, None, False),
        ])
        return js


@dataclass
class MolecularSequenceStructureVariant(BackboneElement):
    """ Structural variant.

    Information about chromosome structure variation.
    """
    resource_type: ClassVar[str] = "MolecularSequenceStructureVariant"
    variantType: Optional[CodeableConcept] = None
    exact: Optional[bool] = None
    length: Optional[int] = None
    outer: Optional[MolecularSequenceStructureVariantOuter] = None
    inner: Optional[MolecularSequenceStructureVariantInner] = None

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariant, self).elementProperties()
        js.extend([
            ("variantType", "variantType", CodeableConcept, False, None, False),
            ("exact", "exact", bool, False, None, False),
            ("length", "length", int, False, None, False),
            ("outer", "outer", MolecularSequenceStructureVariantOuter, False, None, False),
            ("inner", "inner", MolecularSequenceStructureVariantInner, False, None, False),
        ])
        return js


@dataclass
class MolecularSequence(DomainResource):
    """ Information about a biological sequence.

    Raw data describing a biological sequence.
    """
    resource_type: ClassVar[str] = "MolecularSequence"
    identifier: Optional[List[Identifier]] = empty_list()
    type: Optional[str] = None
    coordinateSystem: int = None
    patient: Optional[FHIRReference] = None
    specimen: Optional[FHIRReference] = None
    device: Optional[FHIRReference] = None
    performer: Optional[FHIRReference] = None
    quantity: Optional[Quantity] = None
    referenceSeq: Optional[MolecularSequenceReferenceSeq] = None
    variant: Optional[List[MolecularSequenceVariant]] = empty_list()
    observedSeq: Optional[str] = None
    quality: Optional[List[MolecularSequenceQuality]] = empty_list()
    readCoverage: Optional[int] = None
    repository: Optional[List[MolecularSequenceRepository]] = empty_list()
    pointer: Optional[List[FHIRReference]] = empty_list()
    structureVariant: Optional[List[MolecularSequenceStructureVariant]] = empty_list()

    def elementProperties(self):
        js = super(MolecularSequence, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("type", "type", str, False, None, False),
            ("coordinateSystem", "coordinateSystem", int, False, None, True),
            ("patient", "patient", FHIRReference, False, None, False),
            ("specimen", "specimen", FHIRReference, False, None, False),
            ("device", "device", FHIRReference, False, None, False),
            ("performer", "performer", FHIRReference, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("referenceSeq", "referenceSeq", MolecularSequenceReferenceSeq, False, None, False),
            ("variant", "variant", MolecularSequenceVariant, True, None, False),
            ("observedSeq", "observedSeq", str, False, None, False),
            ("quality", "quality", MolecularSequenceQuality, True, None, False),
            ("readCoverage", "readCoverage", int, False, None, False),
            ("repository", "repository", MolecularSequenceRepository, True, None, False),
            ("pointer", "pointer", FHIRReference, True, None, False),
            ("structureVariant", "structureVariant", MolecularSequenceStructureVariant, True, None, False),
        ])
        return js