#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Organization) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier


@dataclass
class OrganizationContact(BackboneElement):
    """ Contact for the organization for a certain purpose.
    """
    resource_type: ClassVar[str] = "OrganizationContact"
    purpose: Optional[CodeableConcept] = None
    name: Optional[HumanName] = None
    telecom: Optional[List[ContactPoint]] = empty_list()
    address: Optional[Address] = None

    def elementProperties(self):
        js = super(OrganizationContact, self).elementProperties()
        js.extend([
            ("purpose", "purpose", CodeableConcept, False, None, False),
            ("name", "name", HumanName, False, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
            ("address", "address", Address, False, None, False),
        ])
        return js


@dataclass
class Organization(DomainResource):
    """ A grouping of people or organizations with a common purpose.

    A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, payer/insurer, etc.
    """
    resource_type: ClassVar[str] = "Organization"
    identifier: Optional[List[Identifier]] = empty_list()
    active: Optional[bool] = None
    type: Optional[List[CodeableConcept]] = empty_list()
    name: Optional[str] = None
    alias: Optional[List[str]] = empty_list()
    telecom: Optional[List[ContactPoint]] = empty_list()
    address: Optional[List[Address]] = empty_list()
    partOf: Optional[FHIRReference] = None
    contact: Optional[List[OrganizationContact]] = empty_list()
    endpoint: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(Organization, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("active", "active", bool, False, None, False),
            ("type", "type", CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
            ("address", "address", Address, True, None, False),
            ("partOf", "partOf", FHIRReference, False, None, False),
            ("contact", "contact", OrganizationContact, True, None, False),
            ("endpoint", "endpoint", FHIRReference, True, None, False),
        ])
        return js