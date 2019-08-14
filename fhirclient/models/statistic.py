#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Statistic) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .contributor import Contributor
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .range import Range
from .relatedartifact import RelatedArtifact
from .usagecontext import UsageContext


@dataclass
class StatisticCertaintyCertaintySubcomponent(BackboneElement):
    """ A component that contributes to the overall certainty.

    A description of a component of the overall certainty.
    """
    resource_type: ClassVar[str] = "StatisticCertaintyCertaintySubcomponent"
    description: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()
    type: Optional[List[CodeableConcept]] = empty_list()
    rating: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(StatisticCertaintyCertaintySubcomponent, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("type", "type", CodeableConcept, True, None, False),
            ("rating", "rating", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class StatisticStatisticPublisher(BackboneElement):
    """ The individual or organization that produced this statistic.
    """
    resource_type: ClassVar[str] = "StatisticStatisticPublisher"
    name: str = None
    contact: Optional[List[ContactDetail]] = empty_list()

    def elementProperties(self):
        js = super(StatisticStatisticPublisher, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("contact", "contact", ContactDetail, True, None, False),
        ])
        return js


@dataclass
class StatisticSampleSize(BackboneElement):
    """ Population sample size.
    """
    resource_type: ClassVar[str] = "StatisticSampleSize"
    description: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()
    numberOfStudies: Optional[int] = None
    numberOfParticipants: Optional[int] = None
    knownDataCount: Optional[int] = None
    numeratorCount: Optional[int] = None

    def elementProperties(self):
        js = super(StatisticSampleSize, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("numberOfStudies", "numberOfStudies", int, False, None, False),
            ("numberOfParticipants", "numberOfParticipants", int, False, None, False),
            ("knownDataCount", "knownDataCount", int, False, None, False),
            ("numeratorCount", "numeratorCount", int, False, None, False),
        ])
        return js


@dataclass
class StatisticPrecisionEstimate(BackboneElement):
    """ An estimate of the precision of the statistic.
    """
    resource_type: ClassVar[str] = "StatisticPrecisionEstimate"
    description: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()
    type: Optional[CodeableConcept] = None
    level: Optional[float] = None
    from_fhir: Optional[float] = None
    to: Optional[float] = None

    def elementProperties(self):
        js = super(StatisticPrecisionEstimate, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("level", "level", float, False, None, False),
            ("from_fhir", "from", float, False, None, False),
            ("to", "to", float, False, None, False),
        ])
        return js


@dataclass
class StatisticPValue(BackboneElement):
    """ The probability that this statistic would be the same given the null
    hypothesis.
    """
    resource_type: ClassVar[str] = "StatisticPValue"
    description: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()
    type: Optional[CodeableConcept] = None
    quantity: Optional[Quantity] = None
    range: Optional[Range] = None

    def elementProperties(self):
        js = super(StatisticPValue, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("range", "range", Range, False, None, False),
        ])
        return js


@dataclass
class StatisticCertainty(BackboneElement):
    """ How certain is the effect.

    A description of the certainty of the effect estimate.
    """
    resource_type: ClassVar[str] = "StatisticCertainty"
    description: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()
    rating: Optional[List[CodeableConcept]] = empty_list()
    certaintySubcomponent: Optional[List[StatisticCertaintyCertaintySubcomponent]] = empty_list()

    def elementProperties(self):
        js = super(StatisticCertainty, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("rating", "rating", CodeableConcept, True, None, False),
            ("certaintySubcomponent", "certaintySubcomponent", StatisticCertaintyCertaintySubcomponent, True, None, False),
        ])
        return js


@dataclass
class Statistic(DomainResource):
    """ A statistic.

    The Statistic resource codifies a statistical measure and corresponding
    certainty.
    """
    resource_type: ClassVar[str] = "Statistic"
    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    version: Optional[str] = None
    title: Optional[str] = None
    status: str = None
    date: Optional[FHIRDate] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    statisticPublisher: Optional[List[StatisticStatisticPublisher]] = empty_list()
    contributor: Optional[List[Contributor]] = empty_list()
    relatedArtifact: Optional[List[RelatedArtifact]] = empty_list()
    description: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()
    synthesisType: Optional[CodeableConcept] = None
    studyType: Optional[CodeableConcept] = None
    exposureBackground: FHIRReference = None
    exposure: Optional[FHIRReference] = None
    exposureVariant: Optional[List[FHIRReference]] = empty_list()
    measuredVariable: Optional[List[FHIRReference]] = empty_list()
    statisticType: Optional[CodeableConcept] = None
    quantity: Optional[Quantity] = None
    sampleSize: Optional[StatisticSampleSize] = None
    precisionEstimate: Optional[List[StatisticPrecisionEstimate]] = empty_list()
    pValue: Optional[List[StatisticPValue]] = empty_list()
    certainty: Optional[List[StatisticCertainty]] = empty_list()

    def elementProperties(self):
        js = super(Statistic, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("date", "date", FHIRDate, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("statisticPublisher", "statisticPublisher", StatisticStatisticPublisher, True, None, False),
            ("contributor", "contributor", Contributor, True, None, False),
            ("relatedArtifact", "relatedArtifact", RelatedArtifact, True, None, False),
            ("description", "description", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("synthesisType", "synthesisType", CodeableConcept, False, None, False),
            ("studyType", "studyType", CodeableConcept, False, None, False),
            ("exposureBackground", "exposureBackground", FHIRReference, False, None, True),
            ("exposure", "exposure", FHIRReference, False, None, False),
            ("exposureVariant", "exposureVariant", FHIRReference, True, None, False),
            ("measuredVariable", "measuredVariable", FHIRReference, True, None, False),
            ("statisticType", "statisticType", CodeableConcept, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("sampleSize", "sampleSize", StatisticSampleSize, False, None, False),
            ("precisionEstimate", "precisionEstimate", StatisticPrecisionEstimate, True, None, False),
            ("pValue", "pValue", StatisticPValue, True, None, False),
            ("certainty", "certainty", StatisticCertainty, True, None, False),
        ])
        return js