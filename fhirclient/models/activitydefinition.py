#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ActivityDefinition) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .age import Age
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .dosage import Dosage
from .duration import Duration
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .relatedartifact import RelatedArtifact
from .timing import Timing
from .usagecontext import UsageContext


@dataclass
class ActivityDefinitionParticipant(BackboneElement):
    """ Who should participate in the action.

    Indicates who should participate in performing the action described.
    """
    resource_type: ClassVar[str] = "ActivityDefinitionParticipant"
    type: str = None
    role: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ActivityDefinitionParticipant, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("role", "role", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ActivityDefinitionDynamicValue(BackboneElement):
    """ Dynamic aspects of the definition.

    Dynamic values that will be evaluated to produce values for elements of the
    resulting resource. For example, if the dosage of a medication must be
    computed based on the patient's weight, a dynamic value would be used to
    specify an expression that calculated the weight, and the path on the
    request resource that would contain the result.
    """
    resource_type: ClassVar[str] = "ActivityDefinitionDynamicValue"
    path: str = None
    expression: Expression = None

    def elementProperties(self):
        js = super(ActivityDefinitionDynamicValue, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, True),
            ("expression", "expression", Expression, False, None, True),
        ])
        return js


@dataclass
class ActivityDefinition(DomainResource):
    """ The definition of a specific activity to be taken, independent of any
    particular patient or context.

    This resource allows for the definition of some activity to be performed,
    independent of a particular patient, practitioner, or other performance
    context.
    """
    resource_type: ClassVar[str] = "ActivityDefinition"
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
    kind: Optional[str] = None
    profile: Optional[str] = None
    code: Optional[CodeableConcept] = None
    intent: Optional[str] = None
    priority: Optional[str] = None
    doNotPerform: Optional[bool] = None
    timingTiming: Optional[Timing] = None
    timingDateTime: Optional[FHIRDate] = None
    timingAge: Optional[Age] = None
    timingPeriod: Optional[Period] = None
    timingRange: Optional[Range] = None
    timingDuration: Optional[Duration] = None
    location: Optional[FHIRReference] = None
    participant: Optional[List[ActivityDefinitionParticipant]] = empty_list()
    productReference: Optional[FHIRReference] = None
    productCodeableConcept: Optional[CodeableConcept] = None
    quantity: Optional[Quantity] = None
    dosage: Optional[List[Dosage]] = empty_list()
    bodySite: Optional[List[CodeableConcept]] = empty_list()
    specimenRequirement: Optional[List[FHIRReference]] = empty_list()
    observationRequirement: Optional[List[FHIRReference]] = empty_list()
    observationResultRequirement: Optional[List[FHIRReference]] = empty_list()
    transform: Optional[str] = None
    dynamicValue: Optional[List[ActivityDefinitionDynamicValue]] = empty_list()

    def elementProperties(self):
        js = super(ActivityDefinition, self).elementProperties()
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
            ("kind", "kind", str, False, None, False),
            ("profile", "profile", str, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("intent", "intent", str, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("timingTiming", "timingTiming", Timing, False, "timing", False),
            ("timingDateTime", "timingDateTime", FHIRDate, False, "timing", False),
            ("timingAge", "timingAge", Age, False, "timing", False),
            ("timingPeriod", "timingPeriod", Period, False, "timing", False),
            ("timingRange", "timingRange", Range, False, "timing", False),
            ("timingDuration", "timingDuration", Duration, False, "timing", False),
            ("location", "location", FHIRReference, False, None, False),
            ("participant", "participant", ActivityDefinitionParticipant, True, None, False),
            ("productReference", "productReference", FHIRReference, False, "product", False),
            ("productCodeableConcept", "productCodeableConcept", CodeableConcept, False, "product", False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("dosage", "dosage", Dosage, True, None, False),
            ("bodySite", "bodySite", CodeableConcept, True, None, False),
            ("specimenRequirement", "specimenRequirement", FHIRReference, True, None, False),
            ("observationRequirement", "observationRequirement", FHIRReference, True, None, False),
            ("observationResultRequirement", "observationResultRequirement", FHIRReference, True, None, False),
            ("transform", "transform", str, False, None, False),
            ("dynamicValue", "dynamicValue", ActivityDefinitionDynamicValue, True, None, False),
        ])
        return js