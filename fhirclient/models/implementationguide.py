#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ImplementationGuide) on 2019-08-06.
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
class ImplementationGuideManifestResource(BackboneElement):
    """ Resource in the implementation guide.

    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    resource_type: ClassVar[str] = "ImplementationGuideManifestResource"
    reference: FHIRReference = None
    exampleBoolean: Optional[bool] = None
    exampleCanonical: Optional[str] = None
    relativePath: Optional[str] = None

    def elementProperties(self):
        js = super(ImplementationGuideManifestResource, self).elementProperties()
        js.extend([
            ("reference", "reference", FHIRReference, False, None, True),
            ("exampleBoolean", "exampleBoolean", bool, False, "example", False),
            ("exampleCanonical", "exampleCanonical", str, False, "example", False),
            ("relativePath", "relativePath", str, False, None, False),
        ])
        return js


@dataclass
class ImplementationGuideManifestPage(BackboneElement):
    """ HTML page within the parent IG.

    Information about a page within the IG.
    """
    resource_type: ClassVar[str] = "ImplementationGuideManifestPage"
    name: str = None
    title: Optional[str] = None
    anchor: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(ImplementationGuideManifestPage, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("anchor", "anchor", str, True, None, False),
        ])
        return js


@dataclass
class ImplementationGuideDefinitionGrouping(BackboneElement):
    """ Grouping used to present related resources in the IG.

    A logical group of resources. Logical groups can be used when building
    pages.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionGrouping"
    name: str = None
    description: Optional[str] = None

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionGrouping, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("description", "description", str, False, None, False),
        ])
        return js


@dataclass
class ImplementationGuideDefinitionResource(BackboneElement):
    """ Resource in the implementation guide.

    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionResource"
    reference: FHIRReference = None
    fhirVersion: Optional[List[str]] = empty_list()
    name: Optional[str] = None
    description: Optional[str] = None
    exampleBoolean: Optional[bool] = None
    exampleCanonical: Optional[str] = None
    groupingId: Optional[str] = None

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionResource, self).elementProperties()
        js.extend([
            ("reference", "reference", FHIRReference, False, None, True),
            ("fhirVersion", "fhirVersion", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("exampleBoolean", "exampleBoolean", bool, False, "example", False),
            ("exampleCanonical", "exampleCanonical", str, False, "example", False),
            ("groupingId", "groupingId", str, False, None, False),
        ])
        return js


@dataclass
class ImplementationGuideDefinitionPage(BackboneElement):
    """ Page/Section in the Guide.

    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionPage"
    nameUrl: str = None
    nameReference: FHIRReference = None
    title: str = None
    generation: str = None
    page: Optional[List["ImplementationGuideDefinitionPage"]] = empty_list()

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionPage, self).elementProperties()
        js.extend([
            ("nameUrl", "nameUrl", str, False, "name", True),
            ("nameReference", "nameReference", FHIRReference, False, "name", True),
            ("title", "title", str, False, None, True),
            ("generation", "generation", str, False, None, True),
            ("page", "page", ImplementationGuideDefinitionPage, True, None, False),
        ])
        return js


@dataclass
class ImplementationGuideDefinitionParameter(BackboneElement):
    """ Defines how IG is built by tools.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionParameter"
    code: str = None
    value: str = None

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionParameter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


@dataclass
class ImplementationGuideDefinitionTemplate(BackboneElement):
    """ A template for building resources.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionTemplate"
    code: str = None
    source: str = None
    scope: Optional[str] = None

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionTemplate, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("source", "source", str, False, None, True),
            ("scope", "scope", str, False, None, False),
        ])
        return js


