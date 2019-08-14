#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Signature) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .coding import Coding
from .element import Element
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference


@dataclass
class Signature(Element):
    """ A Signature - XML DigSig, JWS, Graphical image of signature, etc..

    A signature along with supporting context. The signature may be a digital
    signature that is cryptographic in nature, or some other signature
    acceptable to the domain. This other signature may be as simple as a
    graphical image representing a hand-written signature, or a signature
    ceremony Different signature approaches have different utilities.
    """
    resource_type: ClassVar[str] = "Signature"
    type: List[Coding] = empty_list()
    when: FHIRDate = None
    who: FHIRReference = None
    onBehalfOf: Optional[FHIRReference] = None
    targetFormat: Optional[str] = None
    sigFormat: Optional[str] = None
    data: Optional[str] = None

    def elementProperties(self):
        js = super(Signature, self).elementProperties()
        js.extend([
            ("type", "type", Coding, True, None, True),
            ("when", "when", FHIRDate, False, None, True),
            ("who", "who", FHIRReference, False, None, True),
            ("onBehalfOf", "onBehalfOf", FHIRReference, False, None, False),
            ("targetFormat", "targetFormat", str, False, None, False),
            ("sigFormat", "sigFormat", str, False, None, False),
            ("data", "data", str, False, None, False),
        ])
        return js