#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Contributor) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .contactdetail import ContactDetail
from .element import Element


@dataclass
class Contributor(Element):
    """ Contributor information.

    A contributor to the content of a knowledge asset, including authors,
    editors, reviewers, and endorsers.
    """
    resource_type: ClassVar[str] = "Contributor"
    type: str = None
    name: str = None
    contact: Optional[List[ContactDetail]] = empty_list()

    def elementProperties(self):
        js = super(Contributor, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("contact", "contact", ContactDetail, True, None, False),
        ])
        return js