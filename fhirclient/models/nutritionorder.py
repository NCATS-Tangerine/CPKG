#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/NutritionOrder) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .ratio import Ratio
from .timing import Timing


@dataclass
class NutritionOrderEnteralFormulaAdministration(BackboneElement):
    """ Formula feeding instruction as structured data.

    Formula administration instructions as structured data.  This repeating
    structure allows for changing the administration rate or volume over time
    for both bolus and continuous feeding.  An example of this would be an
    instruction to increase the rate of continuous feeding every 2 hours.
    """
    resource_type: ClassVar[str] = "NutritionOrderEnteralFormulaAdministration"
    schedule: Optional[Timing] = None
    quantity: Optional[Quantity] = None
    rateQuantity: Optional[Quantity] = None
    rateRatio: Optional[Ratio] = None

    def elementProperties(self):
        js = super(NutritionOrderEnteralFormulaAdministration, self).elementProperties()
        js.extend([
            ("schedule", "schedule", Timing, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("rateQuantity", "rateQuantity", Quantity, False, "rate", False),
            ("rateRatio", "rateRatio", Ratio, False, "rate", False),
        ])
        return js


@dataclass
class NutritionOrderOralDietNutrient(BackboneElement):
    """ Required  nutrient modifications.

    Class that defines the quantity and type of nutrient modifications (for
    example carbohydrate, fiber or sodium) required for the oral diet.
    """
    resource_type: ClassVar[str] = "NutritionOrderOralDietNutrient"
    modifier: Optional[CodeableConcept] = None
    amount: Optional[Quantity] = None

    def elementProperties(self):
        js = super(NutritionOrderOralDietNutrient, self).elementProperties()
        js.extend([
            ("modifier", "modifier", CodeableConcept, False, None, False),
            ("amount", "amount", Quantity, False, None, False),
        ])
        return js


@dataclass
class NutritionOrderOralDietTexture(BackboneElement):
    """ Required  texture modifications.

    Class that describes any texture modifications required for the patient to
    safely consume various types of solid foods.
    """
    resource_type: ClassVar[str] = "NutritionOrderOralDietTexture"
    modifier: Optional[CodeableConcept] = None
    foodType: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(NutritionOrderOralDietTexture, self).elementProperties()
        js.extend([
            ("modifier", "modifier", CodeableConcept, False, None, False),
            ("foodType", "foodType", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class NutritionOrderOralDiet(BackboneElement):
    """ Oral diet components.

    Diet given orally in contrast to enteral (tube) feeding.
    """
    resource_type: ClassVar[str] = "NutritionOrderOralDiet"
    type: Optional[List[CodeableConcept]] = empty_list()
    schedule: Optional[List[Timing]] = empty_list()
    nutrient: Optional[List[NutritionOrderOralDietNutrient]] = empty_list()
    texture: Optional[List[NutritionOrderOralDietTexture]] = empty_list()
    fluidConsistencyType: Optional[List[CodeableConcept]] = empty_list()
    instruction: Optional[str] = None

    def elementProperties(self):
        js = super(NutritionOrderOralDiet, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, True, None, False),
            ("schedule", "schedule", Timing, True, None, False),
            ("nutrient", "nutrient", NutritionOrderOralDietNutrient, True, None, False),
            ("texture", "texture", NutritionOrderOralDietTexture, True, None, False),
            ("fluidConsistencyType", "fluidConsistencyType", CodeableConcept, True, None, False),
            ("instruction", "instruction", str, False, None, False),
        ])
        return js


@dataclass
class NutritionOrderSupplement(BackboneElement):
    """ Supplement components.

    Oral nutritional products given in order to add further nutritional value
    to the patient's diet.
    """
    resource_type: ClassVar[str] = "NutritionOrderSupplement"
    type: Optional[CodeableConcept] = None
    productName: Optional[str] = None
    schedule: Optional[List[Timing]] = empty_list()
    quantity: Optional[Quantity] = None
    instruction: Optional[str] = None

    def elementProperties(self):
        js = super(NutritionOrderSupplement, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("productName", "productName", str, False, None, False),
            ("schedule", "schedule", Timing, True, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("instruction", "instruction", str, False, None, False),
        ])
        return js


@dataclass
class NutritionOrderEnteralFormula(BackboneElement):
    """ Enteral formula components.

    Feeding provided through the gastrointestinal tract via a tube, catheter,
    or stoma that delivers nutrition distal to the oral cavity.
    """
    resource_type: ClassVar[str] = "NutritionOrderEnteralFormula"
    baseFormulaType: Optional[CodeableConcept] = None
    baseFormulaProductName: Optional[str] = None
    additiveType: Optional[CodeableConcept] = None
    additiveProductName: Optional[str] = None
    caloricDensity: Optional[Quantity] = None
    routeofAdministration: Optional[CodeableConcept] = None
    administration: Optional[List[NutritionOrderEnteralFormulaAdministration]] = empty_list()
    maxVolumeToDeliver: Optional[Quantity] = None
    administrationInstruction: Optional[str] = None

    def elementProperties(self):
        js = super(NutritionOrderEnteralFormula, self).elementProperties()
        js.extend([
            ("baseFormulaType", "baseFormulaType", CodeableConcept, False, None, False),
            ("baseFormulaProductName", "baseFormulaProductName", str, False, None, False),
            ("additiveType", "additiveType", CodeableConcept, False, None, False),
            ("additiveProductName", "additiveProductName", str, False, None, False),
            ("caloricDensity", "caloricDensity", Quantity, False, None, False),
            ("routeofAdministration", "routeofAdministration", CodeableConcept, False, None, False),
            ("administration", "administration", NutritionOrderEnteralFormulaAdministration, True, None, False),
            ("maxVolumeToDeliver", "maxVolumeToDeliver", Quantity, False, None, False),
            ("administrationInstruction", "administrationInstruction", str, False, None, False),
        ])
        return js


@dataclass
class NutritionOrder(DomainResource):
    """ Diet, formula or nutritional supplement request.

    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """
    resource_type: ClassVar[str] = "NutritionOrder"
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    instantiates: Optional[List[str]] = empty_list()
    status: str = None
    intent: str = None
    patient: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    dateTime: FHIRDate = None
    orderer: Optional[FHIRReference] = None
    allergyIntolerance: Optional[List[FHIRReference]] = empty_list()
    foodPreferenceModifier: Optional[List[CodeableConcept]] = empty_list()
    excludeFoodModifier: Optional[List[CodeableConcept]] = empty_list()
    oralDiet: Optional[NutritionOrderOralDiet] = None
    supplement: Optional[List[NutritionOrderSupplement]] = empty_list()
    enteralFormula: Optional[NutritionOrderEnteralFormula] = None
    note: Optional[List[Annotation]] = empty_list()

    def elementProperties(self):
        js = super(NutritionOrder, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("status", "status", str, False, None, True),
            ("intent", "intent", str, False, None, True),
            ("patient", "patient", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("dateTime", "dateTime", FHIRDate, False, None, True),
            ("orderer", "orderer", FHIRReference, False, None, False),
            ("allergyIntolerance", "allergyIntolerance", FHIRReference, True, None, False),
            ("foodPreferenceModifier", "foodPreferenceModifier", CodeableConcept, True, None, False),
            ("excludeFoodModifier", "excludeFoodModifier", CodeableConcept, True, None, False),
            ("oralDiet", "oralDiet", NutritionOrderOralDiet, False, None, False),
            ("supplement", "supplement", NutritionOrderSupplement, True, None, False),
            ("enteralFormula", "enteralFormula", NutritionOrderEnteralFormula, False, None, False),
            ("note", "note", Annotation, True, None, False),
        ])
        return js