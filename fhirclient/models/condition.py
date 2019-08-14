#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Condition) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .age import Age
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
class ConditionStage(BackboneElement):
    """ Stage/grade, usually assessed formally.

    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """
    resource_type: ClassVar[str] = "ConditionStage"
    summary: Optional[CodeableConcept] = None
    assessment: Optional[List[FHIRReference]] = empty_list()
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ConditionStage, self).elementProperties()
        js.extend([
            ("summary", "summary", CodeableConcept, False, None, False),
            ("assessment", "assessment", FHIRReference, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ConditionEvidence(BackboneElement):
    """ Supporting evidence.

    Supporting evidence / manifestations that are the basis of the Condition's
    verification status, such as evidence that confirmed or refuted the
    condition.
    """
    resource_type: ClassVar[str] = "ConditionEvidence"
    code: Optional[List[CodeableConcept]] = empty_list()
    detail: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(ConditionEvidence, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, True, None, False),
            ("detail", "detail", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class Condition(DomainResource):
    """ Detailed information about conditions, problems or diagnoses.

    A clinical condition, problem, diagnosis, or other event, situation, issue,
    or clinical concept that has risen to a level of concern.
    """
    resource_type: ClassVar[str] = "Condition"
    identifier: Optional[List[Identifier]] = empty_list()
    clinicalStatus: Optional[CodeableConcept] = None
    verificationStatus: Optional[CodeableConcept] = None
    category: Optional[List[CodeableConcept]] = empty_list()
    severity: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    bodySite: Optional[List[CodeableConcept]] = empty_list()
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    onsetDateTime: Optional[FHIRDate] = None
    onsetAge: Optional[Age] = None
    onsetPeriod: Optional[Period] = None
    onsetRange: Optional[Range] = None
    onsetString: Optional[str] = None
    abatementDateTime: Optional[FHIRDate] = None
    abatementAge: Optional[Age] = None
    abatementPeriod: Optional[Period] = None
    abatementRange: Optional[Range] = None
    abatementString: Optional[str] = None
    recordedDate: Optional[FHIRDate] = None
    recorder: Optional[FHIRReference] = None
    asserter: Optional[FHIRReference] = None
    stage: Optional[List[ConditionStage]] = empty_list()
    evidence: Optional[List[ConditionEvidence]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()

    def elementProperties(self):
        js = super(Condition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("clinicalStatus", "clinicalStatus", CodeableConcept, False, None, False),
            ("verificationStatus", "verificationStatus", CodeableConcept, False, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("severity", "severity", CodeableConcept, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("bodySite", "bodySite", CodeableConcept, True, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("onsetDateTime", "onsetDateTime", FHIRDate, False, "onset", False),
            ("onsetAge", "onsetAge", Age, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", Period, False, "onset", False),
            ("onsetRange", "onsetRange", Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("abatementDateTime", "abatementDateTime", FHIRDate, False, "abatement", False),
            ("abatementAge", "abatementAge", Age, False, "abatement", False),
            ("abatementPeriod", "abatementPeriod", Period, False, "abatement", False),
            ("abatementRange", "abatementRange", Range, False, "abatement", False),
            ("abatementString", "abatementString", str, False, "abatement", False),
            ("recordedDate", "recordedDate", FHIRDate, False, None, False),
            ("recorder", "recorder", FHIRReference, False, None, False),
            ("asserter", "asserter", FHIRReference, False, None, False),
            ("stage", "stage", ConditionStage, True, None, False),
            ("evidence", "evidence", ConditionEvidence, True, None, False),
            ("note", "note", Annotation, True, None, False),
        ])
        return js