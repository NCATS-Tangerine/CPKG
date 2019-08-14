#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ConditionDefinition) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .usagecontext import UsageContext


@dataclass
class ConditionDefinitionObservation(BackboneElement):
    """ Observations particularly relevant to this condition.
    """
    resource_type: ClassVar[str] = "ConditionDefinitionObservation"
    category: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ConditionDefinitionObservation, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ConditionDefinitionMedication(BackboneElement):
    """ Medications particularly relevant for this condition.
    """
    resource_type: ClassVar[str] = "ConditionDefinitionMedication"
    category: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ConditionDefinitionMedication, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ConditionDefinitionPrecondition(BackboneElement):
    """ Observation that suggets this condition.

    An observation that suggests that this condition applies.
    """
    resource_type: ClassVar[str] = "ConditionDefinitionPrecondition"
    type: str = None
    code: CodeableConcept = None
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueQuantity: Optional[Quantity] = None

    def elementProperties(self):
        js = super(ConditionDefinitionPrecondition, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("code", "code", CodeableConcept, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
        ])
        return js


@dataclass
class ConditionDefinitionQuestionnaire(BackboneElement):
    """ Questionnaire for this condition.
    """
    resource_type: ClassVar[str] = "ConditionDefinitionQuestionnaire"
    purpose: str = None
    reference: FHIRReference = None

    def elementProperties(self):
        js = super(ConditionDefinitionQuestionnaire, self).elementProperties()
        js.extend([
            ("purpose", "purpose", str, False, None, True),
            ("reference", "reference", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class ConditionDefinitionPlan(BackboneElement):
    """ Plan that is appropriate.
    """
    resource_type: ClassVar[str] = "ConditionDefinitionPlan"
    role: Optional[CodeableConcept] = None
    reference: FHIRReference = None

    def elementProperties(self):
        js = super(ConditionDefinitionPlan, self).elementProperties()
        js.extend([
            ("role", "role", CodeableConcept, False, None, False),
            ("reference", "reference", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class ConditionDefinition(DomainResource):
    """ A definition of a condition.

    A definition of a condition and information relevant to managing it.
    """
    resource_type: ClassVar[str] = "ConditionDefinition"
    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    code: CodeableConcept = None
    severity: Optional[CodeableConcept] = None
    bodySite: Optional[CodeableConcept] = None
    stage: Optional[CodeableConcept] = None
    hasSeverity: Optional[bool] = None
    hasBodySite: Optional[bool] = None
    hasStage: Optional[bool] = None
    definition: Optional[List[str]] = empty_list()
    observation: Optional[List[ConditionDefinitionObservation]] = empty_list()
    medication: Optional[List[ConditionDefinitionMedication]] = empty_list()
    precondition: Optional[List[ConditionDefinitionPrecondition]] = empty_list()
    team: Optional[List[FHIRReference]] = empty_list()
    questionnaire: Optional[List[ConditionDefinitionQuestionnaire]] = empty_list()
    plan: Optional[List[ConditionDefinitionPlan]] = empty_list()

    def elementProperties(self):
        js = super(ConditionDefinition, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("subtitle", "subtitle", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, True),
            ("severity", "severity", CodeableConcept, False, None, False),
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("stage", "stage", CodeableConcept, False, None, False),
            ("hasSeverity", "hasSeverity", bool, False, None, False),
            ("hasBodySite", "hasBodySite", bool, False, None, False),
            ("hasStage", "hasStage", bool, False, None, False),
            ("definition", "definition", str, True, None, False),
            ("observation", "observation", ConditionDefinitionObservation, True, None, False),
            ("medication", "medication", ConditionDefinitionMedication, True, None, False),
            ("precondition", "precondition", ConditionDefinitionPrecondition, True, None, False),
            ("team", "team", FHIRReference, True, None, False),
            ("questionnaire", "questionnaire", ConditionDefinitionQuestionnaire, True, None, False),
            ("plan", "plan", ConditionDefinitionPlan, True, None, False),
        ])
        return js