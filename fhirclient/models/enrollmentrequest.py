#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/EnrollmentRequest) on 2019-08-06.
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
class EnrollmentRequest(DomainResource):
    """ Enroll in coverage.

    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """
    resource_type: ClassVar[str] = "EnrollmentRequest"
    identifier: Optional[List[Identifier]] = empty_list()
    status: Optional[str] = None
    created: Optional[FHIRDate] = None
    insurer: Optional[FHIRReference] = None
    provider: Optional[FHIRReference] = None
    candidate: Optional[FHIRReference] = None
    coverage: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(EnrollmentRequest, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, False),
            ("created", "created", FHIRDate, False, None, False),
            ("insurer", "insurer", FHIRReference, False, None, False),
            ("provider", "provider", FHIRReference, False, None, False),
            ("candidate", "candidate", FHIRReference, False, None, False),
            ("coverage", "coverage", FHIRReference, False, None, False),
        ])
        return js