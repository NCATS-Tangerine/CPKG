#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Media) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .attachment import Attachment
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class Media(DomainResource):
    """ A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """
    resource_type: ClassVar[str] = "Media"
    identifier: Optional[List[Identifier]] = empty_list()
    basedOn: Optional[List[FHIRReference]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    type: Optional[CodeableConcept] = None
    modality: Optional[CodeableConcept] = None
    view: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    createdDateTime: Optional[FHIRDate] = None
    createdPeriod: Optional[Period] = None
    issued: Optional[FHIRDate] = None
    operator: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    bodySite: Optional[CodeableConcept] = None
    deviceName: Optional[str] = None
    device: Optional[FHIRReference] = None
    height: Optional[int] = None
    width: Optional[int] = None
    frames: Optional[int] = None
    duration: Optional[float] = None
    content: Attachment = None
    note: Optional[List[Annotation]] = empty_list()

    def elementProperties(self):
        js = super(Media, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", CodeableConcept, False, None, False),
            ("modality", "modality", CodeableConcept, False, None, False),
            ("view", "view", CodeableConcept, False, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("createdDateTime", "createdDateTime", FHIRDate, False, "created", False),
            ("createdPeriod", "createdPeriod", Period, False, "created", False),
            ("issued", "issued", FHIRDate, False, None, False),
            ("operator", "operator", FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("deviceName", "deviceName", str, False, None, False),
            ("device", "device", FHIRReference, False, None, False),
            ("height", "height", int, False, None, False),
            ("width", "width", int, False, None, False),
            ("frames", "frames", int, False, None, False),
            ("duration", "duration", float, False, None, False),
            ("content", "content", Attachment, False, None, True),
            ("note", "note", Annotation, True, None, False),
        ])
        return js