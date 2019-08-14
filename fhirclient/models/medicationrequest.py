#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/MedicationRequest) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .dosage import Dosage
from .duration import Duration
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity


@dataclass
class MedicationRequestDispenseRequestInitialFill(BackboneElement):
    """ First fill details.

    Indicates the quantity or duration for the first dispense of the
    medication.
    """
    resource_type: ClassVar[str] = "MedicationRequestDispenseRequestInitialFill"
    quantity: Optional[Quantity] = None
    duration: Optional[Duration] = None

    def elementProperties(self):
        js = super(MedicationRequestDispenseRequestInitialFill, self).elementProperties()
        js.extend([
            ("quantity", "quantity", Quantity, False, None, False),
            ("duration", "duration", Duration, False, None, False),
        ])
        return js


@dataclass
class MedicationRequestDispenseRequest(BackboneElement):
    """ Medication supply authorization.

    Indicates the specific details for the dispense or medication supply part
    of a medication request (also known as a Medication Prescription or
    Medication Order).  Note that this information is not always sent with the
    order.  There may be in some settings (e.g. hospitals) institutional or
    system support for completing the dispense details in the pharmacy
    department.
    """
    resource_type: ClassVar[str] = "MedicationRequestDispenseRequest"
    initialFill: Optional[MedicationRequestDispenseRequestInitialFill] = None
    dispenseInterval: Optional[Duration] = None
    validityPeriod: Optional[Period] = None
    numberOfRepeatsAllowed: Optional[int] = None
    quantity: Optional[Quantity] = None
    expectedSupplyDuration: Optional[Duration] = None
    performer: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(MedicationRequestDispenseRequest, self).elementProperties()
        js.extend([
            ("initialFill", "initialFill", MedicationRequestDispenseRequestInitialFill, False, None, False),
            ("dispenseInterval", "dispenseInterval", Duration, False, None, False),
            ("validityPeriod", "validityPeriod", Period, False, None, False),
            ("numberOfRepeatsAllowed", "numberOfRepeatsAllowed", int, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("expectedSupplyDuration", "expectedSupplyDuration", Duration, False, None, False),
            ("performer", "performer", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class MedicationRequestSubstitution(BackboneElement):
    """ Any restrictions on medication substitution.

    Indicates whether or not substitution can or should be part of the
    dispense. In some cases, substitution must happen, in other cases
    substitution must not happen. This block explains the prescriber's intent.
    If nothing is specified substitution may be done.
    """
    resource_type: ClassVar[str] = "MedicationRequestSubstitution"
    allowedBoolean: bool = None
    allowedCodeableConcept: CodeableConcept = None
    reason: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MedicationRequestSubstitution, self).elementProperties()
        js.extend([
            ("allowedBoolean", "allowedBoolean", bool, False, "allowed", True),
            ("allowedCodeableConcept", "allowedCodeableConcept", CodeableConcept, False, "allowed", True),
            ("reason", "reason", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class MedicationRequest(DomainResource):
    """ Ordering of medication for patient or group.

    An order or request for both supply of the medication and the instructions
    for administration of the medication to a patient. The resource is called
    "MedicationRequest" rather than "MedicationPrescription" or
    "MedicationOrder" to generalize the use across inpatient and outpatient
    settings, including care plans, etc., and to harmonize with workflow
    patterns.
    """
    resource_type: ClassVar[str] = "MedicationRequest"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    intent: str = None
    category: Optional[List[CodeableConcept]] = empty_list()
    priority: Optional[str] = None
    doNotPerform: Optional[bool] = None
    reported: Optional[bool] = None
    informationSource: Optional[FHIRReference] = None
    medicationCodeableConcept: CodeableConcept = None
    medicationReference: FHIRReference = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    supportingInformation: Optional[List[FHIRReference]] = empty_list()
    authoredOn: Optional[FHIRDate] = None
    requester: Optional[FHIRReference] = None
    performer: Optional[FHIRReference] = None
    performerType: Optional[CodeableConcept] = None
    recorder: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    basedOn: Optional[List[FHIRReference]] = empty_list()
    groupIdentifier: Optional[Identifier] = None
    courseOfTherapyType: Optional[CodeableConcept] = None
    insurance: Optional[List[FHIRReference]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    dosageInstruction: Optional[List[Dosage]] = empty_list()
    dispenseRequest: Optional[MedicationRequestDispenseRequest] = None
    substitution: Optional[MedicationRequestSubstitution] = None
    priorPrescription: Optional[FHIRReference] = None
    detectedIssue: Optional[List[FHIRReference]] = empty_list()
    eventHistory: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(MedicationRequest, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", CodeableConcept, False, None, False),
            ("intent", "intent", str, False, None, True),
            ("category", "category", CodeableConcept, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("reported", "reported", bool, False, None, False),
            ("informationSource", "informationSource", FHIRReference, False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", FHIRReference, False, "medication", True),
            ("subject", "subject", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("supportingInformation", "supportingInformation", FHIRReference, True, None, False),
            ("authoredOn", "authoredOn", FHIRDate, False, None, False),
            ("requester", "requester", FHIRReference, False, None, False),
            ("performer", "performer", FHIRReference, False, None, False),
            ("performerType", "performerType", CodeableConcept, False, None, False),
            ("recorder", "recorder", FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("groupIdentifier", "groupIdentifier", Identifier, False, None, False),
            ("courseOfTherapyType", "courseOfTherapyType", CodeableConcept, False, None, False),
            ("insurance", "insurance", FHIRReference, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("dosageInstruction", "dosageInstruction", Dosage, True, None, False),
            ("dispenseRequest", "dispenseRequest", MedicationRequestDispenseRequest, False, None, False),
            ("substitution", "substitution", MedicationRequestSubstitution, False, None, False),
            ("priorPrescription", "priorPrescription", FHIRReference, False, None, False),
            ("detectedIssue", "detectedIssue", FHIRReference, True, None, False),
            ("eventHistory", "eventHistory", FHIRReference, True, None, False),
        ])
        return js