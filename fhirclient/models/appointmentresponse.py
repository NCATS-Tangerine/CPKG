#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/AppointmentResponse) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class AppointmentResponse(DomainResource):
    """ A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """
    resource_type: ClassVar[str] = "AppointmentResponse"
    identifier: Optional[List[Identifier]] = empty_list()
    appointment: FHIRReference = None
    start: Optional[FHIRDate] = None
    end: Optional[FHIRDate] = None
    participantType: Optional[List[CodeableConcept]] = empty_list()
    actor: Optional[FHIRReference] = None
    participantStatus: str = None
    comment: Optional[str] = None

    def elementProperties(self):
        js = super(AppointmentResponse, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("appointment", "appointment", FHIRReference, False, None, True),
            ("start", "start", FHIRDate, False, None, False),
            ("end", "end", FHIRDate, False, None, False),
            ("participantType", "participantType", CodeableConcept, True, None, False),
            ("actor", "actor", FHIRReference, False, None, False),
            ("participantStatus", "participantStatus", str, False, None, True),
            ("comment", "comment", str, False, None, False),
        ])
        return js