#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Observation) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .sampleddata import SampledData
from .timing import Timing


@dataclass
class ObservationReferenceRange(BackboneElement):
    """ Provides guide for interpretation.

    Guidance on how to interpret the value by comparison to a normal or
    recommended range.  Multiple reference ranges are interpreted as an "OR".
    In other words, to represent two distinct target populations, two
    `referenceRange` elements would be used.
    """
    resource_type: ClassVar[str] = "ObservationReferenceRange"
    low: Optional[Quantity] = None
    high: Optional[Quantity] = None
    type: Optional[CodeableConcept] = None
    appliesTo: Optional[List[CodeableConcept]] = empty_list()
    age: Optional[Range] = None
    text: Optional[str] = None

    def elementProperties(self):
        js = super(ObservationReferenceRange, self).elementProperties()
        js.extend([
            ("low", "low", Quantity, False, None, False),
            ("high", "high", Quantity, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("appliesTo", "appliesTo", CodeableConcept, True, None, False),
            ("age", "age", Range, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


@dataclass
class ObservationComponent(BackboneElement):
    """ Component results.

    Some observations have multiple component observations.  These component
    observations are expressed as separate code value pairs that share the same
    attributes.  Examples include systolic and diastolic component observations
    for blood pressure measurement and multiple component observations for
    genetics observations.
    """
    resource_type: ClassVar[str] = "ObservationComponent"
    code: CodeableConcept = None
    valueQuantity: Optional[Quantity] = None
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueString: Optional[str] = None
    valueBoolean: Optional[bool] = None
    valueInteger: Optional[int] = None
    valueRange: Optional[Range] = None
    valueRatio: Optional[Ratio] = None
    valueSampledData: Optional[SampledData] = None
    valueTime: Optional[FHIRDate] = None
    valueDateTime: Optional[FHIRDate] = None
    valuePeriod: Optional[Period] = None
    dataAbsentReason: Optional[CodeableConcept] = None
    interpretation: Optional[List[CodeableConcept]] = empty_list()
    referenceRange: Optional[List[ObservationReferenceRange]] = empty_list()

    def elementProperties(self):
        js = super(ObservationComponent, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueRange", "valueRange", Range, False, "value", False),
            ("valueRatio", "valueRatio", Ratio, False, "value", False),
            ("valueSampledData", "valueSampledData", SampledData, False, "value", False),
            ("valueTime", "valueTime", FHIRDate, False, "value", False),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", False),
            ("valuePeriod", "valuePeriod", Period, False, "value", False),
            ("dataAbsentReason", "dataAbsentReason", CodeableConcept, False, None, False),
            ("interpretation", "interpretation", CodeableConcept, True, None, False),
            ("referenceRange", "referenceRange", ObservationReferenceRange, True, None, False),
        ])
        return js


@dataclass
class Observation(DomainResource):
    """ Measurements and simple assertions.

    Measurements and simple assertions made about a patient, device or other
    subject.
    """
    resource_type: ClassVar[str] = "Observation"
    identifier: Optional[List[Identifier]] = empty_list()
    basedOn: Optional[List[FHIRReference]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    category: Optional[List[CodeableConcept]] = empty_list()
    code: CodeableConcept = None
    subject: Optional[FHIRReference] = None
    focus: Optional[List[FHIRReference]] = empty_list()
    encounter: Optional[FHIRReference] = None
    effectiveDateTime: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    effectiveTiming: Optional[Timing] = None
    effectiveInstant: Optional[FHIRDate] = None
    issued: Optional[FHIRDate] = None
    performer: Optional[List[FHIRReference]] = empty_list()
    valueQuantity: Optional[Quantity] = None
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueString: Optional[str] = None
    valueBoolean: Optional[bool] = None
    valueInteger: Optional[int] = None
    valueRange: Optional[Range] = None
    valueRatio: Optional[Ratio] = None
    valueSampledData: Optional[SampledData] = None
    valueTime: Optional[FHIRDate] = None
    valueDateTime: Optional[FHIRDate] = None
    valuePeriod: Optional[Period] = None
    dataAbsentReason: Optional[CodeableConcept] = None
    interpretation: Optional[List[CodeableConcept]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    bodySite: Optional[CodeableConcept] = None
    method: Optional[CodeableConcept] = None
    specimen: Optional[FHIRReference] = None
    device: Optional[FHIRReference] = None
    referenceRange: Optional[List[ObservationReferenceRange]] = empty_list()
    hasMember: Optional[List[FHIRReference]] = empty_list()
    derivedFrom: Optional[List[FHIRReference]] = empty_list()
    component: Optional[List[ObservationComponent]] = empty_list()

    def elementProperties(self):
        js = super(Observation, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("category", "category", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, True),
            ("subject", "subject", FHIRReference, False, None, False),
            ("focus", "focus", FHIRReference, True, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", Period, False, "effective", False),
            ("effectiveTiming", "effectiveTiming", Timing, False, "effective", False),
            ("effectiveInstant", "effectiveInstant", FHIRDate, False, "effective", False),
            ("issued", "issued", FHIRDate, False, None, False),
            ("performer", "performer", FHIRReference, True, None, False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueRange", "valueRange", Range, False, "value", False),
            ("valueRatio", "valueRatio", Ratio, False, "value", False),
            ("valueSampledData", "valueSampledData", SampledData, False, "value", False),
            ("valueTime", "valueTime", FHIRDate, False, "value", False),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", False),
            ("valuePeriod", "valuePeriod", Period, False, "value", False),
            ("dataAbsentReason", "dataAbsentReason", CodeableConcept, False, None, False),
            ("interpretation", "interpretation", CodeableConcept, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("method", "method", CodeableConcept, False, None, False),
            ("specimen", "specimen", FHIRReference, False, None, False),
            ("device", "device", FHIRReference, False, None, False),
            ("referenceRange", "referenceRange", ObservationReferenceRange, True, None, False),
            ("hasMember", "hasMember", FHIRReference, True, None, False),
            ("derivedFrom", "derivedFrom", FHIRReference, True, None, False),
            ("component", "component", ObservationComponent, True, None, False),
        ])
        return js