#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ServiceRequest) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .timing import Timing


@dataclass
class ServiceRequest(DomainResource):
    """ A request for a service to be performed.

    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
    """
    resource_type: ClassVar[str] = "ServiceRequest"
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    basedOn: Optional[List[FHIRReference]] = empty_list()
    replaces: Optional[List[FHIRReference]] = empty_list()
    requisition: Optional[Identifier] = None
    status: str = None
    intent: str = None
    category: Optional[List[CodeableConcept]] = empty_list()
    priority: Optional[str] = None
    doNotPerform: Optional[bool] = None
    code: Optional[CodeableConcept] = None
    orderDetail: Optional[List[CodeableConcept]] = empty_list()
    quantityQuantity: Optional[Quantity] = None
    quantityRatio: Optional[Ratio] = None
    quantityRange: Optional[Range] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = None
    occurrencePeriod: Optional[Period] = None
    occurrenceTiming: Optional[Timing] = None
    asNeededBoolean: Optional[bool] = None
    asNeededCodeableConcept: Optional[CodeableConcept] = None
    authoredOn: Optional[FHIRDate] = None
    requester: Optional[FHIRReference] = None
    performerType: Optional[CodeableConcept] = None
    performer: Optional[List[FHIRReference]] = empty_list()
    locationCode: Optional[List[CodeableConcept]] = empty_list()
    locationReference: Optional[List[FHIRReference]] = empty_list()
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    insurance: Optional[List[FHIRReference]] = empty_list()
    supportingInfo: Optional[List[FHIRReference]] = empty_list()
    specimen: Optional[List[FHIRReference]] = empty_list()
    bodySite: Optional[List[CodeableConcept]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    patientInstruction: Optional[str] = None
    relevantHistory: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(ServiceRequest, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("replaces", "replaces", FHIRReference, True, None, False),
            ("requisition", "requisition", Identifier, False, None, False),
            ("status", "status", str, False, None, True),
            ("intent", "intent", str, False, None, True),
            ("category", "category", CodeableConcept, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("orderDetail", "orderDetail", CodeableConcept, True, None, False),
            ("quantityQuantity", "quantityQuantity", Quantity, False, "quantity", False),
            ("quantityRatio", "quantityRatio", Ratio, False, "quantity", False),
            ("quantityRange", "quantityRange", Range, False, "quantity", False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", Timing, False, "occurrence", False),
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", CodeableConcept, False, "asNeeded", False),
            ("authoredOn", "authoredOn", FHIRDate, False, None, False),
            ("requester", "requester", FHIRReference, False, None, False),
            ("performerType", "performerType", CodeableConcept, False, None, False),
            ("performer", "performer", FHIRReference, True, None, False),
            ("locationCode", "locationCode", CodeableConcept, True, None, False),
            ("locationReference", "locationReference", FHIRReference, True, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("insurance", "insurance", FHIRReference, True, None, False),
            ("supportingInfo", "supportingInfo", FHIRReference, True, None, False),
            ("specimen", "specimen", FHIRReference, True, None, False),
            ("bodySite", "bodySite", CodeableConcept, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("relevantHistory", "relevantHistory", FHIRReference, True, None, False),
        ])
        return js