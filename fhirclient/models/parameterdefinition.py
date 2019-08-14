#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ParameterDefinition) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element


@dataclass
class ParameterDefinition(Element):
    """ Definition of a parameter to a module.

    The parameters to the module. This collection specifies both the input and
    output parameters. Input parameters are provided by the caller as part of
    the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """
    resource_type: ClassVar[str] = "ParameterDefinition"
    name: Optional[str] = None
    use: str = None
    min: Optional[int] = None
    max: Optional[str] = None
    documentation: Optional[str] = None
    type: str = None
    profile: Optional[str] = None

    def elementProperties(self):
        js = super(ParameterDefinition, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("use", "use", str, False, None, True),
            ("min", "min", int, False, None, False),
            ("max", "max", str, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("profile", "profile", str, False, None, False),
        ])
        return js