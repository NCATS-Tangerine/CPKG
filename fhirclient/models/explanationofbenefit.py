#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period
from .quantity import Quantity


@dataclass
class ExplanationOfBenefitBenefitBalanceFinancial(BackboneElement):
    """ Benefit Summary.

    Benefits Used to date.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitBenefitBalanceFinancial"
    type: CodeableConcept = None
    allowedUnsignedInt: Optional[int] = None
    allowedString: Optional[str] = None
    allowedMoney: Optional[Money] = None
    usedUnsignedInt: Optional[int] = None
    usedMoney: Optional[Money] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalanceFinancial, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("allowedUnsignedInt", "allowedUnsignedInt", int, False, "allowed", False),
            ("allowedString", "allowedString", str, False, "allowed", False),
            ("allowedMoney", "allowedMoney", Money, False, "allowed", False),
            ("usedUnsignedInt", "usedUnsignedInt", int, False, "used", False),
            ("usedMoney", "usedMoney", Money, False, "used", False),
        ])
        return js


@dataclass
class ExplanationOfBenefitAddItemDetailSubDetail(BackboneElement):
    """ Insurer added line items.

    The third-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAddItemDetailSubDetail"
    productOrService: CodeableConcept = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    adjudication: Optional[List["ExplanationOfBenefitItemAdjudication"]] = empty_list()

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("net", "net", Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitAddItemDetail(BackboneElement):
    """ Insurer added line items.

    The second-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAddItemDetail"
    productOrService: CodeableConcept = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    adjudication: Optional[List["ExplanationOfBenefitItemAdjudication"]] = empty_list()
    subDetail: Optional[List[ExplanationOfBenefitAddItemDetailSubDetail]] = empty_list()

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetail, self).elementProperties()
        js.extend([
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("net", "net", Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("subDetail", "subDetail", ExplanationOfBenefitAddItemDetailSubDetail, True, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitItemDetailSubDetail(BackboneElement):
    """ Additional items.

    Third-tier of goods and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemDetailSubDetail"
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
    noteNumber: Optional[List[int]] = empty_list()
    adjudication: Optional[List["ExplanationOfBenefitItemAdjudication"]] = empty_list()

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetailSubDetail, self).elementProperties()
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
            ("noteNumber", "noteNumber", int, True, None, False),
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitItemAdjudication(BackboneElement):
    """ Adjudication details.

    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemAdjudication"
    category: CodeableConcept = None
    reason: Optional[CodeableConcept] = None
    amount: Optional[Money] = None
    value: Optional[float] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemAdjudication, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, True),
            ("reason", "reason", CodeableConcept, False, None, False),
            ("amount", "amount", Money, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitItemDetail(BackboneElement):
    """ Additional items.

    Second-tier of goods and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemDetail"
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
    noteNumber: Optional[List[int]] = empty_list()
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    subDetail: Optional[List[ExplanationOfBenefitItemDetailSubDetail]] = empty_list()

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetail, self).elementProperties()
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
            ("noteNumber", "noteNumber", int, True, None, False),
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("subDetail", "subDetail", ExplanationOfBenefitItemDetailSubDetail, True, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitRelated(BackboneElement):
    """ Prior or corollary claims.

    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitRelated"
    claim: Optional[FHIRReference] = None
    relationship: Optional[CodeableConcept] = None
    reference: Optional[Identifier] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", FHIRReference, False, None, False),
            ("relationship", "relationship", CodeableConcept, False, None, False),
            ("reference", "reference", Identifier, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitPayee(BackboneElement):
    """ Recipient of benefits payable.

    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitPayee"
    type: Optional[CodeableConcept] = None
    party: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitPayee, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("party", "party", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitCareTeam(BackboneElement):
    """ Care Team members.

    The members of the team who provided the products and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitCareTeam"
    sequence: int = None
    provider: FHIRReference = None
    responsible: Optional[bool] = None
    role: Optional[CodeableConcept] = None
    qualification: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitCareTeam, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("provider", "provider", FHIRReference, False, None, True),
            ("responsible", "responsible", bool, False, None, False),
            ("role", "role", CodeableConcept, False, None, False),
            ("qualification", "qualification", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitSupportingInfo(BackboneElement):
    """ Supporting information.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitSupportingInfo"
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
    reason: Optional[Coding] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitSupportingInfo, self).elementProperties()
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
            ("reason", "reason", Coding, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitDiagnosis(BackboneElement):
    """ Pertinent diagnosis information.

    Information about diagnoses relevant to the claim items.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitDiagnosis"
    sequence: int = None
    diagnosisCodeableConcept: CodeableConcept = None
    diagnosisReference: FHIRReference = None
    type: Optional[List[CodeableConcept]] = empty_list()
    onAdmission: Optional[CodeableConcept] = None
    packageCode: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitDiagnosis, self).elementProperties()
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
class ExplanationOfBenefitProcedure(BackboneElement):
    """ Clinical procedures performed.

    Procedures performed on the patient relevant to the billing items with the
    claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitProcedure"
    sequence: int = None
    type: Optional[List[CodeableConcept]] = empty_list()
    date: Optional[FHIRDate] = None
    procedureCodeableConcept: CodeableConcept = None
    procedureReference: FHIRReference = None
    udi: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(ExplanationOfBenefitProcedure, self).elementProperties()
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
class ExplanationOfBenefitInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitInsurance"
    focal: bool = None
    coverage: FHIRReference = None
    preAuthRef: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(ExplanationOfBenefitInsurance, self).elementProperties()
        js.extend([
            ("focal", "focal", bool, False, None, True),
            ("coverage", "coverage", FHIRReference, False, None, True),
            ("preAuthRef", "preAuthRef", str, True, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitAccident(BackboneElement):
    """ Details of the event.

    Details of a accident which resulted in injuries which required the
    products and services listed in the claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAccident"
    date: Optional[FHIRDate] = None
    type: Optional[CodeableConcept] = None
    locationAddress: Optional[Address] = None
    locationReference: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitAccident, self).elementProperties()
        js.extend([
            ("date", "date", FHIRDate, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("locationAddress", "locationAddress", Address, False, "location", False),
            ("locationReference", "locationReference", FHIRReference, False, "location", False),
        ])
        return js


@dataclass
class ExplanationOfBenefitItem(BackboneElement):
    """ Product or service provided.

    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItem"
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
    noteNumber: Optional[List[int]] = empty_list()
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    detail: Optional[List[ExplanationOfBenefitItemDetail]] = empty_list()

    def elementProperties(self):
        js = super(ExplanationOfBenefitItem, self).elementProperties()
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
            ("noteNumber", "noteNumber", int, True, None, False),
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("detail", "detail", ExplanationOfBenefitItemDetail, True, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitAddItem(BackboneElement):
    """ Insurer added line items.

    The first-tier service adjudications for payor added product or service
    lines.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAddItem"
    itemSequence: Optional[List[int]] = empty_list()
    detailSequence: Optional[List[int]] = empty_list()
    subDetailSequence: Optional[List[int]] = empty_list()
    provider: Optional[List[FHIRReference]] = empty_list()
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
    bodySite: Optional[CodeableConcept] = None
    subSite: Optional[List[CodeableConcept]] = empty_list()
    noteNumber: Optional[List[int]] = empty_list()
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    detail: Optional[List[ExplanationOfBenefitAddItemDetail]] = empty_list()

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItem, self).elementProperties()
        js.extend([
            ("itemSequence", "itemSequence", int, True, None, False),
            ("detailSequence", "detailSequence", int, True, None, False),
            ("subDetailSequence", "subDetailSequence", int, True, None, False),
            ("provider", "provider", FHIRReference, True, None, False),
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
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("subSite", "subSite", CodeableConcept, True, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("detail", "detail", ExplanationOfBenefitAddItemDetail, True, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitTotal(BackboneElement):
    """ Adjudication totals.

    Categorized monetary totals for the adjudication.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitTotal"
    category: CodeableConcept = None
    amount: Money = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitTotal, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, True),
            ("amount", "amount", Money, False, None, True),
        ])
        return js


@dataclass
class ExplanationOfBenefitPayment(BackboneElement):
    """ Payment Details.

    Payment details for the adjudication of the claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitPayment"
    type: Optional[CodeableConcept] = None
    adjustment: Optional[Money] = None
    adjustmentReason: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    amount: Optional[Money] = None
    identifier: Optional[Identifier] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitPayment, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("adjustment", "adjustment", Money, False, None, False),
            ("adjustmentReason", "adjustmentReason", CodeableConcept, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("amount", "amount", Money, False, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitProcessNote(BackboneElement):
    """ Note concerning adjudication.

    A note that describes or explains adjudication results in a human readable
    form.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitProcessNote"
    number: Optional[int] = None
    type: Optional[str] = None
    text: Optional[str] = None
    language: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitProcessNote, self).elementProperties()
        js.extend([
            ("number", "number", int, False, None, False),
            ("type", "type", str, False, None, False),
            ("text", "text", str, False, None, False),
            ("language", "language", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitBenefitBalance(BackboneElement):
    """ Balance by Benefit Category.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitBenefitBalance"
    category: CodeableConcept = None
    excluded: Optional[bool] = None
    name: Optional[str] = None
    description: Optional[str] = None
    network: Optional[CodeableConcept] = None
    unit: Optional[CodeableConcept] = None
    term: Optional[CodeableConcept] = None
    financial: Optional[List[ExplanationOfBenefitBenefitBalanceFinancial]] = empty_list()

    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalance, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, True),
            ("excluded", "excluded", bool, False, None, False),
            ("name", "name", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("network", "network", CodeableConcept, False, None, False),
            ("unit", "unit", CodeableConcept, False, None, False),
            ("term", "term", CodeableConcept, False, None, False),
            ("financial", "financial", ExplanationOfBenefitBenefitBalanceFinancial, True, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefit(DomainResource):
    """ Explanation of Benefit resource.

    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefit"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    type: CodeableConcept = None
    subType: Optional[CodeableConcept] = None
    use: str = None
    patient: FHIRReference = None
    billablePeriod: Optional[Period] = None
    created: FHIRDate = None
    enterer: Optional[FHIRReference] = None
    insurer: FHIRReference = None
    provider: FHIRReference = None
    priority: Optional[CodeableConcept] = None
    fundsReserveRequested: Optional[CodeableConcept] = None
    fundsReserve: Optional[CodeableConcept] = None
    related: Optional[List[ExplanationOfBenefitRelated]] = empty_list()
    prescription: Optional[FHIRReference] = None
    originalPrescription: Optional[FHIRReference] = None
    payee: Optional[ExplanationOfBenefitPayee] = None
    referral: Optional[FHIRReference] = None
    facility: Optional[FHIRReference] = None
    claim: Optional[FHIRReference] = None
    claimResponse: Optional[FHIRReference] = None
    outcome: str = None
    disposition: Optional[str] = None
    preAuthRef: Optional[List[str]] = empty_list()
    preAuthRefPeriod: Optional[List[Period]] = empty_list()
    careTeam: Optional[List[ExplanationOfBenefitCareTeam]] = empty_list()
    supportingInfo: Optional[List[ExplanationOfBenefitSupportingInfo]] = empty_list()
    diagnosis: Optional[List[ExplanationOfBenefitDiagnosis]] = empty_list()
    procedure: Optional[List[ExplanationOfBenefitProcedure]] = empty_list()
    precedence: Optional[int] = None
    insurance: List[ExplanationOfBenefitInsurance] = empty_list()
    accident: Optional[ExplanationOfBenefitAccident] = None
    item: Optional[List[ExplanationOfBenefitItem]] = empty_list()
    addItem: Optional[List[ExplanationOfBenefitAddItem]] = empty_list()
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    total: Optional[List[ExplanationOfBenefitTotal]] = empty_list()
    payment: Optional[ExplanationOfBenefitPayment] = None
    formCode: Optional[CodeableConcept] = None
    form: Optional[Attachment] = None
    processNote: Optional[List[ExplanationOfBenefitProcessNote]] = empty_list()
    benefitPeriod: Optional[Period] = None
    benefitBalance: Optional[List[ExplanationOfBenefitBenefitBalance]] = empty_list()

    def elementProperties(self):
        js = super(ExplanationOfBenefit, self).elementProperties()
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
            ("insurer", "insurer", FHIRReference, False, None, True),
            ("provider", "provider", FHIRReference, False, None, True),
            ("priority", "priority", CodeableConcept, False, None, False),
            ("fundsReserveRequested", "fundsReserveRequested", CodeableConcept, False, None, False),
            ("fundsReserve", "fundsReserve", CodeableConcept, False, None, False),
            ("related", "related", ExplanationOfBenefitRelated, True, None, False),
            ("prescription", "prescription", FHIRReference, False, None, False),
            ("originalPrescription", "originalPrescription", FHIRReference, False, None, False),
            ("payee", "payee", ExplanationOfBenefitPayee, False, None, False),
            ("referral", "referral", FHIRReference, False, None, False),
            ("facility", "facility", FHIRReference, False, None, False),
            ("claim", "claim", FHIRReference, False, None, False),
            ("claimResponse", "claimResponse", FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, True),
            ("disposition", "disposition", str, False, None, False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("preAuthRefPeriod", "preAuthRefPeriod", Period, True, None, False),
            ("careTeam", "careTeam", ExplanationOfBenefitCareTeam, True, None, False),
            ("supportingInfo", "supportingInfo", ExplanationOfBenefitSupportingInfo, True, None, False),
            ("diagnosis", "diagnosis", ExplanationOfBenefitDiagnosis, True, None, False),
            ("procedure", "procedure", ExplanationOfBenefitProcedure, True, None, False),
            ("precedence", "precedence", int, False, None, False),
            ("insurance", "insurance", ExplanationOfBenefitInsurance, True, None, True),
            ("accident", "accident", ExplanationOfBenefitAccident, False, None, False),
            ("item", "item", ExplanationOfBenefitItem, True, None, False),
            ("addItem", "addItem", ExplanationOfBenefitAddItem, True, None, False),
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("total", "total", ExplanationOfBenefitTotal, True, None, False),
            ("payment", "payment", ExplanationOfBenefitPayment, False, None, False),
            ("formCode", "formCode", CodeableConcept, False, None, False),
            ("form", "form", Attachment, False, None, False),
            ("processNote", "processNote", ExplanationOfBenefitProcessNote, True, None, False),
            ("benefitPeriod", "benefitPeriod", Period, False, None, False),
            ("benefitBalance", "benefitBalance", ExplanationOfBenefitBenefitBalance, True, None, False),
        ])
        return js