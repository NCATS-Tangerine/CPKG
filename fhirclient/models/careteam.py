#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/CareTeam) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class CareTeamParticipant(BackboneElement):
    """ Members of the team.

    Identifies all people and organizations who are expected to be involved in
    the care team.
    """
    resource_type: ClassVar[str] = "CareTeamParticipant"
    role: Optional[List[CodeableConcept]] = empty_list()
    member: Optional[FHIRReference] = None
    onBehalfOf: Optional[FHIRReference] = None
    period: Optional[Period] = None

    def elementProperties(self):
        js = super(CareTeamParticipant, self).elementProperties()
        js.extend([
            ("role", "role", CodeableConcept, True, None, False),
            ("member", "member", FHIRReference, False, None, False),
            ("onBehalfOf", "onBehalfOf", FHIRReference, False, None, False),
            ("period", "period", Period, False, None, False),
        ])
        return js


@dataclass
class CareTeam(DomainResource):
    """ Planned participants in the coordination and delivery of care.

    The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care.
    """
    resource_type: ClassVar[str] = "CareTeam"
    identifier: Optional[List[Identifier]] = empty_list()
    status: Optional[str] = None
    category: Optional[List[CodeableConcept]] = empty_list()
    name: Optional[str] = None
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    period: Optional[Period] = None
    participant: Optional[List[CareTeamParticipant]] = empty_list()
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    managingOrganization: Optional[List[FHIRReference]] = empty_list()
    telecom: Optional[List[ContactPoint]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()

    def elementProperties(self):
        js = super(CareTeam, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("period", "period", Period, False, None, False),
            ("participant", "participant", CareTeamParticipant, True, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("managingOrganization", "managingOrganization", FHIRReference, True, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
            ("note", "note", Annotation, True, None, False),
        ])
        return js