#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/DetectedIssue) on 2019-08-06.
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
from .period import Period


@dataclass
class DetectedIssueEvidence(BackboneElement):
    """ Supporting evidence.

    Supporting evidence or manifestations that provide the basis for
    identifying the detected issue such as a GuidanceResponse or MeasureReport.
    """
    resource_type: ClassVar[str] = "DetectedIssueEvidence"
    code: Optional[List[CodeableConcept]] = empty_list()
    detail: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(DetectedIssueEvidence, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, True, None, False),
            ("detail", "detail", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class DetectedIssueMitigation(BackboneElement):
    """ Step taken to address.

    Indicates an action that has been taken or is committed to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """
    resource_type: ClassVar[str] = "DetectedIssueMitigation"
    action: CodeableConcept = None
    date: Optional[FHIRDate] = None
    author: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(DetectedIssueMitigation, self).elementProperties()
        js.extend([
            ("action", "action", CodeableConcept, False, None, True),
            ("date", "date", FHIRDate, False, None, False),
            ("author", "author", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class DetectedIssue(DomainResource):
    """ Clinical issue with action.

    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """
    resource_type: ClassVar[str] = "DetectedIssue"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    code: Optional[CodeableConcept] = None
    severity: Optional[str] = None
    patient: Optional[FHIRReference] = None
    identifiedDateTime: Optional[FHIRDate] = None
    identifiedPeriod: Optional[Period] = None
    author: Optional[FHIRReference] = None
    implicated: Optional[List[FHIRReference]] = empty_list()
    evidence: Optional[List[DetectedIssueEvidence]] = empty_list()
    detail: Optional[str] = None
    reference: Optional[str] = None
    mitigation: Optional[List[DetectedIssueMitigation]] = empty_list()

    def elementProperties(self):
        js = super(DetectedIssue, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("code", "code", CodeableConcept, False, None, False),
            ("severity", "severity", str, False, None, False),
            ("patient", "patient", FHIRReference, False, None, False),
            ("identifiedDateTime", "identifiedDateTime", FHIRDate, False, "identified", False),
            ("identifiedPeriod", "identifiedPeriod", Period, False, "identified", False),
            ("author", "author", FHIRReference, False, None, False),
            ("implicated", "implicated", FHIRReference, True, None, False),
            ("evidence", "evidence", DetectedIssueEvidence, True, None, False),
            ("detail", "detail", str, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("mitigation", "mitigation", DetectedIssueMitigation, True, None, False),
        ])
        return js