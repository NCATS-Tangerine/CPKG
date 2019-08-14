#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/SupplyDelivery) on 2019-08-06.
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
from .period import Period
from .quantity import Quantity
from .timing import Timing


@dataclass
class SupplyDeliverySuppliedItem(BackboneElement):
    """ The item that is delivered or supplied.

    The item that is being delivered or has been supplied.
    """
    resource_type: ClassVar[str] = "SupplyDeliverySuppliedItem"
    quantity: Optional[Quantity] = None
    itemCodeableConcept: Optional[CodeableConcept] = None
    itemReference: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(SupplyDeliverySuppliedItem, self).elementProperties()
        js.extend([
            ("quantity", "quantity", Quantity, False, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", CodeableConcept, False, "item", False),
            ("itemReference", "itemReference", FHIRReference, False, "item", False),
        ])
        return js


@dataclass
class SupplyDelivery(DomainResource):
    """ Delivery of bulk Supplies.

    Record of delivery of what is supplied.
    """
    resource_type: ClassVar[str] = "SupplyDelivery"
    identifier: Optional[List[Identifier]] = empty_list()
    basedOn: Optional[List[FHIRReference]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    status: Optional[str] = None
    patient: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None
    suppliedItem: Optional[SupplyDeliverySuppliedItem] = None
    occurrenceDateTime: Optional[FHIRDate] = None
    occurrencePeriod: Optional[Period] = None
    occurrenceTiming: Optional[Timing] = None
    supplier: Optional[FHIRReference] = None
    destination: Optional[FHIRReference] = None
    receiver: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(SupplyDelivery, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("patient", "patient", FHIRReference, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("suppliedItem", "suppliedItem", SupplyDeliverySuppliedItem, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", Timing, False, "occurrence", False),
            ("supplier", "supplier", FHIRReference, False, None, False),
            ("destination", "destination", FHIRReference, False, None, False),
            ("receiver", "receiver", FHIRReference, True, None, False),
        ])
        return js