#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Claim) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period
from .quantity import Quantity


@dataclass
class ClaimItemDetailSubDetail(BackboneElement):
    """ Product or service provided.

    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """
    resource_type: ClassVar[str] = "ClaimItemDetailSubDetail"
    sequence: int = None
    revenue: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    productOrService: CodeableConcept = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    programCode: Optional[List[CodeableConcept]] = empty_list()
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    udi: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(ClaimItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("revenue", "revenue", CodeableConcept, False, None, False),
            ("category", "category", CodeableConcept, False, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("programCode", "programCode", CodeableConcept, True, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("net", "net", Money, False, None, False),
            ("udi", "udi", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class ClaimItemDetail(BackboneElement):
    """ Product or service provided.

    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """
    resource_type: ClassVar[str] = "ClaimItemDetail"
    sequence: int = None
    revenue: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    productOrService: CodeableConcept = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    programCode: Optional[List[CodeableConcept]] = empty_list()
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    udi: Optional[List[FHIRReference]] = empty_list()
    subDetail: Optional[List[ClaimItemDetailSubDetail]] = empty_list()

    def elementProperties(self):
        js = super(ClaimItemDetail, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("revenue", "revenue", CodeableConcept, False, None, False),
            ("category", "category", CodeableConcept, False, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("programCode", "programCode", CodeableConcept, True, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("net", "net", Money, False, None, False),
            ("udi", "udi", FHIRReference, True, None, False),
            ("subDetail", "subDetail", ClaimItemDetailSubDetail, True, None, False),
        ])
        return js


@dataclass
class ClaimRelated(BackboneElement):
    """ Prior or corollary claims.

    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """
    resource_type: ClassVar[str] = "ClaimRelated"
    claim: Optional[FHIRReference] = None
    relationship: Optional[CodeableConcept] = None
    reference: Optional[Identifier] = None

    def elementProperties(self):
        js = super(ClaimRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", FHIRReference, False, None, False),
            ("relationship", "relationship", CodeableConcept, False, None, False),
            ("reference", "reference", Identifier, False, None, False),
        ])
        return js


@dataclass
class ClaimPayee(BackboneElement):
    """ Recipient of benefits payable.

    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """
    resource_type: ClassVar[str] = "ClaimPayee"
    type: CodeableConcept = None
    party: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(ClaimPayee, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("party", "party", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class ClaimCareTeam(BackboneElement):
    """ Members of the care team.

    The members of the team who provided the products and services.
    """
    resource_type: ClassVar[str] = "ClaimCareTeam"
    sequence: int = None
    provider: FHIRReference = None
    responsible: Optional[bool] = None
    role: Optional[CodeableConcept] = None
    qualification: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ClaimCareTeam, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("provider", "provider", FHIRReference, False, None, True),
            ("responsible", "responsible", bool, False, None, False),
            ("role", "role", CodeableConcept, False, None, False),
            ("qualification", "qualification", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ClaimSupportingInfo(BackboneElement):
    """ Supporting information.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    resource_type: ClassVar[str] = "ClaimSupportingInfo"
    sequence: int = None
    category: CodeableConcept = None
    code: Optional[CodeableConcept] = None
    timingDate: Optional[FHIRDate] = None
    timingPeriod: Optional[Period] = None
    valueBoolean: Optional[bool] = None
    valueString: Optional[str] = None
    valueQuantity: Optional[Quantity] = None
    valueAttachment: Optional[Attachment] = None
    valueReference: Optional[FHIRReference] = None
    reason: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ClaimSupportingInfo, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("category", "category", CodeableConcept, False, None, True),
            ("code", "code", CodeableConcept, False, None, False),
            ("timingDate", "timingDate", FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", Period, False, "timing", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
            ("valueAttachment", "valueAttachment", Attachment, False, "value", False),
            ("valueReference", "valueReference", FHIRReference, False, "value", False),
            ("reason", "reason", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ClaimDiagnosis(BackboneElement):
    """ Pertinent diagnosis information.

    Information about diagnoses relevant to the claim items.
    """
    resource_type: ClassVar[str] = "ClaimDiagnosis"
    sequence: int = None
    diagnosisCodeableConcept: CodeableConcept = None
    diagnosisReference: FHIRReference = None
    type: Optional[List[CodeableConcept]] = empty_list()
    onAdmission: Optional[CodeableConcept] = None
    packageCode: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ClaimDiagnosis, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", CodeableConcept, False, "diagnosis", True),
            ("diagnosisReference", "diagnosisReference", FHIRReference, False, "diagnosis", True),
            ("type", "type", CodeableConcept, True, None, False),
            ("onAdmission", "onAdmission", CodeableConcept, False, None, False),
            ("packageCode", "packageCode", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ClaimProcedure(BackboneElement):
    """ Clinical procedures performed.

    Procedures performed on the patient relevant to the billing items with the
    claim.
    """
    resource_type: ClassVar[str] = "ClaimProcedure"
    sequence: int = None
    type: Optional[List[CodeableConcept]] = empty_list()
    date: Optional[FHIRDate] = None
    procedureCodeableConcept: CodeableConcept = None
    procedureReference: FHIRReference = None
    udi: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(ClaimProcedure, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", CodeableConcept, True, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("procedureCodeableConcept", "procedureCodeableConcept", CodeableConcept, False, "procedure", True),
            ("procedureReference", "procedureReference", FHIRReference, False, "procedure", True),
            ("udi", "udi", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class ClaimInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    resource_type: ClassVar[str] = "ClaimInsurance"
    sequence: int = None
    focal: bool = None
    identifier: Optional[Identifier] = None
    coverage: FHIRReference = None
    businessArrangement: Optional[str] = None
    preAuthRef: Optional[List[str]] = empty_list()
    claimResponse: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(ClaimInsurance, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("identifier", "identifier", Identifier, False, None, False),
            ("coverage", "coverage", FHIRReference, False, None, True),
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("claimResponse", "claimResponse", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class ClaimAccident(BackboneElement):
    """ Details of the event.

    Details of an accident which resulted in injuries which required the
    products and services listed in the claim.
    """
    resource_type: ClassVar[str] = "ClaimAccident"
    date: FHIRDate = None
    type: Optional[CodeableConcept] = None
    locationAddress: Optional[Address] = None
    locationReference: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(ClaimAccident, self).elementProperties()
        js.extend([
            ("date", "date", FHIRDate, False, None, True),
            ("type", "type", CodeableConcept, False, None, False),
            ("locationAddress", "locationAddress", Address, False, "location", False),
            ("locationReference", "locationReference", FHIRReference, False, "location", False),
        ])
        return js


@dataclass
class ClaimItem(BackboneElement):
    """ Product or service provided.

    A claim line. Either a simple  product or service or a 'group' of details
    which can each be a simple items or groups of sub-details.
    """
    resource_type: ClassVar[str] = "ClaimItem"
    sequence: int = None
    careTeamSequence: Optional[List[int]] = empty_list()
    diagnosisSequence: Optional[List[int]] = empty_list()
    procedureSequence: Optional[List[int]] = empty_list()
    informationSequence: Optional[List[int]] = empty_list()
    revenue: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    productOrService: CodeableConcept = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    programCode: Optional[List[CodeableConcept]] = empty_list()
    servicedDate: Optional[FHIRDate] = None
    servicedPeriod: Optional[Period] = None
    locationCodeableConcept: Optional[CodeableConcept] = None
    locationAddress: Optional[Address] = None
    locationReference: Optional[FHIRReference] = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    udi: Optional[List[FHIRReference]] = empty_list()
    bodySite: Optional[CodeableConcept] = None
    subSite: Optional[List[CodeableConcept]] = empty_list()
    encounter: Optional[List[FHIRReference]] = empty_list()
    detail: Optional[List[ClaimItemDetail]] = empty_list()

    def elementProperties(self):
        js = super(ClaimItem, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("careTeamSequence", "careTeamSequence", int, True, None, False),
            ("diagnosisSequence", "diagnosisSequence", int, True, None, False),
            ("procedureSequence", "procedureSequence", int, True, None, False),
            ("informationSequence", "informationSequence", int, True, None, False),
            ("revenue", "revenue", CodeableConcept, False, None, False),
            ("category", "category", CodeableConcept, False, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("programCode", "programCode", CodeableConcept, True, None, False),
            ("servicedDate", "servicedDate", FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", Period, False, "serviced", False),
            ("locationCodeableConcept", "locationCodeableConcept", CodeableConcept, False, "location", False),
            ("locationAddress", "locationAddress", Address, False, "location", False),
            ("locationReference", "locationReference", FHIRReference, False, "location", False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("net", "net", Money, False, None, False),
            ("udi", "udi", FHIRReference, True, None, False),
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("subSite", "subSite", CodeableConcept, True, None, False),
            ("encounter", "encounter", FHIRReference, True, None, False),
            ("detail", "detail", ClaimItemDetail, True, None, False),
        ])
        return js


@dataclass
class Claim(DomainResource):
    """ Claim, Pre-determination or Pre-authorization.

    A provider issued list of professional services and products which have
    been provided, or are to be provided, to a patient which is sent to an
    insurer for reimbursement.
    """
    resource_type: ClassVar[str] = "Claim"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    type: CodeableConcept = None
    subType: Optional[CodeableConcept] = None
    use: str = None
    patient: FHIRReference = None
    billablePeriod: Optional[Period] = None
    created: FHIRDate = None
    enterer: Optional[FHIRReference] = None
    insurer: Optional[FHIRReference] = None
    provider: FHIRReference = None
    priority: CodeableConcept = None
    fundsReserve: Optional[CodeableConcept] = None
    related: Optional[List[ClaimRelated]] = empty_list()
    prescription: Optional[FHIRReference] = None
    originalPrescription: Optional[FHIRReference] = None
    payee: Optional[ClaimPayee] = None
    referral: Optional[FHIRReference] = None
    facility: Optional[FHIRReference] = None
    careTeam: Optional[List[ClaimCareTeam]] = empty_list()
    supportingInfo: Optional[List[ClaimSupportingInfo]] = empty_list()
    diagnosis: Optional[List[ClaimDiagnosis]] = empty_list()
    procedure: Optional[List[ClaimProcedure]] = empty_list()
    insurance: List[ClaimInsurance] = empty_list()
    accident: Optional[ClaimAccident] = None
    item: Optional[List[ClaimItem]] = empty_list()
    total: Optional[Money] = None

    def elementProperties(self):
        js = super(Claim, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", CodeableConcept, False, None, True),
            ("subType", "subType", CodeableConcept, False, None, False),
            ("use", "use", str, False, None, True),
            ("patient", "patient", FHIRReference, False, None, True),
            ("billablePeriod", "billablePeriod", Period, False, None, False),
            ("created", "created", FHIRDate, False, None, True),
            ("enterer", "enterer", FHIRReference, False, None, False),
            ("insurer", "insurer", FHIRReference, False, None, False),
            ("provider", "provider", FHIRReference, False, None, True),
            ("priority", "priority", CodeableConcept, False, None, True),
            ("fundsReserve", "fundsReserve", CodeableConcept, False, None, False),
            ("related", "related", ClaimRelated, True, None, False),
            ("prescription", "prescription", FHIRReference, False, None, False),
            ("originalPrescription", "originalPrescription", FHIRReference, False, None, False),
            ("payee", "payee", ClaimPayee, False, None, False),
            ("referral", "referral", FHIRReference, False, None, False),
            ("facility", "facility", FHIRReference, False, None, False),
            ("careTeam", "careTeam", ClaimCareTeam, True, None, False),
            ("supportingInfo", "supportingInfo", ClaimSupportingInfo, True, None, False),
            ("diagnosis", "diagnosis", ClaimDiagnosis, True, None, False),
            ("procedure", "procedure", ClaimProcedure, True, None, False),
            ("insurance", "insurance", ClaimInsurance, True, None, True),
            ("accident", "accident", ClaimAccident, False, None, False),
            ("item", "item", ClaimItem, True, None, False),
            ("total", "total", Money, False, None, False),
        ])
        return js