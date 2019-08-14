#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ResearchStudy) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .relatedartifact import RelatedArtifact


@dataclass
class ResearchStudyArm(BackboneElement):
    """ Defined path through the study for a subject.

    Describes an expected sequence of events for one of the participants of a
    study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
    follow-up.
    """
    resource_type: ClassVar[str] = "ResearchStudyArm"
    name: str = None
    type: Optional[CodeableConcept] = None
    description: Optional[str] = None

    def elementProperties(self):
        js = super(ResearchStudyArm, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("type", "type", CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
        ])
        return js


@dataclass
class ResearchStudyObjective(BackboneElement):
    """ A goal for the study.

    A goal that the study is aiming to achieve in terms of a scientific
    question to be answered by the analysis of data collected during the study.
    """
    resource_type: ClassVar[str] = "ResearchStudyObjective"
    name: Optional[str] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ResearchStudyObjective, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ResearchStudy(DomainResource):
    """ Investigation to increase healthcare-related patient-independent knowledge.

    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques.  A ResearchStudy
    involves the gathering of information about human or animal subjects.
    """
    resource_type: ClassVar[str] = "ResearchStudy"
    identifier: Optional[List[Identifier]] = empty_list()
    title: Optional[str] = None
    protocol: Optional[List[FHIRReference]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    primaryPurposeType: Optional[CodeableConcept] = None
    phase: Optional[CodeableConcept] = None
    category: Optional[List[CodeableConcept]] = empty_list()
    focus: Optional[List[CodeableConcept]] = empty_list()
    condition: Optional[List[CodeableConcept]] = empty_list()
    contact: Optional[List[ContactDetail]] = empty_list()
    relatedArtifact: Optional[List[RelatedArtifact]] = empty_list()
    keyword: Optional[List[CodeableConcept]] = empty_list()
    location: Optional[List[CodeableConcept]] = empty_list()
    description: Optional[str] = None
    enrollment: Optional[List[FHIRReference]] = empty_list()
    period: Optional[Period] = None
    sponsor: Optional[FHIRReference] = None
    principalInvestigator: Optional[FHIRReference] = None
    site: Optional[List[FHIRReference]] = empty_list()
    reasonStopped: Optional[CodeableConcept] = None
    note: Optional[List[Annotation]] = empty_list()
    arm: Optional[List[ResearchStudyArm]] = empty_list()
    objective: Optional[List[ResearchStudyObjective]] = empty_list()

    def elementProperties(self):
        js = super(ResearchStudy, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("title", "title", str, False, None, False),
            ("protocol", "protocol", FHIRReference, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("primaryPurposeType", "primaryPurposeType", CodeableConcept, False, None, False),
            ("phase", "phase", CodeableConcept, False, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("focus", "focus", CodeableConcept, True, None, False),
            ("condition", "condition", CodeableConcept, True, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("relatedArtifact", "relatedArtifact", RelatedArtifact, True, None, False),
            ("keyword", "keyword", CodeableConcept, True, None, False),
            ("location", "location", CodeableConcept, True, None, False),
            ("description", "description", str, False, None, False),
            ("enrollment", "enrollment", FHIRReference, True, None, False),
            ("period", "period", Period, False, None, False),
            ("sponsor", "sponsor", FHIRReference, False, None, False),
            ("principalInvestigator", "principalInvestigator", FHIRReference, False, None, False),
            ("site", "site", FHIRReference, True, None, False),
            ("reasonStopped", "reasonStopped", CodeableConcept, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("arm", "arm", ResearchStudyArm, True, None, False),
            ("objective", "objective", ResearchStudyObjective, True, None, False),
        ])
        return js