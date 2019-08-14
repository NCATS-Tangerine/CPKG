#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Invoice) on 2019-08-06.
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
from .money import Money


@dataclass
class InvoiceLineItemPriceComponent(BackboneElement):
    """ Components of total line item price.

    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice as to how the prices have been calculated.
    """
    resource_type: ClassVar[str] = "InvoiceLineItemPriceComponent"
    type: str = None
    code: Optional[CodeableConcept] = None
    factor: Optional[float] = None
    amount: Optional[Money] = None

    def elementProperties(self):
        js = super(InvoiceLineItemPriceComponent, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("code", "code", CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("amount", "amount", Money, False, None, False),
        ])
        return js


@dataclass
class InvoiceParticipant(BackboneElement):
    """ Participant in creation of this Invoice.

    Indicates who or what performed or participated in the charged service.
    """
    resource_type: ClassVar[str] = "InvoiceParticipant"
    role: Optional[CodeableConcept] = None
    actor: FHIRReference = None

    def elementProperties(self):
        js = super(InvoiceParticipant, self).elementProperties()
        js.extend([
            ("role", "role", CodeableConcept, False, None, False),
            ("actor", "actor", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class InvoiceLineItem(BackboneElement):
    """ Line items of this Invoice.

    Each line item represents one charge for goods and services rendered.
    Details such as date, code and amount are found in the referenced
    ChargeItem resource.
    """
    resource_type: ClassVar[str] = "InvoiceLineItem"
    sequence: Optional[int] = None
    chargeItemReference: FHIRReference = None
    chargeItemCodeableConcept: CodeableConcept = None
    priceComponent: Optional[List[InvoiceLineItemPriceComponent]] = empty_list()

    def elementProperties(self):
        js = super(InvoiceLineItem, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, False),
            ("chargeItemReference", "chargeItemReference", FHIRReference, False, "chargeItem", True),
            ("chargeItemCodeableConcept", "chargeItemCodeableConcept", CodeableConcept, False, "chargeItem", True),
            ("priceComponent", "priceComponent", InvoiceLineItemPriceComponent, True, None, False),
        ])
        return js


@dataclass
class Invoice(DomainResource):
    """ Invoice containing ChargeItems from an Account.

    Invoice containing collected ChargeItems from an Account with calculated
    individual and total price for Billing purpose.
    """
    resource_type: ClassVar[str] = "Invoice"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    cancelledReason: Optional[str] = None
    type: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    recipient: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    participant: Optional[List[InvoiceParticipant]] = empty_list()
    issuer: Optional[FHIRReference] = None
    account: Optional[FHIRReference] = None
    lineItem: Optional[List[InvoiceLineItem]] = empty_list()
    totalPriceComponent: Optional[List[InvoiceLineItemPriceComponent]] = empty_list()
    totalNet: Optional[Money] = None
    totalGross: Optional[Money] = None
    paymentTerms: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()

    def elementProperties(self):
        js = super(Invoice, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("cancelledReason", "cancelledReason", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("recipient", "recipient", FHIRReference, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("participant", "participant", InvoiceParticipant, True, None, False),
            ("issuer", "issuer", FHIRReference, False, None, False),
            ("account", "account", FHIRReference, False, None, False),
            ("lineItem", "lineItem", InvoiceLineItem, True, None, False),
            ("totalPriceComponent", "totalPriceComponent", InvoiceLineItemPriceComponent, True, None, False),
            ("totalNet", "totalNet", Money, False, None, False),
            ("totalGross", "totalGross", Money, False, None, False),
            ("paymentTerms", "paymentTerms", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
        ])
        return js