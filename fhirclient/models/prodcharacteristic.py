#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ProdCharacteristic) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .quantity import Quantity


@dataclass
class ProdCharacteristic(BackboneElement):
    """ The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """
    resource_type: ClassVar[str] = "ProdCharacteristic"
    height: Optional[Quantity] = None
    width: Optional[Quantity] = None
    depth: Optional[Quantity] = None
    weight: Optional[Quantity] = None
    nominalVolume: Optional[Quantity] = None
    externalDiameter: Optional[Quantity] = None
    shape: Optional[str] = None
    color: Optional[List[str]] = empty_list()
    imprint: Optional[List[str]] = empty_list()
    image: Optional[List[Attachment]] = empty_list()
    scoring: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ProdCharacteristic, self).elementProperties()
        js.extend([
            ("height", "height", Quantity, False, None, False),
            ("width", "width", Quantity, False, None, False),
            ("depth", "depth", Quantity, False, None, False),
            ("weight", "weight", Quantity, False, None, False),
            ("nominalVolume", "nominalVolume", Quantity, False, None, False),
            ("externalDiameter", "externalDiameter", Quantity, False, None, False),
            ("shape", "shape", str, False, None, False),
            ("color", "color", str, True, None, False),
            ("imprint", "imprint", str, True, None, False),
            ("image", "image", Attachment, True, None, False),
            ("scoring", "scoring", CodeableConcept, False, None, False),
        ])
        return js