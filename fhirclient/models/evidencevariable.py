#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/EvidenceVariable) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
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
from .relatedartifact import RelatedArtifact
from .timing import Timing
from .triggerdefinition import TriggerDefinition
from .usagecontext import UsageContext


@dataclass
class EvidenceVariableCharacteristic(BackboneElement):
    """ What defines the members of the evidence element.

    A characteristic that defines the members of the evidence element. Multiple
    characteristics are applied with "and" semantics.
    """
    resource_type: ClassVar[str] = "EvidenceVariableCharacteristic"
    description: Optional[str] = None
    definitionReference: FHIRReference = None
    definitionCanonical: str = None
    definitionCodeableConcept: CodeableConcept = None
    definitionExpression: Expression = None
    definitionDataRequirement: DataRequirement = None
    definitionTriggerDefinition: TriggerDefinition = None
    usageContext: Optional[List[UsageContext]] = empty_list()
    exclude: Optional[bool] = None
    participantEffectiveDateTime: Optional[FHIRDate] = None
    participantEffectivePeriod: Optional[Period] = None
    participantEffectiveDuration: Optional[Duration] = None
    participantEffectiveTiming: Optional[Timing] = None
    timeFromStart: Optional[Duration] = None
    groupMeasure: Optional[str] = None

    def elementProperties(self):
        js = super(EvidenceVariableCharacteristic, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("definitionReference", "definitionReference", FHIRReference, False, "definition", True),
            ("definitionCanonical", "definitionCanonical", str, False, "definition", True),
            ("definitionCodeableConcept", "definitionCodeableConcept", CodeableConcept, False, "definition", True),
            ("definitionExpression", "definitionExpression", Expression, False, "definition", True),
            ("definitionDataRequirement", "definitionDataRequirement", DataRequirement, False, "definition", True),
            ("definitionTriggerDefinition", "definitionTriggerDefinition", TriggerDefinition, False, "definition", True),
            ("usageContext", "usageContext", UsageContext, True, None, False),
            ("exclude", "exclude", bool, False, None, False),
            ("participantEffectiveDateTime", "participantEffectiveDateTime", FHIRDate, False, "participantEffective", False),
            ("participantEffectivePeriod", "participantEffectivePeriod", Period, False, "participantEffective", False),
            ("participantEffectiveDuration", "participantEffectiveDuration", Duration, False, "participantEffective", False),
            ("participantEffectiveTiming", "participantEffectiveTiming", Timing, False, "participantEffective", False),
            ("timeFromStart", "timeFromStart", Duration, False, None, False),
            ("groupMeasure", "groupMeasure", str, False, None, False),
        ])
        return js


@dataclass
class EvidenceVariable(DomainResource):
    """ A population, intervention, or exposure definition.

    The EvidenceVariable resource describes a "PICO" element that knowledge
    (evidence, assertion, recommendation) is about.
    """
    resource_type: ClassVar[str] = "EvidenceVariable"
    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    shortTitle: Optional[str] = None
    subtitle: Optional[str] = None
    status: str = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    description: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()
    useContext: Optional[List[UsageContext]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
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
    type: Optional[str] = None
    characteristic: List[EvidenceVariableCharacteristic] = empty_list()

    def elementProperties(self):
        js = super(EvidenceVariable, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("shortTitle", "shortTitle", str, False, None, False),
            ("subtitle", "subtitle", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("date", "date", FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
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
            ("type", "type", str, False, None, False),
            ("characteristic", "characteristic", EvidenceVariableCharacteristic, True, None, True),
        ])
        return js