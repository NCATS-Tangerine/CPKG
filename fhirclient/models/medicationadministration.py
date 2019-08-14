#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/MedicationAdministration) on 2019-08-06.
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
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class MedicationAdministrationPerformer(BackboneElement):
    """ Who performed the medication administration and what they did.

    Indicates who or what performed the medication administration and how they
    were involved.
    """
    resource_type: ClassVar[str] = "MedicationAdministrationPerformer"
    function: Optional[CodeableConcept] = None
    actor: FHIRReference = None

    def elementProperties(self):
        js = super(MedicationAdministrationPerformer, self).elementProperties()
        js.extend([
            ("function", "function", CodeableConcept, False, None, False),
            ("actor", "actor", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class MedicationAdministrationDosage(BackboneElement):
    """ Details of how medication was taken.

    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """
    resource_type: ClassVar[str] = "MedicationAdministrationDosage"
    text: Optional[str] = None
    site: Optional[CodeableConcept] = None
    route: Optional[CodeableConcept] = None
    method: Optional[CodeableConcept] = None
    dose: Optional[Quantity] = None
    rateRatio: Optional[Ratio] = None
    rateQuantity: Optional[Quantity] = None

    def elementProperties(self):
        js = super(MedicationAdministrationDosage, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("site", "site", CodeableConcept, False, None, False),
            ("route", "route", CodeableConcept, False, None, False),
            ("method", "method", CodeableConcept, False, None, False),
            ("dose", "dose", Quantity, False, None, False),
            ("rateRatio", "rateRatio", Ratio, False, "rate", False),
            ("rateQuantity", "rateQuantity", Quantity, False, "rate", False),
        ])
        return js


@dataclass
class MedicationAdministration(DomainResource):
    """ Administration of medication to a patient.

    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """
    resource_type: ClassVar[str] = "MedicationAdministration"
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    statusReason: Optional[List[CodeableConcept]] = empty_list()
    category: Optional[List[CodeableConcept]] = empty_list()
    medicationCodeableConcept: CodeableConcept = None
    medicationReference: FHIRReference = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    supportingInformation: Optional[List[FHIRReference]] = empty_list()
    occurenceDateTime: FHIRDate = None
    occurencePeriod: Period = None
    recorded: Optional[FHIRDate] = None
    performer: Optional[List[MedicationAdministrationPerformer]] = empty_list()
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    request: Optional[FHIRReference] = None
    device: Optional[List[FHIRReference]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    dosage: Optional[MedicationAdministrationDosage] = None
    eventHistory: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(MedicationAdministration, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", CodeableConcept, True, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", FHIRReference, False, "medication", True),
            ("subject", "subject", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("supportingInformation", "supportingInformation", FHIRReference, True, None, False),
            ("occurenceDateTime", "occurenceDateTime", FHIRDate, False, "occurence", True),
            ("occurencePeriod", "occurencePeriod", Period, False, "occurence", True),
            ("recorded", "recorded", FHIRDate, False, None, False),
            ("performer", "performer", MedicationAdministrationPerformer, True, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("request", "request", FHIRReference, False, None, False),
            ("device", "device", FHIRReference, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("dosage", "dosage", MedicationAdministrationDosage, False, None, False),
            ("eventHistory", "eventHistory", FHIRReference, True, None, False),
        ])
        return js