#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Goal) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .range import Range
from .ratio import Ratio


@dataclass
class GoalTarget(BackboneElement):
    """ Target outcome for the goal.

    Indicates what should be done by when.
    """
    resource_type: ClassVar[str] = "GoalTarget"
    measure: Optional[CodeableConcept] = None
    detailQuantity: Optional[Quantity] = None
    detailRange: Optional[Range] = None
    detailCodeableConcept: Optional[CodeableConcept] = None
    detailString: Optional[str] = None
    detailBoolean: Optional[bool] = None
    detailInteger: Optional[int] = None
    detailRatio: Optional[Ratio] = None
    dueDate: Optional[FHIRDate] = None
    dueDuration: Optional[Duration] = None

    def elementProperties(self):
        js = super(GoalTarget, self).elementProperties()
        js.extend([
            ("measure", "measure", CodeableConcept, False, None, False),
            ("detailQuantity", "detailQuantity", Quantity, False, "detail", False),
            ("detailRange", "detailRange", Range, False, "detail", False),
            ("detailCodeableConcept", "detailCodeableConcept", CodeableConcept, False, "detail", False),
            ("detailString", "detailString", str, False, "detail", False),
            ("detailBoolean", "detailBoolean", bool, False, "detail", False),
            ("detailInteger", "detailInteger", int, False, "detail", False),
            ("detailRatio", "detailRatio", Ratio, False, "detail", False),
            ("dueDate", "dueDate", FHIRDate, False, "due", False),
            ("dueDuration", "dueDuration", Duration, False, "due", False),
        ])
        return js


@dataclass
class Goal(DomainResource):
    """ Describes the intended objective(s) for a patient, group or organization.

    Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """
    resource_type: ClassVar[str] = "Goal"
    identifier: Optional[List[Identifier]] = empty_list()
    lifecycleStatus: str = None
    achievementStatus: Optional[CodeableConcept] = None
    category: Optional[List[CodeableConcept]] = empty_list()
    continuous: Optional[bool] = None
    priority: Optional[CodeableConcept] = None
    description: CodeableConcept = None
    subject: FHIRReference = None
    startDate: Optional[FHIRDate] = None
    startCodeableConcept: Optional[CodeableConcept] = None
    target: Optional[List[GoalTarget]] = empty_list()
    statusDate: Optional[FHIRDate] = None
    statusReason: Optional[str] = None
    expressedBy: Optional[FHIRReference] = None
    addresses: Optional[List[FHIRReference]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    outcomeCode: Optional[List[CodeableConcept]] = empty_list()
    outcomeReference: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(Goal, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("lifecycleStatus", "lifecycleStatus", str, False, None, True),
            ("achievementStatus", "achievementStatus", CodeableConcept, False, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("continuous", "continuous", bool, False, None, False),
            ("priority", "priority", CodeableConcept, False, None, False),
            ("description", "description", CodeableConcept, False, None, True),
            ("subject", "subject", FHIRReference, False, None, True),
            ("startDate", "startDate", FHIRDate, False, "start", False),
            ("startCodeableConcept", "startCodeableConcept", CodeableConcept, False, "start", False),
            ("target", "target", GoalTarget, True, None, False),
            ("statusDate", "statusDate", FHIRDate, False, None, False),
            ("statusReason", "statusReason", str, False, None, False),
            ("expressedBy", "expressedBy", FHIRReference, False, None, False),
            ("addresses", "addresses", FHIRReference, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("outcomeCode", "outcomeCode", CodeableConcept, True, None, False),
            ("outcomeReference", "outcomeReference", FHIRReference, True, None, False),
        ])
        return js