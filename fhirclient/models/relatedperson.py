#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/RelatedPerson) on 2019-08-06.
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
class RelatedPersonCommunication(BackboneElement):
    """ A language which may be used to communicate with about the patient's health.
    """
    resource_type: ClassVar[str] = "RelatedPersonCommunication"
    language: CodeableConcept = None
    preferred: Optional[bool] = None

    def elementProperties(self):
        js = super(RelatedPersonCommunication, self).elementProperties()
        js.extend([
            ("language", "language", CodeableConcept, False, None, True),
            ("preferred", "preferred", bool, False, None, False),
        ])
        return js


@dataclass
class RelatedPerson(DomainResource):
    """ A person that is related to a patient, but who is not a direct target of
    care.

    Information about a person that is involved in the care for a patient, but
    who is not the target of healthcare, nor has a formal responsibility in the
    care process.
    """
    resource_type: ClassVar[str] = "RelatedPerson"
    identifier: Optional[List[Identifier]] = empty_list()
    active: Optional[bool] = None
    patient: FHIRReference = None
    relationship: Optional[List[CodeableConcept]] = empty_list()
    name: Optional[List[HumanName]] = empty_list()
    telecom: Optional[List[ContactPoint]] = empty_list()
    gender: Optional[str] = None
    birthDate: Optional[FHIRDate] = None
    address: Optional[List[Address]] = empty_list()
    photo: Optional[List[Attachment]] = empty_list()
    period: Optional[Period] = None
    communication: Optional[List[RelatedPersonCommunication]] = empty_list()

    def elementProperties(self):
        js = super(RelatedPerson, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("active", "active", bool, False, None, False),
            ("patient", "patient", FHIRReference, False, None, True),
            ("relationship", "relationship", CodeableConcept, True, None, False),
            ("name", "name", HumanName, True, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
            ("gender", "gender", str, False, None, False),
            ("birthDate", "birthDate", FHIRDate, False, None, False),
            ("address", "address", Address, True, None, False),
            ("photo", "photo", Attachment, True, None, False),
            ("period", "period", Period, False, None, False),
            ("communication", "communication", RelatedPersonCommunication, True, None, False),
        ])
        return js