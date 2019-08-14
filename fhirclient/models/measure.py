#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Measure) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .relatedartifact import RelatedArtifact
from .usagecontext import UsageContext


@dataclass
class MeasureGroupStratifierComponent(BackboneElement):
    """ Stratifier criteria component for the measure.

    A component of the stratifier criteria for the measure report, specified as
    either the name of a valid CQL expression defined within a referenced
    library or a valid FHIR Resource Path.
    """
    resource_type: ClassVar[str] = "MeasureGroupStratifierComponent"
    code: Optional[CodeableConcept] = None
    description: Optional[str] = None
    criteria: Expression = None

    def elementProperties(self):
        js = super(MeasureGroupStratifierComponent, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("criteria", "criteria", Expression, False, None, True),
        ])
        return js


@dataclass
class MeasureGroupPopulation(BackboneElement):
    """ Population criteria.

    A population criteria for the measure.
    """
    resource_type: ClassVar[str] = "MeasureGroupPopulation"
    code: Optional[CodeableConcept] = None
    description: Optional[str] = None
    criteria: Expression = None

    def elementProperties(self):
        js = super(MeasureGroupPopulation, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("criteria", "criteria", Expression, False, None, True),
        ])
        return js


@dataclass
class MeasureGroupStratifier(BackboneElement):
    """ Stratifier criteria for the measure.

    The stratifier criteria for the measure report, specified as either the
    name of a valid CQL expression defined within a referenced library or a
    valid FHIR Resource Path.
    """
    resource_type: ClassVar[str] = "MeasureGroupStratifier"
    code: Optional[CodeableConcept] = None
    description: Optional[str] = None
    criteria: Optional[Expression] = None
    component: Optional[List[MeasureGroupStratifierComponent]] = empty_list()

    def elementProperties(self):
        js = super(MeasureGroupStratifier, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("criteria", "criteria", Expression, False, None, False),
            ("component", "component", MeasureGroupStratifierComponent, True, None, False),
        ])
        return js


@dataclass
class MeasureGroup(BackboneElement):
    """ Population criteria group.

    A group of population criteria for the measure.
    """
    resource_type: ClassVar[str] = "MeasureGroup"
    code: Optional[CodeableConcept] = None
    description: Optional[str] = None
    population: Optional[List[MeasureGroupPopulation]] = empty_list()
    stratifier: Optional[List[MeasureGroupStratifier]] = empty_list()

    def elementProperties(self):
        js = super(MeasureGroup, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("population", "population", MeasureGroupPopulation, True, None, False),
            ("stratifier", "stratifier", MeasureGroupStratifier, True, None, False),
        ])
        return js


@dataclass
class MeasureSupplementalData(BackboneElement):
    """ What other data should be reported with the measure.

    The supplemental data criteria for the measure report, specified as either
    the name of a valid CQL expression within a referenced library, or a valid
    FHIR Resource Path.
    """
    resource_type: ClassVar[str] = "MeasureSupplementalData"
    code: Optional[CodeableConcept] = None
    usage: Optional[List[CodeableConcept]] = empty_list()
    description: Optional[str] = None
    criteria: Expression = None

    def elementProperties(self):
        js = super(MeasureSupplementalData, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("usage", "usage", CodeableConcept, True, None, False),
            ("description", "description", str, False, None, False),
            ("criteria", "criteria", Expression, False, None, True),
        ])
        return js


@dataclass
class Measure(DomainResource):
    """ A quality measure definition.

    The Measure resource provides the definition of a quality measure.
    """
    resource_type: ClassVar[str] = "Measure"
    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
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
    disclaimer: Optional[str] = None
    scoring: Optional[CodeableConcept] = None
    compositeScoring: Optional[CodeableConcept] = None
    type: Optional[List[CodeableConcept]] = empty_list()
    riskAdjustment: Optional[str] = None
    rateAggregation: Optional[str] = None
    rationale: Optional[str] = None
    clinicalRecommendationStatement: Optional[str] = None
    improvementNotation: Optional[CodeableConcept] = None
    definition: Optional[List[str]] = empty_list()
    guidance: Optional[str] = None
    group: Optional[List[MeasureGroup]] = empty_list()
    supplementalData: Optional[List[MeasureSupplementalData]] = empty_list()

    def elementProperties(self):
        js = super(Measure, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("subtitle", "subtitle", str, False, None, False),
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
            ("disclaimer", "disclaimer", str, False, None, False),
            ("scoring", "scoring", CodeableConcept, False, None, False),
            ("compositeScoring", "compositeScoring", CodeableConcept, False, None, False),
            ("type", "type", CodeableConcept, True, None, False),
            ("riskAdjustment", "riskAdjustment", str, False, None, False),
            ("rateAggregation", "rateAggregation", str, False, None, False),
            ("rationale", "rationale", str, False, None, False),
            ("clinicalRecommendationStatement", "clinicalRecommendationStatement", str, False, None, False),
            ("improvementNotation", "improvementNotation", CodeableConcept, False, None, False),
            ("definition", "definition", str, True, None, False),
            ("guidance", "guidance", str, False, None, False),
            ("group", "group", MeasureGroup, True, None, False),
            ("supplementalData", "supplementalData", MeasureSupplementalData, True, None, False),
        ])
        return js