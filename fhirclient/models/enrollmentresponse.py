#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/EnrollmentResponse) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class EnrollmentResponse(DomainResource):
    """ EnrollmentResponse resource.

    This resource provides enrollment and plan details from the processing of
    an EnrollmentRequest resource.
    """
    resource_type: ClassVar[str] = "EnrollmentResponse"
    identifier: Optional[List[Identifier]] = empty_list()
    status: Optional[str] = None
    request: Optional[FHIRReference] = None
    outcome: Optional[str] = None
    disposition: Optional[str] = None
    created: Optional[FHIRDate] = None
    organization: Optional[FHIRReference] = None
    requestProvider: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(EnrollmentResponse, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, False),
            ("request", "request", FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("created", "created", FHIRDate, False, None, False),
            ("organization", "organization", FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", FHIRReference, False, None, False),
        ])
        return js