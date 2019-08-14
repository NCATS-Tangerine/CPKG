#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/HealthcareService) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class HealthcareServiceEligibility(BackboneElement):
    """ Specific eligibility requirements required to use the service.

    Does this service have specific eligibility requirements that need to be
    met in order to use the service?
    """
    resource_type: ClassVar[str] = "HealthcareServiceEligibility"
    code: Optional[CodeableConcept] = None
    comment: Optional[str] = None

    def elementProperties(self):
        js = super(HealthcareServiceEligibility, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
        ])
        return js


@dataclass
class HealthcareServiceAvailableTime(BackboneElement):
    """ Times the Service Site is available.

    A collection of times that the Service Site is available.
    """
    resource_type: ClassVar[str] = "HealthcareServiceAvailableTime"
    daysOfWeek: Optional[List[str]] = empty_list()
    allDay: Optional[bool] = None
    availableStartTime: Optional[FHIRDate] = None
    availableEndTime: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(HealthcareServiceAvailableTime, self).elementProperties()
        js.extend([
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
            ("allDay", "allDay", bool, False, None, False),
            ("availableStartTime", "availableStartTime", FHIRDate, False, None, False),
            ("availableEndTime", "availableEndTime", FHIRDate, False, None, False),
        ])
        return js


@dataclass
class HealthcareServiceNotAvailable(BackboneElement):
    """ Not available during this time due to provided reason.

    The HealthcareService is not available during this period of time due to
    the provided reason.
    """
    resource_type: ClassVar[str] = "HealthcareServiceNotAvailable"
    description: str = None
    during: Optional[Period] = None

    def elementProperties(self):
        js = super(HealthcareServiceNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("during", "during", Period, False, None, False),
        ])
        return js


@dataclass
class HealthcareService(DomainResource):
    """ The details of a healthcare service available at a location.
    """
    resource_type: ClassVar[str] = "HealthcareService"
    identifier: Optional[List[Identifier]] = empty_list()
    active: Optional[bool] = None
    providedBy: Optional[FHIRReference] = None
    category: Optional[List[CodeableConcept]] = empty_list()
    type: Optional[List[CodeableConcept]] = empty_list()
    specialty: Optional[List[CodeableConcept]] = empty_list()
    location: Optional[List[FHIRReference]] = empty_list()
    name: Optional[str] = None
    comment: Optional[str] = None
    extraDetails: Optional[str] = None
    photo: Optional[Attachment] = None
    telecom: Optional[List[ContactPoint]] = empty_list()
    coverageArea: Optional[List[FHIRReference]] = empty_list()
    serviceProvisionCode: Optional[List[CodeableConcept]] = empty_list()
    eligibility: Optional[List[HealthcareServiceEligibility]] = empty_list()
    program: Optional[List[CodeableConcept]] = empty_list()
    characteristic: Optional[List[CodeableConcept]] = empty_list()
    communication: Optional[List[CodeableConcept]] = empty_list()
    referralMethod: Optional[List[CodeableConcept]] = empty_list()
    appointmentRequired: Optional[bool] = None
    availableTime: Optional[List[HealthcareServiceAvailableTime]] = empty_list()
    notAvailable: Optional[List[HealthcareServiceNotAvailable]] = empty_list()
    availabilityExceptions: Optional[str] = None
    endpoint: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(HealthcareService, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("active", "active", bool, False, None, False),
            ("providedBy", "providedBy", FHIRReference, False, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("type", "type", CodeableConcept, True, None, False),
            ("specialty", "specialty", CodeableConcept, True, None, False),
            ("location", "location", FHIRReference, True, None, False),
            ("name", "name", str, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("extraDetails", "extraDetails", str, False, None, False),
            ("photo", "photo", Attachment, False, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
            ("coverageArea", "coverageArea", FHIRReference, True, None, False),
            ("serviceProvisionCode", "serviceProvisionCode", CodeableConcept, True, None, False),
            ("eligibility", "eligibility", HealthcareServiceEligibility, True, None, False),
            ("program", "program", CodeableConcept, True, None, False),
            ("characteristic", "characteristic", CodeableConcept, True, None, False),
            ("communication", "communication", CodeableConcept, True, None, False),
            ("referralMethod", "referralMethod", CodeableConcept, True, None, False),
            ("appointmentRequired", "appointmentRequired", bool, False, None, False),
            ("availableTime", "availableTime", HealthcareServiceAvailableTime, True, None, False),
            ("notAvailable", "notAvailable", HealthcareServiceNotAvailable, True, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("endpoint", "endpoint", FHIRReference, True, None, False),
        ])
        return js