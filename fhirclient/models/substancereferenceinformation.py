#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation) on 2019-08-06.
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
from .range import Range


@dataclass
class SubstanceReferenceInformationGene(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformationGene"
    geneSequenceOrigin: Optional[CodeableConcept] = None
    gene: Optional[CodeableConcept] = None
    source: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceReferenceInformationGene, self).elementProperties()
        js.extend([
            ("geneSequenceOrigin", "geneSequenceOrigin", CodeableConcept, False, None, False),
            ("gene", "gene", CodeableConcept, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class SubstanceReferenceInformationGeneElement(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformationGeneElement"
    type: Optional[CodeableConcept] = None
    element: Optional[Identifier] = None
    source: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceReferenceInformationGeneElement, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("element", "element", Identifier, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class SubstanceReferenceInformationClassification(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformationClassification"
    domain: Optional[CodeableConcept] = None
    classification: Optional[CodeableConcept] = None
    subtype: Optional[List[CodeableConcept]] = empty_list()
    source: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceReferenceInformationClassification, self).elementProperties()
        js.extend([
            ("domain", "domain", CodeableConcept, False, None, False),
            ("classification", "classification", CodeableConcept, False, None, False),
            ("subtype", "subtype", CodeableConcept, True, None, False),
            ("source", "source", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class SubstanceReferenceInformationTarget(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformationTarget"
    target: Optional[Identifier] = None
    type: Optional[CodeableConcept] = None
    interaction: Optional[CodeableConcept] = None
    organism: Optional[CodeableConcept] = None
    organismType: Optional[CodeableConcept] = None
    amountQuantity: Optional[Quantity] = None
    amountRange: Optional[Range] = None
    amountString: Optional[str] = None
    amountType: Optional[CodeableConcept] = None
    source: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceReferenceInformationTarget, self).elementProperties()
        js.extend([
            ("target", "target", Identifier, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("interaction", "interaction", CodeableConcept, False, None, False),
            ("organism", "organism", CodeableConcept, False, None, False),
            ("organismType", "organismType", CodeableConcept, False, None, False),
            ("amountQuantity", "amountQuantity", Quantity, False, "amount", False),
            ("amountRange", "amountRange", Range, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("amountType", "amountType", CodeableConcept, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class SubstanceReferenceInformation(DomainResource):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformation"
    comment: Optional[str] = None
    gene: Optional[List[SubstanceReferenceInformationGene]] = empty_list()
    geneElement: Optional[List[SubstanceReferenceInformationGeneElement]] = empty_list()
    classification: Optional[List[SubstanceReferenceInformationClassification]] = empty_list()
    target: Optional[List[SubstanceReferenceInformationTarget]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceReferenceInformation, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("gene", "gene", SubstanceReferenceInformationGene, True, None, False),
            ("geneElement", "geneElement", SubstanceReferenceInformationGeneElement, True, None, False),
            ("classification", "classification", SubstanceReferenceInformationClassification, True, None, False),
            ("target", "target", SubstanceReferenceInformationTarget, True, None, False),
        ])
        return js