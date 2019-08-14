#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Dosage) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .element import Element
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .timing import Timing


@dataclass
class DosageDoseAndRate(Element):
    """ Amount of medication administered.

    The amount of medication administered.
    """
    resource_type: ClassVar[str] = "DosageDoseAndRate"
    type: Optional[CodeableConcept] = None
    doseRange: Optional[Range] = None
    doseQuantity: Optional[Quantity] = None
    rateRatio: Optional[Ratio] = None
    rateRange: Optional[Range] = None
    rateQuantity: Optional[Quantity] = None

    def elementProperties(self):
        js = super(DosageDoseAndRate, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("doseRange", "doseRange", Range, False, "dose", False),
            ("doseQuantity", "doseQuantity", Quantity, False, "dose", False),
            ("rateRatio", "rateRatio", Ratio, False, "rate", False),
            ("rateRange", "rateRange", Range, False, "rate", False),
            ("rateQuantity", "rateQuantity", Quantity, False, "rate", False),
        ])
        return js


@dataclass
class Dosage(BackboneElement):
    """ How the medication is/was taken or should be taken.

    Indicates how the medication is/was taken or should be taken by the
    patient.
    """
    resource_type: ClassVar[str] = "Dosage"
    sequence: Optional[int] = None
    text: Optional[str] = None
    additionalInstruction: Optional[List[CodeableConcept]] = empty_list()
    patientInstruction: Optional[str] = None
    timing: Optional[Timing] = None
    asNeededBoolean: Optional[bool] = None
    asNeededCodeableConcept: Optional[CodeableConcept] = None
    site: Optional[CodeableConcept] = None
    route: Optional[CodeableConcept] = None
    method: Optional[CodeableConcept] = None
    doseAndRate: Optional[List[DosageDoseAndRate]] = empty_list()
    maxDosePerPeriod: Optional[Ratio] = None
    maxDosePerAdministration: Optional[Quantity] = None
    maxDosePerLifetime: Optional[Quantity] = None

    def elementProperties(self):
        js = super(Dosage, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, False),
            ("text", "text", str, False, None, False),
            ("additionalInstruction", "additionalInstruction", CodeableConcept, True, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("timing", "timing", Timing, False, None, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", CodeableConcept, False, "asNeeded", False),
            ("site", "site", CodeableConcept, False, None, False),
            ("route", "route", CodeableConcept, False, None, False),
            ("method", "method", CodeableConcept, False, None, False),
            ("doseAndRate", "doseAndRate", DosageDoseAndRate, True, None, False),
            ("maxDosePerPeriod", "maxDosePerPeriod", Ratio, False, None, False),
            ("maxDosePerAdministration", "maxDosePerAdministration", Quantity, False, None, False),
            ("maxDosePerLifetime", "maxDosePerLifetime", Quantity, False, None, False),
        ])
        return js