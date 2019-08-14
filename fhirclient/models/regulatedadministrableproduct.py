#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/RegulatedAdministrableProduct) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class RegulatedAdministrableProductRouteOfAdministrationTargetSpeciesWithdrawalPeriod(BackboneElement):
    """ A species specific time during which consumption of animal product is not
    appropriate.
    """
    resource_type: ClassVar[str] = "RegulatedAdministrableProductRouteOfAdministrationTargetSpeciesWithdrawalPeriod"
    tissue: CodeableConcept = None
    value: Quantity = None
    supportingInformation: Optional[str] = None

    def elementProperties(self):
        js = super(RegulatedAdministrableProductRouteOfAdministrationTargetSpeciesWithdrawalPeriod, self).elementProperties()
        js.extend([
            ("tissue", "tissue", CodeableConcept, False, None, True),
            ("value", "value", Quantity, False, None, True),
            ("supportingInformation", "supportingInformation", str, False, None, False),
        ])
        return js


@dataclass
class RegulatedAdministrableProductRouteOfAdministrationTargetSpecies(BackboneElement):
    """ A species for which this route applies.
    """
    resource_type: ClassVar[str] = "RegulatedAdministrableProductRouteOfAdministrationTargetSpecies"
    code: CodeableConcept = None
    withdrawalPeriod: Optional[List[RegulatedAdministrableProductRouteOfAdministrationTargetSpeciesWithdrawalPeriod]] = empty_list()

    def elementProperties(self):
        js = super(RegulatedAdministrableProductRouteOfAdministrationTargetSpecies, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("withdrawalPeriod", "withdrawalPeriod", RegulatedAdministrableProductRouteOfAdministrationTargetSpeciesWithdrawalPeriod, True, None, False),
        ])
        return js


@dataclass
class RegulatedAdministrableProductCharacteristics(BackboneElement):
    """ Characteristics e.g. a products onset of action.
    """
    resource_type: ClassVar[str] = "RegulatedAdministrableProductCharacteristics"
    code: CodeableConcept = None
    status: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(RegulatedAdministrableProductCharacteristics, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("status", "status", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class RegulatedAdministrableProductRouteOfAdministration(BackboneElement):
    """ The path by which the pharmaceutical product is taken into or makes contact
    with the body.
    """
    resource_type: ClassVar[str] = "RegulatedAdministrableProductRouteOfAdministration"
    code: CodeableConcept = None
    firstDose: Optional[Quantity] = None
    maxSingleDose: Optional[Quantity] = None
    maxDosePerDay: Optional[Quantity] = None
    maxDosePerTreatmentPeriod: Optional[Ratio] = None
    maxTreatmentPeriod: Optional[Duration] = None
    targetSpecies: Optional[List[RegulatedAdministrableProductRouteOfAdministrationTargetSpecies]] = empty_list()

    def elementProperties(self):
        js = super(RegulatedAdministrableProductRouteOfAdministration, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("firstDose", "firstDose", Quantity, False, None, False),
            ("maxSingleDose", "maxSingleDose", Quantity, False, None, False),
            ("maxDosePerDay", "maxDosePerDay", Quantity, False, None, False),
            ("maxDosePerTreatmentPeriod", "maxDosePerTreatmentPeriod", Ratio, False, None, False),
            ("maxTreatmentPeriod", "maxTreatmentPeriod", Duration, False, None, False),
            ("targetSpecies", "targetSpecies", RegulatedAdministrableProductRouteOfAdministrationTargetSpecies, True, None, False),
        ])
        return js


@dataclass
class RegulatedAdministrableProduct(DomainResource):
    """ A pharmaceutical product described in terms of its composition and dose
    form.
    """
    resource_type: ClassVar[str] = "RegulatedAdministrableProduct"
    identifier: Optional[List[Identifier]] = empty_list()
    subject: Optional[List[FHIRReference]] = empty_list()
    administrableDoseForm: CodeableConcept = None
    unitOfPresentation: Optional[CodeableConcept] = None
    ingredient: Optional[List[FHIRReference]] = empty_list()
    device: Optional[List[FHIRReference]] = empty_list()
    characteristics: Optional[List[RegulatedAdministrableProductCharacteristics]] = empty_list()
    routeOfAdministration: List[RegulatedAdministrableProductRouteOfAdministration] = empty_list()

    def elementProperties(self):
        js = super(RegulatedAdministrableProduct, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("subject", "subject", FHIRReference, True, None, False),
            ("administrableDoseForm", "administrableDoseForm", CodeableConcept, False, None, True),
            ("unitOfPresentation", "unitOfPresentation", CodeableConcept, False, None, False),
            ("ingredient", "ingredient", FHIRReference, True, None, False),
            ("device", "device", FHIRReference, True, None, False),
            ("characteristics", "characteristics", RegulatedAdministrableProductCharacteristics, True, None, False),
            ("routeOfAdministration", "routeOfAdministration", RegulatedAdministrableProductRouteOfAdministration, True, None, True),
        ])
        return js