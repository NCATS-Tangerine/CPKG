#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Coverage) on 2019-08-06.
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
from .money import Money
from .period import Period
from .quantity import Quantity


@dataclass
class CoverageCostToBeneficiaryException(BackboneElement):
    """ Exceptions for patient payments.

    A suite of codes indicating exceptions or reductions to patient costs and
    their effective periods.
    """
    resource_type: ClassVar[str] = "CoverageCostToBeneficiaryException"
    type: CodeableConcept = None
    period: Optional[Period] = None

    def elementProperties(self):
        js = super(CoverageCostToBeneficiaryException, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("period", "period", Period, False, None, False),
        ])
        return js


@dataclass
class CoverageClass(BackboneElement):
    """ Additional coverage classifications.

    A suite of underwriter specific classifiers.
    """
    resource_type: ClassVar[str] = "CoverageClass"
    type: CodeableConcept = None
    value: str = None
    name: Optional[str] = None

    def elementProperties(self):
        js = super(CoverageClass, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("value", "value", str, False, None, True),
            ("name", "name", str, False, None, False),
        ])
        return js


@dataclass
class CoverageCostToBeneficiary(BackboneElement):
    """ Patient payments for services/products.

    A suite of codes indicating the cost category and associated amount which
    have been detailed in the policy and may have been  included on the health
    card.
    """
    resource_type: ClassVar[str] = "CoverageCostToBeneficiary"
    type: Optional[CodeableConcept] = None
    valueQuantity: Quantity = None
    valueMoney: Money = None
    exception: Optional[List[CoverageCostToBeneficiaryException]] = empty_list()

    def elementProperties(self):
        js = super(CoverageCostToBeneficiary, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", True),
            ("valueMoney", "valueMoney", Money, False, "value", True),
            ("exception", "exception", CoverageCostToBeneficiaryException, True, None, False),
        ])
        return js


@dataclass
class Coverage(DomainResource):
    """ Insurance or medical plan or a payment agreement.

    Financial instrument which may be used to reimburse or pay for health care
    products and services. Includes both insurance and self-payment.
    """
    resource_type: ClassVar[str] = "Coverage"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    type: Optional[CodeableConcept] = None
    policyHolder: Optional[FHIRReference] = None
    subscriber: Optional[FHIRReference] = None
    subscriberId: Optional[str] = None
    beneficiary: FHIRReference = None
    dependent: Optional[str] = None
    relationship: Optional[CodeableConcept] = None
    period: Optional[Period] = None
    payor: List[FHIRReference] = empty_list()
    class_fhir: Optional[List[CoverageClass]] = empty_list()
    order: Optional[int] = None
    network: Optional[str] = None
    costToBeneficiary: Optional[List[CoverageCostToBeneficiary]] = empty_list()
    subrogation: Optional[bool] = None
    contract: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(Coverage, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", CodeableConcept, False, None, False),
            ("policyHolder", "policyHolder", FHIRReference, False, None, False),
            ("subscriber", "subscriber", FHIRReference, False, None, False),
            ("subscriberId", "subscriberId", str, False, None, False),
            ("beneficiary", "beneficiary", FHIRReference, False, None, True),
            ("dependent", "dependent", str, False, None, False),
            ("relationship", "relationship", CodeableConcept, False, None, False),
            ("period", "period", Period, False, None, False),
            ("payor", "payor", FHIRReference, True, None, True),
            ("class_fhir", "class", CoverageClass, True, None, False),
            ("order", "order", int, False, None, False),
            ("network", "network", str, False, None, False),
            ("costToBeneficiary", "costToBeneficiary", CoverageCostToBeneficiary, True, None, False),
            ("subrogation", "subrogation", bool, False, None, False),
            ("contract", "contract", FHIRReference, True, None, False),
        ])
        return js