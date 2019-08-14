#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ImagingStudy) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class ImagingStudySeriesPerformer(BackboneElement):
    """ Who performed the series.

    Indicates who or what performed the series and how they were involved.
    """
    resource_type: ClassVar[str] = "ImagingStudySeriesPerformer"
    function: Optional[CodeableConcept] = None
    actor: FHIRReference = None

    def elementProperties(self):
        js = super(ImagingStudySeriesPerformer, self).elementProperties()
        js.extend([
            ("function", "function", CodeableConcept, False, None, False),
            ("actor", "actor", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class ImagingStudySeriesInstance(BackboneElement):
    """ A single SOP instance from the series.

    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """
    resource_type: ClassVar[str] = "ImagingStudySeriesInstance"
    uid: str = None
    sopClass: Coding = None
    number: Optional[int] = None
    title: Optional[str] = None

    def elementProperties(self):
        js = super(ImagingStudySeriesInstance, self).elementProperties()
        js.extend([
            ("uid", "uid", str, False, None, True),
            ("sopClass", "sopClass", Coding, False, None, True),
            ("number", "number", int, False, None, False),
            ("title", "title", str, False, None, False),
        ])
        return js


@dataclass
class ImagingStudySeries(BackboneElement):
    """ Each study has one or more series of instances.

    Each study has one or more series of images or other content.
    """
    resource_type: ClassVar[str] = "ImagingStudySeries"
    uid: str = None
    number: Optional[int] = None
    modality: Coding = None
    description: Optional[str] = None
    numberOfInstances: Optional[int] = None
    endpoint: Optional[List[FHIRReference]] = empty_list()
    bodySite: Optional[Coding] = None
    laterality: Optional[Coding] = None
    specimen: Optional[List[FHIRReference]] = empty_list()
    started: Optional[FHIRDate] = None
    performer: Optional[List[ImagingStudySeriesPerformer]] = empty_list()
    instance: Optional[List[ImagingStudySeriesInstance]] = empty_list()

    def elementProperties(self):
        js = super(ImagingStudySeries, self).elementProperties()
        js.extend([
            ("uid", "uid", str, False, None, True),
            ("number", "number", int, False, None, False),
            ("modality", "modality", Coding, False, None, True),
            ("description", "description", str, False, None, False),
            ("numberOfInstances", "numberOfInstances", int, False, None, False),
            ("endpoint", "endpoint", FHIRReference, True, None, False),
            ("bodySite", "bodySite", Coding, False, None, False),
            ("laterality", "laterality", Coding, False, None, False),
            ("specimen", "specimen", FHIRReference, True, None, False),
            ("started", "started", FHIRDate, False, None, False),
            ("performer", "performer", ImagingStudySeriesPerformer, True, None, False),
            ("instance", "instance", ImagingStudySeriesInstance, True, None, False),
        ])
        return js


@dataclass
class ImagingStudy(DomainResource):
    """ A set of images produced in single study (one or more series of references
    images).

    Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-Object
    Pair Instances (SOP Instances - images or other data) acquired or produced
    in a common context.  A series is of only one modality (e.g. X-ray, CT, MR,
    ultrasound), but a study may have multiple series of different modalities.
    """
    resource_type: ClassVar[str] = "ImagingStudy"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    modality: Optional[List[Coding]] = empty_list()
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    started: Optional[FHIRDate] = None
    basedOn: Optional[List[FHIRReference]] = empty_list()
    referrer: Optional[FHIRReference] = None
    interpreter: Optional[List[FHIRReference]] = empty_list()
    endpoint: Optional[List[FHIRReference]] = empty_list()
    numberOfSeries: Optional[int] = None
    numberOfInstances: Optional[int] = None
    procedureReference: Optional[FHIRReference] = None
    procedureCode: Optional[List[CodeableConcept]] = empty_list()
    location: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    description: Optional[str] = None
    series: Optional[List[ImagingStudySeries]] = empty_list()

    def elementProperties(self):
        js = super(ImagingStudy, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("modality", "modality", Coding, True, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("started", "started", FHIRDate, False, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("referrer", "referrer", FHIRReference, False, None, False),
            ("interpreter", "interpreter", FHIRReference, True, None, False),
            ("endpoint", "endpoint", FHIRReference, True, None, False),
            ("numberOfSeries", "numberOfSeries", int, False, None, False),
            ("numberOfInstances", "numberOfInstances", int, False, None, False),
            ("procedureReference", "procedureReference", FHIRReference, False, None, False),
            ("procedureCode", "procedureCode", CodeableConcept, True, None, False),
            ("location", "location", FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("description", "description", str, False, None, False),
            ("series", "series", ImagingStudySeries, True, None, False),
        ])
        return js