#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Slot) on 2019-08-06.
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
class Slot(DomainResource):
    """ A slot of time on a schedule that may be available for booking appointments.
    """
    resource_type: ClassVar[str] = "Slot"
    identifier: Optional[List[Identifier]] = empty_list()
    serviceCategory: Optional[List[CodeableConcept]] = empty_list()
    serviceType: Optional[List[CodeableConcept]] = empty_list()
    specialty: Optional[List[CodeableConcept]] = empty_list()
    appointmentType: Optional[CodeableConcept] = None
    schedule: FHIRReference = None
    status: str = None
    start: FHIRDate = None
    end: FHIRDate = None
    overbooked: Optional[bool] = None
    comment: Optional[str] = None

    def elementProperties(self):
        js = super(Slot, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("serviceCategory", "serviceCategory", CodeableConcept, True, None, False),
            ("serviceType", "serviceType", CodeableConcept, True, None, False),
            ("specialty", "specialty", CodeableConcept, True, None, False),
            ("appointmentType", "appointmentType", CodeableConcept, False, None, False),
            ("schedule", "schedule", FHIRReference, False, None, True),
            ("status", "status", str, False, None, True),
            ("start", "start", FHIRDate, False, None, True),
            ("end", "end", FHIRDate, False, None, True),
            ("overbooked", "overbooked", bool, False, None, False),
            ("comment", "comment", str, False, None, False),
        ])
        return js