#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/SubstanceDefinition) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .range import Range
from .ratio import Ratio


@dataclass
class SubstanceDefinitionNameOfficial(BackboneElement):
    """ Details of the official nature of this name.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionNameOfficial"
    authority: Optional[CodeableConcept] = None
    status: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(SubstanceDefinitionNameOfficial, self).elementProperties()
        js.extend([
            ("authority", "authority", CodeableConcept, False, None, False),
            ("status", "status", CodeableConcept, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
        ])
        return js


@dataclass
class SubstanceDefinitionStructureIsotopeMolecularWeight(BackboneElement):
    """ The molecular weight or weight range (for proteins, polymers or nucleic
    acids).
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionStructureIsotopeMolecularWeight"
    method: Optional[CodeableConcept] = None
    type: Optional[CodeableConcept] = None
    amount: Optional[Quantity] = None

    def elementProperties(self):
        js = super(SubstanceDefinitionStructureIsotopeMolecularWeight, self).elementProperties()
        js.extend([
            ("method", "method", CodeableConcept, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("amount", "amount", Quantity, False, None, False),
        ])
        return js


@dataclass
class SubstanceDefinitionStructureIsotope(BackboneElement):
    """ Applicable for single substances that contain a radionuclide or a non-
    natural isotopic ratio.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionStructureIsotope"
    identifier: Optional[Identifier] = None
    name: Optional[CodeableConcept] = None
    substitution: Optional[CodeableConcept] = None
    halfLife: Optional[Quantity] = None
    molecularWeight: Optional[SubstanceDefinitionStructureIsotopeMolecularWeight] = None

    def elementProperties(self):
        js = super(SubstanceDefinitionStructureIsotope, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("name", "name", CodeableConcept, False, None, False),
            ("substitution", "substitution", CodeableConcept, False, None, False),
            ("halfLife", "halfLife", Quantity, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceDefinitionStructureIsotopeMolecularWeight, False, None, False),
        ])
        return js


@dataclass
class SubstanceDefinitionStructureRepresentation(BackboneElement):
    """ Molecular structural representation.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionStructureRepresentation"
    type: Optional[CodeableConcept] = None
    representation: Optional[str] = None
    attachment: Optional[Attachment] = None

    def elementProperties(self):
        js = super(SubstanceDefinitionStructureRepresentation, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, False),
            ("representation", "representation", str, False, None, False),
            ("attachment", "attachment", Attachment, False, None, False),
        ])
        return js


