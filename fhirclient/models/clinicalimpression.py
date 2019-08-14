#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ClinicalImpression) on 2019-08-06.
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


@dataclass
class ClinicalImpressionFinding(BackboneElement):
    """ Possible or likely findings and diagnoses.

    Specific findings or diagnoses that were considered likely or relevant to
    ongoing treatment.
    """
    resource_type: ClassVar[str] = "ClinicalImpressionFinding"
    itemCodeableConcept: Optional[CodeableConcept] = None
    itemReference: Optional[FHIRReference] = None
    basis: Optional[str] = None

    def elementProperties(self):
        js = super(ClinicalImpressionFinding, self).elementProperties()
        js.extend([
            ("itemCodeableConcept", "itemCodeableConcept", CodeableConcept, False, None, False),
            ("itemReference", "itemReference", FHIRReference, False, None, False),
            ("basis", "basis", str, False, None, False),
        ])
        return js


@dataclass
class ClinicalImpression(DomainResource):
    """ A clinical assessment performed when planning treatments and management
    strategies for a patient.

    A record of a clinical assessment performed to determine what problem(s)
    may affect the patient and before planning the treatments or management
    strategies that are best to manage a patient's condition. Assessments are
    often 1:1 with a clinical consultation / encounter,  but this varies
    greatly depending on the clinical workflow. This resource is called
    "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion
    with the recording of assessment tools such as Apgar score.
    """
    resource_type: ClassVar[str] = "ClinicalImpression"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    description: Optional[str] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    effectiveDateTime: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    date: Optional[FHIRDate] = None
    performer: Optional[FHIRReference] = None
    previous: Optional[FHIRReference] = None
    problem: Optional[List[FHIRReference]] = empty_list()
    protocol: Optional[List[str]] = empty_list()
    summary: Optional[str] = None
    finding: Optional[List[ClinicalImpressionFinding]] = empty_list()
    prognosisCodeableConcept: Optional[List[CodeableConcept]] = empty_list()
    prognosisReference: Optional[List[FHIRReference]] = empty_list()
    supportingInfo: Optional[List[FHIRReference]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()

    def elementProperties(self):
        js = super(ClinicalImpression, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", CodeableConcept, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", Period, False, "effective", False),
            ("date", "date", FHIRDate, False, None, False),
            ("performer", "performer", FHIRReference, False, None, False),
            ("previous", "previous", FHIRReference, False, None, False),
            ("problem", "problem", FHIRReference, True, None, False),
            ("protocol", "protocol", str, True, None, False),
            ("summary", "summary", str, False, None, False),
            ("finding", "finding", ClinicalImpressionFinding, True, None, False),
            ("prognosisCodeableConcept", "prognosisCodeableConcept", CodeableConcept, True, None, False),
            ("prognosisReference", "prognosisReference", FHIRReference, True, None, False),
            ("supportingInfo", "supportingInfo", FHIRReference, True, None, False),
            ("note", "note", Annotation, True, None, False),
        ])
        return js