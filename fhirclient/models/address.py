#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Address) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element
from .period import Period


@dataclass
class Address(Element):
    """ An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).

    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).  This data type may be used to convey
    addresses for use in delivering mail as well as for visiting locations
    which might not be valid for mail delivery.  There are a variety of postal
    address formats defined around the world.
    """
    resource_type: ClassVar[str] = "Address"
    use: Optional[str] = None
    type: Optional[str] = None
    text: Optional[str] = None
    line: Optional[List[str]] = empty_list()
    city: Optional[str] = None
    district: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    country: Optional[str] = None
    period: Optional[Period] = None

    def elementProperties(self):
        js = super(Address, self).elementProperties()
        js.extend([
            ("use", "use", str, False, None, False),
            ("type", "type", str, False, None, False),
            ("text", "text", str, False, None, False),
            ("line", "line", str, True, None, False),
            ("city", "city", str, False, None, False),
            ("district", "district", str, False, None, False),
            ("state", "state", str, False, None, False),
            ("postalCode", "postalCode", str, False, None, False),
            ("country", "country", str, False, None, False),
            ("period", "period", Period, False, None, False),
        ])
        return js