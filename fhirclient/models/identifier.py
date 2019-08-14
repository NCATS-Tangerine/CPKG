#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Identifier) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element



@dataclass
class Identifier(Element):
    """ An identifier intended for computation.

    An identifier - identifies some entity uniquely and unambiguously.
    Typically this is used for business identifiers.
    """
    resource_type: ClassVar[str] = "Identifier"
    use: Optional["str"] = None
    type: Optional["CodeableConcept"] = None
    system: Optional["str"] = None
    value: Optional["str"] = None
    period: Optional["Period"] = None
    assigner: Optional["FHIRReference"] = None

    def elementProperties(self):
        from .codeableconcept import CodeableConcept
        from .fhirreference import FHIRReference
        from .period import Period
        
        js = super(Identifier, self).elementProperties()
        js.extend([
            ("use", "use", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("system", "system", str, False, None, False),
            ("value", "value", str, False, None, False),
            ("period", "period", Period, False, None, False),
            ("assigner", "assigner", FHIRReference, False, None, False),
        ])
        return js