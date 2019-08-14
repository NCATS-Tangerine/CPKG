#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Binary) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .fhirreference import FHIRReference
from .resource import Resource


@dataclass
class Binary(Resource):
    """ Pure binary content defined by a format other than FHIR.

    A resource that represents the data of a single raw artifact as digital
    content accessible in its native format.  A Binary resource can contain any
    content, whether text, image, pdf, zip archive, etc.
    """
    resource_type: ClassVar[str] = "Binary"
    contentType: str = None
    securityContext: Optional[FHIRReference] = None
    data: Optional[str] = None

    def elementProperties(self):
        js = super(Binary, self).elementProperties()
        js.extend([
            ("contentType", "contentType", str, False, None, True),
            ("securityContext", "securityContext", FHIRReference, False, None, False),
            ("data", "data", str, False, None, False),
        ])
        return js