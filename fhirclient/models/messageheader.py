#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/MessageHeader) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirreference import FHIRReference


@dataclass
class MessageHeaderDestination(BackboneElement):
    """ Message destination application(s).

    The destination application which the message is intended for.
    """
    resource_type: ClassVar[str] = "MessageHeaderDestination"
    name: Optional[str] = None
    target: Optional[FHIRReference] = None
    endpoint: str = None
    receiver: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(MessageHeaderDestination, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("target", "target", FHIRReference, False, None, False),
            ("endpoint", "endpoint", str, False, None, True),
            ("receiver", "receiver", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class MessageHeaderSource(BackboneElement):
    """ Message source application.

    The source application from which this message originated.
    """
    resource_type: ClassVar[str] = "MessageHeaderSource"
    name: Optional[str] = None
    software: Optional[str] = None
    version: Optional[str] = None
    contact: Optional[ContactPoint] = None
    endpoint: str = None

    def elementProperties(self):
        js = super(MessageHeaderSource, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("software", "software", str, False, None, False),
            ("version", "version", str, False, None, False),
            ("contact", "contact", ContactPoint, False, None, False),
            ("endpoint", "endpoint", str, False, None, True),
        ])
        return js


@dataclass
class MessageHeaderResponse(BackboneElement):
    """ If this is a reply to prior message.

    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """
    resource_type: ClassVar[str] = "MessageHeaderResponse"
    identifier: str = None
    code: str = None
    details: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(MessageHeaderResponse, self).elementProperties()
        js.extend([
            ("identifier", "identifier", str, False, None, True),
            ("code", "code", str, False, None, True),
            ("details", "details", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class MessageHeader(DomainResource):
    """ A resource that describes a message that is exchanged between systems.

    The header for a message exchange that is either requesting or responding
    to an action.  The reference(s) that are the subject of the action as well
    as other information related to the action are typically transmitted in a
    bundle in which the MessageHeader resource instance is the first resource
    in the bundle.
    """
    resource_type: ClassVar[str] = "MessageHeader"
    eventCoding: Coding = None
    eventUri: str = None
    destination: Optional[List[MessageHeaderDestination]] = empty_list()
    sender: Optional[FHIRReference] = None
    enterer: Optional[FHIRReference] = None
    author: Optional[FHIRReference] = None
    source: MessageHeaderSource = None
    responsible: Optional[FHIRReference] = None
    reason: Optional[CodeableConcept] = None
    response: Optional[MessageHeaderResponse] = None
    focus: Optional[List[FHIRReference]] = empty_list()
    definition: Optional[str] = None

    def elementProperties(self):
        js = super(MessageHeader, self).elementProperties()
        js.extend([
            ("eventCoding", "eventCoding", Coding, False, "event", True),
            ("eventUri", "eventUri", str, False, "event", True),
            ("destination", "destination", MessageHeaderDestination, True, None, False),
            ("sender", "sender", FHIRReference, False, None, False),
            ("enterer", "enterer", FHIRReference, False, None, False),
            ("author", "author", FHIRReference, False, None, False),
            ("source", "source", MessageHeaderSource, False, None, True),
            ("responsible", "responsible", FHIRReference, False, None, False),
            ("reason", "reason", CodeableConcept, False, None, False),
            ("response", "response", MessageHeaderResponse, False, None, False),
            ("focus", "focus", FHIRReference, True, None, False),
            ("definition", "definition", str, False, None, False),
        ])
        return js