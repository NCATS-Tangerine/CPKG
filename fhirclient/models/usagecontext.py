#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/UsageContext) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .coding import Coding
from .element import Element
from .fhirreference import FHIRReference
from .quantity import Quantity
from .range import Range


@dataclass
class UsageContext(Element):
    """ Describes the context of use for a conformance or knowledge resource.

    Specifies clinical/business/etc. metadata that can be used to retrieve,
    index and/or categorize an artifact. This metadata can either be specific
    to the applicable population (e.g., age category, DRG) or the specific
    context of care (e.g., venue, care setting, provider of care).
    """
    resource_type: ClassVar[str] = "UsageContext"
    code: Coding = None
    valueCodeableConcept: CodeableConcept = None
    valueQuantity: Quantity = None
    valueRange: Range = None
    valueReference: FHIRReference = None

    def elementProperties(self):
        js = super(UsageContext, self).elementProperties()
        js.extend([
            ("code", "code", Coding, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", True),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", True),
            ("valueRange", "valueRange", Range, False, "value", True),
            ("valueReference", "valueReference", FHIRReference, False, "value", True),
        ])
        return js