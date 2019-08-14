#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/DocumentManifest) on 2019-08-06.
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


@dataclass
class DocumentManifestRelated(BackboneElement):
    """ Related things.

    Related identifiers or resources associated with the DocumentManifest.
    """
    resource_type: ClassVar[str] = "DocumentManifestRelated"
    identifier: Optional[Identifier] = None
    ref: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(DocumentManifestRelated, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("ref", "ref", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class DocumentManifest(DomainResource):
    """ A list that defines a set of documents.

    A collection of documents compiled for a purpose together with metadata
    that applies to the collection.
    """
    resource_type: ClassVar[str] = "DocumentManifest"
    masterIdentifier: Optional[Identifier] = None
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    type: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    created: Optional[FHIRDate] = None
    author: Optional[List[FHIRReference]] = empty_list()
    recipient: Optional[List[FHIRReference]] = empty_list()
    source: Optional[str] = None
    description: Optional[str] = None
    content: List[FHIRReference] = empty_list()
    related: Optional[List[DocumentManifestRelated]] = empty_list()

    def elementProperties(self):
        js = super(DocumentManifest, self).elementProperties()
        js.extend([
            ("masterIdentifier", "masterIdentifier", Identifier, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", CodeableConcept, False, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
            ("created", "created", FHIRDate, False, None, False),
            ("author", "author", FHIRReference, True, None, False),
            ("recipient", "recipient", FHIRReference, True, None, False),
            ("source", "source", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("content", "content", FHIRReference, True, None, True),
            ("related", "related", DocumentManifestRelated, True, None, False),
        ])
        return js