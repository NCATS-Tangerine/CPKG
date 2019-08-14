#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/RegulatedAuthorization) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class RegulatedAuthorizationRelatedDate(BackboneElement):
    """ Other dates associated with the authorization. It is common for an
    authorization to have renewal dates, initial time limited phases and so on.
    """
    resource_type: ClassVar[str] = "RegulatedAuthorizationRelatedDate"
    datePeriod: Period = None
    dateDateTime: FHIRDate = None
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(RegulatedAuthorizationRelatedDate, self).elementProperties()
        js.extend([
            ("datePeriod", "datePeriod", Period, False, "date", True),
            ("dateDateTime", "dateDateTime", FHIRDate, False, "date", True),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class RegulatedAuthorizationCase(BackboneElement):
    """ The case or regulatory procedure for granting or amending a marketing
    authorization.
    """
    resource_type: ClassVar[str] = "RegulatedAuthorizationCase"
    identifier: Optional[Identifier] = None
    type: Optional[CodeableConcept] = None
    status: Optional[CodeableConcept] = None
    datePeriod: Optional[Period] = None
    dateDateTime: Optional[FHIRDate] = None
    application: Optional[List["RegulatedAuthorizationCase"]] = empty_list()

    def elementProperties(self):
        js = super(RegulatedAuthorizationCase, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("status", "status", CodeableConcept, False, None, False),
            ("datePeriod", "datePeriod", Period, False, "date", False),
            ("dateDateTime", "dateDateTime", FHIRDate, False, "date", False),
            ("application", "application", RegulatedAuthorizationCase, True, None, False),
        ])
        return js


@dataclass
class RegulatedAuthorization(DomainResource):
    """ The regulatory authorization of a medicinal product.
    """
    resource_type: ClassVar[str] = "RegulatedAuthorization"
    identifier: Optional[List[Identifier]] = empty_list()
    subject: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None
    description: Optional[str] = None
    region: Optional[List[CodeableConcept]] = empty_list()
    status: Optional[CodeableConcept] = None
    statusDate: Optional[FHIRDate] = None
    validityPeriod: Optional[Period] = None
    basis: Optional[List[CodeableConcept]] = empty_list()
    relatedDate: Optional[List[RegulatedAuthorizationRelatedDate]] = empty_list()
    jurisdictionalAuthorization: Optional[List[FHIRReference]] = empty_list()
    holder: Optional[FHIRReference] = None
    regulator: Optional[FHIRReference] = None
    case: Optional[RegulatedAuthorizationCase] = None

    def elementProperties(self):
        js = super(RegulatedAuthorization, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("region", "region", CodeableConcept, True, None, False),
            ("status", "status", CodeableConcept, False, None, False),
            ("statusDate", "statusDate", FHIRDate, False, None, False),
            ("validityPeriod", "validityPeriod", Period, False, None, False),
            ("basis", "basis", CodeableConcept, True, None, False),
            ("relatedDate", "relatedDate", RegulatedAuthorizationRelatedDate, True, None, False),
            ("jurisdictionalAuthorization", "jurisdictionalAuthorization", FHIRReference, True, None, False),
            ("holder", "holder", FHIRReference, False, None, False),
            ("regulator", "regulator", FHIRReference, False, None, False),
            ("case", "case", RegulatedAuthorizationCase, False, None, False),
        ])
        return js