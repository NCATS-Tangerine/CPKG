#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/OperationDefinition) on 2019-08-06.
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
class OperationDefinitionParameterBinding(BackboneElement):
    """ ValueSet details if this is coded.

    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """
    resource_type: ClassVar[str] = "OperationDefinitionParameterBinding"
    strength: str = None
    valueSet: str = None

    def elementProperties(self):
        js = super(OperationDefinitionParameterBinding, self).elementProperties()
        js.extend([
            ("strength", "strength", str, False, None, True),
            ("valueSet", "valueSet", str, False, None, True),
        ])
        return js


@dataclass
class OperationDefinitionParameterReferencedFrom(BackboneElement):
    """ References to this parameter.

    Identifies other resource parameters within the operation invocation that
    are expected to resolve to this resource.
    """
    resource_type: ClassVar[str] = "OperationDefinitionParameterReferencedFrom"
    source: str = None
    sourceId: Optional[str] = None

    def elementProperties(self):
        js = super(OperationDefinitionParameterReferencedFrom, self).elementProperties()
        js.extend([
            ("source", "source", str, False, None, True),
            ("sourceId", "sourceId", str, False, None, False),
        ])
        return js


@dataclass
class OperationDefinitionParameter(BackboneElement):
    """ Parameters for the operation/query.

    The parameters for the operation/query.
    """
    resource_type: ClassVar[str] = "OperationDefinitionParameter"
    name: str = None
    use: str = None
    min: int = None
    max: str = None
    documentation: Optional[str] = None
    type: Optional[str] = None
    targetProfile: Optional[List[str]] = empty_list()
    searchType: Optional[str] = None
    binding: Optional[OperationDefinitionParameterBinding] = None
    referencedFrom: Optional[List[OperationDefinitionParameterReferencedFrom]] = empty_list()
    part: Optional[List["OperationDefinitionParameter"]] = empty_list()

    def elementProperties(self):
        js = super(OperationDefinitionParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("use", "use", str, False, None, True),
            ("min", "min", int, False, None, True),
            ("max", "max", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
            ("type", "type", str, False, None, False),
            ("targetProfile", "targetProfile", str, True, None, False),
            ("searchType", "searchType", str, False, None, False),
            ("binding", "binding", OperationDefinitionParameterBinding, False, None, False),
            ("referencedFrom", "referencedFrom", OperationDefinitionParameterReferencedFrom, True, None, False),
            ("part", "part", OperationDefinitionParameter, True, None, False),
        ])
        return js


@dataclass
class OperationDefinitionOverload(BackboneElement):
    """ Define overloaded variants for when  generating code.

    Defines an appropriate combination of parameters to use when invoking this
    operation, to help code generators when generating overloaded parameter
    sets for this operation.
    """
    resource_type: ClassVar[str] = "OperationDefinitionOverload"
    parameterName: Optional[List[str]] = empty_list()
    comment: Optional[str] = None

    def elementProperties(self):
        js = super(OperationDefinitionOverload, self).elementProperties()
        js.extend([
            ("parameterName", "parameterName", str, True, None, False),
            ("comment", "comment", str, False, None, False),
        ])
        return js


@dataclass
class OperationDefinition(DomainResource):
    """ Definition of an operation or a named query.

    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """
    resource_type: ClassVar[str] = "OperationDefinition"
    url: Optional[str] = None
    version: Optional[str] = None
    name: str = None
    title: Optional[str] = None
    status: str = None
    kind: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    purpose: Optional[str] = None
    affectsState: Optional[bool] = None
    code: str = None
    comment: Optional[str] = None
    base: Optional[str] = None
    resource: Optional[List[str]] = empty_list()
    system: bool = None
    type: bool = None
    instance: bool = None
    inputProfile: Optional[str] = None
    outputProfile: Optional[str] = None
    parameter: Optional[List[OperationDefinitionParameter]] = empty_list()
    overload: Optional[List[OperationDefinitionOverload]] = empty_list()

    def elementProperties(self):
        js = super(OperationDefinition, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("kind", "kind", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("affectsState", "affectsState", bool, False, None, False),
            ("code", "code", str, False, None, True),
            ("comment", "comment", str, False, None, False),
            ("base", "base", str, False, None, False),
            ("resource", "resource", str, True, None, False),
            ("system", "system", bool, False, None, True),
            ("type", "type", bool, False, None, True),
            ("instance", "instance", bool, False, None, True),
            ("inputProfile", "inputProfile", str, False, None, False),
            ("outputProfile", "outputProfile", str, False, None, False),
            ("parameter", "parameter", OperationDefinitionParameter, True, None, False),
            ("overload", "overload", OperationDefinitionOverload, True, None, False),
        ])
        return js