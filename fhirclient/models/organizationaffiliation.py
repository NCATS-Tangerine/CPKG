#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/OrganizationAffiliation) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class OrganizationAffiliation(DomainResource):
    """ Defines an affiliation/assotiation/relationship between 2 distinct
    oganizations, that is not a part-of relationship/sub-division relationship.
    """
    resource_type: ClassVar[str] = "OrganizationAffiliation"
    identifier: Optional[List[Identifier]] = empty_list()
    active: Optional[bool] = None
    period: Optional[Period] = None
    organization: Optional[FHIRReference] = None
    participatingOrganization: Optional[FHIRReference] = None
    network: Optional[List[FHIRReference]] = empty_list()
    code: Optional[List[CodeableConcept]] = empty_list()
    specialty: Optional[List[CodeableConcept]] = empty_list()
    location: Optional[List[FHIRReference]] = empty_list()
    healthcareService: Optional[List[FHIRReference]] = empty_list()
    telecom: Optional[List[ContactPoint]] = empty_list()
    endpoint: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(OrganizationAffiliation, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("active", "active", bool, False, None, False),
            ("period", "period", Period, False, None, False),
            ("organization", "organization", FHIRReference, False, None, False),
            ("participatingOrganization", "participatingOrganization", FHIRReference, False, None, False),
            ("network", "network", FHIRReference, True, None, False),
            ("code", "code", CodeableConcept, True, None, False),
            ("specialty", "specialty", CodeableConcept, True, None, False),
            ("location", "location", FHIRReference, True, None, False),
            ("healthcareService", "healthcareService", FHIRReference, True, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
            ("endpoint", "endpoint", FHIRReference, True, None, False),
        ])
        return js