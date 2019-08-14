#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

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
from .usagecontext import UsageContext


@dataclass
class ResearchElementDefinitionCharacteristic(BackboneElement):
    """ What defines the members of the research element.

    A characteristic that defines the members of the research element. Multiple
    characteristics are applied with "and" semantics.
    """
    resource_type: ClassVar[str] = "ResearchElementDefinitionCharacteristic"
    definitionCodeableConcept: CodeableConcept = None
    definitionCanonical: str = None
    definitionExpression: Expression = None
    definitionDataRequirement: DataRequirement = None
    usageContext: Optional[List[UsageContext]] = empty_list()
    exclude: Optional[bool] = None
    unitOfMeasure: Optional[CodeableConcept] = None
    studyEffectiveDescription: Optional[str] = None
    studyEffectiveDateTime: Optional[FHIRDate] = None
    studyEffectivePeriod: Optional[Period] = None
    studyEffectiveDuration: Optional[Duration] = None
    studyEffectiveTiming: Optional[Timing] = None
    studyEffectiveTimeFromStart: Optional[Duration] = None
    studyEffectiveGroupMeasure: Optional[str] = None
    participantEffectiveDescription: Optional[str] = None
    participantEffectiveDateTime: Optional[FHIRDate] = None
    participantEffectivePeriod: Optional[Period] = None
    participantEffectiveDuration: Optional[Duration] = None
    participantEffectiveTiming: Optional[Timing] = None
    participantEffectiveTimeFromStart: Optional[Duration] = None
    participantEffectiveGroupMeasure: Optional[str] = None

    def elementProperties(self):
        js = super(ResearchElementDefinitionCharacteristic, self).elementProperties()
        js.extend([
            ("definitionCodeableConcept", "definitionCodeableConcept", CodeableConcept, False, "definition", True),
            ("definitionCanonical", "definitionCanonical", str, False, "definition", True),
            ("definitionExpression", "definitionExpression", Expression, False, "definition", True),
            ("definitionDataRequirement", "definitionDataRequirement", DataRequirement, False, "definition", True),
            ("usageContext", "usageContext", UsageContext, True, None, False),
            ("exclude", "exclude", bool, False, None, False),
            ("unitOfMeasure", "unitOfMeasure", CodeableConcept, False, None, False),
            ("studyEffectiveDescription", "studyEffectiveDescription", str, False, None, False),
            ("studyEffectiveDateTime", "studyEffectiveDateTime", FHIRDate, False, "studyEffective", False),
            ("studyEffectivePeriod", "studyEffectivePeriod", Period, False, "studyEffective", False),
            ("studyEffectiveDuration", "studyEffectiveDuration", Duration, False, "studyEffective", False),
            ("studyEffectiveTiming", "studyEffectiveTiming", Timing, False, "studyEffective", False),
            ("studyEffectiveTimeFromStart", "studyEffectiveTimeFromStart", Duration, False, None, False),
            ("studyEffectiveGroupMeasure", "studyEffectiveGroupMeasure", str, False, None, False),
            ("participantEffectiveDescription", "participantEffectiveDescription", str, False, None, False),
            ("participantEffectiveDateTime", "participantEffectiveDateTime", FHIRDate, False, "participantEffective", False),
            ("participantEffectivePeriod", "participantEffectivePeriod", Period, False, "participantEffective", False),
            ("participantEffectiveDuration", "participantEffectiveDuration", Duration, False, "participantEffective", False),
            ("participantEffectiveTiming", "participantEffectiveTiming", Timing, False, "participantEffective", False),
            ("participantEffectiveTimeFromStart", "participantEffectiveTimeFromStart", Duration, False, None, False),
            ("participantEffectiveGroupMeasure", "participantEffectiveGroupMeasure", str, False, None, False),
        ])
        return js


@dataclass
class ResearchElementDefinition(DomainResource):
    """ A population, intervention, or exposure definition.

    The ResearchElementDefinition resource describes a "PICO" element that
    knowledge (evidence, assertion, recommendation) is about.
    """
    resource_type: ClassVar[str] = "ResearchElementDefinition"
    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    shortTitle: Optional[str] = None
    subtitle: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    subjectCodeableConcept: Optional[CodeableConcept] = None
    subjectReference: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    description: Optional[str] = None
    comment: Optional[List[str]] = empty_list()
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
    type: str = None
    variableType: Optional[str] = None
    characteristic: List[ResearchElementDefinitionCharacteristic] = empty_list()

    def elementProperties(self):
        js = super(ResearchElementDefinition, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("shortTitle", "shortTitle", str, False, None, False),
            ("subtitle", "subtitle", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", FHIRReference, False, "subject", False),
            ("date", "date", FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("comment", "comment", str, True, None, False),
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
            ("type", "type", str, False, None, True),
            ("variableType", "variableType", str, False, None, False),
            ("characteristic", "characteristic", ResearchElementDefinitionCharacteristic, True, None, True),
        ])
        return js