@dataclass
class SubstanceDefinitionMoiety(BackboneElement):
    """ Moiety, for structural modifications.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionMoiety"
    role: Optional[CodeableConcept] = None
    identifier: Optional[Identifier] = None
    name: Optional[str] = None
    stereochemistry: Optional[CodeableConcept] = None
    opticalActivity: Optional[CodeableConcept] = None
    molecularFormula: Optional[str] = None
    amountQuantity: Optional[Quantity] = None
    amountString: Optional[str] = None
    amountType: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceDefinitionMoiety, self).elementProperties()
        js.extend([
            ("role", "role", CodeableConcept, False, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("name", "name", str, False, None, False),
            ("stereochemistry", "stereochemistry", CodeableConcept, False, None, False),
            ("opticalActivity", "opticalActivity", CodeableConcept, False, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("amountQuantity", "amountQuantity", Quantity, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("amountType", "amountType", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceDefinitionProperty(BackboneElement):
    """ General specifications for this substance, including how it is related to
    other substances.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionProperty"
    category: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    parameters: Optional[str] = None
    definingSubstanceReference: Optional[FHIRReference] = None
    definingSubstanceCodeableConcept: Optional[CodeableConcept] = None
    amountQuantity: Optional[Quantity] = None
    amountString: Optional[str] = None
    referenceRange: Optional[Range] = None
    source: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceDefinitionProperty, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("parameters", "parameters", str, False, None, False),
            ("definingSubstanceReference", "definingSubstanceReference", FHIRReference, False, "definingSubstance", False),
            ("definingSubstanceCodeableConcept", "definingSubstanceCodeableConcept", CodeableConcept, False, "definingSubstance", False),
            ("amountQuantity", "amountQuantity", Quantity, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("referenceRange", "referenceRange", Range, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class SubstanceDefinitionStructure(BackboneElement):
    """ Structural information.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionStructure"
    stereochemistry: Optional[CodeableConcept] = None
    opticalActivity: Optional[CodeableConcept] = None
    molecularFormula: Optional[str] = None
    molecularFormulaByMoiety: Optional[str] = None
    isotope: Optional[List[SubstanceDefinitionStructureIsotope]] = empty_list()
    molecularWeight: Optional[SubstanceDefinitionStructureIsotopeMolecularWeight] = None
    source: Optional[List[FHIRReference]] = empty_list()
    representation: Optional[List[SubstanceDefinitionStructureRepresentation]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceDefinitionStructure, self).elementProperties()
        js.extend([
            ("stereochemistry", "stereochemistry", CodeableConcept, False, None, False),
            ("opticalActivity", "opticalActivity", CodeableConcept, False, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("molecularFormulaByMoiety", "molecularFormulaByMoiety", str, False, None, False),
            ("isotope", "isotope", SubstanceDefinitionStructureIsotope, True, None, False),
            ("molecularWeight", "molecularWeight", SubstanceDefinitionStructureIsotopeMolecularWeight, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
            ("representation", "representation", SubstanceDefinitionStructureRepresentation, True, None, False),
        ])
        return js


@dataclass
class SubstanceDefinitionstr(BackboneElement):
    """ Codes associated with the substance.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionstr"
    code: Optional[CodeableConcept] = None
    status: Optional[CodeableConcept] = None
    statusDate: Optional[FHIRDate] = None
    comment: Optional[str] = None
    source: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceDefinitionstr, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("status", "status", CodeableConcept, False, None, False),
            ("statusDate", "statusDate", FHIRDate, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class SubstanceDefinitionName(BackboneElement):
    """ Names applicable to this substance.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionName"
    name: str = None
    type: Optional[CodeableConcept] = None
    status: Optional[CodeableConcept] = None
    preferred: Optional[bool] = None
    language: Optional[List[CodeableConcept]] = empty_list()
    domain: Optional[List[CodeableConcept]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    synonym: Optional[List["SubstanceDefinitionName"]] = empty_list()
    translation: Optional[List["SubstanceDefinitionName"]] = empty_list()
    official: Optional[List[SubstanceDefinitionNameOfficial]] = empty_list()
    source: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceDefinitionName, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("type", "type", CodeableConcept, False, None, False),
            ("status", "status", CodeableConcept, False, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("language", "language", CodeableConcept, True, None, False),
            ("domain", "domain", CodeableConcept, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("synonym", "synonym", SubstanceDefinitionName, True, None, False),
            ("translation", "translation", SubstanceDefinitionName, True, None, False),
            ("official", "official", SubstanceDefinitionNameOfficial, True, None, False),
            ("source", "source", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class SubstanceDefinitionRelationship(BackboneElement):
    """ A link between this substance and another, with details of the relationship.
    """
    resource_type: ClassVar[str] = "SubstanceDefinitionRelationship"
    substanceDefinitionReference: Optional[FHIRReference] = None
    substanceDefinitionCodeableConcept: Optional[CodeableConcept] = None
    relationship: Optional[CodeableConcept] = None
    isDefining: Optional[bool] = None
    amountQuantity: Optional[Quantity] = None
    amountRange: Optional[Range] = None
    amountRatio: Optional[Ratio] = None
    amountString: Optional[str] = None
    amountRatioLowLimit: Optional[Ratio] = None
    amountType: Optional[CodeableConcept] = None
    source: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceDefinitionRelationship, self).elementProperties()
        js.extend([
            ("substanceDefinitionReference", "substanceDefinitionReference", FHIRReference, False, "substanceDefinition", False),
            ("substanceDefinitionCodeableConcept", "substanceDefinitionCodeableConcept", CodeableConcept, False, "substanceDefinition", False),
            ("relationship", "relationship", CodeableConcept, False, None, False),
            ("isDefining", "isDefining", bool, False, None, False),
            ("amountQuantity", "amountQuantity", Quantity, False, "amount", False),
            ("amountRange", "amountRange", Range, False, "amount", False),
            ("amountRatio", "amountRatio", Ratio, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("amountRatioLowLimit", "amountRatioLowLimit", Ratio, False, None, False),
            ("amountType", "amountType", CodeableConcept, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class SubstanceDefinition(DomainResource):
    """ The detailed description of a substance, typically at a level beyond what
    is used for prescribing.
    """
    resource_type: ClassVar[str] = "SubstanceDefinition"
    identifier: Optional[Identifier] = None
    status: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    domain: Optional[CodeableConcept] = None
    description: Optional[str] = None
    source: Optional[List[FHIRReference]] = empty_list()
    comment: Optional[str] = None
    moiety: Optional[List[SubstanceDefinitionMoiety]] = empty_list()
    property: Optional[List[SubstanceDefinitionProperty]] = empty_list()
    referenceInformation: Optional[FHIRReference] = None
    structure: Optional[SubstanceDefinitionStructure] = None
    code: Optional[List[SubstanceDefinitionstr]] = empty_list()
    name: Optional[List[SubstanceDefinitionName]] = empty_list()
    molecularWeight: Optional[List[SubstanceDefinitionStructureIsotopeMolecularWeight]] = empty_list()
    relationship: Optional[List[SubstanceDefinitionRelationship]] = empty_list()
    nucleicAcid: Optional[FHIRReference] = None
    polymer: Optional[FHIRReference] = None
    protein: Optional[FHIRReference] = None
    sourceMaterial: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(SubstanceDefinition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("status", "status", CodeableConcept, False, None, False),
            ("category", "category", CodeableConcept, False, None, False),
            ("domain", "domain", CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("moiety", "moiety", SubstanceDefinitionMoiety, True, None, False),
            ("property", "property", SubstanceDefinitionProperty, True, None, False),
            ("referenceInformation", "referenceInformation", FHIRReference, False, None, False),
            ("structure", "structure", SubstanceDefinitionStructure, False, None, False),
            ("code", "code", SubstanceDefinitionstr, True, None, False),
            ("name", "name", SubstanceDefinitionName, True, None, False),
            ("molecularWeight", "molecularWeight", SubstanceDefinitionStructureIsotopeMolecularWeight, True, None, False),
            ("relationship", "relationship", SubstanceDefinitionRelationship, True, None, False),
            ("nucleicAcid", "nucleicAcid", FHIRReference, False, None, False),
            ("polymer", "polymer", FHIRReference, False, None, False),
            ("protein", "protein", FHIRReference, False, None, False),
            ("sourceMaterial", "sourceMaterial", FHIRReference, False, None, False),
        ])
        return js