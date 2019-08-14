#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Medication) on 2019-08-06.
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
from .ratio import Ratio


@dataclass
class MedicationIngredient(BackboneElement):
    """ Active or inactive ingredient.

    Identifies a particular constituent of interest in the product.
    """
    resource_type: ClassVar[str] = "MedicationIngredient"
    itemCodeableConcept: CodeableConcept = None
    itemReference: FHIRReference = None
    isActive: Optional[bool] = None
    strengthRatio: Optional[Ratio] = None
    strengthCodeableConcept: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MedicationIngredient, self).elementProperties()
        js.extend([
            ("itemCodeableConcept", "itemCodeableConcept", CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", FHIRReference, False, "item", True),
            ("isActive", "isActive", bool, False, None, False),
            ("strengthRatio", "strengthRatio", Ratio, False, "strength", False),
            ("strengthCodeableConcept", "strengthCodeableConcept", CodeableConcept, False, "strength", False),
        ])
        return js


@dataclass
class MedicationBatch(BackboneElement):
    """ Details about packaged medications.

    Information that only applies to packages (not products).
    """
    resource_type: ClassVar[str] = "MedicationBatch"
    lotNumber: Optional[str] = None
    expirationDate: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(MedicationBatch, self).elementProperties()
        js.extend([
            ("lotNumber", "lotNumber", str, False, None, False),
            ("expirationDate", "expirationDate", FHIRDate, False, None, False),
        ])
        return js


@dataclass
class Medication(DomainResource):
    """ Definition of a Medication.

    This resource is primarily used for the identification and definition of a
    medication for the purposes of prescribing, dispensing, and administering a
    medication as well as for making statements about medication use.
    """
    resource_type: ClassVar[str] = "Medication"
    identifier: Optional[List[Identifier]] = empty_list()
    code: Optional[CodeableConcept] = None
    status: Optional[str] = None
    manufacturer: Optional[FHIRReference] = None
    doseForm: Optional[CodeableConcept] = None
    amount: Optional[Ratio] = None
    ingredient: Optional[List[MedicationIngredient]] = empty_list()
    batch: Optional[MedicationBatch] = None

    def elementProperties(self):
        js = super(Medication, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("status", "status", str, False, None, False),
            ("manufacturer", "manufacturer", FHIRReference, False, None, False),
            ("doseForm", "doseForm", CodeableConcept, False, None, False),
            ("amount", "amount", Ratio, False, None, False),
            ("ingredient", "ingredient", MedicationIngredient, True, None, False),
            ("batch", "batch", MedicationBatch, False, None, False),
        ])
        return js