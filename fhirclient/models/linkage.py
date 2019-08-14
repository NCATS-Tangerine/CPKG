#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Linkage) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .domainresource import DomainResource
from .fhirreference import FHIRReference


@dataclass
class LinkageItem(BackboneElement):
    """ Item to be linked.

    Identifies which record considered as the reference to the same real-world
    occurrence as well as how the items should be evaluated within the
    collection of linked items.
    """
    resource_type: ClassVar[str] = "LinkageItem"
    type: str = None
    resource: FHIRReference = None

    def elementProperties(self):
        js = super(LinkageItem, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("resource", "resource", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class Linkage(DomainResource):
    """ Links records for 'same' item.

    Identifies two or more records (resource instances) that refer to the same
    real-world "occurrence".
    """
    resource_type: ClassVar[str] = "Linkage"
    active: Optional[bool] = None
    author: Optional[FHIRReference] = None
    item: List[LinkageItem] = empty_list()

    def elementProperties(self):
        js = super(Linkage, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("author", "author", FHIRReference, False, None, False),
            ("item", "item", LinkageItem, True, None, True),
        ])
        return js