#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/AdministrableProductDefinition) on 2019-08-06.
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
class AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod(BackboneElement):
    """ A species specific time during which consumption of animal product is not
    appropriate.
    """
    resource_type: ClassVar[str] = "AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod"
    tissue: CodeableConcept = None
    value: Quantity = None
    supportingInformation: Optional[str] = None

    def elementProperties(self):
        js = super(AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod, self).elementProperties()
        js.extend([
            ("tissue", "tissue", CodeableConcept, False, None, True),
            ("value", "value", Quantity, False, None, True),
            ("supportingInformation", "supportingInformation", str, False, None, False),
        ])
        return js


@dataclass
class AdministrableProductDefinitionRouteOfAdministrationTargetSpecies(BackboneElement):
    """ A species for which this route applies.
    """
    resource_type: ClassVar[str] = "AdministrableProductDefinitionRouteOfAdministrationTargetSpecies"
    code: CodeableConcept = None
    withdrawalPeriod: Optional[List[AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod]] = empty_list()

    def elementProperties(self):
        js = super(AdministrableProductDefinitionRouteOfAdministrationTargetSpecies, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("withdrawalPeriod", "withdrawalPeriod", AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod, True, None, False),
        ])
        return js


@dataclass
class AdministrableProductDefinitionCharacteristics(BackboneElement):
    """ Characteristics e.g. a products onset of action.
    """
    resource_type: ClassVar[str] = "AdministrableProductDefinitionCharacteristics"
    code: CodeableConcept = None
    status: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(AdministrableProductDefinitionCharacteristics, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("status", "status", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class AdministrableProductDefinitionRouteOfAdministration(BackboneElement):
    """ The path by which the pharmaceutical product is taken into or makes contact
    with the body.
    """
    resource_type: ClassVar[str] = "AdministrableProductDefinitionRouteOfAdministration"
    code: CodeableConcept = None
    firstDose: Optional[Quantity] = None
    maxSingleDose: Optional[Quantity] = None
    maxDosePerDay: Optional[Quantity] = None
    maxDosePerTreatmentPeriod: Optional[Ratio] = None
    maxTreatmentPeriod: Optional[Duration] = None
    targetSpecies: Optional[List[AdministrableProductDefinitionRouteOfAdministrationTargetSpecies]] = empty_list()

    def elementProperties(self):
        js = super(AdministrableProductDefinitionRouteOfAdministration, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("firstDose", "firstDose", Quantity, False, None, False),
            ("maxSingleDose", "maxSingleDose", Quantity, False, None, False),
            ("maxDosePerDay", "maxDosePerDay", Quantity, False, None, False),
            ("maxDosePerTreatmentPeriod", "maxDosePerTreatmentPeriod", Ratio, False, None, False),
            ("maxTreatmentPeriod", "maxTreatmentPeriod", Duration, False, None, False),
            ("targetSpecies", "targetSpecies", AdministrableProductDefinitionRouteOfAdministrationTargetSpecies, True, None, False),
        ])
        return js


@dataclass
class AdministrableProductDefinition(DomainResource):
    """ A pharmaceutical product described in terms of its composition and dose
    form.
    """
    resource_type: ClassVar[str] = "AdministrableProductDefinition"
    identifier: Optional[List[Identifier]] = empty_list()
    subject: Optional[List[FHIRReference]] = empty_list()
    administrableDoseForm: CodeableConcept = None
    unitOfPresentation: Optional[CodeableConcept] = None
    ingredient: Optional[List[FHIRReference]] = empty_list()
    device: Optional[List[FHIRReference]] = empty_list()
    characteristics: Optional[List[AdministrableProductDefinitionCharacteristics]] = empty_list()
    routeOfAdministration: List[AdministrableProductDefinitionRouteOfAdministration] = empty_list()

    def elementProperties(self):
        js = super(AdministrableProductDefinition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("subject", "subject", FHIRReference, True, None, False),
            ("administrableDoseForm", "administrableDoseForm", CodeableConcept, False, None, True),
            ("unitOfPresentation", "unitOfPresentation", CodeableConcept, False, None, False),
            ("ingredient", "ingredient", FHIRReference, True, None, False),
            ("device", "device", FHIRReference, True, None, False),
            ("characteristics", "characteristics", AdministrableProductDefinitionCharacteristics, True, None, False),
            ("routeOfAdministration", "routeOfAdministration", AdministrableProductDefinitionRouteOfAdministration, True, None, True),
        ])
        return js