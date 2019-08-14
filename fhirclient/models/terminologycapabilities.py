#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities) on 2019-08-06.
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
class TerminologyCapabilitiesExpansionParameter(BackboneElement):
    """ Supported expansion parameter.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesExpansionParameter"
    name: str = None
    documentation: Optional[str] = None

    def elementProperties(self):
        js = super(TerminologyCapabilitiesExpansionParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


@dataclass
class TerminologyCapabilitiesCodeSystemVersionFilter(BackboneElement):
    """ Filter Properties supported.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesCodeSystemVersionFilter"
    code: str = None
    op: List[str] = empty_list()

    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystemVersionFilter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("op", "op", str, True, None, True),
        ])
        return js


@dataclass
class TerminologyCapabilitiesCodeSystemVersion(BackboneElement):
    """ Version of Code System supported.

    For the code system, a list of versions that are supported by the server.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesCodeSystemVersion"
    code: Optional[str] = None
    isDefault: Optional[bool] = None
    compositional: Optional[bool] = None
    language: Optional[List[str]] = empty_list()
    filter: Optional[List[TerminologyCapabilitiesCodeSystemVersionFilter]] = empty_list()
    property: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystemVersion, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("isDefault", "isDefault", bool, False, None, False),
            ("compositional", "compositional", bool, False, None, False),
            ("language", "language", str, True, None, False),
            ("filter", "filter", TerminologyCapabilitiesCodeSystemVersionFilter, True, None, False),
            ("property", "property", str, True, None, False),
        ])
        return js


@dataclass
class TerminologyCapabilitiesSoftware(BackboneElement):
    """ Software that is covered by this terminology capability statement.

    Software that is covered by this terminology capability statement.  It is
    used when the statement describes the capabilities of a particular software
    version, independent of an installation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesSoftware"
    name: str = None
    version: Optional[str] = None

    def elementProperties(self):
        js = super(TerminologyCapabilitiesSoftware, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


@dataclass
class TerminologyCapabilitiesImplementation(BackboneElement):
    """ If this describes a specific instance.

    Identifies a specific implementation instance that is described by the
    terminology capability statement - i.e. a particular installation, rather
    than the capabilities of a software program.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesImplementation"
    description: str = None
    url: Optional[str] = None

    def elementProperties(self):
        js = super(TerminologyCapabilitiesImplementation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js


@dataclass
class TerminologyCapabilitiesCodeSystem(BackboneElement):
    """ A code system supported by the server.

    Identifies a code system that is supported by the server. If there is a no
    code system URL, then this declares the general assumptions a client can
    make about support for any CodeSystem resource.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesCodeSystem"
    uri: Optional[str] = None
    version: Optional[List[TerminologyCapabilitiesCodeSystemVersion]] = empty_list()
    subsumption: Optional[bool] = None

    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystem, self).elementProperties()
        js.extend([
            ("uri", "uri", str, False, None, False),
            ("version", "version", TerminologyCapabilitiesCodeSystemVersion, True, None, False),
            ("subsumption", "subsumption", bool, False, None, False),
        ])
        return js


@dataclass
class TerminologyCapabilitiesExpansion(BackboneElement):
    """ Information about the [ValueSet/$expand](valueset-operation-expand.html)
    operation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesExpansion"
    hierarchical: Optional[bool] = None
    paging: Optional[bool] = None
    incomplete: Optional[bool] = None
    parameter: Optional[List[TerminologyCapabilitiesExpansionParameter]] = empty_list()
    textFilter: Optional[str] = None

    def elementProperties(self):
        js = super(TerminologyCapabilitiesExpansion, self).elementProperties()
        js.extend([
            ("hierarchical", "hierarchical", bool, False, None, False),
            ("paging", "paging", bool, False, None, False),
            ("incomplete", "incomplete", bool, False, None, False),
            ("parameter", "parameter", TerminologyCapabilitiesExpansionParameter, True, None, False),
            ("textFilter", "textFilter", str, False, None, False),
        ])
        return js


@dataclass
class TerminologyCapabilitiesValidateCode(BackboneElement):
    """ Information about the [ValueSet/$validate-code](valueset-operation-
    validate-code.html) operation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesValidateCode"
    translations: bool = None

    def elementProperties(self):
        js = super(TerminologyCapabilitiesValidateCode, self).elementProperties()
        js.extend([
            ("translations", "translations", bool, False, None, True),
        ])
        return js


@dataclass
class TerminologyCapabilitiesTranslation(BackboneElement):
    """ Information about the [ConceptMap/$translate](conceptmap-operation-
    translate.html) operation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesTranslation"
    needsMap: bool = None

    def elementProperties(self):
        js = super(TerminologyCapabilitiesTranslation, self).elementProperties()
        js.extend([
            ("needsMap", "needsMap", bool, False, None, True),
        ])
        return js


@dataclass
class TerminologyCapabilitiesClosure(BackboneElement):
    """ Information about the [ConceptMap/$closure](conceptmap-operation-
    closure.html) operation.

    Whether the $closure operation is supported.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesClosure"
    translation: Optional[bool] = None

    def elementProperties(self):
        js = super(TerminologyCapabilitiesClosure, self).elementProperties()
        js.extend([
            ("translation", "translation", bool, False, None, False),
        ])
        return js


@dataclass
class TerminologyCapabilities(DomainResource):
    """ A statement of system capabilities.

    A TerminologyCapabilities resource documents a set of capabilities
    (behaviors) of a FHIR Terminology Server that may be used as a statement of
    actual server functionality or a statement of required or desired server
    implementation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilities"
    url: Optional[str] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: FHIRDate = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    kind: str = None
    software: Optional[TerminologyCapabilitiesSoftware] = None
    implementation: Optional[TerminologyCapabilitiesImplementation] = None
    lockedDate: Optional[bool] = None
    codeSystem: Optional[List[TerminologyCapabilitiesCodeSystem]] = empty_list()
    expansion: Optional[TerminologyCapabilitiesExpansion] = None
    codeSearch: Optional[str] = None
    validateCode: Optional[TerminologyCapabilitiesValidateCode] = None
    translation: Optional[TerminologyCapabilitiesTranslation] = None
    closure: Optional[TerminologyCapabilitiesClosure] = None

    def elementProperties(self):
        js = super(TerminologyCapabilities, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", FHIRDate, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("kind", "kind", str, False, None, True),
            ("software", "software", TerminologyCapabilitiesSoftware, False, None, False),
            ("implementation", "implementation", TerminologyCapabilitiesImplementation, False, None, False),
            ("lockedDate", "lockedDate", bool, False, None, False),
            ("codeSystem", "codeSystem", TerminologyCapabilitiesCodeSystem, True, None, False),
            ("expansion", "expansion", TerminologyCapabilitiesExpansion, False, None, False),
            ("codeSearch", "codeSearch", str, False, None, False),
            ("validateCode", "validateCode", TerminologyCapabilitiesValidateCode, False, None, False),
            ("translation", "translation", TerminologyCapabilitiesTranslation, False, None, False),
            ("closure", "closure", TerminologyCapabilitiesClosure, False, None, False),
        ])
        return js