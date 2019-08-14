#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/AuditEvent) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .period import Period


@dataclass
class AuditEventEntityDetail(BackboneElement):
    """ Additional Information about the entity.

    Tagged value pairs for conveying additional information about the entity.
    """
    resource_type: ClassVar[str] = "AuditEventEntityDetail"
    type: str = None
    valueString: str = None
    valueBase64Binary: str = None

    def elementProperties(self):
        js = super(AuditEventEntityDetail, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
        ])
        return js


@dataclass
class AuditEventAgentNetwork(BackboneElement):
    """ Logical network location for application activity.

    Logical network location for application activity, if the activity has a
    network location.
    """
    resource_type: ClassVar[str] = "AuditEventAgentNetwork"
    address: Optional[str] = None
    type: Optional[str] = None

    def elementProperties(self):
        js = super(AuditEventAgentNetwork, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


@dataclass
class AuditEventAgent(BackboneElement):
    """ Actor involved in the event.

    An actor taking an active role in the event or activity that is logged.
    """
    resource_type: ClassVar[str] = "AuditEventAgent"
    type: Optional[CodeableConcept] = None
    role: Optional[List[CodeableConcept]] = empty_list()
    who: Optional[FHIRReference] = None
    altId: Optional[str] = None
    name: Optional[str] = None
    requestor: bool = None
    location: Optional[FHIRReference] = None
    policy: Optional[List[str]] = empty_list()
    media: Optional[Coding] = None
    network: Optional[AuditEventAgentNetwork] = None
    purposeOfUse: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(AuditEventAgent, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("role", "role", CodeableConcept, True, None, False),
            ("who", "who", FHIRReference, False, None, False),
            ("altId", "altId", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("requestor", "requestor", bool, False, None, True),
            ("location", "location", FHIRReference, False, None, False),
            ("policy", "policy", str, True, None, False),
            ("media", "media", Coding, False, None, False),
            ("network", "network", AuditEventAgentNetwork, False, None, False),
            ("purposeOfUse", "purposeOfUse", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class AuditEventSource(BackboneElement):
    """ Audit Event Reporter.

    The system that is reporting the event.
    """
    resource_type: ClassVar[str] = "AuditEventSource"
    site: Optional[str] = None
    observer: FHIRReference = None
    type: Optional[List[Coding]] = empty_list()

    def elementProperties(self):
        js = super(AuditEventSource, self).elementProperties()
        js.extend([
            ("site", "site", str, False, None, False),
            ("observer", "observer", FHIRReference, False, None, True),
            ("type", "type", Coding, True, None, False),
        ])
        return js


@dataclass
class AuditEventEntity(BackboneElement):
    """ Data or objects used.

    Specific instances of data or objects that have been accessed.
    """
    resource_type: ClassVar[str] = "AuditEventEntity"
    what: Optional[FHIRReference] = None
    type: Optional[Coding] = None
    role: Optional[Coding] = None
    lifecycle: Optional[Coding] = None
    securityLabel: Optional[List[Coding]] = empty_list()
    name: Optional[str] = None
    description: Optional[str] = None
    query: Optional[str] = None
    detail: Optional[List[AuditEventEntityDetail]] = empty_list()

    def elementProperties(self):
        js = super(AuditEventEntity, self).elementProperties()
        js.extend([
            ("what", "what", FHIRReference, False, None, False),
            ("type", "type", Coding, False, None, False),
            ("role", "role", Coding, False, None, False),
            ("lifecycle", "lifecycle", Coding, False, None, False),
            ("securityLabel", "securityLabel", Coding, True, None, False),
            ("name", "name", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("query", "query", str, False, None, False),
            ("detail", "detail", AuditEventEntityDetail, True, None, False),
        ])
        return js


@dataclass
class AuditEvent(DomainResource):
    """ Record of an event.

    A record of an event relevant for purposes such as operations, privacy,
    security, maintenance, and performance analysis.
    """
    resource_type: ClassVar[str] = "AuditEvent"
    type: Coding = None
    subtype: Optional[List[Coding]] = empty_list()
    action: Optional[str] = None
    period: Optional[Period] = None
    recorded: FHIRDate = None
    outcome: Optional[str] = None
    outcomeDesc: Optional[str] = None
    purposeOfEvent: Optional[List[CodeableConcept]] = empty_list()
    agent: List[AuditEventAgent] = empty_list()
    source: AuditEventSource = None
    entity: Optional[List[AuditEventEntity]] = empty_list()

    def elementProperties(self):
        js = super(AuditEvent, self).elementProperties()
        js.extend([
            ("type", "type", Coding, False, None, True),
            ("subtype", "subtype", Coding, True, None, False),
            ("action", "action", str, False, None, False),
            ("period", "period", Period, False, None, False),
            ("recorded", "recorded", FHIRDate, False, None, True),
            ("outcome", "outcome", str, False, None, False),
            ("outcomeDesc", "outcomeDesc", str, False, None, False),
            ("purposeOfEvent", "purposeOfEvent", CodeableConcept, True, None, False),
            ("agent", "agent", AuditEventAgent, True, None, True),
            ("source", "source", AuditEventSource, False, None, True),
            ("entity", "entity", AuditEventEntity, True, None, False),
        ])
        return js