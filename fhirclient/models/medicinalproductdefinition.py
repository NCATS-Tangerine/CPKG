#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/MedicinalProductDefinition) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .marketingstatus import MarketingStatus


@dataclass
class MedicinalProductDefinitionNameNamePart(BackboneElement):
    """ Coding words or phrases of the name.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionNameNamePart"
    part: str = None
    type: Coding = None

    def elementProperties(self):
        js = super(MedicinalProductDefinitionNameNamePart, self).elementProperties()
        js.extend([
            ("part", "part", str, False, None, True),
            ("type", "type", Coding, False, None, True),
        ])
        return js


@dataclass
class MedicinalProductDefinitionNameCountryLanguage(BackboneElement):
    """ Country where the name applies.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionNameCountryLanguage"
    country: CodeableConcept = None
    jurisdiction: Optional[CodeableConcept] = None
    language: CodeableConcept = None

    def elementProperties(self):
        js = super(MedicinalProductDefinitionNameCountryLanguage, self).elementProperties()
        js.extend([
            ("country", "country", CodeableConcept, False, None, True),
            ("jurisdiction", "jurisdiction", CodeableConcept, False, None, False),
            ("language", "language", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class MedicinalProductDefinitionContact(BackboneElement):
    """ A product specific contact, person (in a role), or an organization.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionContact"
    type: Optional[CodeableConcept] = None
    contact: FHIRReference = None

    def elementProperties(self):
        js = super(MedicinalProductDefinitionContact, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("contact", "contact", FHIRReference, False, None, True),
        ])
        return js


@dataclass
class MedicinalProductDefinitionName(BackboneElement):
    """ The product's name, including full name and possibly coded parts.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionName"
    productName: str = None
    type: Optional[Coding] = None
    namePart: Optional[List[MedicinalProductDefinitionNameNamePart]] = empty_list()
    countryLanguage: Optional[List[MedicinalProductDefinitionNameCountryLanguage]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductDefinitionName, self).elementProperties()
        js.extend([
            ("productName", "productName", str, False, None, True),
            ("type", "type", Coding, False, None, False),
            ("namePart", "namePart", MedicinalProductDefinitionNameNamePart, True, None, False),
            ("countryLanguage", "countryLanguage", MedicinalProductDefinitionNameCountryLanguage, True, None, False),
        ])
        return js


@dataclass
class MedicinalProductDefinitionManufacturingBusinessOperation(BackboneElement):
    """ An operation applied to the product, for manufacturing or adminsitrative
    purpose.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionManufacturingBusinessOperation"
    operationType: Optional[CodeableConcept] = None
    authorisationReferenceNumber: Optional[Identifier] = None
    effectiveDate: Optional[FHIRDate] = None
    confidentialityIndicator: Optional[CodeableConcept] = None
    manufacturer: Optional[List[FHIRReference]] = empty_list()
    regulator: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(MedicinalProductDefinitionManufacturingBusinessOperation, self).elementProperties()
        js.extend([
            ("operationType", "operationType", CodeableConcept, False, None, False),
            ("authorisationReferenceNumber", "authorisationReferenceNumber", Identifier, False, None, False),
            ("effectiveDate", "effectiveDate", FHIRDate, False, None, False),
            ("confidentialityIndicator", "confidentialityIndicator", CodeableConcept, False, None, False),
            ("manufacturer", "manufacturer", FHIRReference, True, None, False),
            ("regulator", "regulator", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class MedicinalProductDefinitionSpecialDesignation(BackboneElement):
    """ Indicates if the medicinal product has an orphan designation for the
    treatment of a rare disease.
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinitionSpecialDesignation"
    identifier: Optional[List[Identifier]] = empty_list()
    type: Optional[CodeableConcept] = None
    intendedUse: Optional[CodeableConcept] = None
    indicationCodeableConcept: Optional[CodeableConcept] = None
    indicationReference: Optional[FHIRReference] = None
    status: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    species: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MedicinalProductDefinitionSpecialDesignation, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("intendedUse", "intendedUse", CodeableConcept, False, None, False),
            ("indicationCodeableConcept", "indicationCodeableConcept", CodeableConcept, False, "indication", False),
            ("indicationReference", "indicationReference", FHIRReference, False, "indication", False),
            ("status", "status", CodeableConcept, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("species", "species", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class MedicinalProductDefinition(DomainResource):
    """ Detailed definition of a medicinal product, typically for uses other than
    direct patient care (e.g. regulatory use).
    """
    resource_type: ClassVar[str] = "MedicinalProductDefinition"
    identifier: Optional[List[Identifier]] = empty_list()
    type: Optional[CodeableConcept] = None
    domain: Optional[Coding] = None
    description: Optional[str] = None
    combinedPharmaceuticalDoseForm: Optional[CodeableConcept] = None
    indication: Optional[str] = None
    legalStatusOfSupply: Optional[CodeableConcept] = None
    additionalMonitoringIndicator: Optional[CodeableConcept] = None
    specialMeasures: Optional[List[str]] = empty_list()
    paediatricUseIndicator: Optional[CodeableConcept] = None
    productClassification: Optional[List[CodeableConcept]] = empty_list()
    marketingStatus: Optional[List[MarketingStatus]] = empty_list()
    pharmaceuticalProduct: Optional[List[FHIRReference]] = empty_list()
    packagedMedicinalProduct: Optional[List[FHIRReference]] = empty_list()
    attachedDocument: Optional[List[FHIRReference]] = empty_list()
    masterFile: Optional[List[FHIRReference]] = empty_list()
    contact: Optional[List[MedicinalProductDefinitionContact]] = empty_list()
    clinicalTrial: Optional[List[FHIRReference]] = empty_list()
    name: List[MedicinalProductDefinitionName] = empty_list()
    crossReference: Optional[List[Identifier]] = empty_list()
    manufacturingBusinessOperation: Optional[List[MedicinalProductDefinitionManufacturingBusinessOperation]] = empty_list()
    specialDesignation: Optional[List[MedicinalProductDefinitionSpecialDesignation]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductDefinition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("domain", "domain", Coding, False, None, False),
            ("description", "description", str, False, None, False),
            ("combinedPharmaceuticalDoseForm", "combinedPharmaceuticalDoseForm", CodeableConcept, False, None, False),
            ("indication", "indication", str, False, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", CodeableConcept, False, None, False),
            ("additionalMonitoringIndicator", "additionalMonitoringIndicator", CodeableConcept, False, None, False),
            ("specialMeasures", "specialMeasures", str, True, None, False),
            ("paediatricUseIndicator", "paediatricUseIndicator", CodeableConcept, False, None, False),
            ("productClassification", "productClassification", CodeableConcept, True, None, False),
            ("marketingStatus", "marketingStatus", MarketingStatus, True, None, False),
            ("pharmaceuticalProduct", "pharmaceuticalProduct", FHIRReference, True, None, False),
            ("packagedMedicinalProduct", "packagedMedicinalProduct", FHIRReference, True, None, False),
            ("attachedDocument", "attachedDocument", FHIRReference, True, None, False),
            ("masterFile", "masterFile", FHIRReference, True, None, False),
            ("contact", "contact", MedicinalProductDefinitionContact, True, None, False),
            ("clinicalTrial", "clinicalTrial", FHIRReference, True, None, False),
            ("name", "name", MedicinalProductDefinitionName, True, None, True),
            ("crossReference", "crossReference", Identifier, True, None, False),
            ("manufacturingBusinessOperation", "manufacturingBusinessOperation", MedicinalProductDefinitionManufacturingBusinessOperation, True, None, False),
            ("specialDesignation", "specialDesignation", MedicinalProductDefinitionSpecialDesignation, True, None, False),
        ])
        return js