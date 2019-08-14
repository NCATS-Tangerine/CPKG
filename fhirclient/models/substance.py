#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Substance) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class SubstanceInstance(BackboneElement):
    """ If this describes a specific package/container of the substance.

    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """
    resource_type: ClassVar[str] = "SubstanceInstance"
    identifier: Optional[Identifier] = None
    expiry: Optional[FHIRDate] = None
    quantity: Optional[Quantity] = None

    def elementProperties(self):
        js = super(SubstanceInstance, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("expiry", "expiry", FHIRDate, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
        ])
        return js


@dataclass
class SubstanceIngredient(BackboneElement):
    """ Composition information about the substance.

    A substance can be composed of other substances.
    """
    resource_type: ClassVar[str] = "SubstanceIngredient"
    quantity: Optional[Ratio] = None
    substanceCodeableConcept: CodeableConcept = None
    substanceReference: FHIRReference = None

    def elementProperties(self):
        js = super(SubstanceIngredient, self).elementProperties()
        js.extend([
            ("quantity", "quantity", Ratio, False, None, False),
            ("substanceCodeableConcept", "substanceCodeableConcept", CodeableConcept, False, "substance", True),
            ("substanceReference", "substanceReference", FHIRReference, False, "substance", True),
        ])
        return js


@dataclass
class Substance(DomainResource):
    """ A homogeneous material with a definite composition.
    """
    resource_type: ClassVar[str] = "Substance"
    identifier: Optional[List[Identifier]] = empty_list()
    status: Optional[str] = None
    category: Optional[List[CodeableConcept]] = empty_list()
    code: CodeableConcept = None
    description: Optional[str] = None
    instance: Optional[List[SubstanceInstance]] = empty_list()
    ingredient: Optional[List[SubstanceIngredient]] = empty_list()

    def elementProperties(self):
        js = super(Substance, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, True),
            ("description", "description", str, False, None, False),
            ("instance", "instance", SubstanceInstance, True, None, False),
            ("ingredient", "ingredient", SubstanceIngredient, True, None, False),
        ])
        return js