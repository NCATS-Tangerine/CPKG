#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ContactPoint) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element
from .period import Period


@dataclass
class ContactPoint(Element):
    """ Details of a Technology mediated contact point (phone, fax, email, etc.).

    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """
    resource_type: ClassVar[str] = "ContactPoint"
    system: Optional[str] = None
    value: Optional[str] = None
    use: Optional[str] = None
    rank: Optional[int] = None
    period: Optional[Period] = None

    def elementProperties(self):
        js = super(ContactPoint, self).elementProperties()
        js.extend([
            ("system", "system", str, False, None, False),
            ("value", "value", str, False, None, False),
            ("use", "use", str, False, None, False),
            ("rank", "rank", int, False, None, False),
            ("period", "period", Period, False, None, False),
        ])
        return js