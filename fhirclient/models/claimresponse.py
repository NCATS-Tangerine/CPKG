#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ClaimResponse) on 2019-08-06.
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
class ClaimResponseAddItemDetailSubDetail(BackboneElement):
    """ Insurer added line items.

    The third-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ClaimResponseAddItemDetailSubDetail"
    productOrService: CodeableConcept = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    adjudication: List["ClaimResponseItemAdjudication"] = empty_list()

    def elementProperties(self):
        js = super(ClaimResponseAddItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("net", "net", Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
        ])
        return js


@dataclass
class ClaimResponseAddItemDetail(BackboneElement):
    """ Insurer added line details.

    The second-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ClaimResponseAddItemDetail"
    productOrService: CodeableConcept = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    adjudication: List["ClaimResponseItemAdjudication"] = empty_list()
    subDetail: Optional[List[ClaimResponseAddItemDetailSubDetail]] = empty_list()

    def elementProperties(self):
        js = super(ClaimResponseAddItemDetail, self).elementProperties()
        js.extend([
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("net", "net", Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("subDetail", "subDetail", ClaimResponseAddItemDetailSubDetail, True, None, False),
        ])
        return js


@dataclass
class ClaimResponseItemDetailSubDetail(BackboneElement):
    """ Adjudication for claim sub-details.

    A sub-detail adjudication of a simple product or service.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemDetailSubDetail"
    subDetailSequence: int = None
    noteNumber: Optional[List[int]] = empty_list()
    adjudication: Optional[List["ClaimResponseItemAdjudication"]] = empty_list()

    def elementProperties(self):
        js = super(ClaimResponseItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("subDetailSequence", "subDetailSequence", int, False, None, True),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
        ])
        return js


@dataclass
class ClaimResponseItemAdjudication(BackboneElement):
    """ Adjudication details.

    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemAdjudication"
    category: CodeableConcept = None
    reason: Optional[CodeableConcept] = None
    amount: Optional[Money] = None
    value: Optional[float] = None

    def elementProperties(self):
        js = super(ClaimResponseItemAdjudication, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, True),
            ("reason", "reason", CodeableConcept, False, None, False),
            ("amount", "amount", Money, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


@dataclass
class ClaimResponseItemDetail(BackboneElement):
    """ Adjudication for claim details.

    A claim detail. Either a simple (a product or service) or a 'group' of sub-
    details which are simple items.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemDetail"
    detailSequence: int = None
    noteNumber: Optional[List[int]] = empty_list()
    adjudication: List[ClaimResponseItemAdjudication] = empty_list()
    subDetail: Optional[List[ClaimResponseItemDetailSubDetail]] = empty_list()

    def elementProperties(self):
        js = super(ClaimResponseItemDetail, self).elementProperties()
        js.extend([
            ("detailSequence", "detailSequence", int, False, None, True),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("subDetail", "subDetail", ClaimResponseItemDetailSubDetail, True, None, False),
        ])
        return js


@dataclass
class ClaimResponseItem(BackboneElement):
    """ Adjudication for claim line items.

    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """
    resource_type: ClassVar[str] = "ClaimResponseItem"
    itemSequence: int = None
    noteNumber: Optional[List[int]] = empty_list()
    adjudication: List[ClaimResponseItemAdjudication] = empty_list()
    detail: Optional[List[ClaimResponseItemDetail]] = empty_list()

    def elementProperties(self):
        js = super(ClaimResponseItem, self).elementProperties()
        js.extend([
            ("itemSequence", "itemSequence", int, False, None, True),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("detail", "detail", ClaimResponseItemDetail, True, None, False),
        ])
        return js


@dataclass
class ClaimResponseAddItem(BackboneElement):
    """ Insurer added line items.

    The first-tier service adjudications for payor added product or service
    lines.
    """
    resource_type: ClassVar[str] = "ClaimResponseAddItem"
    itemSequence: Optional[List[int]] = empty_list()
    detailSequence: Optional[List[int]] = empty_list()
    subdetailSequence: Optional[List[int]] = empty_list()
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
    adjudication: List[ClaimResponseItemAdjudication] = empty_list()
    detail: Optional[List[ClaimResponseAddItemDetail]] = empty_list()

    def elementProperties(self):
        js = super(ClaimResponseAddItem, self).elementProperties()
        js.extend([
            ("itemSequence", "itemSequence", int, True, None, False),
            ("detailSequence", "detailSequence", int, True, None, False),
            ("subdetailSequence", "subdetailSequence", int, True, None, False),
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
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("detail", "detail", ClaimResponseAddItemDetail, True, None, False),
        ])
        return js


@dataclass
class ClaimResponseTotal(BackboneElement):
    """ Adjudication totals.

    Categorized monetary totals for the adjudication.
    """
    resource_type: ClassVar[str] = "ClaimResponseTotal"
    category: CodeableConcept = None
    amount: Money = None

    def elementProperties(self):
        js = super(ClaimResponseTotal, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, True),
            ("amount", "amount", Money, False, None, True),
        ])
        return js


@dataclass
class ClaimResponsePayment(BackboneElement):
    """ Payment Details.

    Payment details for the adjudication of the claim.
    """
    resource_type: ClassVar[str] = "ClaimResponsePayment"
    type: CodeableConcept = None
    adjustment: Optional[Money] = None
    adjustmentReason: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    amount: Money = None
    identifier: Optional[Identifier] = None

    def elementProperties(self):
        js = super(ClaimResponsePayment, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("adjustment", "adjustment", Money, False, None, False),
            ("adjustmentReason", "adjustmentReason", CodeableConcept, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("amount", "amount", Money, False, None, True),
            ("identifier", "identifier", Identifier, False, None, False),
        ])
        return js


@dataclass
class ClaimResponseProcessNote(BackboneElement):
    """ Note concerning adjudication.

    A note that describes or explains adjudication results in a human readable
    form.
    """
    resource_type: ClassVar[str] = "ClaimResponseProcessNote"
    number: Optional[int] = None
    type: Optional[str] = None
    text: str = None
    language: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ClaimResponseProcessNote, self).elementProperties()
        js.extend([
            ("number", "number", int, False, None, False),
            ("type", "type", str, False, None, False),
            ("text", "text", str, False, None, True),
            ("language", "language", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ClaimResponseInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    resource_type: ClassVar[str] = "ClaimResponseInsurance"
    sequence: int = None
    focal: bool = None
    coverage: FHIRReference = None
    businessArrangement: Optional[str] = None
    claimResponse: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(ClaimResponseInsurance, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("coverage", "coverage", FHIRReference, False, None, True),
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("claimResponse", "claimResponse", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class ClaimResponseError(BackboneElement):
    """ Processing errors.

    Errors encountered during the processing of the adjudication.
    """
    resource_type: ClassVar[str] = "ClaimResponseError"
    itemSequence: Optional[int] = None
    detailSequence: Optional[int] = None
    subDetailSequence: Optional[int] = None
    code: CodeableConcept = None

    def elementProperties(self):
        js = super(ClaimResponseError, self).elementProperties()
        js.extend([
            ("itemSequence", "itemSequence", int, False, None, False),
            ("detailSequence", "detailSequence", int, False, None, False),
            ("subDetailSequence", "subDetailSequence", int, False, None, False),
            ("code", "code", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class ClaimResponse(DomainResource):
    """ Response to a claim predetermination or preauthorization.

    This resource provides the adjudication details from the processing of a
    Claim resource.
    """
    resource_type: ClassVar[str] = "ClaimResponse"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    type: CodeableConcept = None
    subType: Optional[CodeableConcept] = None
    use: str = None
    patient: FHIRReference = None
    created: FHIRDate = None
    insurer: FHIRReference = None
    requestor: Optional[FHIRReference] = None
    request: Optional[FHIRReference] = None
    outcome: str = None
    disposition: Optional[str] = None
    preAuthRef: Optional[str] = None
    preAuthPeriod: Optional[Period] = None
    payeeType: Optional[CodeableConcept] = None
    item: Optional[List[ClaimResponseItem]] = empty_list()
    addItem: Optional[List[ClaimResponseAddItem]] = empty_list()
    adjudication: Optional[List[ClaimResponseItemAdjudication]] = empty_list()
    total: Optional[List[ClaimResponseTotal]] = empty_list()
    payment: Optional[ClaimResponsePayment] = None
    fundsReserve: Optional[CodeableConcept] = None
    formCode: Optional[CodeableConcept] = None
    form: Optional[Attachment] = None
    processNote: Optional[List[ClaimResponseProcessNote]] = empty_list()
    communicationRequest: Optional[List[FHIRReference]] = empty_list()
    insurance: Optional[List[ClaimResponseInsurance]] = empty_list()
    error: Optional[List[ClaimResponseError]] = empty_list()

    def elementProperties(self):
        js = super(ClaimResponse, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", CodeableConcept, False, None, True),
            ("subType", "subType", CodeableConcept, False, None, False),
            ("use", "use", str, False, None, True),
            ("patient", "patient", FHIRReference, False, None, True),
            ("created", "created", FHIRDate, False, None, True),
            ("insurer", "insurer", FHIRReference, False, None, True),
            ("requestor", "requestor", FHIRReference, False, None, False),
            ("request", "request", FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, True),
            ("disposition", "disposition", str, False, None, False),
            ("preAuthRef", "preAuthRef", str, False, None, False),
            ("preAuthPeriod", "preAuthPeriod", Period, False, None, False),
            ("payeeType", "payeeType", CodeableConcept, False, None, False),
            ("item", "item", ClaimResponseItem, True, None, False),
            ("addItem", "addItem", ClaimResponseAddItem, True, None, False),
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("total", "total", ClaimResponseTotal, True, None, False),
            ("payment", "payment", ClaimResponsePayment, False, None, False),
            ("fundsReserve", "fundsReserve", CodeableConcept, False, None, False),
            ("formCode", "formCode", CodeableConcept, False, None, False),
            ("form", "form", Attachment, False, None, False),
            ("processNote", "processNote", ClaimResponseProcessNote, True, None, False),
            ("communicationRequest", "communicationRequest", FHIRReference, True, None, False),
            ("insurance", "insurance", ClaimResponseInsurance, True, None, False),
            ("error", "error", ClaimResponseError, True, None, False),
        ])
        return js