#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Ingredient) on 2019-08-06.
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
from .ratio import Ratio


@dataclass
class IngredientSpecifiedSubstanceStrengthReferenceStrength(BackboneElement):
    """ Strength expressed in terms of a reference substance.
    """
    resource_type: ClassVar[str] = "IngredientSpecifiedSubstanceStrengthReferenceStrength"
    substanceCodeableConcept: Optional[CodeableConcept] = None
    substanceReference: Optional[FHIRReference] = None
    strength: Ratio = None
    strengthLowLimit: Optional[Ratio] = None
    measurementPoint: Optional[str] = None
    country: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(IngredientSpecifiedSubstanceStrengthReferenceStrength, self).elementProperties()
        js.extend([
            ("substanceCodeableConcept", "substanceCodeableConcept", CodeableConcept, False, "substance", False),
            ("substanceReference", "substanceReference", FHIRReference, False, "substance", False),
            ("strength", "strength", Ratio, False, None, True),
            ("strengthLowLimit", "strengthLowLimit", Ratio, False, None, False),
            ("measurementPoint", "measurementPoint", str, False, None, False),
            ("country", "country", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class IngredientSpecifiedSubstanceStrength(BackboneElement):
    """ Quantity of the substance or specified substance present in the
    manufactured item or pharmaceutical product.
    """
    resource_type: ClassVar[str] = "IngredientSpecifiedSubstanceStrength"
    presentation: Ratio = None
    presentationLowLimit: Optional[Ratio] = None
    concentration: Optional[Ratio] = None
    concentrationLowLimit: Optional[Ratio] = None
    measurementPoint: Optional[str] = None
    country: Optional[List[CodeableConcept]] = empty_list()
    referenceStrength: Optional[List[IngredientSpecifiedSubstanceStrengthReferenceStrength]] = empty_list()

    def elementProperties(self):
        js = super(IngredientSpecifiedSubstanceStrength, self).elementProperties()
        js.extend([
            ("presentation", "presentation", Ratio, False, None, True),
            ("presentationLowLimit", "presentationLowLimit", Ratio, False, None, False),
            ("concentration", "concentration", Ratio, False, None, False),
            ("concentrationLowLimit", "concentrationLowLimit", Ratio, False, None, False),
            ("measurementPoint", "measurementPoint", str, False, None, False),
            ("country", "country", CodeableConcept, True, None, False),
            ("referenceStrength", "referenceStrength", IngredientSpecifiedSubstanceStrengthReferenceStrength, True, None, False),
        ])
        return js


@dataclass
class IngredientSpecifiedSubstance(BackboneElement):
    """ A specified substance that comprises this ingredient.
    """
    resource_type: ClassVar[str] = "IngredientSpecifiedSubstance"
    codeCodeableConcept: CodeableConcept = None
    codeReference: FHIRReference = None
    group: CodeableConcept = None
    confidentiality: Optional[CodeableConcept] = None
    strength: Optional[List[IngredientSpecifiedSubstanceStrength]] = empty_list()

    def elementProperties(self):
        js = super(IngredientSpecifiedSubstance, self).elementProperties()
        js.extend([
            ("codeCodeableConcept", "codeCodeableConcept", CodeableConcept, False, "code", True),
            ("codeReference", "codeReference", FHIRReference, False, "code", True),
            ("group", "group", CodeableConcept, False, None, True),
            ("confidentiality", "confidentiality", CodeableConcept, False, None, False),
            ("strength", "strength", IngredientSpecifiedSubstanceStrength, True, None, False),
        ])
        return js


@dataclass
class IngredientSubstance(BackboneElement):
    """ The ingredient substance.
    """
    resource_type: ClassVar[str] = "IngredientSubstance"
    codeCodeableConcept: CodeableConcept = None
    codeReference: FHIRReference = None
    strength: Optional[List[IngredientSpecifiedSubstanceStrength]] = empty_list()

    def elementProperties(self):
        js = super(IngredientSubstance, self).elementProperties()
        js.extend([
            ("codeCodeableConcept", "codeCodeableConcept", CodeableConcept, False, "code", True),
            ("codeReference", "codeReference", FHIRReference, False, "code", True),
            ("strength", "strength", IngredientSpecifiedSubstanceStrength, True, None, False),
        ])
        return js


@dataclass
class Ingredient(DomainResource):
    """ An ingredient of a manufactured item or pharmaceutical product.
    """
    resource_type: ClassVar[str] = "Ingredient"
    identifier: Optional[Identifier] = None
    role: CodeableConcept = None
    allergenicIndicator: Optional[bool] = None
    manufacturer: Optional[List[FHIRReference]] = empty_list()
    specifiedSubstance: Optional[List[IngredientSpecifiedSubstance]] = empty_list()
    substance: Optional[IngredientSubstance] = None

    def elementProperties(self):
        js = super(Ingredient, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("role", "role", CodeableConcept, False, None, True),
            ("allergenicIndicator", "allergenicIndicator", bool, False, None, False),
            ("manufacturer", "manufacturer", FHIRReference, True, None, False),
            ("specifiedSubstance", "specifiedSubstance", IngredientSpecifiedSubstance, True, None, False),
            ("substance", "substance", IngredientSubstance, False, None, False),
        ])
        return js