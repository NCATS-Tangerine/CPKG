#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation) on 2019-08-06.
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


@dataclass
class ImmunizationRecommendationRecommendationDateCriterion(BackboneElement):
    """ Dates governing proposed immunization.

    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendationRecommendationDateCriterion"
    code: CodeableConcept = None
    value: FHIRDate = None

    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendationDateCriterion, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("value", "value", FHIRDate, False, None, True),
        ])
        return js


@dataclass
class ImmunizationRecommendationRecommendation(BackboneElement):
    """ Vaccine administration recommendations.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendationRecommendation"
    vaccineCode: Optional[List[CodeableConcept]] = empty_list()
    targetDisease: Optional[List[CodeableConcept]] = empty_list()
    contraindicatedVaccineCode: Optional[List[CodeableConcept]] = empty_list()
    forecastStatus: CodeableConcept = None
    forecastReason: Optional[List[CodeableConcept]] = empty_list()
    dateCriterion: Optional[List[ImmunizationRecommendationRecommendationDateCriterion]] = empty_list()
    description: Optional[str] = None
    series: Optional[str] = None
    doseNumberPositiveInt: Optional[int] = None
    doseNumberString: Optional[str] = None
    seriesDosesPositiveInt: Optional[int] = None
    seriesDosesString: Optional[str] = None
    supportingImmunization: Optional[List[FHIRReference]] = empty_list()
    supportingPatientInformation: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendation, self).elementProperties()
        js.extend([
            ("vaccineCode", "vaccineCode", CodeableConcept, True, None, False),
            ("targetDisease", "targetDisease", CodeableConcept, True, None, False),
            ("contraindicatedVaccineCode", "contraindicatedVaccineCode", CodeableConcept, True, None, False),
            ("forecastStatus", "forecastStatus", CodeableConcept, False, None, True),
            ("forecastReason", "forecastReason", CodeableConcept, True, None, False),
            ("dateCriterion", "dateCriterion", ImmunizationRecommendationRecommendationDateCriterion, True, None, False),
            ("description", "description", str, False, None, False),
            ("series", "series", str, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("supportingImmunization", "supportingImmunization", FHIRReference, True, None, False),
            ("supportingPatientInformation", "supportingPatientInformation", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class ImmunizationRecommendation(DomainResource):
    """ Guidance or advice relating to an immunization.

    A patient's point-in-time set of recommendations (i.e. forecasting)
    according to a published schedule with optional supporting justification.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendation"
    identifier: Optional[List[Identifier]] = empty_list()
    patient: FHIRReference = None
    date: FHIRDate = None
    authority: Optional[FHIRReference] = None
    recommendation: List[ImmunizationRecommendationRecommendation] = empty_list()

    def elementProperties(self):
        js = super(ImmunizationRecommendation, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("patient", "patient", FHIRReference, False, None, True),
            ("date", "date", FHIRDate, False, None, True),
            ("authority", "authority", FHIRReference, False, None, False),
            ("recommendation", "recommendation", ImmunizationRecommendationRecommendation, True, None, True),
        ])
        return js