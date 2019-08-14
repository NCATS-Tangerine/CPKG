#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/AdverseEvent) on 2019-08-06.
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


@dataclass
class AdverseEventSuspectEntityCausality(BackboneElement):
    """ Information on the possible cause of the event.
    """
    resource_type: ClassVar[str] = "AdverseEventSuspectEntityCausality"
    assessmentMethod: Optional[CodeableConcept] = None
    entityRelatedness: Optional[CodeableConcept] = None
    author: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(AdverseEventSuspectEntityCausality, self).elementProperties()
        js.extend([
            ("assessmentMethod", "assessmentMethod", CodeableConcept, False, None, False),
            ("entityRelatedness", "entityRelatedness", CodeableConcept, False, None, False),
            ("author", "author", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class AdverseEventSuspectEntity(BackboneElement):
    """ The suspected agent causing the adverse event.

    Describes the entity that is suspected to have caused the adverse event.
    """
    resource_type: ClassVar[str] = "AdverseEventSuspectEntity"
    instanceCodeableConcept: CodeableConcept = None
    instanceReference: FHIRReference = None
    causality: Optional[List[AdverseEventSuspectEntityCausality]] = empty_list()

    def elementProperties(self):
        js = super(AdverseEventSuspectEntity, self).elementProperties()
        js.extend([
            ("instanceCodeableConcept", "instanceCodeableConcept", CodeableConcept, False, "instance", True),
            ("instanceReference", "instanceReference", FHIRReference, False, "instance", True),
            ("causality", "causality", AdverseEventSuspectEntityCausality, True, None, False),
        ])
        return js


@dataclass
class AdverseEventSupportingInfo(BackboneElement):
    """ Supporting information relevant to the event.
    """
    resource_type: ClassVar[str] = "AdverseEventSupportingInfo"
    item: FHIRReference = None
    contributingFactor: Optional[bool] = None

    def elementProperties(self):
        js = super(AdverseEventSupportingInfo, self).elementProperties()
        js.extend([
            ("item", "item", FHIRReference, False, None, True),
            ("contributingFactor", "contributingFactor", bool, False, None, False),
        ])
        return js


@dataclass
class AdverseEvent(DomainResource):
    """ Medical care, research study or other healthcare event causing physical
    injury.

    An event (i.e. any change to current patient status) that may be related to
    unintended effects on a patient or research subject.  The unintended
    effects may require additional monitoring, treatment or hospitalization or
    may result in death.  The AdverseEvent resource also extends to potential
    or avoided events that could have had such effects.
    """
    resource_type: ClassVar[str] = "AdverseEvent"
    identifier: Optional[List[Identifier]] = empty_list()
    actuality: str = None
    category: Optional[List[CodeableConcept]] = empty_list()
    code: Optional[CodeableConcept] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    detected: Optional[FHIRDate] = None
    recordedDate: Optional[FHIRDate] = None
    resultingCondition: Optional[List[FHIRReference]] = empty_list()
    location: Optional[FHIRReference] = None
    seriousness: Optional[CodeableConcept] = None
    severity: Optional[CodeableConcept] = None
    outcome: Optional[CodeableConcept] = None
    recorder: Optional[FHIRReference] = None
    contributor: Optional[List[FHIRReference]] = empty_list()
    detector: Optional[List[FHIRReference]] = empty_list()
    suspectEntity: Optional[List[AdverseEventSuspectEntity]] = empty_list()
    supportingInfo: Optional[List[AdverseEventSupportingInfo]] = empty_list()
    study: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(AdverseEvent, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("actuality", "actuality", str, False, None, True),
            ("category", "category", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("detected", "detected", FHIRDate, False, None, False),
            ("recordedDate", "recordedDate", FHIRDate, False, None, False),
            ("resultingCondition", "resultingCondition", FHIRReference, True, None, False),
            ("location", "location", FHIRReference, False, None, False),
            ("seriousness", "seriousness", CodeableConcept, False, None, False),
            ("severity", "severity", CodeableConcept, False, None, False),
            ("outcome", "outcome", CodeableConcept, False, None, False),
            ("recorder", "recorder", FHIRReference, False, None, False),
            ("contributor", "contributor", FHIRReference, True, None, False),
            ("detector", "detector", FHIRReference, True, None, False),
            ("suspectEntity", "suspectEntity", AdverseEventSuspectEntity, True, None, False),
            ("supportingInfo", "supportingInfo", AdverseEventSupportingInfo, True, None, False),
            ("study", "study", FHIRReference, True, None, False),
        ])
        return js