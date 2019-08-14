#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/SubstancePolymer) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .substanceamount import SubstanceAmount


@dataclass
class SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation"
    degree: Optional[CodeableConcept] = None
    amount: Optional[SubstanceAmount] = None

    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation, self).elementProperties()
        js.extend([
            ("degree", "degree", CodeableConcept, False, None, False),
            ("amount", "amount", SubstanceAmount, False, None, False),
        ])
        return js


@dataclass
class SubstancePolymerRepeatRepeatUnitStructuralRepresentation(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeatRepeatUnitStructuralRepresentation"
    type: Optional[CodeableConcept] = None
    representation: Optional[str] = None
    attachment: Optional[Attachment] = None

    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnitStructuralRepresentation, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("representation", "representation", str, False, None, False),
            ("attachment", "attachment", Attachment, False, None, False),
        ])
        return js


@dataclass
class SubstancePolymerRepeatRepeatUnit(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeatRepeatUnit"
    orientationOfPolymerisation: Optional[CodeableConcept] = None
    repeatUnit: Optional[str] = None
    amount: Optional[SubstanceAmount] = None
    degreeOfPolymerisation: Optional[List[SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation]] = empty_list()
    structuralRepresentation: Optional[List[SubstancePolymerRepeatRepeatUnitStructuralRepresentation]] = empty_list()

    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnit, self).elementProperties()
        js.extend([
            ("orientationOfPolymerisation", "orientationOfPolymerisation", CodeableConcept, False, None, False),
            ("repeatUnit", "repeatUnit", str, False, None, False),
            ("amount", "amount", SubstanceAmount, False, None, False),
            ("degreeOfPolymerisation", "degreeOfPolymerisation", SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation, True, None, False),
            ("structuralRepresentation", "structuralRepresentation", SubstancePolymerRepeatRepeatUnitStructuralRepresentation, True, None, False),
        ])
        return js


@dataclass
class SubstancePolymerMonomerSetStartingMaterial(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerMonomerSetStartingMaterial"
    material: Optional[CodeableConcept] = None
    type: Optional[CodeableConcept] = None
    isDefining: Optional[bool] = None
    amount: Optional[SubstanceAmount] = None

    def elementProperties(self):
        js = super(SubstancePolymerMonomerSetStartingMaterial, self).elementProperties()
        js.extend([
            ("material", "material", CodeableConcept, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("isDefining", "isDefining", bool, False, None, False),
            ("amount", "amount", SubstanceAmount, False, None, False),
        ])
        return js


@dataclass
class SubstancePolymerMonomerSet(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerMonomerSet"
    ratioType: Optional[CodeableConcept] = None
    startingMaterial: Optional[List[SubstancePolymerMonomerSetStartingMaterial]] = empty_list()

    def elementProperties(self):
        js = super(SubstancePolymerMonomerSet, self).elementProperties()
        js.extend([
            ("ratioType", "ratioType", CodeableConcept, False, None, False),
            ("startingMaterial", "startingMaterial", SubstancePolymerMonomerSetStartingMaterial, True, None, False),
        ])
        return js


@dataclass
class SubstancePolymerRepeat(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeat"
    numberOfUnits: Optional[int] = None
    averageMolecularFormula: Optional[str] = None
    repeatUnitAmountType: Optional[CodeableConcept] = None
    repeatUnit: Optional[List[SubstancePolymerRepeatRepeatUnit]] = empty_list()

    def elementProperties(self):
        js = super(SubstancePolymerRepeat, self).elementProperties()
        js.extend([
            ("numberOfUnits", "numberOfUnits", int, False, None, False),
            ("averageMolecularFormula", "averageMolecularFormula", str, False, None, False),
            ("repeatUnitAmountType", "repeatUnitAmountType", CodeableConcept, False, None, False),
            ("repeatUnit", "repeatUnit", SubstancePolymerRepeatRepeatUnit, True, None, False),
        ])
        return js


@dataclass
class SubstancePolymer(DomainResource):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymer"
    class_fhir: Optional[CodeableConcept] = None
    geometry: Optional[CodeableConcept] = None
    copolymerConnectivity: Optional[List[CodeableConcept]] = empty_list()
    modification: Optional[List[str]] = empty_list()
    monomerSet: Optional[List[SubstancePolymerMonomerSet]] = empty_list()
    repeat: Optional[List[SubstancePolymerRepeat]] = empty_list()

    def elementProperties(self):
        js = super(SubstancePolymer, self).elementProperties()
        js.extend([
            ("class_fhir", "class", CodeableConcept, False, None, False),
            ("geometry", "geometry", CodeableConcept, False, None, False),
            ("copolymerConnectivity", "copolymerConnectivity", CodeableConcept, True, None, False),
            ("modification", "modification", str, True, None, False),
            ("monomerSet", "monomerSet", SubstancePolymerMonomerSet, True, None, False),
            ("repeat", "repeat", SubstancePolymerRepeat, True, None, False),
        ])
        return js