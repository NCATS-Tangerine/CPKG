#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/TriggerDefinition) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .datarequirement import DataRequirement
from .element import Element
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .timing import Timing


@dataclass
class TriggerDefinition(Element):
    """ Defines an expected trigger for a module.

    A description of a triggering event. Triggering events can be named events,
    data events, or periodic, as determined by the type element.
    """
    resource_type: ClassVar[str] = "TriggerDefinition"
    type: str = None
    name: Optional[str] = None
    timingTiming: Optional[Timing] = None
    timingReference: Optional[FHIRReference] = None
    timingDate: Optional[FHIRDate] = None
    timingDateTime: Optional[FHIRDate] = None
    data: Optional[List[DataRequirement]] = empty_list()
    condition: Optional[Expression] = None

    def elementProperties(self):
        js = super(TriggerDefinition, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("timingTiming", "timingTiming", Timing, False, "timing", False),
            ("timingReference", "timingReference", FHIRReference, False, "timing", False),
            ("timingDate", "timingDate", FHIRDate, False, "timing", False),
            ("timingDateTime", "timingDateTime", FHIRDate, False, "timing", False),
            ("data", "data", DataRequirement, True, None, False),
            ("condition", "condition", Expression, False, None, False),
        ])
        return js