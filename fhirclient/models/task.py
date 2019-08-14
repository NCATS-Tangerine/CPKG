#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Task) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .age import Age
from .annotation import Annotation
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .contactpoint import ContactPoint
from .contributor import Contributor
from .count import Count
from .datarequirement import DataRequirement
from .distance import Distance
from .domainresource import DomainResource
from .dosage import Dosage
from .duration import Duration
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier
from .money import Money
from .parameterdefinition import ParameterDefinition
from .period import Period
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .relatedartifact import RelatedArtifact
from .sampleddata import SampledData
from .signature import Signature
from .timing import Timing
from .triggerdefinition import TriggerDefinition
from .usagecontext import UsageContext


@dataclass
class TaskRestriction(BackboneElement):
    """ Constraints on fulfillment tasks.

    If the Task.focus is a request resource and the task is seeking fulfillment
    (i.e. is asking for the request to be actioned), this element identifies
    any limitations on what parts of the referenced request should be actioned.
    """
    resource_type: ClassVar[str] = "TaskRestriction"
    repetitions: Optional[int] = None
    period: Optional[Period] = None
    recipient: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(TaskRestriction, self).elementProperties()
        js.extend([
            ("repetitions", "repetitions", int, False, None, False),
            ("period", "period", Period, False, None, False),
            ("recipient", "recipient", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class TaskInput(BackboneElement):
    """ Information used to perform task.

    Additional information that may be needed in the execution of the task.
    """
    resource_type: ClassVar[str] = "TaskInput"
    type: CodeableConcept = None
    valueBase64Binary: str = None
    valueBoolean: bool = None
    valueCanonical: str = None
    valueCode: str = None
    valueDate: FHIRDate = None
    valueDateTime: FHIRDate = None
    valueDecimal: float = None
    valueId: str = None
    valueInstant: FHIRDate = None
    valueInteger: int = None
    valueMarkdown: str = None
    valueOid: str = None
    valuePositiveInt: int = None
    valueString: str = None
    valueTime: FHIRDate = None
    valueUnsignedInt: int = None
    valueUri: str = None
    valueUrl: str = None
    valueUuid: str = None
    valueAddress: Address = None
    valueAge: Age = None
    valueAnnotation: Annotation = None
    valueAttachment: Attachment = None
    valueCodeableConcept: CodeableConcept = None
    valueCoding: Coding = None
    valueContactPoint: ContactPoint = None
    valueCount: Count = None
    valueDistance: Distance = None
    valueDuration: Duration = None
    valueHumanName: HumanName = None
    valueIdentifier: Identifier = None
    valueMoney: Money = None
    valuePeriod: Period = None
    valueQuantity: Quantity = None
    valueRange: Range = None
    valueRatio: Ratio = None
    valueReference: FHIRReference = None
    valueSampledData: SampledData = None
    valueSignature: Signature = None
    valueTiming: Timing = None
    valueContactDetail: ContactDetail = None
    valueContributor: Contributor = None
    valueDataRequirement: DataRequirement = None
    valueExpression: Expression = None
    valueParameterDefinition: ParameterDefinition = None
    valueRelatedArtifact: RelatedArtifact = None
    valueTriggerDefinition: TriggerDefinition = None
    valueUsageContext: UsageContext = None
    valueDosage: Dosage = None

    def elementProperties(self):
        js = super(TaskInput, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueDate", "valueDate", FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueInstant", "valueInstant", FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("valueOid", "valueOid", str, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", FHIRDate, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("valueUuid", "valueUuid", str, False, "value", True),
            ("valueAddress", "valueAddress", Address, False, "value", True),
            ("valueAge", "valueAge", Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", Attachment, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", Coding, False, "value", True),
            ("valueContactPoint", "valueContactPoint", ContactPoint, False, "value", True),
            ("valueCount", "valueCount", Count, False, "value", True),
            ("valueDistance", "valueDistance", Distance, False, "value", True),
            ("valueDuration", "valueDuration", Duration, False, "value", True),
            ("valueHumanName", "valueHumanName", HumanName, False, "value", True),
            ("valueIdentifier", "valueIdentifier", Identifier, False, "value", True),
            ("valueMoney", "valueMoney", Money, False, "value", True),
            ("valuePeriod", "valuePeriod", Period, False, "value", True),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", True),
            ("valueRange", "valueRange", Range, False, "value", True),
            ("valueRatio", "valueRatio", Ratio, False, "value", True),
            ("valueReference", "valueReference", FHIRReference, False, "value", True),
            ("valueSampledData", "valueSampledData", SampledData, False, "value", True),
            ("valueSignature", "valueSignature", Signature, False, "value", True),
            ("valueTiming", "valueTiming", Timing, False, "value", True),
            ("valueContactDetail", "valueContactDetail", ContactDetail, False, "value", True),
            ("valueContributor", "valueContributor", Contributor, False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", DataRequirement, False, "value", True),
            ("valueExpression", "valueExpression", Expression, False, "value", True),
            ("valueParameterDefinition", "valueParameterDefinition", ParameterDefinition, False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", RelatedArtifact, False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", TriggerDefinition, False, "value", True),
            ("valueUsageContext", "valueUsageContext", UsageContext, False, "value", True),
            ("valueDosage", "valueDosage", Dosage, False, "value", True),
        ])
        return js


@dataclass
class TaskOutput(BackboneElement):
    """ Information produced as part of task.

    Outputs produced by the Task.
    """
    resource_type: ClassVar[str] = "TaskOutput"
    type: CodeableConcept = None
    valueBase64Binary: str = None
    valueBoolean: bool = None
    valueCanonical: str = None
    valueCode: str = None
    valueDate: FHIRDate = None
    valueDateTime: FHIRDate = None
    valueDecimal: float = None
    valueId: str = None
    valueInstant: FHIRDate = None
    valueInteger: int = None
    valueMarkdown: str = None
    valueOid: str = None
    valuePositiveInt: int = None
    valueString: str = None
    valueTime: FHIRDate = None
    valueUnsignedInt: int = None
    valueUri: str = None
    valueUrl: str = None
    valueUuid: str = None
    valueAddress: Address = None
    valueAge: Age = None
    valueAnnotation: Annotation = None
    valueAttachment: Attachment = None
    valueCodeableConcept: CodeableConcept = None
    valueCoding: Coding = None
    valueContactPoint: ContactPoint = None
    valueCount: Count = None
    valueDistance: Distance = None
    valueDuration: Duration = None
    valueHumanName: HumanName = None
    valueIdentifier: Identifier = None
    valueMoney: Money = None
    valuePeriod: Period = None
    valueQuantity: Quantity = None
    valueRange: Range = None
    valueRatio: Ratio = None
    valueReference: FHIRReference = None
    valueSampledData: SampledData = None
    valueSignature: Signature = None
    valueTiming: Timing = None
    valueContactDetail: ContactDetail = None
    valueContributor: Contributor = None
    valueDataRequirement: DataRequirement = None
    valueExpression: Expression = None
    valueParameterDefinition: ParameterDefinition = None
    valueRelatedArtifact: RelatedArtifact = None
    valueTriggerDefinition: TriggerDefinition = None
    valueUsageContext: UsageContext = None
    valueDosage: Dosage = None

    def elementProperties(self):
        js = super(TaskOutput, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueDate", "valueDate", FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueInstant", "valueInstant", FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("valueOid", "valueOid", str, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", FHIRDate, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("valueUuid", "valueUuid", str, False, "value", True),
            ("valueAddress", "valueAddress", Address, False, "value", True),
            ("valueAge", "valueAge", Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", Attachment, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", Coding, False, "value", True),
            ("valueContactPoint", "valueContactPoint", ContactPoint, False, "value", True),
            ("valueCount", "valueCount", Count, False, "value", True),
            ("valueDistance", "valueDistance", Distance, False, "value", True),
            ("valueDuration", "valueDuration", Duration, False, "value", True),
            ("valueHumanName", "valueHumanName", HumanName, False, "value", True),
            ("valueIdentifier", "valueIdentifier", Identifier, False, "value", True),
            ("valueMoney", "valueMoney", Money, False, "value", True),
            ("valuePeriod", "valuePeriod", Period, False, "value", True),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", True),
            ("valueRange", "valueRange", Range, False, "value", True),
            ("valueRatio", "valueRatio", Ratio, False, "value", True),
            ("valueReference", "valueReference", FHIRReference, False, "value", True),
            ("valueSampledData", "valueSampledData", SampledData, False, "value", True),
            ("valueSignature", "valueSignature", Signature, False, "value", True),
            ("valueTiming", "valueTiming", Timing, False, "value", True),
            ("valueContactDetail", "valueContactDetail", ContactDetail, False, "value", True),
            ("valueContributor", "valueContributor", Contributor, False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", DataRequirement, False, "value", True),
            ("valueExpression", "valueExpression", Expression, False, "value", True),
            ("valueParameterDefinition", "valueParameterDefinition", ParameterDefinition, False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", RelatedArtifact, False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", TriggerDefinition, False, "value", True),
            ("valueUsageContext", "valueUsageContext", UsageContext, False, "value", True),
            ("valueDosage", "valueDosage", Dosage, False, "value", True),
        ])
        return js


@dataclass
class Task(DomainResource):
    """ A task to be performed.
    """
    resource_type: ClassVar[str] = "Task"
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[str] = None
    instantiatesUri: Optional[str] = None
    basedOn: Optional[List[FHIRReference]] = empty_list()
    groupIdentifier: Optional[Identifier] = None
    partOf: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    businessStatus: Optional[CodeableConcept] = None
    intent: str = None
    priority: Optional[str] = None
    code: Optional[CodeableConcept] = None
    description: Optional[str] = None
    focus: Optional[FHIRReference] = None
    for_fhir: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    executionPeriod: Optional[Period] = None
    authoredOn: Optional[FHIRDate] = None
    lastModified: Optional[FHIRDate] = None
    requester: Optional[FHIRReference] = None
    performerType: Optional[List[CodeableConcept]] = empty_list()
    owner: Optional[FHIRReference] = None
    location: Optional[FHIRReference] = None
    reasonCode: Optional[CodeableConcept] = None
    reasonReference: Optional[FHIRReference] = None
    insurance: Optional[List[FHIRReference]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    relevantHistory: Optional[List[FHIRReference]] = empty_list()
    restriction: Optional[TaskRestriction] = None
    input: Optional[List[TaskInput]] = empty_list()
    output: Optional[List[TaskOutput]] = empty_list()

    def elementProperties(self):
        js = super(Task, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, False, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("groupIdentifier", "groupIdentifier", Identifier, False, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", CodeableConcept, False, None, False),
            ("businessStatus", "businessStatus", CodeableConcept, False, None, False),
            ("intent", "intent", str, False, None, True),
            ("priority", "priority", str, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("focus", "focus", FHIRReference, False, None, False),
            ("for_fhir", "for", FHIRReference, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("executionPeriod", "executionPeriod", Period, False, None, False),
            ("authoredOn", "authoredOn", FHIRDate, False, None, False),
            ("lastModified", "lastModified", FHIRDate, False, None, False),
            ("requester", "requester", FHIRReference, False, None, False),
            ("performerType", "performerType", CodeableConcept, True, None, False),
            ("owner", "owner", FHIRReference, False, None, False),
            ("location", "location", FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, False, None, False),
            ("reasonReference", "reasonReference", FHIRReference, False, None, False),
            ("insurance", "insurance", FHIRReference, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("relevantHistory", "relevantHistory", FHIRReference, True, None, False),
            ("restriction", "restriction", TaskRestriction, False, None, False),
            ("input", "input", TaskInput, True, None, False),
            ("output", "output", TaskOutput, True, None, False),
        ])
        return js