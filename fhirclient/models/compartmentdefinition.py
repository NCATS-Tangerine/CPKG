#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/CompartmentDefinition) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .usagecontext import UsageContext


@dataclass
class CompartmentDefinitionResource(BackboneElement):
    """ How a resource is related to the compartment.

    Information about how a resource is related to the compartment.
    """
    resource_type: ClassVar[str] = "CompartmentDefinitionResource"
    code: str = None
    param: Optional[List[str]] = empty_list()
    documentation: Optional[str] = None

    def elementProperties(self):
        js = super(CompartmentDefinitionResource, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("param", "param", str, True, None, False),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


@dataclass
class CompartmentDefinition(DomainResource):
    """ Compartment Definition for a resource.

    A compartment definition that defines how resources are accessed on a
    server.
    """
    resource_type: ClassVar[str] = "CompartmentDefinition"
    url: str = None
    version: Optional[str] = None
    name: str = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    purpose: Optional[str] = None
    code: str = None
    search: bool = None
    resource: Optional[List[CompartmentDefinitionResource]] = empty_list()

    def elementProperties(self):
        js = super(CompartmentDefinition, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("code", "code", str, False, None, True),
            ("search", "search", bool, False, None, True),
            ("resource", "resource", CompartmentDefinitionResource, True, None, False),
        ])
        return js