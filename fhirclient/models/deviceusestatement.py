#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .timing import Timing


@dataclass
class DeviceUseStatement(DomainResource):
    """ Record of use of a device.

    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """
    resource_type: ClassVar[str] = "DeviceUseStatement"
    identifier: Optional[List[Identifier]] = empty_list()
    basedOn: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    subject: FHIRReference = None
    derivedFrom: Optional[List[FHIRReference]] = empty_list()
    timingTiming: Optional[Timing] = None
    timingPeriod: Optional[Period] = None
    timingDateTime: Optional[FHIRDate] = None
    recordedOn: Optional[FHIRDate] = None
    source: Optional[FHIRReference] = None
    device: FHIRReference = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    bodySite: Optional[CodeableConcept] = None
    note: Optional[List[Annotation]] = empty_list()

    def elementProperties(self):
        js = super(DeviceUseStatement, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, True),
            ("derivedFrom", "derivedFrom", FHIRReference, True, None, False),
            ("timingTiming", "timingTiming", Timing, False, "timing", False),
            ("timingPeriod", "timingPeriod", Period, False, "timing", False),
            ("timingDateTime", "timingDateTime", FHIRDate, False, "timing", False),
            ("recordedOn", "recordedOn", FHIRDate, False, None, False),
            ("source", "source", FHIRReference, False, None, False),
            ("device", "device", FHIRReference, False, None, True),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("note", "note", Annotation, True, None, False),
        ])
        return js