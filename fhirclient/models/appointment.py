#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Appointment) on 2019-08-06.
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
from .identifier import Identifier
from .period import Period


@dataclass
class AppointmentParticipant(BackboneElement):
    """ Participants involved in appointment.

    List of participants involved in the appointment.
    """
    resource_type: ClassVar[str] = "AppointmentParticipant"
    type: Optional[List[CodeableConcept]] = empty_list()
    actor: Optional[FHIRReference] = None
    required: Optional[str] = None
    status: str = None
    period: Optional[Period] = None

    def elementProperties(self):
        js = super(AppointmentParticipant, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, True, None, False),
            ("actor", "actor", FHIRReference, False, None, False),
            ("required", "required", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("period", "period", Period, False, None, False),
        ])
        return js


@dataclass
class Appointment(DomainResource):
    """ A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
    """
    resource_type: ClassVar[str] = "Appointment"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    cancelationReason: Optional[CodeableConcept] = None
    serviceCategory: Optional[List[CodeableConcept]] = empty_list()
    serviceType: Optional[List[CodeableConcept]] = empty_list()
    specialty: Optional[List[CodeableConcept]] = empty_list()
    appointmentType: Optional[CodeableConcept] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    priority: Optional[int] = None
    description: Optional[str] = None
    supportingInformation: Optional[List[FHIRReference]] = empty_list()
    start: Optional[FHIRDate] = None
    end: Optional[FHIRDate] = None
    minutesDuration: Optional[int] = None
    slot: Optional[List[FHIRReference]] = empty_list()
    created: Optional[FHIRDate] = None
    comment: Optional[str] = None
    patientInstruction: Optional[str] = None
    basedOn: Optional[List[FHIRReference]] = empty_list()
    participant: List[AppointmentParticipant] = empty_list()
    requestedPeriod: Optional[List[Period]] = empty_list()

    def elementProperties(self):
        js = super(Appointment, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("cancelationReason", "cancelationReason", CodeableConcept, False, None, False),
            ("serviceCategory", "serviceCategory", CodeableConcept, True, None, False),
            ("serviceType", "serviceType", CodeableConcept, True, None, False),
            ("specialty", "specialty", CodeableConcept, True, None, False),
            ("appointmentType", "appointmentType", CodeableConcept, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("priority", "priority", int, False, None, False),
            ("description", "description", str, False, None, False),
            ("supportingInformation", "supportingInformation", FHIRReference, True, None, False),
            ("start", "start", FHIRDate, False, None, False),
            ("end", "end", FHIRDate, False, None, False),
            ("minutesDuration", "minutesDuration", int, False, None, False),
            ("slot", "slot", FHIRReference, True, None, False),
            ("created", "created", FHIRDate, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("participant", "participant", AppointmentParticipant, True, None, True),
            ("requestedPeriod", "requestedPeriod", Period, True, None, False),
        ])
        return js