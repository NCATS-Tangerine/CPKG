#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Population) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .range import Range


@dataclass
class Population(BackboneElement):
    """ A definition of a set of people that apply to some clinically related
    context, for example people contraindicated for a certain medication.

    A populatioof people with some set of grouping criteria.
    """
    resource_type: ClassVar[str] = "Population"
    ageRange: Optional[Range] = None
    ageCodeableConcept: Optional[CodeableConcept] = None
    gender: Optional[CodeableConcept] = None
    race: Optional[CodeableConcept] = None
    physiologicalCondition: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(Population, self).elementProperties()
        js.extend([
            ("ageRange", "ageRange", Range, False, "age", False),
            ("ageCodeableConcept", "ageCodeableConcept", CodeableConcept, False, "age", False),
            ("gender", "gender", CodeableConcept, False, None, False),
            ("race", "race", CodeableConcept, False, None, False),
            ("physiologicalCondition", "physiologicalCondition", CodeableConcept, False, None, False),
        ])
        return js