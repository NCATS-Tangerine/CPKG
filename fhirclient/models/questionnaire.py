#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Questionnaire) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .usagecontext import UsageContext


@dataclass
class QuestionnaireItemEnableWhen(BackboneElement):
    """ Only allow data when.

    A constraint indicating that this item should only be enabled
    (displayed/allow answers to be captured) when the specified condition is
    true.
    """
    resource_type: ClassVar[str] = "QuestionnaireItemEnableWhen"
    question: str = None
    operator: str = None
    answerBoolean: bool = None
    answerDecimal: float = None
    answerInteger: int = None
    answerDate: FHIRDate = None
    answerDateTime: FHIRDate = None
    answerTime: FHIRDate = None
    answerString: str = None
    answerCoding: Coding = None
    answerQuantity: Quantity = None
    answerReference: FHIRReference = None

    def elementProperties(self):
        js = super(QuestionnaireItemEnableWhen, self).elementProperties()
        js.extend([
            ("question", "question", str, False, None, True),
            ("operator", "operator", str, False, None, True),
            ("answerBoolean", "answerBoolean", bool, False, "answer", True),
            ("answerDecimal", "answerDecimal", float, False, "answer", True),
            ("answerInteger", "answerInteger", int, False, "answer", True),
            ("answerDate", "answerDate", FHIRDate, False, "answer", True),
            ("answerDateTime", "answerDateTime", FHIRDate, False, "answer", True),
            ("answerTime", "answerTime", FHIRDate, False, "answer", True),
            ("answerString", "answerString", str, False, "answer", True),
            ("answerCoding", "answerCoding", Coding, False, "answer", True),
            ("answerQuantity", "answerQuantity", Quantity, False, "answer", True),
            ("answerReference", "answerReference", FHIRReference, False, "answer", True),
        ])
        return js


@dataclass
class QuestionnaireItemAnswerOption(BackboneElement):
    """ Permitted answer.

    One of the permitted answers for a "choice" or "open-choice" question.
    """
    resource_type: ClassVar[str] = "QuestionnaireItemAnswerOption"
    valueInteger: int = None
    valueDate: FHIRDate = None
    valueTime: FHIRDate = None
    valueString: str = None
    valueCoding: Coding = None
    valueReference: FHIRReference = None
    initialSelected: Optional[bool] = None

    def elementProperties(self):
        js = super(QuestionnaireItemAnswerOption, self).elementProperties()
        js.extend([
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueDate", "valueDate", FHIRDate, False, "value", True),
            ("valueTime", "valueTime", FHIRDate, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueCoding", "valueCoding", Coding, False, "value", True),
            ("valueReference", "valueReference", FHIRReference, False, "value", True),
            ("initialSelected", "initialSelected", bool, False, None, False),
        ])
        return js


@dataclass
class QuestionnaireItemInitial(BackboneElement):
    """ Initial value(s) when item is first rendered.

    One or more values that should be pre-populated in the answer when
    initially rendering the questionnaire for user input.
    """
    resource_type: ClassVar[str] = "QuestionnaireItemInitial"
    valueBoolean: bool = None
    valueDecimal: float = None
    valueInteger: int = None
    valueDate: FHIRDate = None
    valueDateTime: FHIRDate = None
    valueTime: FHIRDate = None
    valueString: str = None
    valueUri: str = None
    valueAttachment: Attachment = None
    valueCoding: Coding = None
    valueQuantity: Quantity = None
    valueReference: FHIRReference = None

    def elementProperties(self):
        js = super(QuestionnaireItemInitial, self).elementProperties()
        js.extend([
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueDate", "valueDate", FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", True),
            ("valueTime", "valueTime", FHIRDate, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
            ("valueAttachment", "valueAttachment", Attachment, False, "value", True),
            ("valueCoding", "valueCoding", Coding, False, "value", True),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", True),
            ("valueReference", "valueReference", FHIRReference, False, "value", True),
        ])
        return js


@dataclass
class QuestionnaireItem(BackboneElement):
    """ Questions and sections within the Questionnaire.

    A particular question, question grouping or display text that is part of
    the questionnaire.
    """
    resource_type: ClassVar[str] = "QuestionnaireItem"
    linkId: str = None
    definition: Optional[str] = None
    code: Optional[List[Coding]] = empty_list()
    prefix: Optional[str] = None
    text: Optional[str] = None
    type: str = None
    enableWhen: Optional[List[QuestionnaireItemEnableWhen]] = empty_list()
    enableBehavior: Optional[str] = None
    required: Optional[bool] = None
    repeats: Optional[bool] = None
    readOnly: Optional[bool] = None
    maxLength: Optional[int] = None
    answerValueSet: Optional[str] = None
    answerOption: Optional[List[QuestionnaireItemAnswerOption]] = empty_list()
    initial: Optional[List[QuestionnaireItemInitial]] = empty_list()
    item: Optional[List["QuestionnaireItem"]] = empty_list()

    def elementProperties(self):
        js = super(QuestionnaireItem, self).elementProperties()
        js.extend([
            ("linkId", "linkId", str, False, None, True),
            ("definition", "definition", str, False, None, False),
            ("code", "code", Coding, True, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("enableWhen", "enableWhen", QuestionnaireItemEnableWhen, True, None, False),
            ("enableBehavior", "enableBehavior", str, False, None, False),
            ("required", "required", bool, False, None, False),
            ("repeats", "repeats", bool, False, None, False),
            ("readOnly", "readOnly", bool, False, None, False),
            ("maxLength", "maxLength", int, False, None, False),
            ("answerValueSet", "answerValueSet", str, False, None, False),
            ("answerOption", "answerOption", QuestionnaireItemAnswerOption, True, None, False),
            ("initial", "initial", QuestionnaireItemInitial, True, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
        ])
        return js


@dataclass
class Questionnaire(DomainResource):
    """ A structured set of questions.

    A structured set of questions intended to guide the collection of answers
    from end-users. Questionnaires provide detailed control over order,
    presentation, phraseology and grouping to allow coherent, consistent data
    collection.
    """
    resource_type: ClassVar[str] = "Questionnaire"
    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    derivedFrom: Optional[List[str]] = empty_list()
    status: str = None
    experimental: Optional[bool] = None
    subjectType: Optional[List[str]] = empty_list()
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    code: Optional[List[Coding]] = empty_list()
    item: Optional[List[QuestionnaireItem]] = empty_list()

    def elementProperties(self):
        js = super(Questionnaire, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("derivedFrom", "derivedFrom", str, True, None, False),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("subjectType", "subjectType", str, True, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("code", "code", Coding, True, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
        ])
        return js