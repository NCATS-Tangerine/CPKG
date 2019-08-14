#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/PlanDefinition) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .age import Age
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .datarequirement import DataRequirement
from .domainresource import DomainResource
from .duration import Duration
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .relatedartifact import RelatedArtifact
from .timing import Timing
from .triggerdefinition import TriggerDefinition
from .usagecontext import UsageContext


@dataclass
class PlanDefinitionActionCondition(BackboneElement):
    """ Whether or not the action is applicable.

    An expression that describes applicability criteria or start/stop
    conditions for the action.
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionCondition"
    kind: str = None
    expression: Optional[Expression] = None

    def elementProperties(self):
        js = super(PlanDefinitionActionCondition, self).elementProperties()
        js.extend([
            ("kind", "kind", str, False, None, True),
            ("expression", "expression", Expression, False, None, False),
        ])
        return js


@dataclass
class PlanDefinitionActionRelatedAction(BackboneElement):
    """ Relationship to another action.

    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionRelatedAction"
    actionId: str = None
    relationship: str = None
    offsetDuration: Optional[Duration] = None
    offsetRange: Optional[Range] = None

    def elementProperties(self):
        js = super(PlanDefinitionActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", str, False, None, True),
            ("relationship", "relationship", str, False, None, True),
            ("offsetDuration", "offsetDuration", Duration, False, "offset", False),
            ("offsetRange", "offsetRange", Range, False, "offset", False),
        ])
        return js


@dataclass
class PlanDefinitionActionParticipant(BackboneElement):
    """ Who should participate in the action.

    Indicates who should participate in performing the action described.
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionParticipant"
    type: str = None
    role: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(PlanDefinitionActionParticipant, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("role", "role", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class PlanDefinitionActionDynamicValue(BackboneElement):
    """ Dynamic aspects of the definition.

    Customizations that should be applied to the statically defined resource.
    For example, if the dosage of a medication must be computed based on the
    patient's weight, a customization would be used to specify an expression
    that calculated the weight, and the path on the resource that would contain
    the result.
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionDynamicValue"
    path: Optional[str] = None
    expression: Optional[Expression] = None

    def elementProperties(self):
        js = super(PlanDefinitionActionDynamicValue, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, False),
            ("expression", "expression", Expression, False, None, False),
        ])
        return js


@dataclass
class PlanDefinitionGoalTarget(BackboneElement):
    """ Target outcome for the goal.

    Indicates what should be done and within what timeframe.
    """
    resource_type: ClassVar[str] = "PlanDefinitionGoalTarget"
    measure: Optional[CodeableConcept] = None
    detailQuantity: Optional[Quantity] = None
    detailRange: Optional[Range] = None
    detailCodeableConcept: Optional[CodeableConcept] = None
    due: Optional[Duration] = None

    def elementProperties(self):
        js = super(PlanDefinitionGoalTarget, self).elementProperties()
        js.extend([
            ("measure", "measure", CodeableConcept, False, None, False),
            ("detailQuantity", "detailQuantity", Quantity, False, "detail", False),
            ("detailRange", "detailRange", Range, False, "detail", False),
            ("detailCodeableConcept", "detailCodeableConcept", CodeableConcept, False, "detail", False),
            ("due", "due", Duration, False, None, False),
        ])
        return js


@dataclass
class PlanDefinitionGoal(BackboneElement):
    """ What the plan is trying to accomplish.

    Goals that describe what the activities within the plan are intended to
    achieve. For example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """
    resource_type: ClassVar[str] = "PlanDefinitionGoal"
    category: Optional[CodeableConcept] = None
    description: CodeableConcept = None
    priority: Optional[CodeableConcept] = None
    start: Optional[CodeableConcept] = None
    addresses: Optional[List[CodeableConcept]] = empty_list()
    documentation: Optional[List[RelatedArtifact]] = empty_list()
    target: Optional[List[PlanDefinitionGoalTarget]] = empty_list()

    def elementProperties(self):
        js = super(PlanDefinitionGoal, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, False),
            ("description", "description", CodeableConcept, False, None, True),
            ("priority", "priority", CodeableConcept, False, None, False),
            ("start", "start", CodeableConcept, False, None, False),
            ("addresses", "addresses", CodeableConcept, True, None, False),
            ("documentation", "documentation", RelatedArtifact, True, None, False),
            ("target", "target", PlanDefinitionGoalTarget, True, None, False),
        ])
        return js


