#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory) on 2019-08-06.
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
class FamilyMemberHistoryCondition(BackboneElement):
    """ Condition that the related person had.

    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """
    resource_type: ClassVar[str] = "FamilyMemberHistoryCondition"
    code: CodeableConcept = None
    outcome: Optional[CodeableConcept] = None
    contributedToDeath: Optional[bool] = None
    onsetAge: Optional[Age] = None
    onsetRange: Optional[Range] = None
    onsetPeriod: Optional[Period] = None
    onsetString: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()

    def elementProperties(self):
        js = super(FamilyMemberHistoryCondition, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("outcome", "outcome", CodeableConcept, False, None, False),
            ("contributedToDeath", "contributedToDeath", bool, False, None, False),
            ("onsetAge", "onsetAge", Age, False, "onset", False),
            ("onsetRange", "onsetRange", Range, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", Period, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("note", "note", Annotation, True, None, False),
        ])
        return js


@dataclass
class FamilyMemberHistoryProcedure(BackboneElement):
    """ Procedures that the related person had.

    The significant Procedures (or procedure) that the family member had. This
    is a repeating section to allow a system to represent more than one
    procedure per resource, though there is nothing stopping multiple resources
    - one per procedure.
    """
    resource_type: ClassVar[str] = "FamilyMemberHistoryProcedure"
    code: CodeableConcept = None
    outcome: Optional[CodeableConcept] = None
    contributedToDeath: Optional[bool] = None
    performedAge: Optional[Age] = None
    performedRange: Optional[Range] = None
    performedPeriod: Optional[Period] = None
    performedString: Optional[str] = None
    performedDateTime: Optional[FHIRDate] = None
    note: Optional[List[Annotation]] = empty_list()

    def elementProperties(self):
        js = super(FamilyMemberHistoryProcedure, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("outcome", "outcome", CodeableConcept, False, None, False),
            ("contributedToDeath", "contributedToDeath", bool, False, None, False),
            ("performedAge", "performedAge", Age, False, "performed", False),
            ("performedRange", "performedRange", Range, False, "performed", False),
            ("performedPeriod", "performedPeriod", Period, False, "performed", False),
            ("performedString", "performedString", str, False, "performed", False),
            ("performedDateTime", "performedDateTime", FHIRDate, False, "performed", False),
            ("note", "note", Annotation, True, None, False),
        ])
        return js


@dataclass
class FamilyMemberHistory(DomainResource):
    """ Information about patient's relatives, relevant for patient.

    Significant health conditions for a person related to the patient relevant
    in the context of care for the patient.
    """
    resource_type: ClassVar[str] = "FamilyMemberHistory"
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    status: str = None
    dataAbsentReason: Optional[CodeableConcept] = None
    patient: FHIRReference = None
    date: Optional[FHIRDate] = None
    name: Optional[str] = None
    relationship: CodeableConcept = None
    sex: Optional[CodeableConcept] = None
    bornPeriod: Optional[Period] = None
    bornDate: Optional[FHIRDate] = None
    bornString: Optional[str] = None
    ageAge: Optional[Age] = None
    ageRange: Optional[Range] = None
    ageString: Optional[str] = None
    estimatedAge: Optional[bool] = None
    deceasedBoolean: Optional[bool] = None
    deceasedAge: Optional[Age] = None
    deceasedRange: Optional[Range] = None
    deceasedDate: Optional[FHIRDate] = None
    deceasedString: Optional[str] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    condition: Optional[List[FamilyMemberHistoryCondition]] = empty_list()
    procedure: Optional[List[FamilyMemberHistoryProcedure]] = empty_list()

    def elementProperties(self):
        js = super(FamilyMemberHistory, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("status", "status", str, False, None, True),
            ("dataAbsentReason", "dataAbsentReason", CodeableConcept, False, None, False),
            ("patient", "patient", FHIRReference, False, None, True),
            ("date", "date", FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("relationship", "relationship", CodeableConcept, False, None, True),
            ("sex", "sex", CodeableConcept, False, None, False),
            ("bornPeriod", "bornPeriod", Period, False, "born", False),
            ("bornDate", "bornDate", FHIRDate, False, "born", False),
            ("bornString", "bornString", str, False, "born", False),
            ("ageAge", "ageAge", Age, False, "age", False),
            ("ageRange", "ageRange", Range, False, "age", False),
            ("ageString", "ageString", str, False, "age", False),
            ("estimatedAge", "estimatedAge", bool, False, None, False),
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False),
            ("deceasedAge", "deceasedAge", Age, False, "deceased", False),
            ("deceasedRange", "deceasedRange", Range, False, "deceased", False),
            ("deceasedDate", "deceasedDate", FHIRDate, False, "deceased", False),
            ("deceasedString", "deceasedString", str, False, "deceased", False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("condition", "condition", FamilyMemberHistoryCondition, True, None, False),
            ("procedure", "procedure", FamilyMemberHistoryProcedure, True, None, False),
        ])
        return js