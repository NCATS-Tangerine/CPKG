#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Account) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class AccountCoverage(BackboneElement):
    """ The party(s) that are responsible for covering the payment of this account,
    and what order should they be applied to the account.
    """
    resource_type: ClassVar[str] = "AccountCoverage"
    coverage: FHIRReference = None
    priority: Optional[int] = None

    def elementProperties(self):
        js = super(AccountCoverage, self).elementProperties()
        js.extend([
            ("coverage", "coverage", FHIRReference, False, None, True),
            ("priority", "priority", int, False, None, False),
        ])
        return js


@dataclass
class AccountGuarantor(BackboneElement):
    """ The parties ultimately responsible for balancing the Account.

    The parties responsible for balancing the account if other payment options
    fall short.
    """
    resource_type: ClassVar[str] = "AccountGuarantor"
    party: FHIRReference = None
    onHold: Optional[bool] = None
    period: Optional[Period] = None

    def elementProperties(self):
        js = super(AccountGuarantor, self).elementProperties()
        js.extend([
            ("party", "party", FHIRReference, False, None, True),
            ("onHold", "onHold", bool, False, None, False),
            ("period", "period", Period, False, None, False),
        ])
        return js


@dataclass
class Account(DomainResource):
    """ Tracks balance, charges, for patient or cost center.

    A financial tool for tracking value accrued for a particular purpose.  In
    the healthcare field, used to track charges for a patient, cost centers,
    etc.
    """
    resource_type: ClassVar[str] = "Account"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    type: Optional[CodeableConcept] = None
    name: Optional[str] = None
    subject: Optional[List[FHIRReference]] = empty_list()
    servicePeriod: Optional[Period] = None
    coverage: Optional[List[AccountCoverage]] = empty_list()
    owner: Optional[FHIRReference] = None
    description: Optional[str] = None
    guarantor: Optional[List[AccountGuarantor]] = empty_list()
    partOf: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(Account, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", CodeableConcept, False, None, False),
            ("name", "name", str, False, None, False),
            ("subject", "subject", FHIRReference, True, None, False),
            ("servicePeriod", "servicePeriod", Period, False, None, False),
            ("coverage", "coverage", AccountCoverage, True, None, False),
            ("owner", "owner", FHIRReference, False, None, False),
            ("description", "description", str, False, None, False),
            ("guarantor", "guarantor", AccountGuarantor, True, None, False),
            ("partOf", "partOf", FHIRReference, False, None, False),
        ])
        return js