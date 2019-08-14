#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/CodeSystem) on 2019-08-06.
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
from .fhirdate import FHIRDate
from .identifier import Identifier
from .usagecontext import UsageContext


@dataclass
class CodeSystemConceptDesignation(BackboneElement):
    """ Additional representations for the concept.

    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """
    resource_type: ClassVar[str] = "CodeSystemConceptDesignation"
    language: Optional[str] = None
    use: Optional[Coding] = None
    value: str = None

    def elementProperties(self):
        js = super(CodeSystemConceptDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False, None, False),
            ("use", "use", Coding, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


@dataclass
class CodeSystemConceptProperty(BackboneElement):
    """ Property value for the concept.

    A property value for this concept.
    """
    resource_type: ClassVar[str] = "CodeSystemConceptProperty"
    code: str = None
    valueCode: str = None
    valueCoding: Coding = None
    valueString: str = None
    valueInteger: int = None
    valueBoolean: bool = None
    valueDateTime: FHIRDate = None
    valueDecimal: float = None

    def elementProperties(self):
        js = super(CodeSystemConceptProperty, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueCoding", "valueCoding", Coding, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
        ])
        return js


@dataclass
class CodeSystemFilter(BackboneElement):
    """ Filter that can be used in a value set.

    A filter that can be used in a value set compose statement when selecting
    concepts using a filter.
    """
    resource_type: ClassVar[str] = "CodeSystemFilter"
    code: str = None
    description: Optional[str] = None
    operator: List[str] = empty_list()
    value: str = None

    def elementProperties(self):
        js = super(CodeSystemFilter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("operator", "operator", str, True, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


@dataclass
class CodeSystemProperty(BackboneElement):
    """ Additional information supplied about each concept.

    A property defines an additional slot through which additional information
    can be provided about a concept.
    """
    resource_type: ClassVar[str] = "CodeSystemProperty"
    code: str = None
    uri: Optional[str] = None
    description: Optional[str] = None
    type: str = None

    def elementProperties(self):
        js = super(CodeSystemProperty, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("uri", "uri", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


@dataclass
class CodeSystemConcept(BackboneElement):
    """ Concepts in the code system.

    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meanings of the hierarchical relationships are.
    """
    resource_type: ClassVar[str] = "CodeSystemConcept"
    code: str = None
    display: Optional[str] = None
    definition: Optional[str] = None
    designation: Optional[List[CodeSystemConceptDesignation]] = empty_list()
    property: Optional[List[CodeSystemConceptProperty]] = empty_list()
    concept: Optional[List["CodeSystemConcept"]] = empty_list()

    def elementProperties(self):
        js = super(CodeSystemConcept, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("display", "display", str, False, None, False),
            ("definition", "definition", str, False, None, False),
            ("designation", "designation", CodeSystemConceptDesignation, True, None, False),
            ("property", "property", CodeSystemConceptProperty, True, None, False),
            ("concept", "concept", CodeSystemConcept, True, None, False),
        ])
        return js


@dataclass
class CodeSystem(DomainResource):
    """ Declares the existence of and describes a code system or code system
    supplement.

    The CodeSystem resource is used to declare the existence of and describe a
    code system or code system supplement and its key properties, and
    optionally define a part or all of its content.
    """
    resource_type: ClassVar[str] = "CodeSystem"
    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    version: Optional[str] = None
    name: Optional[str] = None
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
    caseSensitive: Optional[bool] = None
    valueSet: Optional[str] = None
    hierarchyMeaning: Optional[str] = None
    compositional: Optional[bool] = None
    versionNeeded: Optional[bool] = None
    content: str = None
    supplements: Optional[str] = None
    count: Optional[int] = None
    filter: Optional[List[CodeSystemFilter]] = empty_list()
    property: Optional[List[CodeSystemProperty]] = empty_list()
    concept: Optional[List[CodeSystemConcept]] = empty_list()

    def elementProperties(self):
        js = super(CodeSystem, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
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
            ("caseSensitive", "caseSensitive", bool, False, None, False),
            ("valueSet", "valueSet", str, False, None, False),
            ("hierarchyMeaning", "hierarchyMeaning", str, False, None, False),
            ("compositional", "compositional", bool, False, None, False),
            ("versionNeeded", "versionNeeded", bool, False, None, False),
            ("content", "content", str, False, None, True),
            ("supplements", "supplements", str, False, None, False),
            ("count", "count", int, False, None, False),
            ("filter", "filter", CodeSystemFilter, True, None, False),
            ("property", "property", CodeSystemProperty, True, None, False),
            ("concept", "concept", CodeSystemConcept, True, None, False),
        ])
        return js