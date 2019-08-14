#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/AllergyIntolerance) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .age import Age
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .range import Range


@dataclass
class AllergyIntoleranceReaction(BackboneElement):
    """ Adverse Reaction Events linked to exposure to substance.

    Details about each adverse reaction event linked to exposure to the
    identified substance.
    """
    resource_type: ClassVar[str] = "AllergyIntoleranceReaction"
    substance: Optional[CodeableConcept] = None
    manifestation: List[CodeableConcept] = empty_list()
    description: Optional[str] = None
    onset: Optional[FHIRDate] = None
    severity: Optional[str] = None
    exposureRoute: Optional[CodeableConcept] = None
    note: Optional[List[Annotation]] = empty_list()

    def elementProperties(self):
        js = super(AllergyIntoleranceReaction, self).elementProperties()
        js.extend([
            ("substance", "substance", CodeableConcept, False, None, False),
            ("manifestation", "manifestation", CodeableConcept, True, None, True),
            ("description", "description", str, False, None, False),
            ("onset", "onset", FHIRDate, False, None, False),
            ("severity", "severity", str, False, None, False),
            ("exposureRoute", "exposureRoute", CodeableConcept, False, None, False),
            ("note", "note", Annotation, True, None, False),
        ])
        return js


@dataclass
class AllergyIntolerance(DomainResource):
    """ Allergy or Intolerance (generally: Risk of adverse reaction to a substance).

    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """
    resource_type: ClassVar[str] = "AllergyIntolerance"
    identifier: Optional[List[Identifier]] = empty_list()
    clinicalStatus: Optional[CodeableConcept] = None
    verificationStatus: Optional[CodeableConcept] = None
    type: Optional[str] = None
    category: Optional[List[str]] = empty_list()
    criticality: Optional[str] = None
    code: Optional[CodeableConcept] = None
    patient: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    onsetDateTime: Optional[FHIRDate] = None
    onsetAge: Optional[Age] = None
    onsetPeriod: Optional[Period] = None
    onsetRange: Optional[Range] = None
    onsetString: Optional[str] = None
    recordedDate: Optional[FHIRDate] = None
    recorder: Optional[FHIRReference] = None
    asserter: Optional[FHIRReference] = None
    lastOccurrence: Optional[FHIRDate] = None
    note: Optional[List[Annotation]] = empty_list()
    reaction: Optional[List[AllergyIntoleranceReaction]] = empty_list()

    def elementProperties(self):
        js = super(AllergyIntolerance, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("clinicalStatus", "clinicalStatus", CodeableConcept, False, None, False),
            ("verificationStatus", "verificationStatus", CodeableConcept, False, None, False),
            ("type", "type", str, False, None, False),
            ("category", "category", str, True, None, False),
            ("criticality", "criticality", str, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("patient", "patient", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("onsetDateTime", "onsetDateTime", FHIRDate, False, "onset", False),
            ("onsetAge", "onsetAge", Age, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", Period, False, "onset", False),
            ("onsetRange", "onsetRange", Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("recordedDate", "recordedDate", FHIRDate, False, None, False),
            ("recorder", "recorder", FHIRReference, False, None, False),
            ("asserter", "asserter", FHIRReference, False, None, False),
            ("lastOccurrence", "lastOccurrence", FHIRDate, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("reaction", "reaction", AllergyIntoleranceReaction, True, None, False),
        ])
        return js