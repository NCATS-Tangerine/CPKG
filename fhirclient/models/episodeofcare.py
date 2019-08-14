#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/EpisodeOfCare) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class EpisodeOfCareStatusHistory(BackboneElement):
    """ Past list of status codes (the current status may be included to cover the
    start date of the status).

    The history of statuses that the EpisodeOfCare has been through (without
    requiring processing the history of the resource).
    """
    resource_type: ClassVar[str] = "EpisodeOfCareStatusHistory"
    status: str = None
    period: Period = None

    def elementProperties(self):
        js = super(EpisodeOfCareStatusHistory, self).elementProperties()
        js.extend([
            ("status", "status", str, False, None, True),
            ("period", "period", Period, False, None, True),
        ])
        return js


@dataclass
class EpisodeOfCareDiagnosis(BackboneElement):
    """ The list of diagnosis relevant to this episode of care.
    """
    resource_type: ClassVar[str] = "EpisodeOfCareDiagnosis"
    condition: FHIRReference = None
    role: Optional[CodeableConcept] = None
    rank: Optional[int] = None

    def elementProperties(self):
        js = super(EpisodeOfCareDiagnosis, self).elementProperties()
        js.extend([
            ("condition", "condition", FHIRReference, False, None, True),
            ("role", "role", CodeableConcept, False, None, False),
            ("rank", "rank", int, False, None, False),
        ])
        return js


@dataclass
class EpisodeOfCare(DomainResource):
    """ An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.

    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """
    resource_type: ClassVar[str] = "EpisodeOfCare"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    statusHistory: Optional[List[EpisodeOfCareStatusHistory]] = empty_list()
    type: Optional[List[CodeableConcept]] = empty_list()
    diagnosis: Optional[List[EpisodeOfCareDiagnosis]] = empty_list()
    patient: FHIRReference = None
    managingOrganization: Optional[FHIRReference] = None
    period: Optional[Period] = None
    referralRequest: Optional[List[FHIRReference]] = empty_list()
    careManager: Optional[FHIRReference] = None
    team: Optional[List[FHIRReference]] = empty_list()
    account: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(EpisodeOfCare, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusHistory", "statusHistory", EpisodeOfCareStatusHistory, True, None, False),
            ("type", "type", CodeableConcept, True, None, False),
            ("diagnosis", "diagnosis", EpisodeOfCareDiagnosis, True, None, False),
            ("patient", "patient", FHIRReference, False, None, True),
            ("managingOrganization", "managingOrganization", FHIRReference, False, None, False),
            ("period", "period", Period, False, None, False),
            ("referralRequest", "referralRequest", FHIRReference, True, None, False),
            ("careManager", "careManager", FHIRReference, False, None, False),
            ("team", "team", FHIRReference, True, None, False),
            ("account", "account", FHIRReference, True, None, False),
        ])
        return js