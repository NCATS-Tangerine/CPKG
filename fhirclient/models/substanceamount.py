#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/SubstanceAmount) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .element import Element
from .quantity import Quantity
from .range import Range


@dataclass
class SubstanceAmountReferenceRange(Element):
    """ Reference range of possible or expected values.
    """
    resource_type: ClassVar[str] = "SubstanceAmountReferenceRange"
    lowLimit: Optional[Quantity] = None
    highLimit: Optional[Quantity] = None

    def elementProperties(self):
        js = super(SubstanceAmountReferenceRange, self).elementProperties()
        js.extend([
            ("lowLimit", "lowLimit", Quantity, False, None, False),
            ("highLimit", "highLimit", Quantity, False, None, False),
        ])
        return js


@dataclass
class SubstanceAmount(BackboneElement):
    """ Chemical substances are a single substance type whose primary defining
    element is the molecular structure. Chemical substances shall be defined on
    the basis of their complete covalent molecular structure; the presence of a
    salt (counter-ion) and/or solvates (water, alcohols) is also captured.
    Purity, grade, physical form or particle size are not taken into account in
    the definition of a chemical substance or in the assignment of a Substance
    ID.
    """
    resource_type: ClassVar[str] = "SubstanceAmount"
    amountQuantity: Optional[Quantity] = None
    amountRange: Optional[Range] = None
    amountString: Optional[str] = None
    amountType: Optional[CodeableConcept] = None
    amountText: Optional[str] = None
    referenceRange: Optional[SubstanceAmountReferenceRange] = None

    def elementProperties(self):
        js = super(SubstanceAmount, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", Quantity, False, "amount", False),
            ("amountRange", "amountRange", Range, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("amountType", "amountType", CodeableConcept, False, None, False),
            ("amountText", "amountText", str, False, None, False),
            ("referenceRange", "referenceRange", SubstanceAmountReferenceRange, False, None, False),
        ])
        return js