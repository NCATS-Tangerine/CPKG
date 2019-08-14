#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/MedicationKnowledge) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .dosage import Dosage
from .duration import Duration
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class MedicationKnowledgeRegulatorySubstitution(BackboneElement):
    """ Specifies if changes are allowed when dispensing a medication from a
    regulatory perspective.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatorySubstitution"
    type: CodeableConcept = None
    allowed: bool = None

    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatorySubstitution, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("allowed", "allowed", bool, False, None, True),
        ])
        return js


@dataclass
class MedicationKnowledgeRegulatorySchedule(BackboneElement):
    """ Specifies the schedule of a medication in jurisdiction.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatorySchedule"
    schedule: CodeableConcept = None

    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatorySchedule, self).elementProperties()
        js.extend([
            ("schedule", "schedule", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class MedicationKnowledgeRegulatoryMaxDispense(BackboneElement):
    """ The maximum number of units of the medication that can be dispensed in a
    period.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatoryMaxDispense"
    quantity: Quantity = None
    period: Optional[Duration] = None

    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatoryMaxDispense, self).elementProperties()
        js.extend([
            ("quantity", "quantity", Quantity, False, None, True),
            ("period", "period", Duration, False, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgeAdministrationGuidelineDosage(BackboneElement):
    """ Dosage for the medication for the specific guidelines.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeAdministrationGuidelineDosage"
    type: CodeableConcept = None
    dosage: List[Dosage] = empty_list()

    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelineDosage, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("dosage", "dosage", Dosage, True, None, True),
        ])
        return js


@dataclass
class MedicationKnowledgeAdministrationGuidelinePatientCharacteristic(BackboneElement):
    """ Characteristics of the patient that are relevant to the administration
    guidelines.

    Characteristics of the patient that are relevant to the administration
    guidelines (for example, height, weight, gender, etc.).
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeAdministrationGuidelinePatientCharacteristic"
    characteristicCodeableConcept: CodeableConcept = None
    characteristicQuantity: Quantity = None
    value: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelinePatientCharacteristic, self).elementProperties()
        js.extend([
            ("characteristicCodeableConcept", "characteristicCodeableConcept", CodeableConcept, False, "characteristic", True),
            ("characteristicQuantity", "characteristicQuantity", Quantity, False, "characteristic", True),
            ("value", "value", str, True, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgeRelatedMedicationKnowledge(BackboneElement):
    """ Associated or related medication information.

    Associated or related knowledge about a medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRelatedMedicationKnowledge"
    type: CodeableConcept = None
    reference: List[FHIRReference] = empty_list()

    def elementProperties(self):
        js = super(MedicationKnowledgeRelatedMedicationKnowledge, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("reference", "reference", FHIRReference, True, None, True),
        ])
        return js


