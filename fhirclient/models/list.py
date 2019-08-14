#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/List) on 2019-08-06.
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


@dataclass
class ListEntry(BackboneElement):
    """ Entries in the list.

    Entries in this list.
    """
    resource_type: ClassVar[str] = "ListEntry"
    flag: Optional[CodeableConcept] = None
    deleted: Optional[bool] = None
    date: Optional[FHIRDate] = None
    item: FHIRReference = None

    def elementProperties(self):
        js = super(ListEntry, self).elementProperties()
        js.extend([
            ("flag", "flag", CodeableConcept, False, None, False),
            ("deleted", "deleted", bool, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("item", "item", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class List(DomainResource):
    """ A list is a curated collection of resources.
    """
    resource_type: ClassVar[str] = "List"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    mode: str = None
    title: Optional[str] = None
    code: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    source: Optional[FHIRReference] = None
    orderedBy: Optional[CodeableConcept] = None
    note: Optional[List[Annotation]] = empty_list()
    entry: Optional[List[ListEntry]] = empty_list()
    emptyReason: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(List, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("mode", "mode", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("source", "source", FHIRReference, False, None, False),
            ("orderedBy", "orderedBy", CodeableConcept, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("entry", "entry", ListEntry, True, None, False),
            ("emptyReason", "emptyReason", CodeableConcept, False, None, False),
        ])
        return js