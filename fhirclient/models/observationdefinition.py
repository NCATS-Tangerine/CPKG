#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ObservationDefinition) on 2019-08-06.
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
from .identifier import Identifier
from .period import Period
from .range import Range
from .usagecontext import UsageContext


@dataclass
class ObservationDefinitionQuantitativeDetails(BackboneElement):
    """ Characteristics of quantitative results.

    Characteristics for quantitative results of this observation.
    """
    resource_type: ClassVar[str] = "ObservationDefinitionQuantitativeDetails"
    customaryUnit: Optional[CodeableConcept] = None
    unit: Optional[CodeableConcept] = None
    conversionFactor: Optional[float] = None
    decimalPrecision: Optional[int] = None

    def elementProperties(self):
        js = super(ObservationDefinitionQuantitativeDetails, self).elementProperties()
        js.extend([
            ("customaryUnit", "customaryUnit", CodeableConcept, False, None, False),
            ("unit", "unit", CodeableConcept, False, None, False),
            ("conversionFactor", "conversionFactor", float, False, None, False),
            ("decimalPrecision", "decimalPrecision", int, False, None, False),
        ])
        return js


@dataclass
class ObservationDefinitionQualifiedInterval(BackboneElement):
    """ Qualified range for continuous and ordinal observation results.

    Multiple  ranges of results qualified by different contexts for ordinal or
    continuous observations conforming to this ObservationDefinition.
    """
    resource_type: ClassVar[str] = "ObservationDefinitionQualifiedInterval"
    category: Optional[str] = None
    range: Optional[Range] = None
    context: Optional[CodeableConcept] = None
    appliesTo: Optional[List[CodeableConcept]] = empty_list()
    gender: Optional[str] = None
    age: Optional[Range] = None
    gestationalAge: Optional[Range] = None
    condition: Optional[str] = None

    def elementProperties(self):
        js = super(ObservationDefinitionQualifiedInterval, self).elementProperties()
        js.extend([
            ("category", "category", str, False, None, False),
            ("range", "range", Range, False, None, False),
            ("context", "context", CodeableConcept, False, None, False),
            ("appliesTo", "appliesTo", CodeableConcept, True, None, False),
            ("gender", "gender", str, False, None, False),
            ("age", "age", Range, False, None, False),
            ("gestationalAge", "gestationalAge", Range, False, None, False),
            ("condition", "condition", str, False, None, False),
        ])
        return js


@dataclass
class ObservationDefinitionComponent(BackboneElement):
    """ Component results.

    Some observations have multiple component observations, expressed as
    separate code value pairs.
    """
    resource_type: ClassVar[str] = "ObservationDefinitionComponent"
    code: CodeableConcept = None
    permittedDataType: Optional[List[str]] = empty_list()
    quantitativeDetails: Optional[ObservationDefinitionQuantitativeDetails] = None
    qualifiedInterval: Optional[List[ObservationDefinitionQualifiedInterval]] = empty_list()

    def elementProperties(self):
        js = super(ObservationDefinitionComponent, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("permittedDataType", "permittedDataType", str, True, None, False),
            ("quantitativeDetails", "quantitativeDetails", ObservationDefinitionQuantitativeDetails, False, None, False),
            ("qualifiedInterval", "qualifiedInterval", ObservationDefinitionQualifiedInterval, True, None, False),
        ])
        return js


@dataclass
class ObservationDefinition(DomainResource):
    """ Definition of an observation.

    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """
    resource_type: ClassVar[str] = "ObservationDefinition"
    url: Optional[str] = None
    identifier: Optional[Identifier] = None
    version: Optional[str] = None
    title: Optional[str] = None
    derivedFromCanonical: Optional[List[str]] = empty_list()
    derivedFromUri: Optional[List[str]] = empty_list()
    status: str = None
    experimental: Optional[bool] = None
    subjectCodeableConcept: Optional[CodeableConcept] = None
    subjectReference: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[FHIRReference] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    performerType: Optional[CodeableConcept] = None
    category: Optional[List[CodeableConcept]] = empty_list()
    code: CodeableConcept = None
    permittedDataType: Optional[List[str]] = empty_list()
    multipleResultsAllowed: Optional[bool] = None
    bodySite: Optional[CodeableConcept] = None
    method: Optional[CodeableConcept] = None
    specimen: Optional[FHIRReference] = None
    device: Optional[FHIRReference] = None
    preferredReportName: Optional[str] = None
    quantitativeDetails: Optional[ObservationDefinitionQuantitativeDetails] = None
    qualifiedInterval: Optional[List[ObservationDefinitionQualifiedInterval]] = empty_list()
    validCodedValueSet: Optional[FHIRReference] = None
    normalCodedValueSet: Optional[FHIRReference] = None
    abnormalCodedValueSet: Optional[FHIRReference] = None
    criticalCodedValueSet: Optional[FHIRReference] = None
    hasMember: Optional[List[FHIRReference]] = empty_list()
    component: Optional[List[ObservationDefinitionComponent]] = empty_list()

    def elementProperties(self):
        js = super(ObservationDefinition, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("version", "version", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("derivedFromCanonical", "derivedFromCanonical", str, True, None, False),
            ("derivedFromUri", "derivedFromUri", str, True, None, False),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", FHIRReference, False, "subject", False),
            ("date", "date", FHIRDate, False, None, False),
            ("publisher", "publisher", FHIRReference, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("performerType", "performerType", CodeableConcept, False, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, True),
            ("permittedDataType", "permittedDataType", str, True, None, False),
            ("multipleResultsAllowed", "multipleResultsAllowed", bool, False, None, False),
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("method", "method", CodeableConcept, False, None, False),
            ("specimen", "specimen", FHIRReference, False, None, False),
            ("device", "device", FHIRReference, False, None, False),
            ("preferredReportName", "preferredReportName", str, False, None, False),
            ("quantitativeDetails", "quantitativeDetails", ObservationDefinitionQuantitativeDetails, False, None, False),
            ("qualifiedInterval", "qualifiedInterval", ObservationDefinitionQualifiedInterval, True, None, False),
            ("validCodedValueSet", "validCodedValueSet", FHIRReference, False, None, False),
            ("normalCodedValueSet", "normalCodedValueSet", FHIRReference, False, None, False),
            ("abnormalCodedValueSet", "abnormalCodedValueSet", FHIRReference, False, None, False),
            ("criticalCodedValueSet", "criticalCodedValueSet", FHIRReference, False, None, False),
            ("hasMember", "hasMember", FHIRReference, True, None, False),
            ("component", "component", ObservationDefinitionComponent, True, None, False),
        ])
        return js