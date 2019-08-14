#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/RequestGroup) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .age import Age
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .range import Range
from .relatedartifact import RelatedArtifact
from .timing import Timing


@dataclass
class RequestGroupActionCondition(BackboneElement):
    """ Whether or not the action is applicable.

    An expression that describes applicability criteria, or start/stop
    conditions for the action.
    """
    resource_type: ClassVar[str] = "RequestGroupActionCondition"
    kind: str = None
    expression: Optional[Expression] = None

    def elementProperties(self):
        js = super(RequestGroupActionCondition, self).elementProperties()
        js.extend([
            ("kind", "kind", str, False, None, True),
            ("expression", "expression", Expression, False, None, False),
        ])
        return js


@dataclass
class RequestGroupActionRelatedAction(BackboneElement):
    """ Relationship to another action.

    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    resource_type: ClassVar[str] = "RequestGroupActionRelatedAction"
    actionId: str = None
    relationship: str = None
    offsetDuration: Optional[Duration] = None
    offsetRange: Optional[Range] = None

    def elementProperties(self):
        js = super(RequestGroupActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", str, False, None, True),
            ("relationship", "relationship", str, False, None, True),
            ("offsetDuration", "offsetDuration", Duration, False, "offset", False),
            ("offsetRange", "offsetRange", Range, False, "offset", False),
        ])
        return js


@dataclass
class RequestGroupAction(BackboneElement):
    """ Proposed actions, if any.

    The actions, if any, produced by the evaluation of the artifact.
    """
    resource_type: ClassVar[str] = "RequestGroupAction"
    prefix: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    textEquivalent: Optional[str] = None
    priority: Optional[str] = None
    code: Optional[List[CodeableConcept]] = empty_list()
    documentation: Optional[List[RelatedArtifact]] = empty_list()
    condition: Optional[List[RequestGroupActionCondition]] = empty_list()
    relatedAction: Optional[List[RequestGroupActionRelatedAction]] = empty_list()
    timingDateTime: Optional[FHIRDate] = None
    timingAge: Optional[Age] = None
    timingPeriod: Optional[Period] = None
    timingDuration: Optional[Duration] = None
    timingRange: Optional[Range] = None
    timingTiming: Optional[Timing] = None
    participant: Optional[List[FHIRReference]] = empty_list()
    type: Optional[CodeableConcept] = None
    groupingBehavior: Optional[str] = None
    selectionBehavior: Optional[str] = None
    requiredBehavior: Optional[str] = None
    precheckBehavior: Optional[str] = None
    cardinalityBehavior: Optional[str] = None
    resource: Optional[FHIRReference] = None
    action: Optional[List["RequestGroupAction"]] = empty_list()

    def elementProperties(self):
        js = super(RequestGroupAction, self).elementProperties()
        js.extend([
            ("prefix", "prefix", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("code", "code", CodeableConcept, True, None, False),
            ("documentation", "documentation", RelatedArtifact, True, None, False),
            ("condition", "condition", RequestGroupActionCondition, True, None, False),
            ("relatedAction", "relatedAction", RequestGroupActionRelatedAction, True, None, False),
            ("timingDateTime", "timingDateTime", FHIRDate, False, "timing", False),
            ("timingAge", "timingAge", Age, False, "timing", False),
            ("timingPeriod", "timingPeriod", Period, False, "timing", False),
            ("timingDuration", "timingDuration", Duration, False, "timing", False),
            ("timingRange", "timingRange", Range, False, "timing", False),
            ("timingTiming", "timingTiming", Timing, False, "timing", False),
            ("participant", "participant", FHIRReference, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("groupingBehavior", "groupingBehavior", str, False, None, False),
            ("selectionBehavior", "selectionBehavior", str, False, None, False),
            ("requiredBehavior", "requiredBehavior", str, False, None, False),
            ("precheckBehavior", "precheckBehavior", str, False, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", str, False, None, False),
            ("resource", "resource", FHIRReference, False, None, False),
            ("action", "action", RequestGroupAction, True, None, False),
        ])
        return js


@dataclass
class RequestGroup(DomainResource):
    """ A group of related requests.

    A group of related requests that can be used to capture intended activities
    that have inter-dependencies such as "give this medication after that one".
    """
    resource_type: ClassVar[str] = "RequestGroup"
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    basedOn: Optional[List[FHIRReference]] = empty_list()
    replaces: Optional[List[FHIRReference]] = empty_list()
    groupIdentifier: Optional[Identifier] = None
    status: str = None
    intent: str = None
    priority: Optional[str] = None
    code: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    authoredOn: Optional[FHIRDate] = None
    author: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    action: Optional[List[RequestGroupAction]] = empty_list()

    def elementProperties(self):
        js = super(RequestGroup, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("replaces", "replaces", FHIRReference, True, None, False),
            ("groupIdentifier", "groupIdentifier", Identifier, False, None, False),
            ("status", "status", str, False, None, True),
            ("intent", "intent", str, False, None, True),
            ("priority", "priority", str, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("authoredOn", "authoredOn", FHIRDate, False, None, False),
            ("author", "author", FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("action", "action", RequestGroupAction, True, None, False),
        ])
        return js