#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Endpoint) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class Endpoint(DomainResource):
    """ The technical details of an endpoint that can be used for electronic
    services.

    The technical details of an endpoint that can be used for electronic
    services, such as for web services providing XDS.b or a REST endpoint for
    another FHIR server. This may include any security context information.
    """
    resource_type: ClassVar[str] = "Endpoint"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    connectionType: Coding = None
    name: Optional[str] = None
    managingOrganization: Optional[FHIRReference] = None
    contact: Optional[List[ContactPoint]] = empty_list()
    period: Optional[Period] = None
    payloadType: List[CodeableConcept] = empty_list()
    payloadMimeType: Optional[List[str]] = empty_list()
    address: str = None
    header: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(Endpoint, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("connectionType", "connectionType", Coding, False, None, True),
            ("name", "name", str, False, None, False),
            ("managingOrganization", "managingOrganization", FHIRReference, False, None, False),
            ("contact", "contact", ContactPoint, True, None, False),
            ("period", "period", Period, False, None, False),
            ("payloadType", "payloadType", CodeableConcept, True, None, True),
            ("payloadMimeType", "payloadMimeType", str, True, None, False),
            ("address", "address", str, False, None, True),
            ("header", "header", str, True, None, False),
        ])
        return js