@dataclass
class PlanDefinitionAction(BackboneElement):
    """ Action defined by the plan.

    An action or group of actions to be taken as part of the plan.
    """
    resource_type: ClassVar[str] = "PlanDefinitionAction"
    prefix: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    textEquivalent: Optional[str] = None
    priority: Optional[str] = None
    code: Optional[List[CodeableConcept]] = empty_list()
    reason: Optional[List[CodeableConcept]] = empty_list()
    documentation: Optional[List[RelatedArtifact]] = empty_list()
    goalId: Optional[List[str]] = empty_list()
    subjectCodeableConcept: Optional[CodeableConcept] = None
    subjectReference: Optional[FHIRReference] = None
    trigger: Optional[List[TriggerDefinition]] = empty_list()
    condition: Optional[List[PlanDefinitionActionCondition]] = empty_list()
    input: Optional[List[DataRequirement]] = empty_list()
    output: Optional[List[DataRequirement]] = empty_list()
    relatedAction: Optional[List[PlanDefinitionActionRelatedAction]] = empty_list()
    timingDateTime: Optional[FHIRDate] = None
    timingAge: Optional[Age] = None
    timingPeriod: Optional[Period] = None
    timingDuration: Optional[Duration] = None
    timingRange: Optional[Range] = None
    timingTiming: Optional[Timing] = None
    participant: Optional[List[PlanDefinitionActionParticipant]] = empty_list()
    type: Optional[CodeableConcept] = None
    groupingBehavior: Optional[str] = None
    selectionBehavior: Optional[str] = None
    requiredBehavior: Optional[str] = None
    precheckBehavior: Optional[str] = None
    cardinalityBehavior: Optional[str] = None
    definitionCanonical: Optional[str] = None
    definitionUri: Optional[str] = None
    transform: Optional[str] = None
    dynamicValue: Optional[List[PlanDefinitionActionDynamicValue]] = empty_list()
    action: Optional[List["PlanDefinitionAction"]] = empty_list()

    def elementProperties(self):
        js = super(PlanDefinitionAction, self).elementProperties()
        js.extend([
            ("prefix", "prefix", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("code", "code", CodeableConcept, True, None, False),
            ("reason", "reason", CodeableConcept, True, None, False),
            ("documentation", "documentation", RelatedArtifact, True, None, False),
            ("goalId", "goalId", str, True, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", FHIRReference, False, "subject", False),
            ("trigger", "trigger", TriggerDefinition, True, None, False),
            ("condition", "condition", PlanDefinitionActionCondition, True, None, False),
            ("input", "input", DataRequirement, True, None, False),
            ("output", "output", DataRequirement, True, None, False),
            ("relatedAction", "relatedAction", PlanDefinitionActionRelatedAction, True, None, False),
            ("timingDateTime", "timingDateTime", FHIRDate, False, "timing", False),
            ("timingAge", "timingAge", Age, False, "timing", False),
            ("timingPeriod", "timingPeriod", Period, False, "timing", False),
            ("timingDuration", "timingDuration", Duration, False, "timing", False),
            ("timingRange", "timingRange", Range, False, "timing", False),
            ("timingTiming", "timingTiming", Timing, False, "timing", False),
            ("participant", "participant", PlanDefinitionActionParticipant, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("groupingBehavior", "groupingBehavior", str, False, None, False),
            ("selectionBehavior", "selectionBehavior", str, False, None, False),
            ("requiredBehavior", "requiredBehavior", str, False, None, False),
            ("precheckBehavior", "precheckBehavior", str, False, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", str, False, None, False),
            ("definitionCanonical", "definitionCanonical", str, False, "definition", False),
            ("definitionUri", "definitionUri", str, False, "definition", False),
            ("transform", "transform", str, False, None, False),
            ("dynamicValue", "dynamicValue", PlanDefinitionActionDynamicValue, True, None, False),
            ("action", "action", PlanDefinitionAction, True, None, False),
        ])
        return js


@dataclass
class PlanDefinition(DomainResource):
    """ The definition of a plan for a series of actions, independent of any
    specific patient or context.

    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """
    resource_type: ClassVar[str] = "PlanDefinition"
    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
    type: Optional[CodeableConcept] = None
    status: str = None
    experimental: Optional[bool] = None
    subjectCodeableConcept: Optional[CodeableConcept] = None
    subjectReference: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    purpose: Optional[str] = None
    usage: Optional[str] = None
    copyright: Optional[str] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    topic: Optional[List[CodeableConcept]] = empty_list()
    author: Optional[List[ContactDetail]] = empty_list()
    editor: Optional[List[ContactDetail]] = empty_list()
    reviewer: Optional[List[ContactDetail]] = empty_list()
    endorser: Optional[List[ContactDetail]] = empty_list()
    relatedArtifact: Optional[List[RelatedArtifact]] = empty_list()
    library: Optional[List[str]] = empty_list()
    goal: Optional[List[PlanDefinitionGoal]] = empty_list()
    action: Optional[List[PlanDefinitionAction]] = empty_list()

    def elementProperties(self):
        js = super(PlanDefinition, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("subtitle", "subtitle", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", FHIRReference, False, "subject", False),
            ("date", "date", FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("topic", "topic", CodeableConcept, True, None, False),
            ("author", "author", ContactDetail, True, None, False),
            ("editor", "editor", ContactDetail, True, None, False),
            ("reviewer", "reviewer", ContactDetail, True, None, False),
            ("endorser", "endorser", ContactDetail, True, None, False),
            ("relatedArtifact", "relatedArtifact", RelatedArtifact, True, None, False),
            ("library", "library", str, True, None, False),
            ("goal", "goal", PlanDefinitionGoal, True, None, False),
            ("action", "action", PlanDefinitionAction, True, None, False),
        ])
        return js