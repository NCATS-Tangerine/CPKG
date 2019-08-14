#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Flag) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class Flag(DomainResource):
    """ Key information to flag to healthcare providers.

    Prospective warnings of potential issues when providing care to the
    patient.
    """
    resource_type: ClassVar[str] = "Flag"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    category: Optional[List[CodeableConcept]] = empty_list()
    code: CodeableConcept = None
    subject: FHIRReference = None
    period: Optional[Period] = None
    encounter: Optional[FHIRReference] = None
    author: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(Flag, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("category", "category", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, True),
            ("subject", "subject", FHIRReference, False, None, True),
            ("period", "period", Period, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("author", "author", FHIRReference, False, None, False),
        ])
        return js