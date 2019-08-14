#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse) on 2019-08-06.
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
class CoverageEligibilityResponseInsuranceItemBenefit(BackboneElement):
    """ Benefit Summary.

    Benefits used to date.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponseInsuranceItemBenefit"
    type: CodeableConcept = None
    allowedUnsignedInt: Optional[int] = None
    allowedString: Optional[str] = None
    allowedMoney: Optional[Money] = None
    usedUnsignedInt: Optional[int] = None
    usedString: Optional[str] = None
    usedMoney: Optional[Money] = None

    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsuranceItemBenefit, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("allowedUnsignedInt", "allowedUnsignedInt", int, False, "allowed", False),
            ("allowedString", "allowedString", str, False, "allowed", False),
            ("allowedMoney", "allowedMoney", Money, False, "allowed", False),
            ("usedUnsignedInt", "usedUnsignedInt", int, False, "used", False),
            ("usedString", "usedString", str, False, "used", False),
            ("usedMoney", "usedMoney", Money, False, "used", False),
        ])
        return js


@dataclass
class CoverageEligibilityResponseInsuranceItem(BackboneElement):
    """ Benefits and authorization details.

    Benefits and optionally current balances, and authorization details by
    category or service.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponseInsuranceItem"
    category: Optional[CodeableConcept] = None
    productOrService: Optional[CodeableConcept] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    provider: Optional[FHIRReference] = None
    excluded: Optional[bool] = None
    name: Optional[str] = None
    description: Optional[str] = None
    network: Optional[CodeableConcept] = None
    unit: Optional[CodeableConcept] = None
    term: Optional[CodeableConcept] = None
    benefit: Optional[List[CoverageEligibilityResponseInsuranceItemBenefit]] = empty_list()
    authorizationRequired: Optional[bool] = None
    authorizationSupporting: Optional[List[CodeableConcept]] = empty_list()
    authorizationUrl: Optional[str] = None

    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsuranceItem, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, False),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("provider", "provider", FHIRReference, False, None, False),
            ("excluded", "excluded", bool, False, None, False),
            ("name", "name", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("network", "network", CodeableConcept, False, None, False),
            ("unit", "unit", CodeableConcept, False, None, False),
            ("term", "term", CodeableConcept, False, None, False),
            ("benefit", "benefit", CoverageEligibilityResponseInsuranceItemBenefit, True, None, False),
            ("authorizationRequired", "authorizationRequired", bool, False, None, False),
            ("authorizationSupporting", "authorizationSupporting", CodeableConcept, True, None, False),
            ("authorizationUrl", "authorizationUrl", str, False, None, False),
        ])
        return js


@dataclass
class CoverageEligibilityResponseInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponseInsurance"
    coverage: FHIRReference = None
    inforce: Optional[bool] = None
    benefitPeriod: Optional[Period] = None
    item: Optional[List[CoverageEligibilityResponseInsuranceItem]] = empty_list()

    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsurance, self).elementProperties()
        js.extend([
            ("coverage", "coverage", FHIRReference, False, None, True),
            ("inforce", "inforce", bool, False, None, False),
            ("benefitPeriod", "benefitPeriod", Period, False, None, False),
            ("item", "item", CoverageEligibilityResponseInsuranceItem, True, None, False),
        ])
        return js


@dataclass
class CoverageEligibilityResponseError(BackboneElement):
    """ Processing errors.

    Errors encountered during the processing of the request.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponseError"
    code: CodeableConcept = None

    def elementProperties(self):
        js = super(CoverageEligibilityResponseError, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class CoverageEligibilityResponse(DomainResource):
    """ CoverageEligibilityResponse resource.

    This resource provides eligibility and plan details from the processing of
    an CoverageEligibilityRequest resource.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponse"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    purpose: List[str] = empty_list()
    patient: FHIRReference = None
    servicedDate: Optional[FHIRDate] = None
    servicedPeriod: Optional[Period] = None
    created: FHIRDate = None
    requestor: Optional[FHIRReference] = None
    request: FHIRReference = None
    outcome: str = None
    disposition: Optional[str] = None
    insurer: FHIRReference = None
    insurance: Optional[List[CoverageEligibilityResponseInsurance]] = empty_list()
    preAuthRef: Optional[str] = None
    form: Optional[CodeableConcept] = None
    error: Optional[List[CoverageEligibilityResponseError]] = empty_list()

    def elementProperties(self):
        js = super(CoverageEligibilityResponse, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("purpose", "purpose", str, True, None, True),
            ("patient", "patient", FHIRReference, False, None, True),
            ("servicedDate", "servicedDate", FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", Period, False, "serviced", False),
            ("created", "created", FHIRDate, False, None, True),
            ("requestor", "requestor", FHIRReference, False, None, False),
            ("request", "request", FHIRReference, False, None, True),
            ("outcome", "outcome", str, False, None, True),
            ("disposition", "disposition", str, False, None, False),
            ("insurer", "insurer", FHIRReference, False, None, True),
            ("insurance", "insurance", CoverageEligibilityResponseInsurance, True, None, False),
            ("preAuthRef", "preAuthRef", str, False, None, False),
            ("form", "form", CodeableConcept, False, None, False),
            ("error", "error", CoverageEligibilityResponseError, True, None, False),
        ])
        return js