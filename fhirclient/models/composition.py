#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Composition) on 2019-08-06.
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
from .narrative import Narrative
from .period import Period


@dataclass
class CompositionAttester(BackboneElement):
    """ Attests to accuracy of composition.

    A participant who has attested to the accuracy of the composition/document.
    """
    resource_type: ClassVar[str] = "CompositionAttester"
    mode: str = None
    time: Optional[FHIRDate] = None
    party: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(CompositionAttester, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, True),
            ("time", "time", FHIRDate, False, None, False),
            ("party", "party", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class CompositionRelatesTo(BackboneElement):
    """ Relationships to other compositions/documents.

    Relationships that this composition has with other compositions or
    documents that already exist.
    """
    resource_type: ClassVar[str] = "CompositionRelatesTo"
    code: str = None
    targetIdentifier: Identifier = None
    targetReference: FHIRReference = None

    def elementProperties(self):
        js = super(CompositionRelatesTo, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("targetIdentifier", "targetIdentifier", Identifier, False, "target", True),
            ("targetReference", "targetReference", FHIRReference, False, "target", True),
        ])
        return js


@dataclass
class CompositionEvent(BackboneElement):
    """ The clinical service(s) being documented.

    The clinical service, such as a colonoscopy or an appendectomy, being
    documented.
    """
    resource_type: ClassVar[str] = "CompositionEvent"
    code: Optional[List[CodeableConcept]] = empty_list()
    period: Optional[Period] = None
    detail: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(CompositionEvent, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, True, None, False),
            ("period", "period", Period, False, None, False),
            ("detail", "detail", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class CompositionSection(BackboneElement):
    """ Composition is broken into sections.

    The root of the sections that make up the composition.
    """
    resource_type: ClassVar[str] = "CompositionSection"
    title: Optional[str] = None
    code: Optional[CodeableConcept] = None
    author: Optional[List[FHIRReference]] = empty_list()
    focus: Optional[FHIRReference] = None
    text: Optional[Narrative] = None
    mode: Optional[str] = None
    orderedBy: Optional[CodeableConcept] = None
    entry: Optional[List[FHIRReference]] = empty_list()
    emptyReason: Optional[CodeableConcept] = None
    section: Optional[List["CompositionSection"]] = empty_list()

    def elementProperties(self):
        js = super(CompositionSection, self).elementProperties()
        js.extend([
            ("title", "title", str, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("author", "author", FHIRReference, True, None, False),
            ("focus", "focus", FHIRReference, False, None, False),
            ("text", "text", Narrative, False, None, False),
            ("mode", "mode", str, False, None, False),
            ("orderedBy", "orderedBy", CodeableConcept, False, None, False),
            ("entry", "entry", FHIRReference, True, None, False),
            ("emptyReason", "emptyReason", CodeableConcept, False, None, False),
            ("section", "section", CompositionSection, True, None, False),
        ])
        return js


@dataclass
class Composition(DomainResource):
    """ A set of resources composed into a single coherent clinical statement with
    clinical attestation.

    A set of healthcare-related information that is assembled together into a
    single logical package that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation with
    regard to who is making the statement. A Composition defines the structure
    and narrative content necessary for a document. However, a Composition
    alone does not constitute a document. Rather, the Composition must be the
    first entry in a Bundle where Bundle.type=document, and any other resources
    referenced from Composition must be included as subsequent entries in the
    Bundle (for example Patient, Practitioner, Encounter, etc.).
    """
    resource_type: ClassVar[str] = "Composition"
    identifier: Optional[Identifier] = None
    status: str = None
    type: CodeableConcept = None
    category: Optional[List[CodeableConcept]] = empty_list()
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    date: FHIRDate = None
    author: List[FHIRReference] = empty_list()
    title: str = None
    confidentiality: Optional[str] = None
    attester: Optional[List[CompositionAttester]] = empty_list()
    custodian: Optional[FHIRReference] = None
    relatesTo: Optional[List[CompositionRelatesTo]] = empty_list()
    event: Optional[List[CompositionEvent]] = empty_list()
    section: Optional[List[CompositionSection]] = empty_list()

    def elementProperties(self):
        js = super(Composition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", CodeableConcept, False, None, True),
            ("category", "category", CodeableConcept, True, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("date", "date", FHIRDate, False, None, True),
            ("author", "author", FHIRReference, True, None, True),
            ("title", "title", str, False, None, True),
            ("confidentiality", "confidentiality", str, False, None, False),
            ("attester", "attester", CompositionAttester, True, None, False),
            ("custodian", "custodian", FHIRReference, False, None, False),
            ("relatesTo", "relatesTo", CompositionRelatesTo, True, None, False),
            ("event", "event", CompositionEvent, True, None, False),
            ("section", "section", CompositionSection, True, None, False),
        ])
        return js