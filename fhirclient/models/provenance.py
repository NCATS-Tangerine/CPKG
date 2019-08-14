#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Provenance) on 2019-08-06.
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
from .period import Period
from .signature import Signature


@dataclass
class ProvenanceAgent(BackboneElement):
    """ Actor involved.

    An actor taking a role in an activity  for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    resource_type: ClassVar[str] = "ProvenanceAgent"
    type: Optional[CodeableConcept] = None
    role: Optional[List[CodeableConcept]] = empty_list()
    who: FHIRReference = None
    onBehalfOf: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(ProvenanceAgent, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("role", "role", CodeableConcept, True, None, False),
            ("who", "who", FHIRReference, False, None, True),
            ("onBehalfOf", "onBehalfOf", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class ProvenanceEntity(BackboneElement):
    """ An entity used in this activity.
    """
    resource_type: ClassVar[str] = "ProvenanceEntity"
    role: str = None
    what: FHIRReference = None
    agent: Optional[List[ProvenanceAgent]] = empty_list()

    def elementProperties(self):
        js = super(ProvenanceEntity, self).elementProperties()
        js.extend([
            ("role", "role", str, False, None, True),
            ("what", "what", FHIRReference, False, None, True),
            ("agent", "agent", ProvenanceAgent, True, None, False),
        ])
        return js


@dataclass
class Provenance(DomainResource):
    """ Who, What, When for a set of resources.

    Provenance of a resource is a record that describes entities and processes
    involved in producing and delivering or otherwise influencing that
    resource. Provenance provides a critical foundation for assessing
    authenticity, enabling trust, and allowing reproducibility. Provenance
    assertions are a form of contextual metadata and can themselves become
    important records with their own provenance. Provenance statement indicates
    clinical significance in terms of confidence in authenticity, reliability,
    and trustworthiness, integrity, and stage in lifecycle (e.g. Document
    Completion - has the artifact been legally authenticated), all of which may
    impact security, privacy, and trust policies.
    """
    resource_type: ClassVar[str] = "Provenance"
    target: List[FHIRReference] = empty_list()
    occurredPeriod: Optional[Period] = None
    occurredDateTime: Optional[FHIRDate] = None
    recorded: FHIRDate = None
    policy: Optional[List[str]] = empty_list()
    location: Optional[FHIRReference] = None
    reason: Optional[List[CodeableConcept]] = empty_list()
    activity: Optional[CodeableConcept] = None
    agent: List[ProvenanceAgent] = empty_list()
    entity: Optional[List[ProvenanceEntity]] = empty_list()
    signature: Optional[List[Signature]] = empty_list()

    def elementProperties(self):
        js = super(Provenance, self).elementProperties()
        js.extend([
            ("target", "target", FHIRReference, True, None, True),
            ("occurredPeriod", "occurredPeriod", Period, False, "occurred", False),
            ("occurredDateTime", "occurredDateTime", FHIRDate, False, "occurred", False),
            ("recorded", "recorded", FHIRDate, False, None, True),
            ("policy", "policy", str, True, None, False),
            ("location", "location", FHIRReference, False, None, False),
            ("reason", "reason", CodeableConcept, True, None, False),
            ("activity", "activity", CodeableConcept, False, None, False),
            ("agent", "agent", ProvenanceAgent, True, None, True),
            ("entity", "entity", ProvenanceEntity, True, None, False),
            ("signature", "signature", Signature, True, None, False),
        ])
        return js