#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/DomainResource) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .extension import Extension
from .narrative import Narrative
from .resource import Resource


@dataclass
class DomainResource(Resource):
    """ A resource with narrative, extensions, and contained resources.

    A resource that includes narrative, extensions, and contained resources.
    """
    resource_type: ClassVar[str] = "DomainResource"
    text: Optional[Narrative] = None
    contained: Optional[List[Resource]] = empty_list()
    extension: Optional[List[Extension]] = empty_list()
    modifierExtension: Optional[List[Extension]] = empty_list()

    def elementProperties(self):
        js = super(DomainResource, self).elementProperties()
        js.extend([
            ("text", "text", Narrative, False, None, False),
            ("contained", "contained", Resource, True, None, False),
            ("extension", "extension", Extension, True, None, False),
            ("modifierExtension", "modifierExtension", Extension, True, None, False),
        ])
        return js