#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/InsurancePlan) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier
from .money import Money
from .period import Period
from .quantity import Quantity


@dataclass
class InsurancePlanPlanSpecificCostBenefitCost(BackboneElement):
    """ List of the costs.

    List of the costs associated with a specific benefit.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanSpecificCostBenefitCost"
    type: CodeableConcept = None
    applicability: Optional[CodeableConcept] = None
    qualifiers: Optional[List[CodeableConcept]] = empty_list()
    value: Optional[Quantity] = None

    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCostBenefitCost, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("applicability", "applicability", CodeableConcept, False, None, False),
            ("qualifiers", "qualifiers", CodeableConcept, True, None, False),
            ("value", "value", Quantity, False, None, False),
        ])
        return js


@dataclass
class InsurancePlanPlanSpecificCostBenefit(BackboneElement):
    """ Benefits list.

    List of the specific benefits under this category of benefit.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanSpecificCostBenefit"
    type: CodeableConcept = None
    cost: Optional[List[InsurancePlanPlanSpecificCostBenefitCost]] = empty_list()

    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCostBenefit, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("cost", "cost", InsurancePlanPlanSpecificCostBenefitCost, True, None, False),
        ])
        return js


@dataclass
class InsurancePlanPlanGeneralCost(BackboneElement):
    """ Overall costs.

    Overall costs associated with the plan.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanGeneralCost"
    type: Optional[CodeableConcept] = None
    groupSize: Optional[int] = None
    cost: Optional[Money] = None
    comment: Optional[str] = None

    def elementProperties(self):
        js = super(InsurancePlanPlanGeneralCost, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("groupSize", "groupSize", int, False, None, False),
            ("cost", "cost", Money, False, None, False),
            ("comment", "comment", str, False, None, False),
        ])
        return js


@dataclass
class InsurancePlanPlanSpecificCost(BackboneElement):
    """ Specific costs.

    Costs associated with the coverage provided by the product.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanSpecificCost"
    category: CodeableConcept = None
    benefit: Optional[List[InsurancePlanPlanSpecificCostBenefit]] = empty_list()

    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCost, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, True),
            ("benefit", "benefit", InsurancePlanPlanSpecificCostBenefit, True, None, False),
        ])
        return js


@dataclass
class InsurancePlanCoverageBenefitLimit(BackboneElement):
    """ Benefit limits.

    The specific limits on the benefit.
    """
    resource_type: ClassVar[str] = "InsurancePlanCoverageBenefitLimit"
    value: Optional[Quantity] = None
    code: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(InsurancePlanCoverageBenefitLimit, self).elementProperties()
        js.extend([
            ("value", "value", Quantity, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class InsurancePlanCoverageBenefit(BackboneElement):
    """ List of benefits.

    Specific benefits under this type of coverage.
    """
    resource_type: ClassVar[str] = "InsurancePlanCoverageBenefit"
    type: CodeableConcept = None
    requirement: Optional[str] = None
    limit: Optional[List[InsurancePlanCoverageBenefitLimit]] = empty_list()

    def elementProperties(self):
        js = super(InsurancePlanCoverageBenefit, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("requirement", "requirement", str, False, None, False),
            ("limit", "limit", InsurancePlanCoverageBenefitLimit, True, None, False),
        ])
        return js


@dataclass
class InsurancePlanContact(BackboneElement):
    """ Contact for the product.

    The contact for the health insurance product for a certain purpose.
    """
    resource_type: ClassVar[str] = "InsurancePlanContact"
    purpose: Optional[CodeableConcept] = None
    name: Optional[HumanName] = None
    telecom: Optional[List[ContactPoint]] = empty_list()
    address: Optional[Address] = None

    def elementProperties(self):
        js = super(InsurancePlanContact, self).elementProperties()
        js.extend([
            ("purpose", "purpose", CodeableConcept, False, None, False),
            ("name", "name", HumanName, False, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
            ("address", "address", Address, False, None, False),
        ])
        return js


@dataclass
class InsurancePlanCoverage(BackboneElement):
    """ Coverage details.

    Details about the coverage offered by the insurance product.
    """
    resource_type: ClassVar[str] = "InsurancePlanCoverage"
    type: CodeableConcept = None
    network: Optional[List[FHIRReference]] = empty_list()
    benefit: List[InsurancePlanCoverageBenefit] = empty_list()

    def elementProperties(self):
        js = super(InsurancePlanCoverage, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("network", "network", FHIRReference, True, None, False),
            ("benefit", "benefit", InsurancePlanCoverageBenefit, True, None, True),
        ])
        return js


@dataclass
class InsurancePlanPlan(BackboneElement):
    """ Plan details.

    Details about an insurance plan.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlan"
    identifier: Optional[List[Identifier]] = empty_list()
    type: Optional[CodeableConcept] = None
    coverageArea: Optional[List[FHIRReference]] = empty_list()
    network: Optional[List[FHIRReference]] = empty_list()
    generalCost: Optional[List[InsurancePlanPlanGeneralCost]] = empty_list()
    specificCost: Optional[List[InsurancePlanPlanSpecificCost]] = empty_list()

    def elementProperties(self):
        js = super(InsurancePlanPlan, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("coverageArea", "coverageArea", FHIRReference, True, None, False),
            ("network", "network", FHIRReference, True, None, False),
            ("generalCost", "generalCost", InsurancePlanPlanGeneralCost, True, None, False),
            ("specificCost", "specificCost", InsurancePlanPlanSpecificCost, True, None, False),
        ])
        return js


@dataclass
class InsurancePlan(DomainResource):
    """ Details of a Health Insurance product/plan provided by an organization.
    """
    resource_type: ClassVar[str] = "InsurancePlan"
    identifier: Optional[List[Identifier]] = empty_list()
    status: Optional[str] = None
    type: Optional[List[CodeableConcept]] = empty_list()
    name: Optional[str] = None
    alias: Optional[List[str]] = empty_list()
    period: Optional[Period] = None
    ownedBy: Optional[FHIRReference] = None
    administeredBy: Optional[FHIRReference] = None
    coverageArea: Optional[List[FHIRReference]] = empty_list()
    contact: Optional[List[InsurancePlanContact]] = empty_list()
    endpoint: Optional[List[FHIRReference]] = empty_list()
    network: Optional[List[FHIRReference]] = empty_list()
    coverage: Optional[List[InsurancePlanCoverage]] = empty_list()
    plan: Optional[List[InsurancePlanPlan]] = empty_list()

    def elementProperties(self):
        js = super(InsurancePlan, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, False),
            ("type", "type", CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("period", "period", Period, False, None, False),
            ("ownedBy", "ownedBy", FHIRReference, False, None, False),
            ("administeredBy", "administeredBy", FHIRReference, False, None, False),
            ("coverageArea", "coverageArea", FHIRReference, True, None, False),
            ("contact", "contact", InsurancePlanContact, True, None, False),
            ("endpoint", "endpoint", FHIRReference, True, None, False),
            ("network", "network", FHIRReference, True, None, False),
            ("coverage", "coverage", InsurancePlanCoverage, True, None, False),
            ("plan", "plan", InsurancePlanPlan, True, None, False),
        ])
        return js