#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ExampleScenario) on 2019-08-06.
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
class ExampleScenarioProcessStepOperation(BackboneElement):
    """ Each interaction or action.
    """
    resource_type: ClassVar[str] = "ExampleScenarioProcessStepOperation"
    number: str = None
    type: Optional[str] = None
    name: Optional[str] = None
    initiator: Optional[str] = None
    receiver: Optional[str] = None
    description: Optional[str] = None
    initiatorActive: Optional[bool] = None
    receiverActive: Optional[bool] = None
    request: Optional["ExampleScenarioInstanceContainedInstance"] = None
    response: Optional["ExampleScenarioInstanceContainedInstance"] = None

    def elementProperties(self):
        js = super(ExampleScenarioProcessStepOperation, self).elementProperties()
        js.extend([
            ("number", "number", str, False, None, True),
            ("type", "type", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("initiator", "initiator", str, False, None, False),
            ("receiver", "receiver", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("initiatorActive", "initiatorActive", bool, False, None, False),
            ("receiverActive", "receiverActive", bool, False, None, False),
            ("request", "request", ExampleScenarioInstanceContainedInstance, False, None, False),
            ("response", "response", ExampleScenarioInstanceContainedInstance, False, None, False),
        ])
        return js


@dataclass
class ExampleScenarioProcessStepAlternative(BackboneElement):
    """ Alternate non-typical step action.

    Indicates an alternative step that can be taken instead of the operations
    on the base step in exceptional/atypical circumstances.
    """
    resource_type: ClassVar[str] = "ExampleScenarioProcessStepAlternative"
    title: str = None
    description: Optional[str] = None
    step: Optional[List["ExampleScenarioProcessStep"]] = empty_list()

    def elementProperties(self):
        js = super(ExampleScenarioProcessStepAlternative, self).elementProperties()
        js.extend([
            ("title", "title", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("step", "step", ExampleScenarioProcessStep, True, None, False),
        ])
        return js


@dataclass
class ExampleScenarioProcessStep(BackboneElement):
    """ Each step of the process.
    """
    resource_type: ClassVar[str] = "ExampleScenarioProcessStep"
    process: Optional[List["ExampleScenarioProcess"]] = empty_list()
    pause: Optional[bool] = None
    operation: Optional[ExampleScenarioProcessStepOperation] = None
    alternative: Optional[List[ExampleScenarioProcessStepAlternative]] = empty_list()

    def elementProperties(self):
        js = super(ExampleScenarioProcessStep, self).elementProperties()
        js.extend([
            ("process", "process", ExampleScenarioProcess, True, None, False),
            ("pause", "pause", bool, False, None, False),
            ("operation", "operation", ExampleScenarioProcessStepOperation, False, None, False),
            ("alternative", "alternative", ExampleScenarioProcessStepAlternative, True, None, False),
        ])
        return js


@dataclass
class ExampleScenarioInstanceVersion(BackboneElement):
    """ A specific version of the resource.
    """
    resource_type: ClassVar[str] = "ExampleScenarioInstanceVersion"
    versionId: str = None
    description: str = None

    def elementProperties(self):
        js = super(ExampleScenarioInstanceVersion, self).elementProperties()
        js.extend([
            ("versionId", "versionId", str, False, None, True),
            ("description", "description", str, False, None, True),
        ])
        return js


@dataclass
class ExampleScenarioInstanceContainedInstance(BackboneElement):
    """ Resources contained in the instance.

    Resources contained in the instance (e.g. the observations contained in a
    bundle).
    """
    resource_type: ClassVar[str] = "ExampleScenarioInstanceContainedInstance"
    resourceId: str = None
    versionId: Optional[str] = None

    def elementProperties(self):
        js = super(ExampleScenarioInstanceContainedInstance, self).elementProperties()
        js.extend([
            ("resourceId", "resourceId", str, False, None, True),
            ("versionId", "versionId", str, False, None, False),
        ])
        return js


@dataclass
class ExampleScenarioActor(BackboneElement):
    """ Actor participating in the resource.
    """
    resource_type: ClassVar[str] = "ExampleScenarioActor"
    actorId: str = None
    type: str = None
    name: Optional[str] = None
    description: Optional[str] = None

    def elementProperties(self):
        js = super(ExampleScenarioActor, self).elementProperties()
        js.extend([
            ("actorId", "actorId", str, False, None, True),
            ("type", "type", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("description", "description", str, False, None, False),
        ])
        return js


@dataclass
class ExampleScenarioInstance(BackboneElement):
    """ Each resource and each version that is present in the workflow.
    """
    resource_type: ClassVar[str] = "ExampleScenarioInstance"
    resourceId: str = None
    resourceType: str = None
    name: Optional[str] = None
    description: Optional[str] = None
    version: Optional[List[ExampleScenarioInstanceVersion]] = empty_list()
    containedInstance: Optional[List[ExampleScenarioInstanceContainedInstance]] = empty_list()

    def elementProperties(self):
        js = super(ExampleScenarioInstance, self).elementProperties()
        js.extend([
            ("resourceId", "resourceId", str, False, None, True),
            ("resourceType", "resourceType", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("version", "version", ExampleScenarioInstanceVersion, True, None, False),
            ("containedInstance", "containedInstance", ExampleScenarioInstanceContainedInstance, True, None, False),
        ])
        return js


@dataclass
class ExampleScenarioProcess(BackboneElement):
    """ Each major process - a group of operations.
    """
    resource_type: ClassVar[str] = "ExampleScenarioProcess"
    title: str = None
    description: Optional[str] = None
    preConditions: Optional[str] = None
    postConditions: Optional[str] = None
    step: Optional[List[ExampleScenarioProcessStep]] = empty_list()

    def elementProperties(self):
        js = super(ExampleScenarioProcess, self).elementProperties()
        js.extend([
            ("title", "title", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("preConditions", "preConditions", str, False, None, False),
            ("postConditions", "postConditions", str, False, None, False),
            ("step", "step", ExampleScenarioProcessStep, True, None, False),
        ])
        return js


@dataclass
class ExampleScenario(DomainResource):
    """ Example of workflow instance.
    """
    resource_type: ClassVar[str] = "ExampleScenario"
    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    version: Optional[str] = None
    name: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    useContext: Optional[List[UsageContext]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    copyright: Optional[str] = None
    purpose: Optional[str] = None
    actor: Optional[List[ExampleScenarioActor]] = empty_list()
    instance: Optional[List[ExampleScenarioInstance]] = empty_list()
    process: Optional[List[ExampleScenarioProcess]] = empty_list()
    workflow: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(ExampleScenario, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("actor", "actor", ExampleScenarioActor, True, None, False),
            ("instance", "instance", ExampleScenarioInstance, True, None, False),
            ("process", "process", ExampleScenarioProcess, True, None, False),
            ("workflow", "workflow", str, True, None, False),
        ])
        return js