@dataclass
class MedicationKnowledgeMonograph(BackboneElement):
    """ Associated documentation about the medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeMonograph"
    type: Optional[CodeableConcept] = None
    source: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(MedicationKnowledgeMonograph, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("source", "source", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgeIngredient(BackboneElement):
    """ Active or inactive ingredient.

    Identifies a particular constituent of interest in the product.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeIngredient"
    itemCodeableConcept: CodeableConcept = None
    itemReference: FHIRReference = None
    isActive: Optional[bool] = None
    strength: Optional[Ratio] = None

    def elementProperties(self):
        js = super(MedicationKnowledgeIngredient, self).elementProperties()
        js.extend([
            ("itemCodeableConcept", "itemCodeableConcept", CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", FHIRReference, False, "item", True),
            ("isActive", "isActive", bool, False, None, False),
            ("strength", "strength", Ratio, False, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgeCost(BackboneElement):
    """ The pricing of the medication.

    The price of the medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeCost"
    type: CodeableConcept = None
    source: Optional[str] = None
    cost: Money = None

    def elementProperties(self):
        js = super(MedicationKnowledgeCost, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("source", "source", str, False, None, False),
            ("cost", "cost", Money, False, None, True),
        ])
        return js


@dataclass
class MedicationKnowledgeMonitoringProgram(BackboneElement):
    """ Program under which a medication is reviewed.

    The program under which the medication is reviewed.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeMonitoringProgram"
    type: Optional[CodeableConcept] = None
    name: Optional[str] = None

    def elementProperties(self):
        js = super(MedicationKnowledgeMonitoringProgram, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("name", "name", str, False, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgeAdministrationGuideline(BackboneElement):
    """ Guidelines or protocols for administration of the medication.

    Guidelines or protocols that are applicable for the administration of the
    medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeAdministrationGuideline"
    dosage: Optional[List[MedicationKnowledgeAdministrationGuidelineDosage]] = empty_list()
    indicationCodeableConcept: Optional[CodeableConcept] = None
    indicationReference: Optional[FHIRReference] = None
    patientCharacteristic: Optional[List[MedicationKnowledgeAdministrationGuidelinePatientCharacteristic]] = empty_list()

    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuideline, self).elementProperties()
        js.extend([
            ("dosage", "dosage", MedicationKnowledgeAdministrationGuidelineDosage, True, None, False),
            ("indicationCodeableConcept", "indicationCodeableConcept", CodeableConcept, False, "indication", False),
            ("indicationReference", "indicationReference", FHIRReference, False, "indication", False),
            ("patientCharacteristic", "patientCharacteristic", MedicationKnowledgeAdministrationGuidelinePatientCharacteristic, True, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgeMedicineClassification(BackboneElement):
    """ Categorization of the medication within a formulary or classification
    system.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeMedicineClassification"
    type: CodeableConcept = None
    classification: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(MedicationKnowledgeMedicineClassification, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("classification", "classification", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgePackaging(BackboneElement):
    """ Details about packaged medications.

    Information that only applies to packages (not products).
    """
    resource_type: ClassVar[str] = "MedicationKnowledgePackaging"
    type: Optional[CodeableConcept] = None
    quantity: Optional[Quantity] = None
    device: Optional[FHIRReference] = None
    material: Optional[CodeableConcept] = None
    packaging: Optional[List["MedicationKnowledgePackaging"]] = empty_list()

    def elementProperties(self):
        js = super(MedicationKnowledgePackaging, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("device", "device", FHIRReference, False, None, False),
            ("material", "material", CodeableConcept, False, None, False),
            ("packaging", "packaging", MedicationKnowledgePackaging, True, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgeDrugCharacteristic(BackboneElement):
    """ Specifies descriptive properties of the medicine.

    Specifies descriptive properties of the medicine, such as color, shape,
    imprints, etc.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeDrugCharacteristic"
    type: Optional[CodeableConcept] = None
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueString: Optional[str] = None
    valueQuantity: Optional[Quantity] = None
    valueBase64Binary: Optional[str] = None

    def elementProperties(self):
        js = super(MedicationKnowledgeDrugCharacteristic, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", False),
        ])
        return js


@dataclass
class MedicationKnowledgeRegulatory(BackboneElement):
    """ Regulatory information about a medication.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeRegulatory"
    regulatoryAuthority: FHIRReference = None
    substitution: Optional[List[MedicationKnowledgeRegulatorySubstitution]] = empty_list()
    schedule: Optional[List[MedicationKnowledgeRegulatorySchedule]] = empty_list()
    maxDispense: Optional[MedicationKnowledgeRegulatoryMaxDispense] = None

    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatory, self).elementProperties()
        js.extend([
            ("regulatoryAuthority", "regulatoryAuthority", FHIRReference, False, None, True),
            ("substitution", "substitution", MedicationKnowledgeRegulatorySubstitution, True, None, False),
            ("schedule", "schedule", MedicationKnowledgeRegulatorySchedule, True, None, False),
            ("maxDispense", "maxDispense", MedicationKnowledgeRegulatoryMaxDispense, False, None, False),
        ])
        return js


@dataclass
class MedicationKnowledgeKineticCharacteristic(BackboneElement):
    """ The time course of drug absorption, distribution, metabolism and excretion
    of a medication from the body.
    """
    resource_type: ClassVar[str] = "MedicationKnowledgeKineticCharacteristic"
    type: Optional[CodeableConcept] = None
    valueQuantity: Optional[Quantity] = None
    valueDuration: Optional[Duration] = None

    def elementProperties(self):
        js = super(MedicationKnowledgeKineticCharacteristic, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
            ("valueDuration", "valueDuration", Duration, False, "value", False),
        ])
        return js


@dataclass
class MedicationKnowledge(DomainResource):
    """ Definition of Medication Knowledge.

    Information about a medication that is used to support knowledge.
    """
    resource_type: ClassVar[str] = "MedicationKnowledge"
    identifier: Optional[List[Identifier]] = empty_list()
    code: Optional[CodeableConcept] = None
    status: Optional[str] = None
    manufacturer: Optional[FHIRReference] = None
    doseForm: Optional[CodeableConcept] = None
    amount: Optional[Quantity] = None
    synonym: Optional[List[str]] = empty_list()
    relatedMedicationKnowledge: Optional[List[MedicationKnowledgeRelatedMedicationKnowledge]] = empty_list()
    associatedMedication: Optional[List[FHIRReference]] = empty_list()
    productType: Optional[List[CodeableConcept]] = empty_list()
    monograph: Optional[List[MedicationKnowledgeMonograph]] = empty_list()
    ingredient: Optional[List[MedicationKnowledgeIngredient]] = empty_list()
    device: Optional[List[FHIRReference]] = empty_list()
    preparationInstruction: Optional[str] = None
    intendedRoute: Optional[List[CodeableConcept]] = empty_list()
    cost: Optional[List[MedicationKnowledgeCost]] = empty_list()
    monitoringProgram: Optional[List[MedicationKnowledgeMonitoringProgram]] = empty_list()
    administrationGuideline: Optional[List[MedicationKnowledgeAdministrationGuideline]] = empty_list()
    medicineClassification: Optional[List[MedicationKnowledgeMedicineClassification]] = empty_list()
    packaging: Optional[MedicationKnowledgePackaging] = None
    drugCharacteristic: Optional[List[MedicationKnowledgeDrugCharacteristic]] = empty_list()
    clinicalUseIssue: Optional[List[FHIRReference]] = empty_list()
    regulatory: Optional[List[MedicationKnowledgeRegulatory]] = empty_list()
    kineticCharacteristic: Optional[List[MedicationKnowledgeKineticCharacteristic]] = empty_list()

    def elementProperties(self):
        js = super(MedicationKnowledge, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("status", "status", str, False, None, False),
            ("manufacturer", "manufacturer", FHIRReference, False, None, False),
            ("doseForm", "doseForm", CodeableConcept, False, None, False),
            ("amount", "amount", Quantity, False, None, False),
            ("synonym", "synonym", str, True, None, False),
            ("relatedMedicationKnowledge", "relatedMedicationKnowledge", MedicationKnowledgeRelatedMedicationKnowledge, True, None, False),
            ("associatedMedication", "associatedMedication", FHIRReference, True, None, False),
            ("productType", "productType", CodeableConcept, True, None, False),
            ("monograph", "monograph", MedicationKnowledgeMonograph, True, None, False),
            ("ingredient", "ingredient", MedicationKnowledgeIngredient, True, None, False),
            ("device", "device", FHIRReference, True, None, False),
            ("preparationInstruction", "preparationInstruction", str, False, None, False),
            ("intendedRoute", "intendedRoute", CodeableConcept, True, None, False),
            ("cost", "cost", MedicationKnowledgeCost, True, None, False),
            ("monitoringProgram", "monitoringProgram", MedicationKnowledgeMonitoringProgram, True, None, False),
            ("administrationGuideline", "administrationGuideline", MedicationKnowledgeAdministrationGuideline, True, None, False),
            ("medicineClassification", "medicineClassification", MedicationKnowledgeMedicineClassification, True, None, False),
            ("packaging", "packaging", MedicationKnowledgePackaging, False, None, False),
            ("drugCharacteristic", "drugCharacteristic", MedicationKnowledgeDrugCharacteristic, True, None, False),
            ("clinicalUseIssue", "clinicalUseIssue", FHIRReference, True, None, False),
            ("regulatory", "regulatory", MedicationKnowledgeRegulatory, True, None, False),
            ("kineticCharacteristic", "kineticCharacteristic", MedicationKnowledgeKineticCharacteristic, True, None, False),
        ])
        return js