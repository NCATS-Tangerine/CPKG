#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Patient) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier
from .period import Period


@dataclass
class PatientContact(BackboneElement):
    """ A contact party (e.g. guardian, partner, friend) for the patient.
    """
    resource_type: ClassVar[str] = "PatientContact"
    relationship: Optional[List[CodeableConcept]] = empty_list()
    name: Optional[HumanName] = None
    telecom: Optional[List[ContactPoint]] = empty_list()
    address: Optional[Address] = None
    gender: Optional[str] = None
    organization: Optional[FHIRReference] = None
    period: Optional[Period] = None

    def elementProperties(self):
        js = super(PatientContact, self).elementProperties()
        js.extend([
            ("relationship", "relationship", CodeableConcept, True, None, False),
            ("name", "name", HumanName, False, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
            ("address", "address", Address, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("organization", "organization", FHIRReference, False, None, False),
            ("period", "period", Period, False, None, False),
        ])
        return js


@dataclass
class PatientCommunication(BackboneElement):
    """ A language which may be used to communicate with the patient about his or
    her health.
    """
    resource_type: ClassVar[str] = "PatientCommunication"
    language: CodeableConcept = None
    preferred: Optional[bool] = None

    def elementProperties(self):
        js = super(PatientCommunication, self).elementProperties()
        js.extend([
            ("language", "language", CodeableConcept, False, None, True),
            ("preferred", "preferred", bool, False, None, False),
        ])
        return js


@dataclass
class PatientLink(BackboneElement):
    """ Link to another patient resource that concerns the same actual person.

    Link to another patient resource that concerns the same actual patient.
    """
    resource_type: ClassVar[str] = "PatientLink"
    other: FHIRReference = None
    type: str = None

    def elementProperties(self):
        js = super(PatientLink, self).elementProperties()
        js.extend([
            ("other", "other", FHIRReference, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


@dataclass
class Patient(DomainResource):
    """ Information about an individual or animal receiving health care services.

    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """
    resource_type: ClassVar[str] = "Patient"
    identifier: Optional[List[Identifier]] = empty_list()
    active: Optional[bool] = None
    name: Optional[List[HumanName]] = empty_list()
    telecom: Optional[List[ContactPoint]] = empty_list()
    gender: Optional[str] = None
    birthDate: Optional[FHIRDate] = None
    deceasedBoolean: Optional[bool] = None
    deceasedDateTime: Optional[FHIRDate] = None
    address: Optional[List[Address]] = empty_list()
    maritalStatus: Optional[CodeableConcept] = None
    multipleBirthBoolean: Optional[bool] = None
    multipleBirthInteger: Optional[int] = None
    photo: Optional[List[Attachment]] = empty_list()
    contact: Optional[List[PatientContact]] = empty_list()
    communication: Optional[List[PatientCommunication]] = empty_list()
    generalPractitioner: Optional[List[FHIRReference]] = empty_list()
    managingOrganization: Optional[FHIRReference] = None
    link: Optional[List[PatientLink]] = empty_list()

    def elementProperties(self):
        js = super(Patient, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("active", "active", bool, False, None, False),
            ("name", "name", HumanName, True, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
            ("gender", "gender", str, False, None, False),
            ("birthDate", "birthDate", FHIRDate, False, None, False),
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False),
            ("deceasedDateTime", "deceasedDateTime", FHIRDate, False, "deceased", False),
            ("address", "address", Address, True, None, False),
            ("maritalStatus", "maritalStatus", CodeableConcept, False, None, False),
            ("multipleBirthBoolean", "multipleBirthBoolean", bool, False, "multipleBirth", False),
            ("multipleBirthInteger", "multipleBirthInteger", int, False, "multipleBirth", False),
            ("photo", "photo", Attachment, True, None, False),
            ("contact", "contact", PatientContact, True, None, False),
            ("communication", "communication", PatientCommunication, True, None, False),
            ("generalPractitioner", "generalPractitioner", FHIRReference, True, None, False),
            ("managingOrganization", "managingOrganization", FHIRReference, False, None, False),
            ("link", "link", PatientLink, True, None, False),
        ])
        return js