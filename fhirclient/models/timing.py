#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Timing) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .duration import Duration
from .element import Element
from .fhirdate import FHIRDate
from .period import Period
from .range import Range


@dataclass
class TimingRepeat(Element):
    """ When the event is to occur.

    A set of rules that describe when the event is scheduled.
    """
    resource_type: ClassVar[str] = "TimingRepeat"
    boundsDuration: Optional[Duration] = None
    boundsRange: Optional[Range] = None
    boundsPeriod: Optional[Period] = None
    count: Optional[int] = None
    countMax: Optional[int] = None
    duration: Optional[float] = None
    durationMax: Optional[float] = None
    durationUnit: Optional[str] = None
    frequency: Optional[int] = None
    frequencyMax: Optional[int] = None
    period: Optional[float] = None
    periodMax: Optional[float] = None
    periodUnit: Optional[str] = None
    dayOfWeek: Optional[List[str]] = empty_list()
    timeOfDay: Optional[List[FHIRDate]] = empty_list()
    when: Optional[List[str]] = empty_list()
    offset: Optional[int] = None

    def elementProperties(self):
        js = super(TimingRepeat, self).elementProperties()
        js.extend([
            ("boundsDuration", "boundsDuration", Duration, False, "bounds", False),
            ("boundsRange", "boundsRange", Range, False, "bounds", False),
            ("boundsPeriod", "boundsPeriod", Period, False, "bounds", False),
            ("count", "count", int, False, None, False),
            ("countMax", "countMax", int, False, None, False),
            ("duration", "duration", float, False, None, False),
            ("durationMax", "durationMax", float, False, None, False),
            ("durationUnit", "durationUnit", str, False, None, False),
            ("frequency", "frequency", int, False, None, False),
            ("frequencyMax", "frequencyMax", int, False, None, False),
            ("period", "period", float, False, None, False),
            ("periodMax", "periodMax", float, False, None, False),
            ("periodUnit", "periodUnit", str, False, None, False),
            ("dayOfWeek", "dayOfWeek", str, True, None, False),
            ("timeOfDay", "timeOfDay", FHIRDate, True, None, False),
            ("when", "when", str, True, None, False),
            ("offset", "offset", int, False, None, False),
        ])
        return js


@dataclass
class Timing(BackboneElement):
    """ A timing schedule that specifies an event that may occur multiple times.

    Specifies an event that may occur multiple times. Timing schedules are used
    to record when things are planned, expected or requested to occur. The most
    common usage is in dosage instructions for medications. They are also used
    when planning care of various kinds, and may be used for reporting the
    schedule to which past regular activities were carried out.
    """
    resource_type: ClassVar[str] = "Timing"
    event: Optional[List[FHIRDate]] = empty_list()
    repeat: Optional[TimingRepeat] = None
    code: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(Timing, self).elementProperties()
        js.extend([
            ("event", "event", FHIRDate, True, None, False),
            ("repeat", "repeat", TimingRepeat, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
        ])
        return js