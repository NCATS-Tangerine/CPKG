#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Annotation) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference


@dataclass
class Annotation(Element):
    """ Text node with attribution.

    A  text note which also  contains information about who made the statement
    and when.
    """
    resource_type: ClassVar[str] = "Annotation"
    authorReference: Optional[FHIRReference] = None
    authorString: Optional[str] = None
    time: Optional[FHIRDate] = None
    text: str = None

    def elementProperties(self):
        js = super(Annotation, self).elementProperties()
        js.extend([
            ("authorReference", "authorReference", FHIRReference, False, "author", False),
            ("authorString", "authorString", str, False, "author", False),
            ("time", "time", FHIRDate, False, None, False),
            ("text", "text", str, False, None, True),
        ])
        return js