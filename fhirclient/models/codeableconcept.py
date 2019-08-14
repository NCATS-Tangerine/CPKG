#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/CodeableConcept) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .coding import Coding
from .element import Element


@dataclass
class CodeableConcept(Element):
    """ Concept - reference to a terminology or just  text.

    A concept that may be defined by a formal reference to a terminology or
    ontology or may be provided by text.
    """
    resource_type: ClassVar[str] = "CodeableConcept"
    coding: Optional[List[Coding]] = empty_list()
    text: Optional[str] = None

    def elementProperties(self):
        js = super(CodeableConcept, self).elementProperties()
        js.extend([
            ("coding", "coding", Coding, True, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js