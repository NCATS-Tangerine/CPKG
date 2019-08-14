#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Person) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier


@dataclass
class PersonLink(BackboneElement):
    """ Link to a resource that concerns the same actual person.
    """
    resource_type: ClassVar[str] = "PersonLink"
    target: FHIRReference = None
    assurance: Optional[str] = None

    def elementProperties(self):
        js = super(PersonLink, self).elementProperties()
        js.extend([
            ("target", "target", FHIRReference, False, None, True),
            ("assurance", "assurance", str, False, None, False),
        ])
        return js


@dataclass
class Person(DomainResource):
    """ A generic person record.

    Demographics and administrative information about a person independent of a
    specific health-related context.
    """
    resource_type: ClassVar[str] = "Person"
    identifier: Optional[List[Identifier]] = empty_list()
    name: Optional[List[HumanName]] = empty_list()
    telecom: Optional[List[ContactPoint]] = empty_list()
    gender: Optional[str] = None
    birthDate: Optional[FHIRDate] = None
    address: Optional[List[Address]] = empty_list()
    photo: Optional[Attachment] = None
    managingOrganization: Optional[FHIRReference] = None
    active: Optional[bool] = None
    link: Optional[List[PersonLink]] = empty_list()

    def elementProperties(self):
        js = super(Person, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("name", "name", HumanName, True, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
            ("gender", "gender", str, False, None, False),
            ("birthDate", "birthDate", FHIRDate, False, None, False),
            ("address", "address", Address, True, None, False),
            ("photo", "photo", Attachment, False, None, False),
            ("managingOrganization", "managingOrganization", FHIRReference, False, None, False),
            ("active", "active", bool, False, None, False),
            ("link", "link", PersonLink, True, None, False),
        ])
        return js