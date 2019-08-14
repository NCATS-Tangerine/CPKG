#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/CatalogEntry) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class CatalogEntryRelatedEntry(BackboneElement):
    """ Another entry of the catalog related to this one.

    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """
    resource_type: ClassVar[str] = "CatalogEntryRelatedEntry"
    relationship: str = None
    target: FHIRReference = None

    def elementProperties(self):
        js = super(CatalogEntryRelatedEntry, self).elementProperties()
        js.extend([
            ("relationship", "relationship", str, False, None, True),
            ("target", "target", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class CatalogEntry(DomainResource):
    """ An entry in a catalog.

    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """
    resource_type: ClassVar[str] = "CatalogEntry"
    identifier: Optional[List[Identifier]] = empty_list()
    name: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None
    effectivePeriod: Optional[Period] = None
    orderable: bool = None
    referencedItem: FHIRReference = None
    relatedEntry: Optional[List[CatalogEntryRelatedEntry]] = empty_list()
    updatedBy: Optional[FHIRReference] = None
    note: Optional[List[Annotation]] = empty_list()
    estimatedDuration: Optional[Duration] = None
    billingCode: Optional[List[CodeableConcept]] = empty_list()
    billingSummary: Optional[str] = None
    scheduleSummary: Optional[str] = None
    limitationSummary: Optional[str] = None
    regulatorySummary: Optional[str] = None

    def elementProperties(self):
        js = super(CatalogEntry, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("type", "type", str, False, None, False),
            ("status", "status", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("orderable", "orderable", bool, False, None, True),
            ("referencedItem", "referencedItem", FHIRReference, False, None, True),
            ("relatedEntry", "relatedEntry", CatalogEntryRelatedEntry, True, None, False),
            ("updatedBy", "updatedBy", FHIRReference, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("estimatedDuration", "estimatedDuration", Duration, False, None, False),
            ("billingCode", "billingCode", CodeableConcept, True, None, False),
            ("billingSummary", "billingSummary", str, False, None, False),
            ("scheduleSummary", "scheduleSummary", str, False, None, False),
            ("limitationSummary", "limitationSummary", str, False, None, False),
            ("regulatorySummary", "regulatorySummary", str, False, None, False),
        ])
        return js