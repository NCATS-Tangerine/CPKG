#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Encounter) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .duration import Duration
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class EncounterStatusHistory(BackboneElement):
    """ List of past encounter statuses.

    The status history permits the encounter resource to contain the status
    history without needing to read through the historical versions of the
    resource, or even have the server store them.
    """
    resource_type: ClassVar[str] = "EncounterStatusHistory"
    status: str = None
    period: Period = None

    def elementProperties(self):
        js = super(EncounterStatusHistory, self).elementProperties()
        js.extend([
            ("status", "status", str, False, None, True),
            ("period", "period", Period, False, None, True),
        ])
        return js


@dataclass
class EncounterClassHistory(BackboneElement):
    """ List of past encounter classes.

    The class history permits the tracking of the encounters transitions
    without needing to go  through the resource history.  This would be used
    for a case where an admission starts of as an emergency encounter, then
    transitions into an inpatient scenario. Doing this and not restarting a new
    encounter ensures that any lab/diagnostic results can more easily follow
    the patient and not require re-processing and not get lost or cancelled
    during a kind of discharge from emergency to inpatient.
    """
    resource_type: ClassVar[str] = "EncounterClassHistory"
    class_fhir: Coding = None
    period: Period = None

    def elementProperties(self):
        js = super(EncounterClassHistory, self).elementProperties()
        js.extend([
            ("class_fhir", "class", Coding, False, None, True),
            ("period", "period", Period, False, None, True),
        ])
        return js


@dataclass
class EncounterParticipant(BackboneElement):
    """ List of participants involved in the encounter.

    The list of people responsible for providing the service.
    """
    resource_type: ClassVar[str] = "EncounterParticipant"
    type: Optional[List[CodeableConcept]] = empty_list()
    period: Optional[Period] = None
    individual: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(EncounterParticipant, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, True, None, False),
            ("period", "period", Period, False, None, False),
            ("individual", "individual", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class EncounterDiagnosis(BackboneElement):
    """ The list of diagnosis relevant to this encounter.
    """
    resource_type: ClassVar[str] = "EncounterDiagnosis"
    condition: FHIRReference = None
    use: Optional[CodeableConcept] = None
    rank: Optional[int] = None

    def elementProperties(self):
        js = super(EncounterDiagnosis, self).elementProperties()
        js.extend([
            ("condition", "condition", FHIRReference, False, None, True),
            ("use", "use", CodeableConcept, False, None, False),
            ("rank", "rank", int, False, None, False),
        ])
        return js


@dataclass
class EncounterHospitalization(BackboneElement):
    """ Details about the admission to a healthcare service.
    """
    resource_type: ClassVar[str] = "EncounterHospitalization"
    preAdmissionIdentifier: Optional[Identifier] = None
    origin: Optional[FHIRReference] = None
    admitSource: Optional[CodeableConcept] = None
    reAdmission: Optional[CodeableConcept] = None
    dietPreference: Optional[List[CodeableConcept]] = empty_list()
    specialCourtesy: Optional[List[CodeableConcept]] = empty_list()
    specialArrangement: Optional[List[CodeableConcept]] = empty_list()
    destination: Optional[FHIRReference] = None
    dischargeDisposition: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(EncounterHospitalization, self).elementProperties()
        js.extend([
            ("preAdmissionIdentifier", "preAdmissionIdentifier", Identifier, False, None, False),
            ("origin", "origin", FHIRReference, False, None, False),
            ("admitSource", "admitSource", CodeableConcept, False, None, False),
            ("reAdmission", "reAdmission", CodeableConcept, False, None, False),
            ("dietPreference", "dietPreference", CodeableConcept, True, None, False),
            ("specialCourtesy", "specialCourtesy", CodeableConcept, True, None, False),
            ("specialArrangement", "specialArrangement", CodeableConcept, True, None, False),
            ("destination", "destination", FHIRReference, False, None, False),
            ("dischargeDisposition", "dischargeDisposition", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class EncounterLocation(BackboneElement):
    """ List of locations where the patient has been.

    List of locations where  the patient has been during this encounter.
    """
    resource_type: ClassVar[str] = "EncounterLocation"
    location: FHIRReference = None
    status: Optional[str] = None
    physicalType: Optional[CodeableConcept] = None
    period: Optional[Period] = None

    def elementProperties(self):
        js = super(EncounterLocation, self).elementProperties()
        js.extend([
            ("location", "location", FHIRReference, False, None, True),
            ("status", "status", str, False, None, False),
            ("physicalType", "physicalType", CodeableConcept, False, None, False),
            ("period", "period", Period, False, None, False),
        ])
        return js


@dataclass
class Encounter(DomainResource):
    """ An interaction during which services are provided to the patient.

    An interaction between a patient and healthcare provider(s) for the purpose
    of providing healthcare service(s) or assessing the health status of a
    patient.
    """
    resource_type: ClassVar[str] = "Encounter"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    statusHistory: Optional[List[EncounterStatusHistory]] = empty_list()
    class_fhir: Coding = None
    classHistory: Optional[List[EncounterClassHistory]] = empty_list()
    type: Optional[List[CodeableConcept]] = empty_list()
    serviceType: Optional[CodeableConcept] = None
    priority: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    subjectStatus: Optional[CodeableConcept] = None
    episodeOfCare: Optional[List[FHIRReference]] = empty_list()
    basedOn: Optional[List[FHIRReference]] = empty_list()
    participant: Optional[List[EncounterParticipant]] = empty_list()
    appointment: Optional[List[FHIRReference]] = empty_list()
    period: Optional[Period] = None
    length: Optional[Duration] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    diagnosis: Optional[List[EncounterDiagnosis]] = empty_list()
    account: Optional[List[FHIRReference]] = empty_list()
    hospitalization: Optional[EncounterHospitalization] = None
    location: Optional[List[EncounterLocation]] = empty_list()
    serviceProvider: Optional[FHIRReference] = None
    partOf: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(Encounter, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusHistory", "statusHistory", EncounterStatusHistory, True, None, False),
            ("class_fhir", "class", Coding, False, None, True),
            ("classHistory", "classHistory", EncounterClassHistory, True, None, False),
            ("type", "type", CodeableConcept, True, None, False),
            ("serviceType", "serviceType", CodeableConcept, False, None, False),
            ("priority", "priority", CodeableConcept, False, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("subjectStatus", "subjectStatus", CodeableConcept, False, None, False),
            ("episodeOfCare", "episodeOfCare", FHIRReference, True, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("participant", "participant", EncounterParticipant, True, None, False),
            ("appointment", "appointment", FHIRReference, True, None, False),
            ("period", "period", Period, False, None, False),
            ("length", "length", Duration, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("diagnosis", "diagnosis", EncounterDiagnosis, True, None, False),
            ("account", "account", FHIRReference, True, None, False),
            ("hospitalization", "hospitalization", EncounterHospitalization, False, None, False),
            ("location", "location", EncounterLocation, True, None, False),
            ("serviceProvider", "serviceProvider", FHIRReference, False, None, False),
            ("partOf", "partOf", FHIRReference, False, None, False),
        ])
        return js