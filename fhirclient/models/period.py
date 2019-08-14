#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Period) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element
from .fhirdate import FHIRDate


@dataclass
class Period(Element):
    """ Time range defined by start and end date/time.

    A time period defined by a start and end date and optionally time.
    """
    resource_type: ClassVar[str] = "Period"
    start: Optional[FHIRDate] = None
    end: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(Period, self).elementProperties()
        js.extend([
            ("start", "start", FHIRDate, False, None, False),
            ("end", "end", FHIRDate, False, None, False),
        ])
        return js