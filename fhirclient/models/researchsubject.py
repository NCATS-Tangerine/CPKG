#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ResearchSubject) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class ResearchSubject(DomainResource):
    """ Physical entity which is the primary unit of interest in the study.

    A physical entity which is the primary unit of operational and/or
    administrative interest in a study.
    """
    resource_type: ClassVar[str] = "ResearchSubject"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    period: Optional[Period] = None
    study: FHIRReference = None
    individual: FHIRReference = None
    assignedArm: Optional[str] = None
    actualArm: Optional[str] = None
    consent: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(ResearchSubject, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("period", "period", Period, False, None, False),
            ("study", "study", FHIRReference, False, None, True),
            ("individual", "individual", FHIRReference, False, None, True),
            ("assignedArm", "assignedArm", str, False, None, False),
            ("actualArm", "actualArm", str, False, None, False),
            ("consent", "consent", FHIRReference, False, None, False),
        ])
        return js