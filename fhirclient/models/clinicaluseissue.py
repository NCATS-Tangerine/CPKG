#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ClinicalUseIssue) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .population import Population
from .quantity import Quantity


@dataclass
class ClinicalUseIssueInteractionInteractant(BackboneElement):
    """ The specific medication, food or laboratory test that interacts.
    """
    resource_type: ClassVar[str] = "ClinicalUseIssueInteractionInteractant"
    itemReference: FHIRReference = None
    itemCodeableConcept: CodeableConcept = None

    def elementProperties(self):
        js = super(ClinicalUseIssueInteractionInteractant, self).elementProperties()
        js.extend([
            ("itemReference", "itemReference", FHIRReference, False, "item", True),
            ("itemCodeableConcept", "itemCodeableConcept", CodeableConcept, False, "item", True),
        ])
        return js


@dataclass
class ClinicalUseIssueContraindicationOtherTherapy(BackboneElement):
    """ Information about the use of the medicinal product in relation to other
    therapies described as part of the indication.
    """
    resource_type: ClassVar[str] = "ClinicalUseIssueContraindicationOtherTherapy"
    therapyRelationshipType: CodeableConcept = None
    medicationCodeableConcept: CodeableConcept = None
    medicationReference: FHIRReference = None

    def elementProperties(self):
        js = super(ClinicalUseIssueContraindicationOtherTherapy, self).elementProperties()
        js.extend([
            ("therapyRelationshipType", "therapyRelationshipType", CodeableConcept, False, None, True),
            ("medicationCodeableConcept", "medicationCodeableConcept", CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", FHIRReference, False, "medication", True),
        ])
        return js


@dataclass
class ClinicalUseIssueContraindication(BackboneElement):
    """ Specifics for when this is a contraindication.
    """
    resource_type: ClassVar[str] = "ClinicalUseIssueContraindication"
    diseaseSymptomProcedure: Optional[CodeableConcept] = None
    diseaseStatus: Optional[CodeableConcept] = None
    comorbidity: Optional[List[CodeableConcept]] = empty_list()
    indication: Optional[List[FHIRReference]] = empty_list()
    otherTherapy: Optional[List[ClinicalUseIssueContraindicationOtherTherapy]] = empty_list()

    def elementProperties(self):
        js = super(ClinicalUseIssueContraindication, self).elementProperties()
        js.extend([
            ("diseaseSymptomProcedure", "diseaseSymptomProcedure", CodeableConcept, False, None, False),
            ("diseaseStatus", "diseaseStatus", CodeableConcept, False, None, False),
            ("comorbidity", "comorbidity", CodeableConcept, True, None, False),
            ("indication", "indication", FHIRReference, True, None, False),
            ("otherTherapy", "otherTherapy", ClinicalUseIssueContraindicationOtherTherapy, True, None, False),
        ])
        return js


@dataclass
class ClinicalUseIssueIndication(BackboneElement):
    """ Specifics for when this is an indication.
    """
    resource_type: ClassVar[str] = "ClinicalUseIssueIndication"
    diseaseSymptomProcedure: Optional[CodeableConcept] = None
    diseaseStatus: Optional[CodeableConcept] = None
    comorbidity: Optional[List[CodeableConcept]] = empty_list()
    intendedEffect: Optional[CodeableConcept] = None
    duration: Optional[Quantity] = None
    undesirableEffect: Optional[List[FHIRReference]] = empty_list()
    otherTherapy: Optional[List[ClinicalUseIssueContraindicationOtherTherapy]] = empty_list()

    def elementProperties(self):
        js = super(ClinicalUseIssueIndication, self).elementProperties()
        js.extend([
            ("diseaseSymptomProcedure", "diseaseSymptomProcedure", CodeableConcept, False, None, False),
            ("diseaseStatus", "diseaseStatus", CodeableConcept, False, None, False),
            ("comorbidity", "comorbidity", CodeableConcept, True, None, False),
            ("intendedEffect", "intendedEffect", CodeableConcept, False, None, False),
            ("duration", "duration", Quantity, False, None, False),
            ("undesirableEffect", "undesirableEffect", FHIRReference, True, None, False),
            ("otherTherapy", "otherTherapy", ClinicalUseIssueContraindicationOtherTherapy, True, None, False),
        ])
        return js


@dataclass
class ClinicalUseIssueInteraction(BackboneElement):
    """ Specifics for when this is an interaction.
    """
    resource_type: ClassVar[str] = "ClinicalUseIssueInteraction"
    interactant: Optional[List[ClinicalUseIssueInteractionInteractant]] = empty_list()
    type: Optional[CodeableConcept] = None
    effect: Optional[CodeableConcept] = None
    incidence: Optional[CodeableConcept] = None
    management: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ClinicalUseIssueInteraction, self).elementProperties()
        js.extend([
            ("interactant", "interactant", ClinicalUseIssueInteractionInteractant, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("effect", "effect", CodeableConcept, False, None, False),
            ("incidence", "incidence", CodeableConcept, False, None, False),
            ("management", "management", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ClinicalUseIssueUndesirableEffect(BackboneElement):
    """ UndesirableEffect.

    Describe the undesirable effects of the medicinal product.
    """
    resource_type: ClassVar[str] = "ClinicalUseIssueUndesirableEffect"
    symptomConditionEffect: Optional[CodeableConcept] = None
    classification: Optional[CodeableConcept] = None
    frequencyOfOccurrence: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ClinicalUseIssueUndesirableEffect, self).elementProperties()
        js.extend([
            ("symptomConditionEffect", "symptomConditionEffect", CodeableConcept, False, None, False),
            ("classification", "classification", CodeableConcept, False, None, False),
            ("frequencyOfOccurrence", "frequencyOfOccurrence", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ClinicalUseIssue(DomainResource):
    """ ClinicalUseIssue.

    A single item of clinical particulars - an indication, contraindication,
    interaction etc. for a medicinal product.
    """
    resource_type: ClassVar[str] = "ClinicalUseIssue"
    type: str = None
    subject: Optional[List[FHIRReference]] = empty_list()
    description: Optional[str] = None
    contraindication: Optional[ClinicalUseIssueContraindication] = None
    indication: Optional[ClinicalUseIssueIndication] = None
    interaction: Optional[ClinicalUseIssueInteraction] = None
    population: Optional[List[Population]] = empty_list()
    undesirableEffect: Optional[ClinicalUseIssueUndesirableEffect] = None

    def elementProperties(self):
        js = super(ClinicalUseIssue, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("subject", "subject", FHIRReference, True, None, False),
            ("description", "description", str, False, None, False),
            ("contraindication", "contraindication", ClinicalUseIssueContraindication, False, None, False),
            ("indication", "indication", ClinicalUseIssueIndication, False, None, False),
            ("interaction", "interaction", ClinicalUseIssueInteraction, False, None, False),
            ("population", "population", Population, True, None, False),
            ("undesirableEffect", "undesirableEffect", ClinicalUseIssueUndesirableEffect, False, None, False),
        ])
        return js