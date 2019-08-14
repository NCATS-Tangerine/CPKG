#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/DeviceRequest) on 2019-08-06.
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
from .range import Range
from .timing import Timing


@dataclass
class DeviceRequestParameter(BackboneElement):
    """ Device details.

    Specific parameters for the ordered item.  For example, the prism value for
    lenses.
    """
    resource_type: ClassVar[str] = "DeviceRequestParameter"
    code: Optional[CodeableConcept] = None
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueQuantity: Optional[Quantity] = None
    valueRange: Optional[Range] = None
    valueBoolean: Optional[bool] = None

    def elementProperties(self):
        js = super(DeviceRequestParameter, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
            ("valueRange", "valueRange", Range, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
        ])
        return js


@dataclass
class DeviceRequest(DomainResource):
    """ Medical device request.

    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """
    resource_type: ClassVar[str] = "DeviceRequest"
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    basedOn: Optional[List[FHIRReference]] = empty_list()
    priorRequest: Optional[List[FHIRReference]] = empty_list()
    groupIdentifier: Optional[Identifier] = None
    status: Optional[str] = None
    intent: str = None
    priority: Optional[str] = None
    codeReference: FHIRReference = None
    codeCodeableConcept: CodeableConcept = None
    parameter: Optional[List[DeviceRequestParameter]] = empty_list()
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = None
    occurrencePeriod: Optional[Period] = None
    occurrenceTiming: Optional[Timing] = None
    authoredOn: Optional[FHIRDate] = None
    requester: Optional[FHIRReference] = None
    performerType: Optional[CodeableConcept] = None
    performer: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    insurance: Optional[List[FHIRReference]] = empty_list()
    supportingInfo: Optional[List[FHIRReference]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    relevantHistory: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(DeviceRequest, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("priorRequest", "priorRequest", FHIRReference, True, None, False),
            ("groupIdentifier", "groupIdentifier", Identifier, False, None, False),
            ("status", "status", str, False, None, False),
            ("intent", "intent", str, False, None, True),
            ("priority", "priority", str, False, None, False),
            ("codeReference", "codeReference", FHIRReference, False, "code", True),
            ("codeCodeableConcept", "codeCodeableConcept", CodeableConcept, False, "code", True),
            ("parameter", "parameter", DeviceRequestParameter, True, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", Timing, False, "occurrence", False),
            ("authoredOn", "authoredOn", FHIRDate, False, None, False),
            ("requester", "requester", FHIRReference, False, None, False),
            ("performerType", "performerType", CodeableConcept, False, None, False),
            ("performer", "performer", FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("insurance", "insurance", FHIRReference, True, None, False),
            ("supportingInfo", "supportingInfo", FHIRReference, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("relevantHistory", "relevantHistory", FHIRReference, True, None, False),
        ])
        return js