#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/RiskAssessment) on 2019-08-06.
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
from .period import Period
from .range import Range


@dataclass
class RiskAssessmentPrediction(BackboneElement):
    """ Outcome predicted.

    Describes the expected outcome for the subject.
    """
    resource_type: ClassVar[str] = "RiskAssessmentPrediction"
    outcome: Optional[CodeableConcept] = None
    probabilityDecimal: Optional[float] = None
    probabilityRange: Optional[Range] = None
    qualitativeRisk: Optional[CodeableConcept] = None
    relativeRisk: Optional[float] = None
    whenPeriod: Optional[Period] = None
    whenRange: Optional[Range] = None
    rationale: Optional[str] = None

    def elementProperties(self):
        js = super(RiskAssessmentPrediction, self).elementProperties()
        js.extend([
            ("outcome", "outcome", CodeableConcept, False, None, False),
            ("probabilityDecimal", "probabilityDecimal", float, False, "probability", False),
            ("probabilityRange", "probabilityRange", Range, False, "probability", False),
            ("qualitativeRisk", "qualitativeRisk", CodeableConcept, False, None, False),
            ("relativeRisk", "relativeRisk", float, False, None, False),
            ("whenPeriod", "whenPeriod", Period, False, "when", False),
            ("whenRange", "whenRange", Range, False, "when", False),
            ("rationale", "rationale", str, False, None, False),
        ])
        return js


@dataclass
class RiskAssessment(DomainResource):
    """ Potential outcomes for a subject with likelihood.

    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """
    resource_type: ClassVar[str] = "RiskAssessment"
    identifier: Optional[List[Identifier]] = empty_list()
    basedOn: Optional[FHIRReference] = None
    parent: Optional[FHIRReference] = None
    status: str = None
    method: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = None
    occurrencePeriod: Optional[Period] = None
    condition: Optional[FHIRReference] = None
    performer: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    basis: Optional[List[FHIRReference]] = empty_list()
    prediction: Optional[List[RiskAssessmentPrediction]] = empty_list()
    mitigation: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()

    def elementProperties(self):
        js = super(RiskAssessment, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("basedOn", "basedOn", FHIRReference, False, None, False),
            ("parent", "parent", FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("method", "method", CodeableConcept, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", Period, False, "occurrence", False),
            ("condition", "condition", FHIRReference, False, None, False),
            ("performer", "performer", FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("basis", "basis", FHIRReference, True, None, False),
            ("prediction", "prediction", RiskAssessmentPrediction, True, None, False),
            ("mitigation", "mitigation", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
        ])
        return js