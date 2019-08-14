#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/GuidanceResponse) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .codeableconcept import CodeableConcept
from .datarequirement import DataRequirement
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class GuidanceResponse(DomainResource):
    """ The formal response to a guidance request.

    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """
    resource_type: ClassVar[str] = "GuidanceResponse"
    requestIdentifier: Optional[Identifier] = None
    identifier: Optional[List[Identifier]] = empty_list()
    moduleUri: str = None
    moduleCanonical: str = None
    moduleCodeableConcept: CodeableConcept = None
    status: str = None
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = None
    performer: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    evaluationMessage: Optional[List[FHIRReference]] = empty_list()
    outputParameters: Optional[FHIRReference] = None
    result: Optional[FHIRReference] = None
    dataRequirement: Optional[List[DataRequirement]] = empty_list()

    def elementProperties(self):
        js = super(GuidanceResponse, self).elementProperties()
        js.extend([
            ("requestIdentifier", "requestIdentifier", Identifier, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("moduleUri", "moduleUri", str, False, "module", True),
            ("moduleCanonical", "moduleCanonical", str, False, "module", True),
            ("moduleCodeableConcept", "moduleCodeableConcept", CodeableConcept, False, "module", True),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, None, False),
            ("performer", "performer", FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("evaluationMessage", "evaluationMessage", FHIRReference, True, None, False),
            ("outputParameters", "outputParameters", FHIRReference, False, None, False),
            ("result", "result", FHIRReference, False, None, False),
            ("dataRequirement", "dataRequirement", DataRequirement, True, None, False),
        ])
        return js