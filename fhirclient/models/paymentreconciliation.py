#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation) on 2019-08-06.
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
from .identifier import Identifier
from .money import Money
from .period import Period


@dataclass
class PaymentReconciliationDetail(BackboneElement):
    """ Settlement particulars.

    Distribution of the payment amount for a previously acknowledged payable.
    """
    resource_type: ClassVar[str] = "PaymentReconciliationDetail"
    identifier: Optional[Identifier] = None
    predecessor: Optional[Identifier] = None
    type: CodeableConcept = None
    request: Optional[FHIRReference] = None
    submitter: Optional[FHIRReference] = None
    response: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    responsible: Optional[FHIRReference] = None
    payee: Optional[FHIRReference] = None
    amount: Optional[Money] = None

    def elementProperties(self):
        js = super(PaymentReconciliationDetail, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("predecessor", "predecessor", Identifier, False, None, False),
            ("type", "type", CodeableConcept, False, None, True),
            ("request", "request", FHIRReference, False, None, False),
            ("submitter", "submitter", FHIRReference, False, None, False),
            ("response", "response", FHIRReference, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("responsible", "responsible", FHIRReference, False, None, False),
            ("payee", "payee", FHIRReference, False, None, False),
            ("amount", "amount", Money, False, None, False),
        ])
        return js


@dataclass
class PaymentReconciliationProcessNote(BackboneElement):
    """ Note concerning processing.

    A note that describes or explains the processing in a human readable form.
    """
    resource_type: ClassVar[str] = "PaymentReconciliationProcessNote"
    type: Optional[str] = None
    text: Optional[str] = None

    def elementProperties(self):
        js = super(PaymentReconciliationProcessNote, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


@dataclass
class PaymentReconciliation(DomainResource):
    """ PaymentReconciliation resource.

    This resource provides the details including amount of a payment and
    allocates the payment items being paid.
    """
    resource_type: ClassVar[str] = "PaymentReconciliation"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    period: Optional[Period] = None
    created: FHIRDate = None
    paymentIssuer: Optional[FHIRReference] = None
    request: Optional[FHIRReference] = None
    requestor: Optional[FHIRReference] = None
    outcome: Optional[str] = None
    disposition: Optional[str] = None
    paymentDate: FHIRDate = None
    paymentAmount: Money = None
    paymentIdentifier: Optional[Identifier] = None
    detail: Optional[List[PaymentReconciliationDetail]] = empty_list()
    formCode: Optional[CodeableConcept] = None
    processNote: Optional[List[PaymentReconciliationProcessNote]] = empty_list()

    def elementProperties(self):
        js = super(PaymentReconciliation, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("period", "period", Period, False, None, False),
            ("created", "created", FHIRDate, False, None, True),
            ("paymentIssuer", "paymentIssuer", FHIRReference, False, None, False),
            ("request", "request", FHIRReference, False, None, False),
            ("requestor", "requestor", FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("paymentDate", "paymentDate", FHIRDate, False, None, True),
            ("paymentAmount", "paymentAmount", Money, False, None, True),
            ("paymentIdentifier", "paymentIdentifier", Identifier, False, None, False),
            ("detail", "detail", PaymentReconciliationDetail, True, None, False),
            ("formCode", "formCode", CodeableConcept, False, None, False),
            ("processNote", "processNote", PaymentReconciliationProcessNote, True, None, False),
        ])
        return js