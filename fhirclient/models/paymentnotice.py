#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/PaymentNotice) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money


@dataclass
class PaymentNotice(DomainResource):
    """ PaymentNotice request.

    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """
    resource_type: ClassVar[str] = "PaymentNotice"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    request: Optional[FHIRReference] = None
    response: Optional[FHIRReference] = None
    created: FHIRDate = None
    provider: Optional[FHIRReference] = None
    payment: FHIRReference = None
    paymentDate: Optional[FHIRDate] = None
    payee: Optional[FHIRReference] = None
    recipient: FHIRReference = None
    amount: Money = None
    paymentStatus: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(PaymentNotice, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("request", "request", FHIRReference, False, None, False),
            ("response", "response", FHIRReference, False, None, False),
            ("created", "created", FHIRDate, False, None, True),
            ("provider", "provider", FHIRReference, False, None, False),
            ("payment", "payment", FHIRReference, False, None, True),
            ("paymentDate", "paymentDate", FHIRDate, False, None, False),
            ("payee", "payee", FHIRReference, False, None, False),
            ("recipient", "recipient", FHIRReference, False, None, True),
            ("amount", "amount", Money, False, None, True),
            ("paymentStatus", "paymentStatus", CodeableConcept, False, None, False),
        ])
        return js