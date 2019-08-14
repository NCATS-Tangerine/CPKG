#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/DeviceMetric) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .timing import Timing


@dataclass
class DeviceMetricCalibration(BackboneElement):
    """ Describes the calibrations that have been performed or that are required to
    be performed.
    """
    resource_type: ClassVar[str] = "DeviceMetricCalibration"
    type: Optional[str] = None
    state: Optional[str] = None
    time: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(DeviceMetricCalibration, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, False),
            ("state", "state", str, False, None, False),
            ("time", "time", FHIRDate, False, None, False),
        ])
        return js


@dataclass
class DeviceMetric(DomainResource):
    """ Measurement, calculation or setting capability of a medical device.

    Describes a measurement, calculation or setting capability of a medical
    device.
    """
    resource_type: ClassVar[str] = "DeviceMetric"
    identifier: Optional[List[Identifier]] = empty_list()
    type: CodeableConcept = None
    unit: Optional[CodeableConcept] = None
    source: Optional[FHIRReference] = None
    parent: Optional[FHIRReference] = None
    operationalStatus: Optional[str] = None
    color: Optional[str] = None
    category: str = None
    measurementPeriod: Optional[Timing] = None
    calibration: Optional[List[DeviceMetricCalibration]] = empty_list()

    def elementProperties(self):
        js = super(DeviceMetric, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("type", "type", CodeableConcept, False, None, True),
            ("unit", "unit", CodeableConcept, False, None, False),
            ("source", "source", FHIRReference, False, None, False),
            ("parent", "parent", FHIRReference, False, None, False),
            ("operationalStatus", "operationalStatus", str, False, None, False),
            ("color", "color", str, False, None, False),
            ("category", "category", str, False, None, True),
            ("measurementPeriod", "measurementPeriod", Timing, False, None, False),
            ("calibration", "calibration", DeviceMetricCalibration, True, None, False),
        ])
        return js