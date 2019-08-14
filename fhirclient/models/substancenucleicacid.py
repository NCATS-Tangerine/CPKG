#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/SubstanceNucleicAcid) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .identifier import Identifier


@dataclass
class SubstanceNucleicAcidSubunitLinkage(BackboneElement):
    """ The linkages between sugar residues will also be captured.
    """
    resource_type: ClassVar[str] = "SubstanceNucleicAcidSubunitLinkage"
    connectivity: Optional[str] = None
    identifier: Optional[Identifier] = None
    name: Optional[str] = None
    residueSite: Optional[str] = None

    def elementProperties(self):
        js = super(SubstanceNucleicAcidSubunitLinkage, self).elementProperties()
        js.extend([
            ("connectivity", "connectivity", str, False, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("name", "name", str, False, None, False),
            ("residueSite", "residueSite", str, False, None, False),
        ])
        return js


@dataclass
class SubstanceNucleicAcidSubunitSugar(BackboneElement):
    """ 5.3.6.8.1 Sugar ID (Mandatory).
    """
    resource_type: ClassVar[str] = "SubstanceNucleicAcidSubunitSugar"
    identifier: Optional[Identifier] = None
    name: Optional[str] = None
    residueSite: Optional[str] = None

    def elementProperties(self):
        js = super(SubstanceNucleicAcidSubunitSugar, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("name", "name", str, False, None, False),
            ("residueSite", "residueSite", str, False, None, False),
        ])
        return js


@dataclass
class SubstanceNucleicAcidSubunit(BackboneElement):
    """ Subunits are listed in order of decreasing length; sequences of the same
    length will be ordered by molecular weight; subunits that have identical
    sequences will be repeated multiple times.
    """
    resource_type: ClassVar[str] = "SubstanceNucleicAcidSubunit"
    subunit: Optional[int] = None
    sequence: Optional[str] = None
    length: Optional[int] = None
    sequenceAttachment: Optional[Attachment] = None
    fivePrime: Optional[CodeableConcept] = None
    threePrime: Optional[CodeableConcept] = None
    linkage: Optional[List[SubstanceNucleicAcidSubunitLinkage]] = empty_list()
    sugar: Optional[List[SubstanceNucleicAcidSubunitSugar]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceNucleicAcidSubunit, self).elementProperties()
        js.extend([
            ("subunit", "subunit", int, False, None, False),
            ("sequence", "sequence", str, False, None, False),
            ("length", "length", int, False, None, False),
            ("sequenceAttachment", "sequenceAttachment", Attachment, False, None, False),
            ("fivePrime", "fivePrime", CodeableConcept, False, None, False),
            ("threePrime", "threePrime", CodeableConcept, False, None, False),
            ("linkage", "linkage", SubstanceNucleicAcidSubunitLinkage, True, None, False),
            ("sugar", "sugar", SubstanceNucleicAcidSubunitSugar, True, None, False),
        ])
        return js


@dataclass
class SubstanceNucleicAcid(DomainResource):
    """ Nucleic acids are defined by three distinct elements: the base, sugar and
    linkage. Individual substance/moiety IDs will be created for each of these
    elements. The nucleotide sequence will be always entered in the 5’-3’
    direction.
    """
    resource_type: ClassVar[str] = "SubstanceNucleicAcid"
    sequenceType: Optional[CodeableConcept] = None
    numberOfSubunits: Optional[int] = None
    areaOfHybridisation: Optional[str] = None
    oligoNucleotideType: Optional[CodeableConcept] = None
    subunit: Optional[List[SubstanceNucleicAcidSubunit]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceNucleicAcid, self).elementProperties()
        js.extend([
            ("sequenceType", "sequenceType", CodeableConcept, False, None, False),
            ("numberOfSubunits", "numberOfSubunits", int, False, None, False),
            ("areaOfHybridisation", "areaOfHybridisation", str, False, None, False),
            ("oligoNucleotideType", "oligoNucleotideType", CodeableConcept, False, None, False),
            ("subunit", "subunit", SubstanceNucleicAcidSubunit, True, None, False),
        ])
        return js