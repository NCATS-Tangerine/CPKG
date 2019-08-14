#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Age) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .quantity import Quantity


@dataclass
class Age(Quantity):
    """ A duration of time during which an organism (or a process) has existed.
    """
    resource_type: ClassVar[str] = "Age"