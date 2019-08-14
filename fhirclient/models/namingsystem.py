#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/NamingSystem) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .period import Period
from .usagecontext import UsageContext


@dataclass
class NamingSystemUniqueId(BackboneElement):
    """ Unique identifiers used for system.

    Indicates how the system may be identified when referenced in electronic
    exchange.
    """
    resource_type: ClassVar[str] = "NamingSystemUniqueId"
    type: str = None
    value: str = None
    preferred: Optional[bool] = None
    comment: Optional[str] = None
    period: Optional[Period] = None

    def elementProperties(self):
        js = super(NamingSystemUniqueId, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("value", "value", str, False, None, True),
            ("preferred", "preferred", bool, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("period", "period", Period, False, None, False),
        ])
        return js


@dataclass
class NamingSystem(DomainResource):
    """ System of unique identification.

    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """
    resource_type: ClassVar[str] = "NamingSystem"
    name: str = None
    status: str = None
    kind: str = None
    date: FHIRDate = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    responsible: Optional[str] = None
    type: Optional[CodeableConcept] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    usage: Optional[str] = None
    uniqueId: List[NamingSystemUniqueId] = empty_list()

    def elementProperties(self):
        js = super(NamingSystem, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("status", "status", str, False, None, True),
            ("kind", "kind", str, False, None, True),
            ("date", "date", FHIRDate, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("responsible", "responsible", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("usage", "usage", str, False, None, False),
            ("uniqueId", "uniqueId", NamingSystemUniqueId, True, None, True),
        ])
        return js