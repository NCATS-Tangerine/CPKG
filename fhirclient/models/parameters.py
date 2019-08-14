#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Parameters) on 2019-08-06.
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
from .resource import Resource
from .sampleddata import SampledData
from .signature import Signature
from .timing import Timing
from .triggerdefinition import TriggerDefinition
from .usagecontext import UsageContext


@dataclass
class ParametersParameter(BackboneElement):
    """ Operation Parameter.

    A parameter passed to or received from the operation.
    """
    resource_type: ClassVar[str] = "ParametersParameter"
    name: str = None
    valueBase64Binary: Optional[str] = None
    valueBoolean: Optional[bool] = None
    valueCanonical: Optional[str] = None
    valueCode: Optional[str] = None
    valueDate: Optional[FHIRDate] = None
    valueDateTime: Optional[FHIRDate] = None
    valueDecimal: Optional[float] = None
    valueId: Optional[str] = None
    valueInstant: Optional[FHIRDate] = None
    valueInteger: Optional[int] = None
    valueMarkdown: Optional[str] = None
    valueOid: Optional[str] = None
    valuePositiveInt: Optional[int] = None
    valueString: Optional[str] = None
    valueTime: Optional[FHIRDate] = None
    valueUnsignedInt: Optional[int] = None
    valueUri: Optional[str] = None
    valueUrl: Optional[str] = None
    valueUuid: Optional[str] = None
    valueAddress: Optional[Address] = None
    valueAge: Optional[Age] = None
    valueAnnotation: Optional[Annotation] = None
    valueAttachment: Optional[Attachment] = None
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueCoding: Optional[Coding] = None
    valueContactPoint: Optional[ContactPoint] = None
    valueCount: Optional[Count] = None
    valueDistance: Optional[Distance] = None
    valueDuration: Optional[Duration] = None
    valueHumanName: Optional[HumanName] = None
    valueIdentifier: Optional[Identifier] = None
    valueMoney: Optional[Money] = None
    valuePeriod: Optional[Period] = None
    valueQuantity: Optional[Quantity] = None
    valueRange: Optional[Range] = None
    valueRatio: Optional[Ratio] = None
    valueReference: Optional[FHIRReference] = None
    valueSampledData: Optional[SampledData] = None
    valueSignature: Optional[Signature] = None
    valueTiming: Optional[Timing] = None
    valueContactDetail: Optional[ContactDetail] = None
    valueContributor: Optional[Contributor] = None
    valueDataRequirement: Optional[DataRequirement] = None
    valueExpression: Optional[Expression] = None
    valueParameterDefinition: Optional[ParameterDefinition] = None
    valueRelatedArtifact: Optional[RelatedArtifact] = None
    valueTriggerDefinition: Optional[TriggerDefinition] = None
    valueUsageContext: Optional[UsageContext] = None
    valueDosage: Optional[Dosage] = None
    resource: Optional[Resource] = None
    part: Optional[List["ParametersParameter"]] = empty_list()

    def elementProperties(self):
        js = super(ParametersParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCanonical", "valueCanonical", str, False, "value", False),
            ("valueCode", "valueCode", str, False, "value", False),
            ("valueDate", "valueDate", FHIRDate, False, "value", False),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueId", "valueId", str, False, "value", False),
            ("valueInstant", "valueInstant", FHIRDate, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueMarkdown", "valueMarkdown", str, False, "value", False),
            ("valueOid", "valueOid", str, False, "value", False),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", FHIRDate, False, "value", False),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", False),
            ("valueUri", "valueUri", str, False, "value", False),
            ("valueUrl", "valueUrl", str, False, "value", False),
            ("valueUuid", "valueUuid", str, False, "value", False),
            ("valueAddress", "valueAddress", Address, False, "value", False),
            ("valueAge", "valueAge", Age, False, "value", False),
            ("valueAnnotation", "valueAnnotation", Annotation, False, "value", False),
            ("valueAttachment", "valueAttachment", Attachment, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", False),
            ("valueCoding", "valueCoding", Coding, False, "value", False),
            ("valueContactPoint", "valueContactPoint", ContactPoint, False, "value", False),
            ("valueCount", "valueCount", Count, False, "value", False),
            ("valueDistance", "valueDistance", Distance, False, "value", False),
            ("valueDuration", "valueDuration", Duration, False, "value", False),
            ("valueHumanName", "valueHumanName", HumanName, False, "value", False),
            ("valueIdentifier", "valueIdentifier", Identifier, False, "value", False),
            ("valueMoney", "valueMoney", Money, False, "value", False),
            ("valuePeriod", "valuePeriod", Period, False, "value", False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
            ("valueRange", "valueRange", Range, False, "value", False),
            ("valueRatio", "valueRatio", Ratio, False, "value", False),
            ("valueReference", "valueReference", FHIRReference, False, "value", False),
            ("valueSampledData", "valueSampledData", SampledData, False, "value", False),
            ("valueSignature", "valueSignature", Signature, False, "value", False),
            ("valueTiming", "valueTiming", Timing, False, "value", False),
            ("valueContactDetail", "valueContactDetail", ContactDetail, False, "value", False),
            ("valueContributor", "valueContributor", Contributor, False, "value", False),
            ("valueDataRequirement", "valueDataRequirement", DataRequirement, False, "value", False),
            ("valueExpression", "valueExpression", Expression, False, "value", False),
            ("valueParameterDefinition", "valueParameterDefinition", ParameterDefinition, False, "value", False),
            ("valueRelatedArtifact", "valueRelatedArtifact", RelatedArtifact, False, "value", False),
            ("valueTriggerDefinition", "valueTriggerDefinition", TriggerDefinition, False, "value", False),
            ("valueUsageContext", "valueUsageContext", UsageContext, False, "value", False),
            ("valueDosage", "valueDosage", Dosage, False, "value", False),
            ("resource", "resource", Resource, False, None, False),
            ("part", "part", ParametersParameter, True, None, False),
        ])
        return js


@dataclass
class Parameters(Resource):
    """ Operation Request or Response.

    This resource is a non-persisted resource used to pass information into and
    back from an [operation](operations.html). It has no other use, and there
    is no RESTful endpoint associated with it.
    """
    resource_type: ClassVar[str] = "Parameters"
    parameter: Optional[List[ParametersParameter]] = empty_list()

    def elementProperties(self):
        js = super(Parameters, self).elementProperties()
        js.extend([
            ("parameter", "parameter", ParametersParameter, True, None, False),
        ])
        return js