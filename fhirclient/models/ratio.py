#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Ratio) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element
from .quantity import Quantity


@dataclass
class Ratio(Element):
    """ A ratio of two Quantity values - a numerator and a denominator.

    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """
    resource_type: ClassVar[str] = "Ratio"
    numerator: Optional[Quantity] = None
    denominator: Optional[Quantity] = None

    def elementProperties(self):
        js = super(Ratio, self).elementProperties()
        js.extend([
            ("numerator", "numerator", Quantity, False, None, False),
            ("denominator", "denominator", Quantity, False, None, False),
        ])
        return js