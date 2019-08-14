#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ConceptMap) on 2019-08-06.
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
from .identifier import Identifier
from .usagecontext import UsageContext


@dataclass
class ConceptMapGroupElementTargetDependsOn(BackboneElement):
    """ Other elements required for this mapping (from context).

    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """
    resource_type: ClassVar[str] = "ConceptMapGroupElementTargetDependsOn"
    property: str = None
    system: Optional[str] = None
    value: str = None
    display: Optional[str] = None

    def elementProperties(self):
        js = super(ConceptMapGroupElementTargetDependsOn, self).elementProperties()
        js.extend([
            ("property", "property", str, False, None, True),
            ("system", "system", str, False, None, False),
            ("value", "value", str, False, None, True),
            ("display", "display", str, False, None, False),
        ])
        return js


@dataclass
class ConceptMapGroupElementTarget(BackboneElement):
    """ Concept in target system for element.

    A concept from the target value set that this concept maps to.
    """
    resource_type: ClassVar[str] = "ConceptMapGroupElementTarget"
    code: Optional[str] = None
    display: Optional[str] = None
    equivalence: str = None
    comment: Optional[str] = None
    dependsOn: Optional[List[ConceptMapGroupElementTargetDependsOn]] = empty_list()
    product: Optional[List[ConceptMapGroupElementTargetDependsOn]] = empty_list()

    def elementProperties(self):
        js = super(ConceptMapGroupElementTarget, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("equivalence", "equivalence", str, False, None, True),
            ("comment", "comment", str, False, None, False),
            ("dependsOn", "dependsOn", ConceptMapGroupElementTargetDependsOn, True, None, False),
            ("product", "product", ConceptMapGroupElementTargetDependsOn, True, None, False),
        ])
        return js


@dataclass
class ConceptMapGroupElement(BackboneElement):
    """ Mappings for a concept from the source set.

    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """
    resource_type: ClassVar[str] = "ConceptMapGroupElement"
    code: Optional[str] = None
    display: Optional[str] = None
    target: Optional[List[ConceptMapGroupElementTarget]] = empty_list()

    def elementProperties(self):
        js = super(ConceptMapGroupElement, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("target", "target", ConceptMapGroupElementTarget, True, None, False),
        ])
        return js


@dataclass
class ConceptMapGroupUnmapped(BackboneElement):
    """ What to do when there is no mapping for the source concept.

    What to do when there is no mapping for the source concept. "Unmapped" does
    not include codes that are unmatched, and the unmapped element is ignored
    in a code is specified to have equivalence = unmatched.
    """
    resource_type: ClassVar[str] = "ConceptMapGroupUnmapped"
    mode: str = None
    code: Optional[str] = None
    display: Optional[str] = None
    url: Optional[str] = None

    def elementProperties(self):
        js = super(ConceptMapGroupUnmapped, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, True),
            ("code", "code", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("url", "url", str, False, None, False),
        ])
        return js


@dataclass
class ConceptMapGroup(BackboneElement):
    """ Same source and target systems.

    A group of mappings that all have the same source and target system.
    """
    resource_type: ClassVar[str] = "ConceptMapGroup"
    source: Optional[str] = None
    sourceVersion: Optional[str] = None
    target: Optional[str] = None
    targetVersion: Optional[str] = None
    element: List[ConceptMapGroupElement] = empty_list()
    unmapped: Optional[ConceptMapGroupUnmapped] = None

    def elementProperties(self):
        js = super(ConceptMapGroup, self).elementProperties()
        js.extend([
            ("source", "source", str, False, None, False),
            ("sourceVersion", "sourceVersion", str, False, None, False),
            ("target", "target", str, False, None, False),
            ("targetVersion", "targetVersion", str, False, None, False),
            ("element", "element", ConceptMapGroupElement, True, None, True),
            ("unmapped", "unmapped", ConceptMapGroupUnmapped, False, None, False),
        ])
        return js


@dataclass
class ConceptMap(DomainResource):
    """ A map from one set of concepts to one or more other concepts.

    A statement of relationships from one set of concepts to one or more other
    concepts - either concepts in code systems, or data element/data element
    concepts, or classes in class models.
    """
    resource_type: ClassVar[str] = "ConceptMap"
    url: Optional[str] = None
    identifier: Optional[Identifier] = None
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
    sourceUri: Optional[str] = None
    sourceCanonical: Optional[str] = None
    targetUri: Optional[str] = None
    targetCanonical: Optional[str] = None
    group: Optional[List[ConceptMapGroup]] = empty_list()

    def elementProperties(self):
        js = super(ConceptMap, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
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
            ("sourceUri", "sourceUri", str, False, "source", False),
            ("sourceCanonical", "sourceCanonical", str, False, "source", False),
            ("targetUri", "targetUri", str, False, "target", False),
            ("targetCanonical", "targetCanonical", str, False, "target", False),
            ("group", "group", ConceptMapGroup, True, None, False),
        ])
        return js