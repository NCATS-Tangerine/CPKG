#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/SearchParameter) on 2019-08-06.
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
from .usagecontext import UsageContext


@dataclass
class SearchParameterComponent(BackboneElement):
    """ For Composite resources to define the parts.

    Used to define the parts of a composite search parameter.
    """
    resource_type: ClassVar[str] = "SearchParameterComponent"
    definition: str = None
    expression: str = None

    def elementProperties(self):
        js = super(SearchParameterComponent, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, True),
            ("expression", "expression", str, False, None, True),
        ])
        return js


@dataclass
class SearchParameter(DomainResource):
    """ Search parameter for a resource.

    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """
    resource_type: ClassVar[str] = "SearchParameter"
    url: str = None
    version: Optional[str] = None
    name: str = None
    derivedFrom: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    description: str = None
    useContext: Optional[List[UsageContext]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    purpose: Optional[str] = None
    code: str = None
    base: List[str] = empty_list()
    type: str = None
    expression: Optional[str] = None
    xpath: Optional[str] = None
    xpathUsage: Optional[str] = None
    target: Optional[List[str]] = empty_list()
    multipleOr: Optional[bool] = None
    multipleAnd: Optional[bool] = None
    comparator: Optional[List[str]] = empty_list()
    modifier: Optional[List[str]] = empty_list()
    chain: Optional[List[str]] = empty_list()
    component: Optional[List[SearchParameterComponent]] = empty_list()

    def elementProperties(self):
        js = super(SearchParameter, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("derivedFrom", "derivedFrom", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, True),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("code", "code", str, False, None, True),
            ("base", "base", str, True, None, True),
            ("type", "type", str, False, None, True),
            ("expression", "expression", str, False, None, False),
            ("xpath", "xpath", str, False, None, False),
            ("xpathUsage", "xpathUsage", str, False, None, False),
            ("target", "target", str, True, None, False),
            ("multipleOr", "multipleOr", bool, False, None, False),
            ("multipleAnd", "multipleAnd", bool, False, None, False),
            ("comparator", "comparator", str, True, None, False),
            ("modifier", "modifier", str, True, None, False),
            ("chain", "chain", str, True, None, False),
            ("component", "component", SearchParameterComponent, True, None, False),
        ])
        return js