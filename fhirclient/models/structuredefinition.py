#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/StructureDefinition) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .elementdefinition import ElementDefinition
from .fhirdate import FHIRDate
from .identifier import Identifier
from .usagecontext import UsageContext


@dataclass
class StructureDefinitionMapping(BackboneElement):
    """ External specification that the content is mapped to.

    An external specification that the content is mapped to.
    """
    resource_type: ClassVar[str] = "StructureDefinitionMapping"
    identity: str = None
    uri: Optional[str] = None
    name: Optional[str] = None
    comment: Optional[str] = None

    def elementProperties(self):
        js = super(StructureDefinitionMapping, self).elementProperties()
        js.extend([
            ("identity", "identity", str, False, None, True),
            ("uri", "uri", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("comment", "comment", str, False, None, False),
        ])
        return js


@dataclass
class StructureDefinitionContext(BackboneElement):
    """ If an extension, where it can be used in instances.

    Identifies the types of resource or data type elements to which the
    extension can be applied.
    """
    resource_type: ClassVar[str] = "StructureDefinitionContext"
    type: str = None
    expression: str = None

    def elementProperties(self):
        js = super(StructureDefinitionContext, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("expression", "expression", str, False, None, True),
        ])
        return js


@dataclass
class StructureDefinitionSnapshot(BackboneElement):
    """ Snapshot view of the structure.

    A snapshot view is expressed in a standalone form that can be used and
    interpreted without considering the base StructureDefinition.
    """
    resource_type: ClassVar[str] = "StructureDefinitionSnapshot"
    element: List[ElementDefinition] = empty_list()

    def elementProperties(self):
        js = super(StructureDefinitionSnapshot, self).elementProperties()
        js.extend([
            ("element", "element", ElementDefinition, True, None, True),
        ])
        return js


@dataclass
class StructureDefinitionDifferential(BackboneElement):
    """ Differential view of the structure.

    A differential view is expressed relative to the base StructureDefinition -
    a statement of differences that it applies.
    """
    resource_type: ClassVar[str] = "StructureDefinitionDifferential"
    element: List[ElementDefinition] = empty_list()

    def elementProperties(self):
        js = super(StructureDefinitionDifferential, self).elementProperties()
        js.extend([
            ("element", "element", ElementDefinition, True, None, True),
        ])
        return js


@dataclass
class StructureDefinition(DomainResource):
    """ Structural Definition.

    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions and constraints on resources and data types.
    """
    resource_type: ClassVar[str] = "StructureDefinition"
    url: str = None
    identifier: Optional[List[Identifier]] = empty_list()
    version: Optional[str] = None
    name: str = None
    title: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    keyword: Optional[List[Coding]] = empty_list()
    fhirVersion: Optional[str] = None
    mapping: Optional[List[StructureDefinitionMapping]] = empty_list()
    kind: str = None
    abstract: bool = None
    context: Optional[List[StructureDefinitionContext]] = empty_list()
    contextInvariant: Optional[List[str]] = empty_list()
    type: str = None
    baseDefinition: Optional[str] = None
    derivation: Optional[str] = None
    snapshot: Optional[StructureDefinitionSnapshot] = None
    differential: Optional[StructureDefinitionDifferential] = None

    def elementProperties(self):
        js = super(StructureDefinition, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("identifier", "identifier", Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("keyword", "keyword", Coding, True, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, False),
            ("mapping", "mapping", StructureDefinitionMapping, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("abstract", "abstract", bool, False, None, True),
            ("context", "context", StructureDefinitionContext, True, None, False),
            ("contextInvariant", "contextInvariant", str, True, None, False),
            ("type", "type", str, False, None, True),
            ("baseDefinition", "baseDefinition", str, False, None, False),
            ("derivation", "derivation", str, False, None, False),
            ("snapshot", "snapshot", StructureDefinitionSnapshot, False, None, False),
            ("differential", "differential", StructureDefinitionDifferential, False, None, False),
        ])
        return js