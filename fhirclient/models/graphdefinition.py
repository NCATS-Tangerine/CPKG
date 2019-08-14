#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/GraphDefinition) on 2019-08-06.
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
class GraphDefinitionLinkTargetCompartment(BackboneElement):
    """ Compartment Consistency Rules.
    """
    resource_type: ClassVar[str] = "GraphDefinitionLinkTargetCompartment"
    use: str = None
    code: str = None
    rule: str = None
    expression: Optional[str] = None
    description: Optional[str] = None

    def elementProperties(self):
        js = super(GraphDefinitionLinkTargetCompartment, self).elementProperties()
        js.extend([
            ("use", "use", str, False, None, True),
            ("code", "code", str, False, None, True),
            ("rule", "rule", str, False, None, True),
            ("expression", "expression", str, False, None, False),
            ("description", "description", str, False, None, False),
        ])
        return js


@dataclass
class GraphDefinitionLinkTarget(BackboneElement):
    """ Potential target for the link.
    """
    resource_type: ClassVar[str] = "GraphDefinitionLinkTarget"
    type: str = None
    params: Optional[str] = None
    profile: Optional[str] = None
    compartment: Optional[List[GraphDefinitionLinkTargetCompartment]] = empty_list()
    link: Optional[List["GraphDefinitionLink"]] = empty_list()

    def elementProperties(self):
        js = super(GraphDefinitionLinkTarget, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("params", "params", str, False, None, False),
            ("profile", "profile", str, False, None, False),
            ("compartment", "compartment", GraphDefinitionLinkTargetCompartment, True, None, False),
            ("link", "link", GraphDefinitionLink, True, None, False),
        ])
        return js


@dataclass
class GraphDefinitionLink(BackboneElement):
    """ Links this graph makes rules about.
    """
    resource_type: ClassVar[str] = "GraphDefinitionLink"
    path: Optional[str] = None
    sliceName: Optional[str] = None
    min: Optional[int] = None
    max: Optional[str] = None
    description: Optional[str] = None
    target: Optional[List[GraphDefinitionLinkTarget]] = empty_list()

    def elementProperties(self):
        js = super(GraphDefinitionLink, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, False),
            ("sliceName", "sliceName", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("max", "max", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("target", "target", GraphDefinitionLinkTarget, True, None, False),
        ])
        return js


@dataclass
class GraphDefinition(DomainResource):
    """ Definition of a graph of resources.

    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references. The
    Graph Definition resource defines a set and makes rules about the set.
    """
    resource_type: ClassVar[str] = "GraphDefinition"
    url: Optional[str] = None
    version: Optional[str] = None
    name: str = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    purpose: Optional[str] = None
    start: str = None
    profile: Optional[str] = None
    link: Optional[List[GraphDefinitionLink]] = empty_list()

    def elementProperties(self):
        js = super(GraphDefinition, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("start", "start", str, False, None, True),
            ("profile", "profile", str, False, None, False),
            ("link", "link", GraphDefinitionLink, True, None, False),
        ])
        return js