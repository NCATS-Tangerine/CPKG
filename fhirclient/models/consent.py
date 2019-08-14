#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Consent) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class ConsentProvisionActor(BackboneElement):
    """ Who|what controlled by this rule (or group, by role).

    Who or what is controlled by this rule. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """
    resource_type: ClassVar[str] = "ConsentProvisionActor"
    role: CodeableConcept = None
    reference: FHIRReference = None

    def elementProperties(self):
        js = super(ConsentProvisionActor, self).elementProperties()
        js.extend([
            ("role", "role", CodeableConcept, False, None, True),
            ("reference", "reference", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class ConsentProvisionData(BackboneElement):
    """ Data controlled by this rule.

    The resources controlled by this rule if specific resources are referenced.
    """
    resource_type: ClassVar[str] = "ConsentProvisionData"
    meaning: str = None
    reference: FHIRReference = None

    def elementProperties(self):
        js = super(ConsentProvisionData, self).elementProperties()
        js.extend([
            ("meaning", "meaning", str, False, None, True),
            ("reference", "reference", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class ConsentPolicy(BackboneElement):
    """ Policies covered by this consent.

    The references to the policies that are included in this consent scope.
    Policies may be organizational, but are often defined jurisdictionally, or
    in law.
    """
    resource_type: ClassVar[str] = "ConsentPolicy"
    authority: Optional[str] = None
    uri: Optional[str] = None

    def elementProperties(self):
        js = super(ConsentPolicy, self).elementProperties()
        js.extend([
            ("authority", "authority", str, False, None, False),
            ("uri", "uri", str, False, None, False),
        ])
        return js


@dataclass
class ConsentVerification(BackboneElement):
    """ Consent Verified by patient or family.

    Whether a treatment instruction (e.g. artificial respiration yes or no) was
    verified with the patient, his/her family or another authorized person.
    """
    resource_type: ClassVar[str] = "ConsentVerification"
    verified: bool = None
    verifiedWith: Optional[FHIRReference] = None
    verificationDate: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(ConsentVerification, self).elementProperties()
        js.extend([
            ("verified", "verified", bool, False, None, True),
            ("verifiedWith", "verifiedWith", FHIRReference, False, None, False),
            ("verificationDate", "verificationDate", FHIRDate, False, None, False),
        ])
        return js


@dataclass
class ConsentProvision(BackboneElement):
    """ Constraints to the base Consent.policyRule.

    An exception to the base policy of this consent. An exception can be an
    addition or removal of access permissions.
    """
    resource_type: ClassVar[str] = "ConsentProvision"
    type: Optional[str] = None
    period: Optional[Period] = None
    actor: Optional[List[ConsentProvisionActor]] = empty_list()
    action: Optional[List[CodeableConcept]] = empty_list()
    securityLabel: Optional[List[Coding]] = empty_list()
    purpose: Optional[List[Coding]] = empty_list()
    class_fhir: Optional[List[Coding]] = empty_list()
    code: Optional[List[CodeableConcept]] = empty_list()
    dataPeriod: Optional[Period] = None
    data: Optional[List[ConsentProvisionData]] = empty_list()
    provision: Optional[List["ConsentProvision"]] = empty_list()

    def elementProperties(self):
        js = super(ConsentProvision, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, False),
            ("period", "period", Period, False, None, False),
            ("actor", "actor", ConsentProvisionActor, True, None, False),
            ("action", "action", CodeableConcept, True, None, False),
            ("securityLabel", "securityLabel", Coding, True, None, False),
            ("purpose", "purpose", Coding, True, None, False),
            ("class_fhir", "class", Coding, True, None, False),
            ("code", "code", CodeableConcept, True, None, False),
            ("dataPeriod", "dataPeriod", Period, False, None, False),
            ("data", "data", ConsentProvisionData, True, None, False),
            ("provision", "provision", ConsentProvision, True, None, False),
        ])
        return js


@dataclass
class Consent(DomainResource):
    """ A healthcare consumer's  choices to permit or deny recipients or roles to
    perform actions for specific purposes and periods of time.

    A record of a healthcare consumer’s  choices, which permits or denies
    identified recipient(s) or recipient role(s) to perform one or more actions
    within a given policy context, for specific purposes and periods of time.
    """
    resource_type: ClassVar[str] = "Consent"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    scope: CodeableConcept = None
    category: List[CodeableConcept] = empty_list()
    patient: Optional[FHIRReference] = None
    dateTime: Optional[FHIRDate] = None
    performer: Optional[List[FHIRReference]] = empty_list()
    organization: Optional[List[FHIRReference]] = empty_list()
    sourceAttachment: Optional[Attachment] = None
    sourceReference: Optional[FHIRReference] = None
    policy: Optional[List[ConsentPolicy]] = empty_list()
    policyRule: Optional[CodeableConcept] = None
    verification: Optional[List[ConsentVerification]] = empty_list()
    provision: Optional[ConsentProvision] = None

    def elementProperties(self):
        js = super(Consent, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("scope", "scope", CodeableConcept, False, None, True),
            ("category", "category", CodeableConcept, True, None, True),
            ("patient", "patient", FHIRReference, False, None, False),
            ("dateTime", "dateTime", FHIRDate, False, None, False),
            ("performer", "performer", FHIRReference, True, None, False),
            ("organization", "organization", FHIRReference, True, None, False),
            ("sourceAttachment", "sourceAttachment", Attachment, False, "source", False),
            ("sourceReference", "sourceReference", FHIRReference, False, "source", False),
            ("policy", "policy", ConsentPolicy, True, None, False),
            ("policyRule", "policyRule", CodeableConcept, False, None, False),
            ("verification", "verification", ConsentVerification, True, None, False),
            ("provision", "provision", ConsentProvision, False, None, False),
        ])
        return js