#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity


@dataclass
class QuestionnaireResponseItemAnswer(BackboneElement):
    """ The response(s) to the question.

    The respondent's answer(s) to the question.
    """
    resource_type: ClassVar[str] = "QuestionnaireResponseItemAnswer"
    valueBoolean: Optional[bool] = None
    valueDecimal: Optional[float] = None
    valueInteger: Optional[int] = None
    valueDate: Optional[FHIRDate] = None
    valueDateTime: Optional[FHIRDate] = None
    valueTime: Optional[FHIRDate] = None
    valueString: Optional[str] = None
    valueUri: Optional[str] = None
    valueAttachment: Optional[Attachment] = None
    valueCoding: Optional[Coding] = None
    valueQuantity: Optional[Quantity] = None
    valueReference: Optional[FHIRReference] = None
    item: Optional[List["QuestionnaireResponseItem"]] = empty_list()

    def elementProperties(self):
        js = super(QuestionnaireResponseItemAnswer, self).elementProperties()
        js.extend([
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueDate", "valueDate", FHIRDate, False, "value", False),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", False),
            ("valueTime", "valueTime", FHIRDate, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueUri", "valueUri", str, False, "value", False),
            ("valueAttachment", "valueAttachment", Attachment, False, "value", False),
            ("valueCoding", "valueCoding", Coding, False, "value", False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
            ("valueReference", "valueReference", FHIRReference, False, "value", False),
            ("item", "item", QuestionnaireResponseItem, True, None, False),
        ])
        return js


@dataclass
class QuestionnaireResponseItem(BackboneElement):
    """ Groups and questions.

    A group or question item from the original questionnaire for which answers
    are provided.
    """
    resource_type: ClassVar[str] = "QuestionnaireResponseItem"
    linkId: str = None
    definition: Optional[str] = None
    text: Optional[str] = None
    answer: Optional[List[QuestionnaireResponseItemAnswer]] = empty_list()
    item: Optional[List["QuestionnaireResponseItem"]] = empty_list()

    def elementProperties(self):
        js = super(QuestionnaireResponseItem, self).elementProperties()
        js.extend([
            ("linkId", "linkId", str, False, None, True),
            ("definition", "definition", str, False, None, False),
            ("text", "text", str, False, None, False),
            ("answer", "answer", QuestionnaireResponseItemAnswer, True, None, False),
            ("item", "item", QuestionnaireResponseItem, True, None, False),
        ])
        return js


@dataclass
class QuestionnaireResponse(DomainResource):
    """ A structured set of questions and their answers.

    A structured set of questions and their answers. The questions are ordered
    and grouped into coherent subsets, corresponding to the structure of the
    grouping of the questionnaire being responded to.
    """
    resource_type: ClassVar[str] = "QuestionnaireResponse"
    identifier: Optional[Identifier] = None
    basedOn: Optional[List[FHIRReference]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    questionnaire: Optional[str] = None
    status: str = None
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    authored: Optional[FHIRDate] = None
    author: Optional[FHIRReference] = None
    source: Optional[FHIRReference] = None
    item: Optional[List[QuestionnaireResponseItem]] = empty_list()

    def elementProperties(self):
        js = super(QuestionnaireResponse, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("questionnaire", "questionnaire", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("authored", "authored", FHIRDate, False, None, False),
            ("author", "author", FHIRReference, False, None, False),
            ("source", "source", FHIRReference, False, None, False),
            ("item", "item", QuestionnaireResponseItem, True, None, False),
        ])
        return js