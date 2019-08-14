#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/CarePlan) on 2019-08-06.
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
from .quantity import Quantity
from .timing import Timing


@dataclass
class CarePlanActivityDetail(BackboneElement):
    """ In-line definition of activity.

    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """
    resource_type: ClassVar[str] = "CarePlanActivityDetail"
    kind: Optional[str] = None
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    code: Optional[CodeableConcept] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    goal: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    doNotPerform: Optional[bool] = None
    scheduledTiming: Optional[Timing] = None
    scheduledPeriod: Optional[Period] = None
    scheduledString: Optional[str] = None
    location: Optional[FHIRReference] = None
    reportedBoolean: Optional[bool] = None
    reportedReference: Optional[FHIRReference] = None
    performer: Optional[List[FHIRReference]] = empty_list()
    productCodeableConcept: Optional[CodeableConcept] = None
    productReference: Optional[FHIRReference] = None
    dailyAmount: Optional[Quantity] = None
    quantity: Optional[Quantity] = None
    description: Optional[str] = None

    def elementProperties(self):
        js = super(CarePlanActivityDetail, self).elementProperties()
        js.extend([
            ("kind", "kind", str, False, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("goal", "goal", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", CodeableConcept, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("scheduledTiming", "scheduledTiming", Timing, False, "scheduled", False),
            ("scheduledPeriod", "scheduledPeriod", Period, False, "scheduled", False),
            ("scheduledString", "scheduledString", str, False, "scheduled", False),
            ("location", "location", FHIRReference, False, None, False),
            ("reportedBoolean", "reportedBoolean", bool, False, "reported", False),
            ("reportedReference", "reportedReference", FHIRReference, False, "reported", False),
            ("performer", "performer", FHIRReference, True, None, False),
            ("productCodeableConcept", "productCodeableConcept", CodeableConcept, False, "product", False),
            ("productReference", "productReference", FHIRReference, False, "product", False),
            ("dailyAmount", "dailyAmount", Quantity, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("description", "description", str, False, None, False),
        ])
        return js


@dataclass
class CarePlanActivity(BackboneElement):
    """ Action to occur or has occurred as part of plan.

    Identifies an action that has occurred or is a planned action to occur as
    part of the plan. For example, a medication to be used, lab tests to
    perform, self-monitoring that has occurred, education etc.
    """
    resource_type: ClassVar[str] = "CarePlanActivity"
    outcomeCodeableConcept: Optional[List[CodeableConcept]] = empty_list()
    outcomeReference: Optional[List[FHIRReference]] = empty_list()
    progress: Optional[List[Annotation]] = empty_list()
    reference: Optional[FHIRReference] = None
    detail: Optional[CarePlanActivityDetail] = None

    def elementProperties(self):
        js = super(CarePlanActivity, self).elementProperties()
        js.extend([
            ("outcomeCodeableConcept", "outcomeCodeableConcept", CodeableConcept, True, None, False),
            ("outcomeReference", "outcomeReference", FHIRReference, True, None, False),
            ("progress", "progress", Annotation, True, None, False),
            ("reference", "reference", FHIRReference, False, None, False),
            ("detail", "detail", CarePlanActivityDetail, False, None, False),
        ])
        return js


@dataclass
class CarePlan(DomainResource):
    """ Healthcare plan for patient or group.

    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    """
    resource_type: ClassVar[str] = "CarePlan"
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    basedOn: Optional[List[FHIRReference]] = empty_list()
    replaces: Optional[List[FHIRReference]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    intent: str = None
    category: Optional[List[CodeableConcept]] = empty_list()
    title: Optional[str] = None
    description: Optional[str] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    period: Optional[Period] = None
    created: Optional[FHIRDate] = None
    author: Optional[FHIRReference] = None
    contributor: Optional[List[FHIRReference]] = empty_list()
    careTeam: Optional[List[FHIRReference]] = empty_list()
    addressesCode: Optional[List[CodeableConcept]] = empty_list()
    addressesReference: Optional[List[FHIRReference]] = empty_list()
    supportingInfo: Optional[List[FHIRReference]] = empty_list()
    goal: Optional[List[FHIRReference]] = empty_list()
    activity: Optional[List[CarePlanActivity]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()

    def elementProperties(self):
        js = super(CarePlan, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("replaces", "replaces", FHIRReference, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("intent", "intent", str, False, None, True),
            ("category", "category", CodeableConcept, True, None, False),
            ("title", "title", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("period", "period", Period, False, None, False),
            ("created", "created", FHIRDate, False, None, False),
            ("author", "author", FHIRReference, False, None, False),
            ("contributor", "contributor", FHIRReference, True, None, False),
            ("careTeam", "careTeam", FHIRReference, True, None, False),
            ("addressesCode", "addressesCode", CodeableConcept, True, None, False),
            ("addressesReference", "addressesReference", FHIRReference, True, None, False),
            ("supportingInfo", "supportingInfo", FHIRReference, True, None, False),
            ("goal", "goal", FHIRReference, True, None, False),
            ("activity", "activity", CarePlanActivity, True, None, False),
            ("note", "note", Annotation, True, None, False),
        ])
        return js