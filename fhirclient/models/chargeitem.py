#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ChargeItem) on 2019-08-06.
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
from .period import Period
from .quantity import Quantity
from .timing import Timing


@dataclass
class ChargeItemPerformer(BackboneElement):
    """ Who performed charged service.

    Indicates who or what performed or participated in the charged service.
    """
    resource_type: ClassVar[str] = "ChargeItemPerformer"
    function: Optional[CodeableConcept] = None
    actor: FHIRReference = None

    def elementProperties(self):
        js = super(ChargeItemPerformer, self).elementProperties()
        js.extend([
            ("function", "function", CodeableConcept, False, None, False),
            ("actor", "actor", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class ChargeItem(DomainResource):
    """ Item containing charge code(s) associated with the provision of healthcare
    provider products.

    The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like date,
    time, amounts and participating organizations and persons. Main Usage of
    the ChargeItem is to enable the billing process and internal cost
    allocation.
    """
    resource_type: ClassVar[str] = "ChargeItem"
    identifier: Optional[List[Identifier]] = empty_list()
    definitionUri: Optional[List[str]] = empty_list()
    definitionCanonical: Optional[List[str]] = empty_list()
    status: str = None
    partOf: Optional[List[FHIRReference]] = empty_list()
    code: CodeableConcept = None
    subject: FHIRReference = None
    context: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = None
    occurrencePeriod: Optional[Period] = None
    occurrenceTiming: Optional[Timing] = None
    performer: Optional[List[ChargeItemPerformer]] = empty_list()
    performingOrganization: Optional[FHIRReference] = None
    requestingOrganization: Optional[FHIRReference] = None
    costCenter: Optional[FHIRReference] = None
    quantity: Optional[Quantity] = None
    bodysite: Optional[List[CodeableConcept]] = empty_list()
    factorOverride: Optional[float] = None
    priceOverride: Optional[Money] = None
    overrideReason: Optional[str] = None
    enterer: Optional[FHIRReference] = None
    enteredDate: Optional[FHIRDate] = None
    reason: Optional[List[CodeableConcept]] = empty_list()
    service: Optional[List[FHIRReference]] = empty_list()
    productReference: Optional[FHIRReference] = None
    productCodeableConcept: Optional[CodeableConcept] = None
    account: Optional[List[FHIRReference]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    supportingInformation: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(ChargeItem, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("definitionUri", "definitionUri", str, True, None, False),
            ("definitionCanonical", "definitionCanonical", str, True, None, False),
            ("status", "status", str, False, None, True),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("code", "code", CodeableConcept, False, None, True),
            ("subject", "subject", FHIRReference, False, None, True),
            ("context", "context", FHIRReference, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", Timing, False, "occurrence", False),
            ("performer", "performer", ChargeItemPerformer, True, None, False),
            ("performingOrganization", "performingOrganization", FHIRReference, False, None, False),
            ("requestingOrganization", "requestingOrganization", FHIRReference, False, None, False),
            ("costCenter", "costCenter", FHIRReference, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("bodysite", "bodysite", CodeableConcept, True, None, False),
            ("factorOverride", "factorOverride", float, False, None, False),
            ("priceOverride", "priceOverride", Money, False, None, False),
            ("overrideReason", "overrideReason", str, False, None, False),
            ("enterer", "enterer", FHIRReference, False, None, False),
            ("enteredDate", "enteredDate", FHIRDate, False, None, False),
            ("reason", "reason", CodeableConcept, True, None, False),
            ("service", "service", FHIRReference, True, None, False),
            ("productReference", "productReference", FHIRReference, False, "product", False),
            ("productCodeableConcept", "productCodeableConcept", CodeableConcept, False, "product", False),
            ("account", "account", FHIRReference, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("supportingInformation", "supportingInformation", FHIRReference, True, None, False),
        ])
        return js