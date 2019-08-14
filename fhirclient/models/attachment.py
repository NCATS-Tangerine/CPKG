#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Attachment) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element
from .fhirdate import FHIRDate


@dataclass
class Attachment(Element):
    """ Content in a format defined elsewhere.

    For referring to data content defined in other formats.
    """
    resource_type: ClassVar[str] = "Attachment"
    contentType: Optional[str] = None
    language: Optional[str] = None
    data: Optional[str] = None
    url: Optional[str] = None
    size: Optional[int] = None
    hash: Optional[str] = None
    title: Optional[str] = None
    creation: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(Attachment, self).elementProperties()
        js.extend([
            ("contentType", "contentType", str, False, None, False),
            ("language", "language", str, False, None, False),
            ("data", "data", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("size", "size", int, False, None, False),
            ("hash", "hash", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("creation", "creation", FHIRDate, False, None, False),
        ])
        return js