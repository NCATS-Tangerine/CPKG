#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Group) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range


@dataclass
class GroupCharacteristic(BackboneElement):
    """ Include / Exclude group members by Trait.

    Identifies traits whose presence r absence is shared by members of the
    group.
    """
    resource_type: ClassVar[str] = "GroupCharacteristic"
    code: CodeableConcept = None
    valueCodeableConcept: CodeableConcept = None
    valueBoolean: bool = None
    valueQuantity: Quantity = None
    valueRange: Range = None
    valueReference: FHIRReference = None
    exclude: bool = None
    period: Optional[Period] = None

    def elementProperties(self):
        js = super(GroupCharacteristic, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", True),
            ("valueRange", "valueRange", Range, False, "value", True),
            ("valueReference", "valueReference", FHIRReference, False, "value", True),
            ("exclude", "exclude", bool, False, None, True),
            ("period", "period", Period, False, None, False),
        ])
        return js


@dataclass
class GroupMember(BackboneElement):
    """ Who or what is in group.

    Identifies the resource instances that are members of the group.
    """
    resource_type: ClassVar[str] = "GroupMember"
    entity: FHIRReference = None
    period: Optional[Period] = None
    inactive: Optional[bool] = None

    def elementProperties(self):
        js = super(GroupMember, self).elementProperties()
        js.extend([
            ("entity", "entity", FHIRReference, False, None, True),
            ("period", "period", Period, False, None, False),
            ("inactive", "inactive", bool, False, None, False),
        ])
        return js


@dataclass
class Group(DomainResource):
    """ Group of multiple entities.

    Represents a defined collection of entities that may be discussed or acted
    upon collectively but which are not expected to act collectively, and are
    not formally or legally recognized; i.e. a collection of entities that
    isn't an Organization.
    """
    resource_type: ClassVar[str] = "Group"
    identifier: Optional[List[Identifier]] = empty_list()
    active: Optional[bool] = None
    type: str = None
    actual: bool = None
    code: Optional[CodeableConcept] = None
    name: Optional[str] = None
    quantity: Optional[int] = None
    managingEntity: Optional[FHIRReference] = None
    characteristic: Optional[List[GroupCharacteristic]] = empty_list()
    member: Optional[List[GroupMember]] = empty_list()

    def elementProperties(self):
        js = super(Group, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("active", "active", bool, False, None, False),
            ("type", "type", str, False, None, True),
            ("actual", "actual", bool, False, None, True),
            ("code", "code", CodeableConcept, False, None, False),
            ("name", "name", str, False, None, False),
            ("quantity", "quantity", int, False, None, False),
            ("managingEntity", "managingEntity", FHIRReference, False, None, False),
            ("characteristic", "characteristic", GroupCharacteristic, True, None, False),
            ("member", "member", GroupMember, True, None, False),
        ])
        return js