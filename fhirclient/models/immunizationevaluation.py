#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class ImmunizationEvaluation(DomainResource):
    """ Immunization evaluation information.

    Describes a comparison of an immunization event against published
    recommendations to determine if the administration is "valid" in relation
    to those  recommendations.
    """
    resource_type: ClassVar[str] = "ImmunizationEvaluation"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    patient: FHIRReference = None
    date: Optional[FHIRDate] = None
    authority: Optional[FHIRReference] = None
    targetDisease: CodeableConcept = None
    immunizationEvent: FHIRReference = None
    doseStatus: CodeableConcept = None
    doseStatusReason: Optional[List[CodeableConcept]] = empty_list()
    description: Optional[str] = None
    series: Optional[str] = None
    doseNumberPositiveInt: Optional[int] = None
    doseNumberString: Optional[str] = None
    seriesDosesPositiveInt: Optional[int] = None
    seriesDosesString: Optional[str] = None

    def elementProperties(self):
        js = super(ImmunizationEvaluation, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("patient", "patient", FHIRReference, False, None, True),
            ("date", "date", FHIRDate, False, None, False),
            ("authority", "authority", FHIRReference, False, None, False),
            ("targetDisease", "targetDisease", CodeableConcept, False, None, True),
            ("immunizationEvent", "immunizationEvent", FHIRReference, False, None, True),
            ("doseStatus", "doseStatus", CodeableConcept, False, None, True),
            ("doseStatusReason", "doseStatusReason", CodeableConcept, True, None, False),
            ("description", "description", str, False, None, False),
            ("series", "series", str, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
        ])
        return js