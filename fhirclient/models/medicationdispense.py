#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/MedicationDispense) on 2019-08-06.
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
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity


@dataclass
class MedicationDispensePerformer(BackboneElement):
    """ Who performed event.

    Indicates who or what performed the event.
    """
    resource_type: ClassVar[str] = "MedicationDispensePerformer"
    function: Optional[CodeableConcept] = None
    actor: FHIRReference = None

    def elementProperties(self):
        js = super(MedicationDispensePerformer, self).elementProperties()
        js.extend([
            ("function", "function", CodeableConcept, False, None, False),
            ("actor", "actor", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class MedicationDispenseSubstitution(BackboneElement):
    """ Whether a substitution was performed on the dispense.

    Indicates whether or not substitution was made as part of the dispense.  In
    some cases, substitution will be expected but does not happen, in other
    cases substitution is not expected but does happen.  This block explains
    what substitution did or did not happen and why.  If nothing is specified,
    substitution was not done.
    """
    resource_type: ClassVar[str] = "MedicationDispenseSubstitution"
    wasSubstituted: bool = None
    type: Optional[CodeableConcept] = None
    reason: Optional[List[CodeableConcept]] = empty_list()
    responsibleParty: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(MedicationDispenseSubstitution, self).elementProperties()
        js.extend([
            ("wasSubstituted", "wasSubstituted", bool, False, None, True),
            ("type", "type", CodeableConcept, False, None, False),
            ("reason", "reason", CodeableConcept, True, None, False),
            ("responsibleParty", "responsibleParty", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class MedicationDispense(DomainResource):
    """ Dispensing a medication to a named patient.

    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """
    resource_type: ClassVar[str] = "MedicationDispense"
    identifier: Optional[List[Identifier]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    statusReasonCodeableConcept: Optional[CodeableConcept] = None
    statusReasonReference: Optional[FHIRReference] = None
    category: Optional[List[CodeableConcept]] = empty_list()
    medicationCodeableConcept: CodeableConcept = None
    medicationReference: FHIRReference = None
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    supportingInformation: Optional[List[FHIRReference]] = empty_list()
    performer: Optional[List[MedicationDispensePerformer]] = empty_list()
    location: Optional[FHIRReference] = None
    authorizingPrescription: Optional[List[FHIRReference]] = empty_list()
    type: Optional[CodeableConcept] = None
    quantity: Optional[Quantity] = None
    daysSupply: Optional[Quantity] = None
    whenPrepared: Optional[FHIRDate] = None
    whenHandedOver: Optional[FHIRDate] = None
    destination: Optional[FHIRReference] = None
    receiver: Optional[List[FHIRReference]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    dosageInstruction: Optional[List[Dosage]] = empty_list()
    substitution: Optional[MedicationDispenseSubstitution] = None
    detectedIssue: Optional[List[FHIRReference]] = empty_list()
    eventHistory: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(MedicationDispense, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReasonCodeableConcept", "statusReasonCodeableConcept", CodeableConcept, False, "statusReason", False),
            ("statusReasonReference", "statusReasonReference", FHIRReference, False, "statusReason", False),
            ("category", "category", CodeableConcept, True, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", FHIRReference, False, "medication", True),
            ("subject", "subject", FHIRReference, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("supportingInformation", "supportingInformation", FHIRReference, True, None, False),
            ("performer", "performer", MedicationDispensePerformer, True, None, False),
            ("location", "location", FHIRReference, False, None, False),
            ("authorizingPrescription", "authorizingPrescription", FHIRReference, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("daysSupply", "daysSupply", Quantity, False, None, False),
            ("whenPrepared", "whenPrepared", FHIRDate, False, None, False),
            ("whenHandedOver", "whenHandedOver", FHIRDate, False, None, False),
            ("destination", "destination", FHIRReference, False, None, False),
            ("receiver", "receiver", FHIRReference, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("dosageInstruction", "dosageInstruction", Dosage, True, None, False),
            ("substitution", "substitution", MedicationDispenseSubstitution, False, None, False),
            ("detectedIssue", "detectedIssue", FHIRReference, True, None, False),
            ("eventHistory", "eventHistory", FHIRReference, True, None, False),
        ])
        return js