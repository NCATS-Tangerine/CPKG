#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Location) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class LocationPosition(BackboneElement):
    """ The absolute geographic location.

    The absolute geographic location of the Location, expressed using the WGS84
    datum (This is the same co-ordinate system used in KML).
    """
    resource_type: ClassVar[str] = "LocationPosition"
    longitude: float = None
    latitude: float = None
    altitude: Optional[float] = None

    def elementProperties(self):
        js = super(LocationPosition, self).elementProperties()
        js.extend([
            ("longitude", "longitude", float, False, None, True),
            ("latitude", "latitude", float, False, None, True),
            ("altitude", "altitude", float, False, None, False),
        ])
        return js


@dataclass
class LocationHoursOfOperation(BackboneElement):
    """ What days/times during a week is this location usually open.
    """
    resource_type: ClassVar[str] = "LocationHoursOfOperation"
    daysOfWeek: Optional[List[str]] = empty_list()
    allDay: Optional[bool] = None
    openingTime: Optional[FHIRDate] = None
    closingTime: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(LocationHoursOfOperation, self).elementProperties()
        js.extend([
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
            ("allDay", "allDay", bool, False, None, False),
            ("openingTime", "openingTime", FHIRDate, False, None, False),
            ("closingTime", "closingTime", FHIRDate, False, None, False),
        ])
        return js


@dataclass
class Location(DomainResource):
    """ Details and position information for a physical place.

    Details and position information for a physical place where services are
    provided and resources and participants may be stored, found, contained, or
    accommodated.
    """
    resource_type: ClassVar[str] = "Location"
    identifier: Optional[List[Identifier]] = empty_list()
    status: Optional[str] = None
    operationalStatus: Optional[Coding] = None
    name: Optional[str] = None
    alias: Optional[List[str]] = empty_list()
    description: Optional[str] = None
    mode: Optional[str] = None
    type: Optional[List[CodeableConcept]] = empty_list()
    telecom: Optional[List[ContactPoint]] = empty_list()
    address: Optional[Address] = None
    physicalType: Optional[CodeableConcept] = None
    position: Optional[LocationPosition] = None
    managingOrganization: Optional[FHIRReference] = None
    partOf: Optional[FHIRReference] = None
    hoursOfOperation: Optional[List[LocationHoursOfOperation]] = empty_list()
    availabilityExceptions: Optional[str] = None
    endpoint: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(Location, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, False),
            ("operationalStatus", "operationalStatus", Coding, False, None, False),
            ("name", "name", str, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("description", "description", str, False, None, False),
            ("mode", "mode", str, False, None, False),
            ("type", "type", CodeableConcept, True, None, False),
            ("telecom", "telecom", ContactPoint, True, None, False),
            ("address", "address", Address, False, None, False),
            ("physicalType", "physicalType", CodeableConcept, False, None, False),
            ("position", "position", LocationPosition, False, None, False),
            ("managingOrganization", "managingOrganization", FHIRReference, False, None, False),
            ("partOf", "partOf", FHIRReference, False, None, False),
            ("hoursOfOperation", "hoursOfOperation", LocationHoursOfOperation, True, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("endpoint", "endpoint", FHIRReference, True, None, False),
        ])
        return js