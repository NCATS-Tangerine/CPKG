#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/CapabilityStatement) on 2019-08-06.
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
from .fhirreference import FHIRReference
from .usagecontext import UsageContext


@dataclass
class CapabilityStatementMessagingEndpoint(BackboneElement):
    """ Where messages should be sent.

    An endpoint (network accessible address) to which messages and/or replies
    are to be sent.
    """
    resource_type: ClassVar[str] = "CapabilityStatementMessagingEndpoint"
    protocol: Coding = None
    address: str = None

    def elementProperties(self):
        js = super(CapabilityStatementMessagingEndpoint, self).elementProperties()
        js.extend([
            ("protocol", "protocol", Coding, False, None, True),
            ("address", "address", str, False, None, True),
        ])
        return js


@dataclass
class CapabilityStatementMessagingSupportedMessage(BackboneElement):
    """ Messages supported by this system.

    References to message definitions for messages this system can send or
    receive.
    """
    resource_type: ClassVar[str] = "CapabilityStatementMessagingSupportedMessage"
    mode: str = None
    definition: str = None

    def elementProperties(self):
        js = super(CapabilityStatementMessagingSupportedMessage, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, True),
            ("definition", "definition", str, False, None, True),
        ])
        return js


@dataclass
class CapabilityStatementRestResourceInteraction(BackboneElement):
    """ What operations are supported?.

    Identifies a restful operation supported by the solution.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestResourceInteraction"
    code: str = None
    documentation: Optional[str] = None

    def elementProperties(self):
        js = super(CapabilityStatementRestResourceInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


@dataclass
class CapabilityStatementRestResourceSearchParam(BackboneElement):
    """ Search parameters supported by implementation.

    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestResourceSearchParam"
    name: str = None
    definition: Optional[str] = None
    type: str = None
    documentation: Optional[str] = None

    def elementProperties(self):
        js = super(CapabilityStatementRestResourceSearchParam, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("definition", "definition", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


@dataclass
class CapabilityStatementRestResourceOperation(BackboneElement):
    """ Definition of a resource operation.

    Definition of an operation or a named query together with its parameters
    and their meaning and type. Consult the definition of the operation for
    details about how to invoke the operation, and the parameters.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestResourceOperation"
    name: str = None
    definition: str = None
    documentation: Optional[str] = None

    def elementProperties(self):
        js = super(CapabilityStatementRestResourceOperation, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("definition", "definition", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


@dataclass
class CapabilityStatementRestSecurity(BackboneElement):
    """ Information about security of implementation.

    Information about security implementation from an interface perspective -
    what a client needs to know.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestSecurity"
    cors: Optional[bool] = None
    service: Optional[List[CodeableConcept]] = empty_list()
    description: Optional[str] = None

    def elementProperties(self):
        js = super(CapabilityStatementRestSecurity, self).elementProperties()
        js.extend([
            ("cors", "cors", bool, False, None, False),
            ("service", "service", CodeableConcept, True, None, False),
            ("description", "description", str, False, None, False),
        ])
        return js


@dataclass
class CapabilityStatementRestResource(BackboneElement):
    """ Resource served on the REST interface.

    A specification of the restful capabilities of the solution for a specific
    resource type.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestResource"
    type: str = None
    profile: Optional[str] = None
    supportedProfile: Optional[List[str]] = empty_list()
    documentation: Optional[str] = None
    interaction: Optional[List[CapabilityStatementRestResourceInteraction]] = empty_list()
    versioning: Optional[str] = None
    readHistory: Optional[bool] = None
    updateCreate: Optional[bool] = None
    conditionalCreate: Optional[bool] = None
    conditionalRead: Optional[str] = None
    conditionalUpdate: Optional[bool] = None
    conditionalDelete: Optional[str] = None
    referencePolicy: Optional[List[str]] = empty_list()
    searchInclude: Optional[List[str]] = empty_list()
    searchRevInclude: Optional[List[str]] = empty_list()
    searchParam: Optional[List[CapabilityStatementRestResourceSearchParam]] = empty_list()
    operation: Optional[List[CapabilityStatementRestResourceOperation]] = empty_list()

    def elementProperties(self):
        js = super(CapabilityStatementRestResource, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("profile", "profile", str, False, None, False),
            ("supportedProfile", "supportedProfile", str, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("interaction", "interaction", CapabilityStatementRestResourceInteraction, True, None, False),
            ("versioning", "versioning", str, False, None, False),
            ("readHistory", "readHistory", bool, False, None, False),
            ("updateCreate", "updateCreate", bool, False, None, False),
            ("conditionalCreate", "conditionalCreate", bool, False, None, False),
            ("conditionalRead", "conditionalRead", str, False, None, False),
            ("conditionalUpdate", "conditionalUpdate", bool, False, None, False),
            ("conditionalDelete", "conditionalDelete", str, False, None, False),
            ("referencePolicy", "referencePolicy", str, True, None, False),
            ("searchInclude", "searchInclude", str, True, None, False),
            ("searchRevInclude", "searchRevInclude", str, True, None, False),
            ("searchParam", "searchParam", CapabilityStatementRestResourceSearchParam, True, None, False),
            ("operation", "operation", CapabilityStatementRestResourceOperation, True, None, False),
        ])
        return js


@dataclass
class CapabilityStatementRestInteraction(BackboneElement):
    """ What operations are supported?.

    A specification of restful operations supported by the system.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestInteraction"
    code: str = None
    documentation: Optional[str] = None

    def elementProperties(self):
        js = super(CapabilityStatementRestInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


@dataclass
class CapabilityStatementSoftware(BackboneElement):
    """ Software that is covered by this capability statement.

    Software that is covered by this capability statement.  It is used when the
    capability statement describes the capabilities of a particular software
    version, independent of an installation.
    """
    resource_type: ClassVar[str] = "CapabilityStatementSoftware"
    name: str = None
    version: Optional[str] = None
    releaseDate: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(CapabilityStatementSoftware, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("version", "version", str, False, None, False),
            ("releaseDate", "releaseDate", FHIRDate, False, None, False),
        ])
        return js


@dataclass
class CapabilityStatementImplementation(BackboneElement):
    """ If this describes a specific instance.

    Identifies a specific implementation instance that is described by the
    capability statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """
    resource_type: ClassVar[str] = "CapabilityStatementImplementation"
    description: str = None
    url: Optional[str] = None
    custodian: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(CapabilityStatementImplementation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("custodian", "custodian", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class CapabilityStatementRest(BackboneElement):
    """ If the endpoint is a RESTful one.

    A definition of the restful capabilities of the solution, if any.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRest"
    mode: str = None
    documentation: Optional[str] = None
    security: Optional[CapabilityStatementRestSecurity] = None
    resource: Optional[List[CapabilityStatementRestResource]] = empty_list()
    interaction: Optional[List[CapabilityStatementRestInteraction]] = empty_list()
    searchParam: Optional[List[CapabilityStatementRestResourceSearchParam]] = empty_list()
    operation: Optional[List[CapabilityStatementRestResourceOperation]] = empty_list()
    compartment: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(CapabilityStatementRest, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
            ("security", "security", CapabilityStatementRestSecurity, False, None, False),
            ("resource", "resource", CapabilityStatementRestResource, True, None, False),
            ("interaction", "interaction", CapabilityStatementRestInteraction, True, None, False),
            ("searchParam", "searchParam", CapabilityStatementRestResourceSearchParam, True, None, False),
            ("operation", "operation", CapabilityStatementRestResourceOperation, True, None, False),
            ("compartment", "compartment", str, True, None, False),
        ])
        return js


@dataclass
class CapabilityStatementMessaging(BackboneElement):
    """ If messaging is supported.

    A description of the messaging capabilities of the solution.
    """
    resource_type: ClassVar[str] = "CapabilityStatementMessaging"
    endpoint: Optional[List[CapabilityStatementMessagingEndpoint]] = empty_list()
    reliableCache: Optional[int] = None
    documentation: Optional[str] = None
    supportedMessage: Optional[List[CapabilityStatementMessagingSupportedMessage]] = empty_list()

    def elementProperties(self):
        js = super(CapabilityStatementMessaging, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", CapabilityStatementMessagingEndpoint, True, None, False),
            ("reliableCache", "reliableCache", int, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("supportedMessage", "supportedMessage", CapabilityStatementMessagingSupportedMessage, True, None, False),
        ])
        return js


@dataclass
class CapabilityStatementDocument(BackboneElement):
    """ Document definition.

    A document definition.
    """
    resource_type: ClassVar[str] = "CapabilityStatementDocument"
    mode: str = None
    documentation: Optional[str] = None
    profile: str = None

    def elementProperties(self):
        js = super(CapabilityStatementDocument, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
            ("profile", "profile", str, False, None, True),
        ])
        return js


@dataclass
class CapabilityStatement(DomainResource):
    """ A statement of system capabilities.

    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server for a particular version of FHIR that may be used as a
    statement of actual server functionality or a statement of required or
    desired server implementation.
    """
    resource_type: ClassVar[str] = "CapabilityStatement"
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
    software: Optional[CapabilityStatementSoftware] = None
    implementation: Optional[CapabilityStatementImplementation] = None
    fhirVersion: str = None
    format: List[str] = empty_list()
    patchFormat: Optional[List[str]] = empty_list()
    implementationGuide: Optional[List[str]] = empty_list()
    rest: Optional[List[CapabilityStatementRest]] = empty_list()
    messaging: Optional[List[CapabilityStatementMessaging]] = empty_list()
    document: Optional[List[CapabilityStatementDocument]] = empty_list()

    def elementProperties(self):
        js = super(CapabilityStatement, self).elementProperties()
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
            ("software", "software", CapabilityStatementSoftware, False, None, False),
            ("implementation", "implementation", CapabilityStatementImplementation, False, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, True),
            ("format", "format", str, True, None, True),
            ("patchFormat", "patchFormat", str, True, None, False),
            ("implementationGuide", "implementationGuide", str, True, None, False),
            ("rest", "rest", CapabilityStatementRest, True, None, False),
            ("messaging", "messaging", CapabilityStatementMessaging, True, None, False),
            ("document", "document", CapabilityStatementDocument, True, None, False),
        ])
        return js