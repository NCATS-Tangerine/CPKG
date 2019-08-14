#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Element) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .fhirabstractbase import FHIRAbstractBase



@dataclass
class Element(FHIRAbstractBase):
    """ Base for all elements.

    Base definition for all elements in a resource.
    """
    resource_type: ClassVar[str] = "Element"
    id: Optional["str"] = None
    extension: Optional[List["Extension"]] = empty_list()

    def elementProperties(self):
        from .extension import Extension
        
        js = super(Element, self).elementProperties()
        js.extend([
            ("id", "id", str, False, None, False),
            ("extension", "extension", Extension, True, None, False),
        ])
        return js