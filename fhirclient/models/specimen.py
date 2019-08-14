#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Specimen) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity


@dataclass
class SpecimenCollection(BackboneElement):
    """ Collection details.

    Details concerning the specimen collection.
    """
    resource_type: ClassVar[str] = "SpecimenCollection"
    collector: Optional[FHIRReference] = None
    collectedDateTime: Optional[FHIRDate] = None
    collectedPeriod: Optional[Period] = None
    duration: Optional[Duration] = None
    quantity: Optional[Quantity] = None
    method: Optional[CodeableConcept] = None
    bodySite: Optional[CodeableConcept] = None
    fastingStatusCodeableConcept: Optional[CodeableConcept] = None
    fastingStatusDuration: Optional[Duration] = None

    def elementProperties(self):
        js = super(SpecimenCollection, self).elementProperties()
        js.extend([
            ("collector", "collector", FHIRReference, False, None, False),
            ("collectedDateTime", "collectedDateTime", FHIRDate, False, "collected", False),
            ("collectedPeriod", "collectedPeriod", Period, False, "collected", False),
            ("duration", "duration", Duration, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("method", "method", CodeableConcept, False, None, False),
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("fastingStatusCodeableConcept", "fastingStatusCodeableConcept", CodeableConcept, False, "fastingStatus", False),
            ("fastingStatusDuration", "fastingStatusDuration", Duration, False, "fastingStatus", False),
        ])
        return js


@dataclass
class SpecimenProcessing(BackboneElement):
    """ Processing and processing step details.

    Details concerning processing and processing steps for the specimen.
    """
    resource_type: ClassVar[str] = "SpecimenProcessing"
    description: Optional[str] = None
    procedure: Optional[CodeableConcept] = None
    additive: Optional[List[FHIRReference]] = empty_list()
    timeDateTime: Optional[FHIRDate] = None
    timePeriod: Optional[Period] = None

    def elementProperties(self):
        js = super(SpecimenProcessing, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("procedure", "procedure", CodeableConcept, False, None, False),
            ("additive", "additive", FHIRReference, True, None, False),
            ("timeDateTime", "timeDateTime", FHIRDate, False, "time", False),
            ("timePeriod", "timePeriod", Period, False, "time", False),
        ])
        return js


@dataclass
class SpecimenContainer(BackboneElement):
    """ Direct container of specimen (tube/slide, etc.).

    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """
    resource_type: ClassVar[str] = "SpecimenContainer"
    identifier: Optional[List[Identifier]] = empty_list()
    description: Optional[str] = None
    type: Optional[CodeableConcept] = None
    capacity: Optional[Quantity] = None
    specimenQuantity: Optional[Quantity] = None
    additiveCodeableConcept: Optional[CodeableConcept] = None
    additiveReference: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(SpecimenContainer, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("description", "description", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("capacity", "capacity", Quantity, False, None, False),
            ("specimenQuantity", "specimenQuantity", Quantity, False, None, False),
            ("additiveCodeableConcept", "additiveCodeableConcept", CodeableConcept, False, "additive", False),
            ("additiveReference", "additiveReference", FHIRReference, False, "additive", False),
        ])
        return js


@dataclass
class Specimen(DomainResource):
    """ Sample for analysis.

    A sample to be used for analysis.
    """
    resource_type: ClassVar[str] = "Specimen"
    identifier: Optional[List[Identifier]] = empty_list()
    accessionIdentifier: Optional[Identifier] = None
    status: Optional[str] = None
    type: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    receivedTime: Optional[FHIRDate] = None
    parent: Optional[List[FHIRReference]] = empty_list()
    request: Optional[List[FHIRReference]] = empty_list()
    collection: Optional[SpecimenCollection] = None
    processing: Optional[List[SpecimenProcessing]] = empty_list()
    container: Optional[List[SpecimenContainer]] = empty_list()
    condition: Optional[List[CodeableConcept]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()

    def elementProperties(self):
        js = super(Specimen, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("accessionIdentifier", "accessionIdentifier", Identifier, False, None, False),
            ("status", "status", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("receivedTime", "receivedTime", FHIRDate, False, None, False),
            ("parent", "parent", FHIRReference, True, None, False),
            ("request", "request", FHIRReference, True, None, False),
            ("collection", "collection", SpecimenCollection, False, None, False),
            ("processing", "processing", SpecimenProcessing, True, None, False),
            ("container", "container", SpecimenContainer, True, None, False),
            ("condition", "condition", CodeableConcept, True, None, False),
            ("note", "note", Annotation, True, None, False),
        ])
        return js