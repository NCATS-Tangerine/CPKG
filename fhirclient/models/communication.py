#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Communication) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class CommunicationPayload(BackboneElement):
    """ Message payload.

    Text, attachment(s), or resource(s) that was communicated to the recipient.
    """
    resource_type: ClassVar[str] = "CommunicationPayload"
    contentAttachment: Attachment = None
    contentReference: FHIRReference = None
    contentCodeableConcept: CodeableConcept = None

    def elementProperties(self):
        js = super(CommunicationPayload, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", Attachment, False, "content", True),
            ("contentReference", "contentReference", FHIRReference, False, "content", True),
            ("contentCodeableConcept", "contentCodeableConcept", CodeableConcept, False, "content", True),
        ])
        return js


@dataclass
class Communication(DomainResource):
    """ A record of information transmitted from a sender to a receiver.

    An occurrence of information being transmitted; e.g. an alert that was sent
    to a responsible provider, a public health agency communication to a
    provider/reporter in response to a case report for a reportable condition.
    """
    resource_type: ClassVar[str] = "Communication"
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    basedOn: Optional[List[FHIRReference]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    inResponseTo: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    category: Optional[List[CodeableConcept]] = empty_list()
    priority: Optional[str] = None
    medium: Optional[List[CodeableConcept]] = empty_list()
    subject: Optional[FHIRReference] = None
    topic: Optional[CodeableConcept] = None
    about: Optional[List[FHIRReference]] = empty_list()
    encounter: Optional[FHIRReference] = None
    sent: Optional[FHIRDate] = None
    received: Optional[FHIRDate] = None
    recipient: Optional[List[FHIRReference]] = empty_list()
    sender: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    payload: Optional[List[CommunicationPayload]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()

    def elementProperties(self):
        js = super(Communication, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("inResponseTo", "inResponseTo", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", CodeableConcept, False, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("medium", "medium", CodeableConcept, True, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("topic", "topic", CodeableConcept, False, None, False),
            ("about", "about", FHIRReference, True, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("sent", "sent", FHIRDate, False, None, False),
            ("received", "received", FHIRDate, False, None, False),
            ("recipient", "recipient", FHIRReference, True, None, False),
            ("sender", "sender", FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("payload", "payload", CommunicationPayload, True, None, False),
            ("note", "note", Annotation, True, None, False),
        ])
        return js