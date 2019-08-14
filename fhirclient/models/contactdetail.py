#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ContactDetail) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .contactpoint import ContactPoint
from .element import Element


@dataclass
class ContactDetail(Element):
    """ Contact information.

    Specifies contact information for a person or organization.
    """
    resource_type: ClassVar[str] = "ContactDetail"
    name: Optional[str] = None
    telecom: Optional[List[ContactPoint]] = empty_list()

    def elementProperties(self):
        js = super(ContactDetail, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
        ])
        return js