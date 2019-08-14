#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest) on 2019-08-06.
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
from .quantity import Quantity


@dataclass
class CoverageEligibilityRequestItemDiagnosis(BackboneElement):
    """ Applicable diagnosis.

    Patient diagnosis for which care is sought.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestItemDiagnosis"
    diagnosisCodeableConcept: Optional[CodeableConcept] = None
    diagnosisReference: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(CoverageEligibilityRequestItemDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", CodeableConcept, False, "diagnosis", False),
            ("diagnosisReference", "diagnosisReference", FHIRReference, False, "diagnosis", False),
        ])
        return js


@dataclass
class CoverageEligibilityRequestSupportingInfo(BackboneElement):
    """ Supporting information.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestSupportingInfo"
    sequence: int = None
    information: FHIRReference = None
    appliesToAll: Optional[bool] = None

    def elementProperties(self):
        js = super(CoverageEligibilityRequestSupportingInfo, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, True),
            ("information", "information", FHIRReference, False, None, True),
            ("appliesToAll", "appliesToAll", bool, False, None, False),
        ])
        return js


@dataclass
class CoverageEligibilityRequestInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestInsurance"
    focal: Optional[bool] = None
    coverage: FHIRReference = None
    businessArrangement: Optional[str] = None

    def elementProperties(self):
        js = super(CoverageEligibilityRequestInsurance, self).elementProperties()
        js.extend([
            ("focal", "focal", bool, False, None, False),
            ("coverage", "coverage", FHIRReference, False, None, True),
            ("businessArrangement", "businessArrangement", str, False, None, False),
        ])
        return js


@dataclass
class CoverageEligibilityRequestItem(BackboneElement):
    """ Item to be evaluated for eligibiity.

    Service categories or billable services for which benefit details and/or an
    authorization prior to service delivery may be required by the payor.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestItem"
    supportingInfoSequence: Optional[List[int]] = empty_list()
    category: Optional[CodeableConcept] = None
    productOrService: Optional[CodeableConcept] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    provider: Optional[FHIRReference] = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    facility: Optional[FHIRReference] = None
    diagnosis: Optional[List[CoverageEligibilityRequestItemDiagnosis]] = empty_list()
    detail: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(CoverageEligibilityRequestItem, self).elementProperties()
        js.extend([
            ("supportingInfoSequence", "supportingInfoSequence", int, True, None, False),
            ("category", "category", CodeableConcept, False, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, False),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("provider", "provider", FHIRReference, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
            ("facility", "facility", FHIRReference, False, None, False),
            ("diagnosis", "diagnosis", CoverageEligibilityRequestItemDiagnosis, True, None, False),
            ("detail", "detail", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class CoverageEligibilityRequest(DomainResource):
    """ CoverageEligibilityRequest resource.

    The CoverageEligibilityRequest provides patient and insurance coverage
    information to an insurer for them to respond, in the form of an
    CoverageEligibilityResponse, with information regarding whether the stated
    coverage is valid and in-force and optionally to provide the insurance
    details of the policy.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequest"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    priority: Optional[CodeableConcept] = None
    purpose: List[str] = empty_list()
    patient: FHIRReference = None
    servicedDate: Optional[FHIRDate] = None
    servicedPeriod: Optional[Period] = None
    created: FHIRDate = None
    enterer: Optional[FHIRReference] = None
    provider: Optional[FHIRReference] = None
    insurer: FHIRReference = None
    facility: Optional[FHIRReference] = None
    supportingInfo: Optional[List[CoverageEligibilityRequestSupportingInfo]] = empty_list()
    insurance: Optional[List[CoverageEligibilityRequestInsurance]] = empty_list()
    item: Optional[List[CoverageEligibilityRequestItem]] = empty_list()

    def elementProperties(self):
        js = super(CoverageEligibilityRequest, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("priority", "priority", CodeableConcept, False, None, False),
            ("purpose", "purpose", str, True, None, True),
            ("patient", "patient", FHIRReference, False, None, True),
            ("servicedDate", "servicedDate", FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", Period, False, "serviced", False),
            ("created", "created", FHIRDate, False, None, True),
            ("enterer", "enterer", FHIRReference, False, None, False),
            ("provider", "provider", FHIRReference, False, None, False),
            ("insurer", "insurer", FHIRReference, False, None, True),
            ("facility", "facility", FHIRReference, False, None, False),
            ("supportingInfo", "supportingInfo", CoverageEligibilityRequestSupportingInfo, True, None, False),
            ("insurance", "insurance", CoverageEligibilityRequestInsurance, True, None, False),
            ("item", "item", CoverageEligibilityRequestItem, True, None, False),
        ])
        return js