#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/RelatedArtifact) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .element import Element


@dataclass
class RelatedArtifact(Element):
    """ Related artifacts for a knowledge resource.

    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """
    resource_type: ClassVar[str] = "RelatedArtifact"
    type: str = None
    label: Optional[str] = None
    display: Optional[str] = None
    citation: Optional[str] = None
    url: Optional[str] = None
    document: Optional[Attachment] = None
    resource: Optional[str] = None

    def elementProperties(self):
        js = super(RelatedArtifact, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("label", "label", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("citation", "citation", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("document", "document", Attachment, False, None, False),
            ("resource", "resource", str, False, None, False),
        ])
        return js