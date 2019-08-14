#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Immunization) on 2019-08-06.
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
from .quantity import Quantity


@dataclass
class ImmunizationPerformer(BackboneElement):
    """ Who performed event.

    Indicates who performed the immunization event.
    """
    resource_type: ClassVar[str] = "ImmunizationPerformer"
    function: Optional[CodeableConcept] = None
    actor: FHIRReference = None

    def elementProperties(self):
        js = super(ImmunizationPerformer, self).elementProperties()
        js.extend([
            ("function", "function", CodeableConcept, False, None, False),
            ("actor", "actor", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class ImmunizationEducation(BackboneElement):
    """ Educational material presented to patient.

    Educational material presented to the patient (or guardian) at the time of
    vaccine administration.
    """
    resource_type: ClassVar[str] = "ImmunizationEducation"
    documentType: Optional[str] = None
    reference: Optional[str] = None
    publicationDate: Optional[FHIRDate] = None
    presentationDate: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(ImmunizationEducation, self).elementProperties()
        js.extend([
            ("documentType", "documentType", str, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("publicationDate", "publicationDate", FHIRDate, False, None, False),
            ("presentationDate", "presentationDate", FHIRDate, False, None, False),
        ])
        return js


@dataclass
class ImmunizationReaction(BackboneElement):
    """ Details of a reaction that follows immunization.

    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """
    resource_type: ClassVar[str] = "ImmunizationReaction"
    date: Optional[FHIRDate] = None
    detail: Optional[FHIRReference] = None
    reported: Optional[bool] = None

    def elementProperties(self):
        js = super(ImmunizationReaction, self).elementProperties()
        js.extend([
            ("date", "date", FHIRDate, False, None, False),
            ("detail", "detail", FHIRReference, False, None, False),
            ("reported", "reported", bool, False, None, False),
        ])
        return js


@dataclass
class ImmunizationProtocolApplied(BackboneElement):
    """ Protocol followed by the provider.

    The protocol (set of recommendations) being followed by the provider who
    administered the dose.
    """
    resource_type: ClassVar[str] = "ImmunizationProtocolApplied"
    series: Optional[str] = None
    authority: Optional[FHIRReference] = None
    targetDisease: Optional[List[CodeableConcept]] = empty_list()
    doseNumberPositiveInt: int = None
    doseNumberString: str = None
    seriesDosesPositiveInt: Optional[int] = None
    seriesDosesString: Optional[str] = None

    def elementProperties(self):
        js = super(ImmunizationProtocolApplied, self).elementProperties()
        js.extend([
            ("series", "series", str, False, None, False),
            ("authority", "authority", FHIRReference, False, None, False),
            ("targetDisease", "targetDisease", CodeableConcept, True, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", True),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", True),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
        ])
        return js


@dataclass
class Immunization(DomainResource):
    """ Immunization event information.

    Describes the event of a patient being administered a vaccine or a record
    of an immunization as reported by a patient, a clinician or another party.
    """
    resource_type: ClassVar[str] = "Immunization"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    vaccineCode: CodeableConcept = None
    patient: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    occurrenceDateTime: FHIRDate = None
    occurrenceString: str = None
    recorded: Optional[FHIRDate] = None
    primarySource: Optional[bool] = None
    informationSourceCodeableConcept: Optional[CodeableConcept] = None
    informationSourceReference: Optional[FHIRReference] = None
    location: Optional[FHIRReference] = None
    manufacturer: Optional[FHIRReference] = None
    lotNumber: Optional[str] = None
    expirationDate: Optional[FHIRDate] = None
    site: Optional[CodeableConcept] = None
    route: Optional[CodeableConcept] = None
    doseQuantity: Optional[Quantity] = None
    performer: Optional[List[ImmunizationPerformer]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    isSubpotent: Optional[bool] = None
    subpotentReason: Optional[List[CodeableConcept]] = empty_list()
    education: Optional[List[ImmunizationEducation]] = empty_list()
    programEligibility: Optional[List[CodeableConcept]] = empty_list()
    fundingSource: Optional[CodeableConcept] = None
    reaction: Optional[List[ImmunizationReaction]] = empty_list()
    protocolApplied: Optional[List[ImmunizationProtocolApplied]] = empty_list()

    def elementProperties(self):
        js = super(Immunization, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", CodeableConcept, False, None, False),
            ("vaccineCode", "vaccineCode", CodeableConcept, False, None, True),
            ("patient", "patient", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", True),
            ("occurrenceString", "occurrenceString", str, False, "occurrence", True),
            ("recorded", "recorded", FHIRDate, False, None, False),
            ("primarySource", "primarySource", bool, False, None, False),
            ("informationSourceCodeableConcept", "informationSourceCodeableConcept", CodeableConcept, False, "informationSource", False),
            ("informationSourceReference", "informationSourceReference", FHIRReference, False, "informationSource", False),
            ("location", "location", FHIRReference, False, None, False),
            ("manufacturer", "manufacturer", FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("expirationDate", "expirationDate", FHIRDate, False, None, False),
            ("site", "site", CodeableConcept, False, None, False),
            ("route", "route", CodeableConcept, False, None, False),
            ("doseQuantity", "doseQuantity", Quantity, False, None, False),
            ("performer", "performer", ImmunizationPerformer, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("isSubpotent", "isSubpotent", bool, False, None, False),
            ("subpotentReason", "subpotentReason", CodeableConcept, True, None, False),
            ("education", "education", ImmunizationEducation, True, None, False),
            ("programEligibility", "programEligibility", CodeableConcept, True, None, False),
            ("fundingSource", "fundingSource", CodeableConcept, False, None, False),
            ("reaction", "reaction", ImmunizationReaction, True, None, False),
            ("protocolApplied", "protocolApplied", ImmunizationProtocolApplied, True, None, False),
        ])
        return js