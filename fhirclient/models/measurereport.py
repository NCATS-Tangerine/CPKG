#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/MeasureReport) on 2019-08-06.
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
from .period import Period
from .quantity import Quantity


@dataclass
class MeasureReportGroupStratifierStratumComponent(BackboneElement):
    """ Stratifier component values.

    A stratifier component value.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifierStratumComponent"
    code: CodeableConcept = None
    value: CodeableConcept = None

    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratumComponent, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("value", "value", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class MeasureReportGroupStratifierStratumPopulation(BackboneElement):
    """ Population results in this stratum.

    The populations that make up the stratum, one for each type of population
    appropriate to the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifierStratumPopulation"
    code: Optional[CodeableConcept] = None
    count: Optional[int] = None
    subjectResults: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratumPopulation, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("count", "count", int, False, None, False),
            ("subjectResults", "subjectResults", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class MeasureReportGroupStratifierStratum(BackboneElement):
    """ Stratum results, one for each unique value, or set of values, in the
    stratifier, or stratifier components.

    This element contains the results for a single stratum within the
    stratifier. For example, when stratifying on administrative gender, there
    will be four strata, one for each possible gender value.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifierStratum"
    value: Optional[CodeableConcept] = None
    component: Optional[List[MeasureReportGroupStratifierStratumComponent]] = empty_list()
    population: Optional[List[MeasureReportGroupStratifierStratumPopulation]] = empty_list()
    measureScore: Optional[Quantity] = None

    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratum, self).elementProperties()
        js.extend([
            ("value", "value", CodeableConcept, False, None, False),
            ("component", "component", MeasureReportGroupStratifierStratumComponent, True, None, False),
            ("population", "population", MeasureReportGroupStratifierStratumPopulation, True, None, False),
            ("measureScore", "measureScore", Quantity, False, None, False),
        ])
        return js


@dataclass
class MeasureReportGroupPopulation(BackboneElement):
    """ The populations in the group.

    The populations that make up the population group, one for each type of
    population appropriate for the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupPopulation"
    code: Optional[CodeableConcept] = None
    count: Optional[int] = None
    subjectResults: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(MeasureReportGroupPopulation, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("count", "count", int, False, None, False),
            ("subjectResults", "subjectResults", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class MeasureReportGroupStratifier(BackboneElement):
    """ Stratification results.

    When a measure includes multiple stratifiers, there will be a stratifier
    group for each stratifier defined by the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifier"
    code: Optional[List[CodeableConcept]] = empty_list()
    stratum: Optional[List[MeasureReportGroupStratifierStratum]] = empty_list()

    def elementProperties(self):
        js = super(MeasureReportGroupStratifier, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, True, None, False),
            ("stratum", "stratum", MeasureReportGroupStratifierStratum, True, None, False),
        ])
        return js


@dataclass
class MeasureReportGroup(BackboneElement):
    """ Measure results for each group.

    The results of the calculation, one for each population group in the
    measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroup"
    code: Optional[CodeableConcept] = None
    population: Optional[List[MeasureReportGroupPopulation]] = empty_list()
    measureScore: Optional[Quantity] = None
    stratifier: Optional[List[MeasureReportGroupStratifier]] = empty_list()

    def elementProperties(self):
        js = super(MeasureReportGroup, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("population", "population", MeasureReportGroupPopulation, True, None, False),
            ("measureScore", "measureScore", Quantity, False, None, False),
            ("stratifier", "stratifier", MeasureReportGroupStratifier, True, None, False),
        ])
        return js


@dataclass
class MeasureReport(DomainResource):
    """ Results of a measure evaluation.

    The MeasureReport resource contains the results of the calculation of a
    measure; and optionally a reference to the resources involved in that
    calculation.
    """
    resource_type: ClassVar[str] = "MeasureReport"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    type: str = None
    measure: str = None
    subject: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    reporter: Optional[FHIRReference] = None
    period: Period = None
    improvementNotation: Optional[CodeableConcept] = None
    group: Optional[List[MeasureReportGroup]] = empty_list()
    evaluatedResource: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(MeasureReport, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", str, False, None, True),
            ("measure", "measure", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("reporter", "reporter", FHIRReference, False, None, False),
            ("period", "period", Period, False, None, True),
            ("improvementNotation", "improvementNotation", CodeableConcept, False, None, False),
            ("group", "group", MeasureReportGroup, True, None, False),
            ("evaluatedResource", "evaluatedResource", FHIRReference, True, None, False),
        ])
        return js