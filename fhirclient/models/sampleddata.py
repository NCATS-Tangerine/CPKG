#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/SampledData) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element
from .quantity import Quantity


@dataclass
class SampledData(Element):
    """ A series of measurements taken by a device.

    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """
    resource_type: ClassVar[str] = "SampledData"
    origin: Quantity = None
    period: float = None
    factor: Optional[float] = None
    lowerLimit: Optional[float] = None
    upperLimit: Optional[float] = None
    dimensions: int = None
    data: Optional[str] = None

    def elementProperties(self):
        js = super(SampledData, self).elementProperties()
        js.extend([
            ("origin", "origin", Quantity, False, None, True),
            ("period", "period", float, False, None, True),
            ("factor", "factor", float, False, None, False),
            ("lowerLimit", "lowerLimit", float, False, None, False),
            ("upperLimit", "upperLimit", float, False, None, False),
            ("dimensions", "dimensions", int, False, None, True),
            ("data", "data", str, False, None, False),
        ])
        return js