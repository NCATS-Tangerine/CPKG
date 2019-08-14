#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/CapabilityStatement2) on 2019-08-06.
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
from .fhirreference import FHIRReference
from .usagecontext import UsageContext


@dataclass
class CapabilityStatement2RestResourceInteraction(BackboneElement):
    """ What operations are supported?.

    Identifies a restful operation supported by the solution.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2RestResourceInteraction"
    code: str = None
    documentation: Optional[str] = None

    def elementProperties(self):
        js = super(CapabilityStatement2RestResourceInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


@dataclass
class CapabilityStatement2RestResourceSearchParam(BackboneElement):
    """ Search parameters supported by implementation.

    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2RestResourceSearchParam"
    name: str = None
    definition: Optional[str] = None
    type: str = None
    documentation: Optional[str] = None

    def elementProperties(self):
        js = super(CapabilityStatement2RestResourceSearchParam, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("definition", "definition", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


@dataclass
class CapabilityStatement2RestResourceOperation(BackboneElement):
    """ Definition of a resource operation.

    Definition of an operation or a named query together with its parameters
    and their meaning and type. Consult the definition of the operation for
    details about how to invoke the operation, and the parameters.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2RestResourceOperation"
    name: str = None
    definition: str = None
    documentation: Optional[str] = None

    def elementProperties(self):
        js = super(CapabilityStatement2RestResourceOperation, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("definition", "definition", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


@dataclass
class CapabilityStatement2RestResource(BackboneElement):
    """ Resource served on the REST interface.

    A specification of the restful capabilities of the solution for a specific
    resource type.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2RestResource"
    type: str = None
    profile: Optional[str] = None
    supportedProfile: Optional[List[str]] = empty_list()
    documentation: Optional[str] = None
    interaction: Optional[List[CapabilityStatement2RestResourceInteraction]] = empty_list()
    searchParam: Optional[List[CapabilityStatement2RestResourceSearchParam]] = empty_list()
    operation: Optional[List[CapabilityStatement2RestResourceOperation]] = empty_list()

    def elementProperties(self):
        js = super(CapabilityStatement2RestResource, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("profile", "profile", str, False, None, False),
            ("supportedProfile", "supportedProfile", str, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("interaction", "interaction", CapabilityStatement2RestResourceInteraction, True, None, False),
            ("searchParam", "searchParam", CapabilityStatement2RestResourceSearchParam, True, None, False),
            ("operation", "operation", CapabilityStatement2RestResourceOperation, True, None, False),
        ])
        return js


@dataclass
class CapabilityStatement2RestInteraction(BackboneElement):
    """ What operations are supported?.

    A specification of restful operations supported by the system.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2RestInteraction"
    code: str = None
    documentation: Optional[str] = None

    def elementProperties(self):
        js = super(CapabilityStatement2RestInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


@dataclass
class CapabilityStatement2Software(BackboneElement):
    """ Software that is covered by this capability statement.

    Software that is covered by this capability statement.  It is used when the
    capability statement describes the capabilities of a particular software
    version, independent of an installation.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2Software"
    name: str = None
    version: Optional[str] = None
    releaseDate: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(CapabilityStatement2Software, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("version", "version", str, False, None, False),
            ("releaseDate", "releaseDate", FHIRDate, False, None, False),
        ])
        return js


@dataclass
class CapabilityStatement2Implementation(BackboneElement):
    """ If this describes a specific instance.

    Identifies a specific implementation instance that is described by the
    capability statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2Implementation"
    description: str = None
    url: Optional[str] = None
    custodian: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(CapabilityStatement2Implementation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("custodian", "custodian", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class CapabilityStatement2Rest(BackboneElement):
    """ If the endpoint is a RESTful one.

    A definition of the restful capabilities of the solution, if any.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2Rest"
    mode: str = None
    documentation: Optional[str] = None
    resource: Optional[List[CapabilityStatement2RestResource]] = empty_list()
    interaction: Optional[List[CapabilityStatement2RestInteraction]] = empty_list()
    searchParam: Optional[List[CapabilityStatement2RestResourceSearchParam]] = empty_list()
    operation: Optional[List[CapabilityStatement2RestResourceOperation]] = empty_list()
    compartment: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(CapabilityStatement2Rest, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
            ("resource", "resource", CapabilityStatement2RestResource, True, None, False),
            ("interaction", "interaction", CapabilityStatement2RestInteraction, True, None, False),
            ("searchParam", "searchParam", CapabilityStatement2RestResourceSearchParam, True, None, False),
            ("operation", "operation", CapabilityStatement2RestResourceOperation, True, None, False),
            ("compartment", "compartment", str, True, None, False),
        ])
        return js


@dataclass
class CapabilityStatement2(DomainResource):
    """ A statement of system capabilities.

    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server for a particular version of FHIR that may be used as a
    statement of actual server functionality or a statement of required or
    desired server implementation.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2"
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
    instantiates: Optional[List[str]] = empty_list()
    imports: Optional[List[str]] = empty_list()
    software: Optional[CapabilityStatement2Software] = None
    implementation: Optional[CapabilityStatement2Implementation] = None
    fhirVersion: str = None
    format: List[str] = empty_list()
    patchFormat: Optional[List[str]] = empty_list()
    implementationGuide: Optional[List[str]] = empty_list()
    rest: Optional[List[CapabilityStatement2Rest]] = empty_list()

    def elementProperties(self):
        js = super(CapabilityStatement2, self).elementProperties()
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
            ("instantiates", "instantiates", str, True, None, False),
            ("imports", "imports", str, True, None, False),
            ("software", "software", CapabilityStatement2Software, False, None, False),
            ("implementation", "implementation", CapabilityStatement2Implementation, False, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, True),
            ("format", "format", str, True, None, True),
            ("patchFormat", "patchFormat", str, True, None, False),
            ("implementationGuide", "implementationGuide", str, True, None, False),
            ("rest", "rest", CapabilityStatement2Rest, True, None, False),
        ])
        return js