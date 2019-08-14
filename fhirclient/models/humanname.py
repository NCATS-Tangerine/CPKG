#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/HumanName) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element
from .period import Period


@dataclass
class HumanName(Element):
    """ Name of a human - parts and usage.

    A human's name with the ability to identify parts and usage.
    """
    resource_type: ClassVar[str] = "HumanName"
    use: Optional[str] = None
    text: Optional[str] = None
    family: Optional[str] = None
    given: Optional[List[str]] = empty_list()
    prefix: Optional[List[str]] = empty_list()
    suffix: Optional[List[str]] = empty_list()
    period: Optional[Period] = None

    def elementProperties(self):
        js = super(HumanName, self).elementProperties()
        js.extend([
            ("use", "use", str, False, None, False),
            ("text", "text", str, False, None, False),
            ("family", "family", str, False, None, False),
            ("given", "given", str, True, None, False),
            ("prefix", "prefix", str, True, None, False),
            ("suffix", "suffix", str, True, None, False),
            ("period", "period", Period, False, None, False),
        ])
        return js