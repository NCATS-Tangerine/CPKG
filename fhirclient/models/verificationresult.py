#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/VerificationResult) on 2019-08-06.
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
from .signature import Signature
from .timing import Timing


@dataclass
class VerificationResultPrimarySource(BackboneElement):
    """ Information about the primary source(s) involved in validation.
    """
    resource_type: ClassVar[str] = "VerificationResultPrimarySource"
    who: Optional[FHIRReference] = None
    type: Optional[List[CodeableConcept]] = empty_list()
    communicationMethod: Optional[List[CodeableConcept]] = empty_list()
    validationStatus: Optional[CodeableConcept] = None
    validationDate: Optional[FHIRDate] = None
    canPushUpdates: Optional[CodeableConcept] = None
    pushTypeAvailable: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(VerificationResultPrimarySource, self).elementProperties()
        js.extend([
            ("who", "who", FHIRReference, False, None, False),
            ("type", "type", CodeableConcept, True, None, False),
            ("communicationMethod", "communicationMethod", CodeableConcept, True, None, False),
            ("validationStatus", "validationStatus", CodeableConcept, False, None, False),
            ("validationDate", "validationDate", FHIRDate, False, None, False),
            ("canPushUpdates", "canPushUpdates", CodeableConcept, False, None, False),
            ("pushTypeAvailable", "pushTypeAvailable", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class VerificationResultAttestation(BackboneElement):
    """ Information about the entity attesting to information.
    """
    resource_type: ClassVar[str] = "VerificationResultAttestation"
    who: Optional[FHIRReference] = None
    onBehalfOf: Optional[FHIRReference] = None
    communicationMethod: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    sourceIdentityCertificate: Optional[str] = None
    proxyIdentityCertificate: Optional[str] = None
    proxySignature: Optional[Signature] = None
    sourceSignature: Optional[Signature] = None

    def elementProperties(self):
        js = super(VerificationResultAttestation, self).elementProperties()
        js.extend([
            ("who", "who", FHIRReference, False, None, False),
            ("onBehalfOf", "onBehalfOf", FHIRReference, False, None, False),
            ("communicationMethod", "communicationMethod", CodeableConcept, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("sourceIdentityCertificate", "sourceIdentityCertificate", str, False, None, False),
            ("proxyIdentityCertificate", "proxyIdentityCertificate", str, False, None, False),
            ("proxySignature", "proxySignature", Signature, False, None, False),
            ("sourceSignature", "sourceSignature", Signature, False, None, False),
        ])
        return js


@dataclass
class VerificationResultValidator(BackboneElement):
    """ Information about the entity validating information.
    """
    resource_type: ClassVar[str] = "VerificationResultValidator"
    organization: FHIRReference = None
    identityCertificate: Optional[str] = None
    attestationSignature: Optional[Signature] = None

    def elementProperties(self):
        js = super(VerificationResultValidator, self).elementProperties()
        js.extend([
            ("organization", "organization", FHIRReference, False, None, True),
            ("identityCertificate", "identityCertificate", str, False, None, False),
            ("attestationSignature", "attestationSignature", Signature, False, None, False),
        ])
        return js


@dataclass
class VerificationResult(DomainResource):
    """ Describes validation requirements, source(s), status and dates for one or
    more elements.
    """
    resource_type: ClassVar[str] = "VerificationResult"
    target: Optional[List[FHIRReference]] = empty_list()
    targetLocation: Optional[List[str]] = empty_list()
    need: Optional[CodeableConcept] = None
    status: str = None
    statusDate: Optional[FHIRDate] = None
    validationType: Optional[CodeableConcept] = None
    validationProcess: Optional[List[CodeableConcept]] = empty_list()
    frequency: Optional[Timing] = None
    lastPerformed: Optional[FHIRDate] = None
    nextScheduled: Optional[FHIRDate] = None
    failureAction: Optional[CodeableConcept] = None
    primarySource: Optional[List[VerificationResultPrimarySource]] = empty_list()
    attestation: Optional[VerificationResultAttestation] = None
    validator: Optional[List[VerificationResultValidator]] = empty_list()

    def elementProperties(self):
        js = super(VerificationResult, self).elementProperties()
        js.extend([
            ("target", "target", FHIRReference, True, None, False),
            ("targetLocation", "targetLocation", str, True, None, False),
            ("need", "need", CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusDate", "statusDate", FHIRDate, False, None, False),
            ("validationType", "validationType", CodeableConcept, False, None, False),
            ("validationProcess", "validationProcess", CodeableConcept, True, None, False),
            ("frequency", "frequency", Timing, False, None, False),
            ("lastPerformed", "lastPerformed", FHIRDate, False, None, False),
            ("nextScheduled", "nextScheduled", FHIRDate, False, None, False),
            ("failureAction", "failureAction", CodeableConcept, False, None, False),
            ("primarySource", "primarySource", VerificationResultPrimarySource, True, None, False),
            ("attestation", "attestation", VerificationResultAttestation, False, None, False),
            ("validator", "validator", VerificationResultValidator, True, None, False),
        ])
        return js