@dataclass
class ImplementationGuideDependsOn(BackboneElement):
    """ Another Implementation guide this depends on.

    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDependsOn"
    uri: str = None
    packageId: Optional[str] = None
    version: Optional[str] = None

    def elementProperties(self):
        js = super(ImplementationGuideDependsOn, self).elementProperties()
        js.extend([
            ("uri", "uri", str, False, None, True),
            ("packageId", "packageId", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


@dataclass
class ImplementationGuideGlobal(BackboneElement):
    """ Profiles that apply globally.

    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """
    resource_type: ClassVar[str] = "ImplementationGuideGlobal"
    type: str = None
    profile: str = None

    def elementProperties(self):
        js = super(ImplementationGuideGlobal, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("profile", "profile", str, False, None, True),
        ])
        return js


@dataclass
class ImplementationGuideDefinition(BackboneElement):
    """ Information needed to build the IG.

    The information needed by an IG publisher tool to publish the whole
    implementation guide.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinition"
    grouping: Optional[List[ImplementationGuideDefinitionGrouping]] = empty_list()
    resource: List[ImplementationGuideDefinitionResource] = empty_list()
    page: Optional[ImplementationGuideDefinitionPage] = None
    parameter: Optional[List[ImplementationGuideDefinitionParameter]] = empty_list()
    template: Optional[List[ImplementationGuideDefinitionTemplate]] = empty_list()

    def elementProperties(self):
        js = super(ImplementationGuideDefinition, self).elementProperties()
        js.extend([
            ("grouping", "grouping", ImplementationGuideDefinitionGrouping, True, None, False),
            ("resource", "resource", ImplementationGuideDefinitionResource, True, None, True),
            ("page", "page", ImplementationGuideDefinitionPage, False, None, False),
            ("parameter", "parameter", ImplementationGuideDefinitionParameter, True, None, False),
            ("template", "template", ImplementationGuideDefinitionTemplate, True, None, False),
        ])
        return js


@dataclass
class ImplementationGuideManifest(BackboneElement):
    """ Information about an assembled IG.

    Information about an assembled implementation guide, created by the
    publication tooling.
    """
    resource_type: ClassVar[str] = "ImplementationGuideManifest"
    rendering: Optional[str] = None
    resource: List[ImplementationGuideManifestResource] = empty_list()
    page: Optional[List[ImplementationGuideManifestPage]] = empty_list()
    image: Optional[List[str]] = empty_list()
    other: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(ImplementationGuideManifest, self).elementProperties()
        js.extend([
            ("rendering", "rendering", str, False, None, False),
            ("resource", "resource", ImplementationGuideManifestResource, True, None, True),
            ("page", "page", ImplementationGuideManifestPage, True, None, False),
            ("image", "image", str, True, None, False),
            ("other", "other", str, True, None, False),
        ])
        return js


@dataclass
class ImplementationGuide(DomainResource):
    """ A set of rules about how FHIR is used.

    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used
    to gather all the parts of an implementation guide into a logical whole and
    to publish a computable definition of all the parts.
    """
    resource_type: ClassVar[str] = "ImplementationGuide"
    url: str = None
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
    copyright: Optional[str] = None
    packageId: str = None
    license: Optional[str] = None
    fhirVersion: List[str] = empty_list()
    dependsOn: Optional[List[ImplementationGuideDependsOn]] = empty_list()
    global_fhir: Optional[List[ImplementationGuideGlobal]] = empty_list()
    definition: Optional[ImplementationGuideDefinition] = None
    manifest: Optional[ImplementationGuideManifest] = None

    def elementProperties(self):
        js = super(ImplementationGuide, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
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
            ("copyright", "copyright", str, False, None, False),
            ("packageId", "packageId", str, False, None, True),
            ("license", "license", str, False, None, False),
            ("fhirVersion", "fhirVersion", str, True, None, True),
            ("dependsOn", "dependsOn", ImplementationGuideDependsOn, True, None, False),
            ("global_fhir", "global", ImplementationGuideGlobal, True, None, False),
            ("definition", "definition", ImplementationGuideDefinition, False, None, False),
            ("manifest", "manifest", ImplementationGuideManifest, False, None, False),
        ])
        return js