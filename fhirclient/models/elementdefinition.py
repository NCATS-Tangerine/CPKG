#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ElementDefinition) on 2019-08-06.
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
from .element import Element
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
class ElementDefinitionSlicingDiscriminator(Element):
    """ Element values that are used to distinguish the slices.

    Designates which child elements are used to discriminate between the slices
    when processing an instance. If one or more discriminators are provided,
    the value of the child elements in the instance data SHALL completely
    distinguish which slice the element in the resource matches based on the
    allowed values for those elements in each of the slices.
    """
    resource_type: ClassVar[str] = "ElementDefinitionSlicingDiscriminator"
    type: str = None
    path: str = None

    def elementProperties(self):
        js = super(ElementDefinitionSlicingDiscriminator, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js


@dataclass
class ElementDefinitionSlicing(Element):
    """ This element is sliced - slices follow.

    Indicates that the element is sliced into a set of alternative definitions
    (i.e. in a structure definition, there are multiple different constraints
    on a single element in the base resource). Slicing can be used in any
    resource that has cardinality ..* on the base resource, or any resource
    with a choice of types. The set of slices is any elements that come after
    this in the element sequence that have the same path, until a shorter path
    occurs (the shorter path terminates the set).
    """
    resource_type: ClassVar[str] = "ElementDefinitionSlicing"
    discriminator: Optional[List[ElementDefinitionSlicingDiscriminator]] = empty_list()
    description: Optional[str] = None
    ordered: Optional[bool] = None
    rules: str = None

    def elementProperties(self):
        js = super(ElementDefinitionSlicing, self).elementProperties()
        js.extend([
            ("discriminator", "discriminator", ElementDefinitionSlicingDiscriminator, True, None, False),
            ("description", "description", str, False, None, False),
            ("ordered", "ordered", bool, False, None, False),
            ("rules", "rules", str, False, None, True),
        ])
        return js


@dataclass
class ElementDefinitionBase(Element):
    """ Base definition information for tools.

    Information about the base definition of the element, provided to make it
    unnecessary for tools to trace the deviation of the element through the
    derived and related profiles. When the element definition is not the
    original definition of an element - i.g. either in a constraint on another
    type, or for elements from a super type in a snap shot - then the
    information in provided in the element definition may be different to the
    base definition. On the original definition of the element, it will be
    same.
    """
    resource_type: ClassVar[str] = "ElementDefinitionBase"
    path: str = None
    min: int = None
    max: str = None

    def elementProperties(self):
        js = super(ElementDefinitionBase, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, True),
            ("min", "min", int, False, None, True),
            ("max", "max", str, False, None, True),
        ])
        return js


@dataclass
class ElementDefinitionType(Element):
    """ Data type and Profile for this element.

    The data type or resource that the value of this element is permitted to
    be.
    """
    resource_type: ClassVar[str] = "ElementDefinitionType"
    code: str = None
    profile: Optional[List[str]] = empty_list()
    targetProfile: Optional[List[str]] = empty_list()
    aggregation: Optional[List[str]] = empty_list()
    versioning: Optional[str] = None

    def elementProperties(self):
        js = super(ElementDefinitionType, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("profile", "profile", str, True, None, False),
            ("targetProfile", "targetProfile", str, True, None, False),
            ("aggregation", "aggregation", str, True, None, False),
            ("versioning", "versioning", str, False, None, False),
        ])
        return js


@dataclass
class ElementDefinitionExample(Element):
    """ Example value (as defined for type).

    A sample value for this element demonstrating the type of information that
    would typically be found in the element.
    """
    resource_type: ClassVar[str] = "ElementDefinitionExample"
    label: str = None
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
        js = super(ElementDefinitionExample, self).elementProperties()
        js.extend([
            ("label", "label", str, False, None, True),
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
class ElementDefinitionConstraint(Element):
    """ Condition that must evaluate to true.

    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """
    resource_type: ClassVar[str] = "ElementDefinitionConstraint"
    key: str = None
    requirements: Optional[str] = None
    severity: str = None
    human: str = None
    expression: Optional[str] = None
    xpath: Optional[str] = None
    source: Optional[str] = None

    def elementProperties(self):
        js = super(ElementDefinitionConstraint, self).elementProperties()
        js.extend([
            ("key", "key", str, False, None, True),
            ("requirements", "requirements", str, False, None, False),
            ("severity", "severity", str, False, None, True),
            ("human", "human", str, False, None, True),
            ("expression", "expression", str, False, None, False),
            ("xpath", "xpath", str, False, None, False),
            ("source", "source", str, False, None, False),
        ])
        return js


@dataclass
class ElementDefinitionBinding(Element):
    """ ValueSet details if this is coded.

    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept, Quantity), or the data types (string, uri).
    """
    resource_type: ClassVar[str] = "ElementDefinitionBinding"
    strength: str = None
    description: Optional[str] = None
    valueSet: Optional[str] = None

    def elementProperties(self):
        js = super(ElementDefinitionBinding, self).elementProperties()
        js.extend([
            ("strength", "strength", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("valueSet", "valueSet", str, False, None, False),
        ])
        return js


@dataclass
class ElementDefinitionMapping(Element):
    """ Map element to another set of definitions.

    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """
    resource_type: ClassVar[str] = "ElementDefinitionMapping"
    identity: str = None
    language: Optional[str] = None
    map: str = None
    comment: Optional[str] = None

    def elementProperties(self):
        js = super(ElementDefinitionMapping, self).elementProperties()
        js.extend([
            ("identity", "identity", str, False, None, True),
            ("language", "language", str, False, None, False),
            ("map", "map", str, False, None, True),
            ("comment", "comment", str, False, None, False),
        ])
        return js


@dataclass
class ElementDefinition(BackboneElement):
    """ Definition of an element in a resource or extension.

    Captures constraints on each element within the resource, profile, or
    extension.
    """
    resource_type: ClassVar[str] = "ElementDefinition"
    path: str = None
    representation: Optional[List[str]] = empty_list()
    sliceName: Optional[str] = None
    sliceIsConstraining: Optional[bool] = None
    label: Optional[str] = None
    code: Optional[List[Coding]] = empty_list()
    slicing: Optional[ElementDefinitionSlicing] = None
    short: Optional[str] = None
    definition: Optional[str] = None
    comment: Optional[str] = None
    requirements: Optional[str] = None
    alias: Optional[List[str]] = empty_list()
    min: Optional[int] = None
    max: Optional[str] = None
    base: Optional[ElementDefinitionBase] = None
    contentReference: Optional[str] = None
    type: Optional[List[ElementDefinitionType]] = empty_list()
    defaultValueBase64Binary: Optional[str] = None
    defaultValueBoolean: Optional[bool] = None
    defaultValueCanonical: Optional[str] = None
    defaultValueCode: Optional[str] = None
    defaultValueDate: Optional[FHIRDate] = None
    defaultValueDateTime: Optional[FHIRDate] = None
    defaultValueDecimal: Optional[float] = None
    defaultValueId: Optional[str] = None
    defaultValueInstant: Optional[FHIRDate] = None
    defaultValueInteger: Optional[int] = None
    defaultValueMarkdown: Optional[str] = None
    defaultValueOid: Optional[str] = None
    defaultValuePositiveInt: Optional[int] = None
    defaultValueString: Optional[str] = None
    defaultValueTime: Optional[FHIRDate] = None
    defaultValueUnsignedInt: Optional[int] = None
    defaultValueUri: Optional[str] = None
    defaultValueUrl: Optional[str] = None
    defaultValueUuid: Optional[str] = None
    defaultValueAddress: Optional[Address] = None
    defaultValueAge: Optional[Age] = None
    defaultValueAnnotation: Optional[Annotation] = None
    defaultValueAttachment: Optional[Attachment] = None
    defaultValueCodeableConcept: Optional[CodeableConcept] = None
    defaultValueCoding: Optional[Coding] = None
    defaultValueContactPoint: Optional[ContactPoint] = None
    defaultValueCount: Optional[Count] = None
    defaultValueDistance: Optional[Distance] = None
    defaultValueDuration: Optional[Duration] = None
    defaultValueHumanName: Optional[HumanName] = None
    defaultValueIdentifier: Optional[Identifier] = None
    defaultValueMoney: Optional[Money] = None
    defaultValuePeriod: Optional[Period] = None
    defaultValueQuantity: Optional[Quantity] = None
    defaultValueRange: Optional[Range] = None
    defaultValueRatio: Optional[Ratio] = None
    defaultValueReference: Optional[FHIRReference] = None
    defaultValueSampledData: Optional[SampledData] = None
    defaultValueSignature: Optional[Signature] = None
    defaultValueTiming: Optional[Timing] = None
    defaultValueContactDetail: Optional[ContactDetail] = None
    defaultValueContributor: Optional[Contributor] = None
    defaultValueDataRequirement: Optional[DataRequirement] = None
    defaultValueExpression: Optional[Expression] = None
    defaultValueParameterDefinition: Optional[ParameterDefinition] = None
    defaultValueRelatedArtifact: Optional[RelatedArtifact] = None
    defaultValueTriggerDefinition: Optional[TriggerDefinition] = None
    defaultValueUsageContext: Optional[UsageContext] = None
    defaultValueDosage: Optional[Dosage] = None
    meaningWhenMissing: Optional[str] = None
    orderMeaning: Optional[str] = None
    fixedBase64Binary: Optional[str] = None
    fixedBoolean: Optional[bool] = None
    fixedCanonical: Optional[str] = None
    fixedCode: Optional[str] = None
    fixedDate: Optional[FHIRDate] = None
    fixedDateTime: Optional[FHIRDate] = None
    fixedDecimal: Optional[float] = None
    fixedId: Optional[str] = None
    fixedInstant: Optional[FHIRDate] = None
    fixedInteger: Optional[int] = None
    fixedMarkdown: Optional[str] = None
    fixedOid: Optional[str] = None
    fixedPositiveInt: Optional[int] = None
    fixedString: Optional[str] = None
    fixedTime: Optional[FHIRDate] = None
    fixedUnsignedInt: Optional[int] = None
    fixedUri: Optional[str] = None
    fixedUrl: Optional[str] = None
    fixedUuid: Optional[str] = None
    fixedAddress: Optional[Address] = None
    fixedAge: Optional[Age] = None
    fixedAnnotation: Optional[Annotation] = None
    fixedAttachment: Optional[Attachment] = None
    fixedCodeableConcept: Optional[CodeableConcept] = None
    fixedCoding: Optional[Coding] = None
    fixedContactPoint: Optional[ContactPoint] = None
    fixedCount: Optional[Count] = None
    fixedDistance: Optional[Distance] = None
    fixedDuration: Optional[Duration] = None
    fixedHumanName: Optional[HumanName] = None
    fixedIdentifier: Optional[Identifier] = None
    fixedMoney: Optional[Money] = None
    fixedPeriod: Optional[Period] = None
    fixedQuantity: Optional[Quantity] = None
    fixedRange: Optional[Range] = None
    fixedRatio: Optional[Ratio] = None
    fixedReference: Optional[FHIRReference] = None
    fixedSampledData: Optional[SampledData] = None
    fixedSignature: Optional[Signature] = None
    fixedTiming: Optional[Timing] = None
    fixedContactDetail: Optional[ContactDetail] = None
    fixedContributor: Optional[Contributor] = None
    fixedDataRequirement: Optional[DataRequirement] = None
    fixedExpression: Optional[Expression] = None
    fixedParameterDefinition: Optional[ParameterDefinition] = None
    fixedRelatedArtifact: Optional[RelatedArtifact] = None
    fixedTriggerDefinition: Optional[TriggerDefinition] = None
    fixedUsageContext: Optional[UsageContext] = None
    fixedDosage: Optional[Dosage] = None
    patternBase64Binary: Optional[str] = None
    patternBoolean: Optional[bool] = None
    patternCanonical: Optional[str] = None
    patternCode: Optional[str] = None
    patternDate: Optional[FHIRDate] = None
    patternDateTime: Optional[FHIRDate] = None
    patternDecimal: Optional[float] = None
    patternId: Optional[str] = None
    patternInstant: Optional[FHIRDate] = None
    patternInteger: Optional[int] = None
    patternMarkdown: Optional[str] = None
    patternOid: Optional[str] = None
    patternPositiveInt: Optional[int] = None
    patternString: Optional[str] = None
    patternTime: Optional[FHIRDate] = None
    patternUnsignedInt: Optional[int] = None
    patternUri: Optional[str] = None
    patternUrl: Optional[str] = None
    patternUuid: Optional[str] = None
    patternAddress: Optional[Address] = None
    patternAge: Optional[Age] = None
    patternAnnotation: Optional[Annotation] = None
    patternAttachment: Optional[Attachment] = None
    patternCodeableConcept: Optional[CodeableConcept] = None
    patternCoding: Optional[Coding] = None
    patternContactPoint: Optional[ContactPoint] = None
    patternCount: Optional[Count] = None
    patternDistance: Optional[Distance] = None
    patternDuration: Optional[Duration] = None
    patternHumanName: Optional[HumanName] = None
    patternIdentifier: Optional[Identifier] = None
    patternMoney: Optional[Money] = None
    patternPeriod: Optional[Period] = None
    patternQuantity: Optional[Quantity] = None
    patternRange: Optional[Range] = None
    patternRatio: Optional[Ratio] = None
    patternReference: Optional[FHIRReference] = None
    patternSampledData: Optional[SampledData] = None
    patternSignature: Optional[Signature] = None
    patternTiming: Optional[Timing] = None
    patternContactDetail: Optional[ContactDetail] = None
    patternContributor: Optional[Contributor] = None
    patternDataRequirement: Optional[DataRequirement] = None
    patternExpression: Optional[Expression] = None
    patternParameterDefinition: Optional[ParameterDefinition] = None
    patternRelatedArtifact: Optional[RelatedArtifact] = None
    patternTriggerDefinition: Optional[TriggerDefinition] = None
    patternUsageContext: Optional[UsageContext] = None
    patternDosage: Optional[Dosage] = None
    example: Optional[List[ElementDefinitionExample]] = empty_list()
    minValueDate: Optional[FHIRDate] = None
    minValueDateTime: Optional[FHIRDate] = None
    minValueInstant: Optional[FHIRDate] = None
    minValueTime: Optional[FHIRDate] = None
    minValueDecimal: Optional[float] = None
    minValueInteger: Optional[int] = None
    minValuePositiveInt: Optional[int] = None
    minValueUnsignedInt: Optional[int] = None
    minValueQuantity: Optional[Quantity] = None
    maxValueDate: Optional[FHIRDate] = None
    maxValueDateTime: Optional[FHIRDate] = None
    maxValueInstant: Optional[FHIRDate] = None
    maxValueTime: Optional[FHIRDate] = None
    maxValueDecimal: Optional[float] = None
    maxValueInteger: Optional[int] = None
    maxValuePositiveInt: Optional[int] = None
    maxValueUnsignedInt: Optional[int] = None
    maxValueQuantity: Optional[Quantity] = None
    maxLength: Optional[int] = None
    condition: Optional[List[str]] = empty_list()
    constraint: Optional[List[ElementDefinitionConstraint]] = empty_list()
    mustSupport: Optional[bool] = None
    isModifier: Optional[bool] = None
    isModifierReason: Optional[str] = None
    isSummary: Optional[bool] = None
    binding: Optional[ElementDefinitionBinding] = None
    mapping: Optional[List[ElementDefinitionMapping]] = empty_list()

    def elementProperties(self):
        js = super(ElementDefinition, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, True),
            ("representation", "representation", str, True, None, False),
            ("sliceName", "sliceName", str, False, None, False),
            ("sliceIsConstraining", "sliceIsConstraining", bool, False, None, False),
            ("label", "label", str, False, None, False),
            ("code", "code", Coding, True, None, False),
            ("slicing", "slicing", ElementDefinitionSlicing, False, None, False),
            ("short", "short", str, False, None, False),
            ("definition", "definition", str, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("min", "min", int, False, None, False),
            ("max", "max", str, False, None, False),
            ("base", "base", ElementDefinitionBase, False, None, False),
            ("contentReference", "contentReference", str, False, None, False),
            ("type", "type", ElementDefinitionType, True, None, False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, False, "defaultValue", False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, False, "defaultValue", False),
            ("defaultValueCanonical", "defaultValueCanonical", str, False, "defaultValue", False),
            ("defaultValueCode", "defaultValueCode", str, False, "defaultValue", False),
            ("defaultValueDate", "defaultValueDate", FHIRDate, False, "defaultValue", False),
            ("defaultValueDateTime", "defaultValueDateTime", FHIRDate, False, "defaultValue", False),
            ("defaultValueDecimal", "defaultValueDecimal", float, False, "defaultValue", False),
            ("defaultValueId", "defaultValueId", str, False, "defaultValue", False),
            ("defaultValueInstant", "defaultValueInstant", FHIRDate, False, "defaultValue", False),
            ("defaultValueInteger", "defaultValueInteger", int, False, "defaultValue", False),
            ("defaultValueMarkdown", "defaultValueMarkdown", str, False, "defaultValue", False),
            ("defaultValueOid", "defaultValueOid", str, False, "defaultValue", False),
            ("defaultValuePositiveInt", "defaultValuePositiveInt", int, False, "defaultValue", False),
            ("defaultValueString", "defaultValueString", str, False, "defaultValue", False),
            ("defaultValueTime", "defaultValueTime", FHIRDate, False, "defaultValue", False),
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", int, False, "defaultValue", False),
            ("defaultValueUri", "defaultValueUri", str, False, "defaultValue", False),
            ("defaultValueUrl", "defaultValueUrl", str, False, "defaultValue", False),
            ("defaultValueUuid", "defaultValueUuid", str, False, "defaultValue", False),
            ("defaultValueAddress", "defaultValueAddress", Address, False, "defaultValue", False),
            ("defaultValueAge", "defaultValueAge", Age, False, "defaultValue", False),
            ("defaultValueAnnotation", "defaultValueAnnotation", Annotation, False, "defaultValue", False),
            ("defaultValueAttachment", "defaultValueAttachment", Attachment, False, "defaultValue", False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", CodeableConcept, False, "defaultValue", False),
            ("defaultValueCoding", "defaultValueCoding", Coding, False, "defaultValue", False),
            ("defaultValueContactPoint", "defaultValueContactPoint", ContactPoint, False, "defaultValue", False),
            ("defaultValueCount", "defaultValueCount", Count, False, "defaultValue", False),
            ("defaultValueDistance", "defaultValueDistance", Distance, False, "defaultValue", False),
            ("defaultValueDuration", "defaultValueDuration", Duration, False, "defaultValue", False),
            ("defaultValueHumanName", "defaultValueHumanName", HumanName, False, "defaultValue", False),
            ("defaultValueIdentifier", "defaultValueIdentifier", Identifier, False, "defaultValue", False),
            ("defaultValueMoney", "defaultValueMoney", Money, False, "defaultValue", False),
            ("defaultValuePeriod", "defaultValuePeriod", Period, False, "defaultValue", False),
            ("defaultValueQuantity", "defaultValueQuantity", Quantity, False, "defaultValue", False),
            ("defaultValueRange", "defaultValueRange", Range, False, "defaultValue", False),
            ("defaultValueRatio", "defaultValueRatio", Ratio, False, "defaultValue", False),
            ("defaultValueReference", "defaultValueReference", FHIRReference, False, "defaultValue", False),
            ("defaultValueSampledData", "defaultValueSampledData", SampledData, False, "defaultValue", False),
            ("defaultValueSignature", "defaultValueSignature", Signature, False, "defaultValue", False),
            ("defaultValueTiming", "defaultValueTiming", Timing, False, "defaultValue", False),
            ("defaultValueContactDetail", "defaultValueContactDetail", ContactDetail, False, "defaultValue", False),
            ("defaultValueContributor", "defaultValueContributor", Contributor, False, "defaultValue", False),
            ("defaultValueDataRequirement", "defaultValueDataRequirement", DataRequirement, False, "defaultValue", False),
            ("defaultValueExpression", "defaultValueExpression", Expression, False, "defaultValue", False),
            ("defaultValueParameterDefinition", "defaultValueParameterDefinition", ParameterDefinition, False, "defaultValue", False),
            ("defaultValueRelatedArtifact", "defaultValueRelatedArtifact", RelatedArtifact, False, "defaultValue", False),
            ("defaultValueTriggerDefinition", "defaultValueTriggerDefinition", TriggerDefinition, False, "defaultValue", False),
            ("defaultValueUsageContext", "defaultValueUsageContext", UsageContext, False, "defaultValue", False),
            ("defaultValueDosage", "defaultValueDosage", Dosage, False, "defaultValue", False),
            ("meaningWhenMissing", "meaningWhenMissing", str, False, None, False),
            ("orderMeaning", "orderMeaning", str, False, None, False),
            ("fixedBase64Binary", "fixedBase64Binary", str, False, "fixed", False),
            ("fixedBoolean", "fixedBoolean", bool, False, "fixed", False),
            ("fixedCanonical", "fixedCanonical", str, False, "fixed", False),
            ("fixedCode", "fixedCode", str, False, "fixed", False),
            ("fixedDate", "fixedDate", FHIRDate, False, "fixed", False),
            ("fixedDateTime", "fixedDateTime", FHIRDate, False, "fixed", False),
            ("fixedDecimal", "fixedDecimal", float, False, "fixed", False),
            ("fixedId", "fixedId", str, False, "fixed", False),
            ("fixedInstant", "fixedInstant", FHIRDate, False, "fixed", False),
            ("fixedInteger", "fixedInteger", int, False, "fixed", False),
            ("fixedMarkdown", "fixedMarkdown", str, False, "fixed", False),
            ("fixedOid", "fixedOid", str, False, "fixed", False),
            ("fixedPositiveInt", "fixedPositiveInt", int, False, "fixed", False),
            ("fixedString", "fixedString", str, False, "fixed", False),
            ("fixedTime", "fixedTime", FHIRDate, False, "fixed", False),
            ("fixedUnsignedInt", "fixedUnsignedInt", int, False, "fixed", False),
            ("fixedUri", "fixedUri", str, False, "fixed", False),
            ("fixedUrl", "fixedUrl", str, False, "fixed", False),
            ("fixedUuid", "fixedUuid", str, False, "fixed", False),
            ("fixedAddress", "fixedAddress", Address, False, "fixed", False),
            ("fixedAge", "fixedAge", Age, False, "fixed", False),
            ("fixedAnnotation", "fixedAnnotation", Annotation, False, "fixed", False),
            ("fixedAttachment", "fixedAttachment", Attachment, False, "fixed", False),
            ("fixedCodeableConcept", "fixedCodeableConcept", CodeableConcept, False, "fixed", False),
            ("fixedCoding", "fixedCoding", Coding, False, "fixed", False),
            ("fixedContactPoint", "fixedContactPoint", ContactPoint, False, "fixed", False),
            ("fixedCount", "fixedCount", Count, False, "fixed", False),
            ("fixedDistance", "fixedDistance", Distance, False, "fixed", False),
            ("fixedDuration", "fixedDuration", Duration, False, "fixed", False),
            ("fixedHumanName", "fixedHumanName", HumanName, False, "fixed", False),
            ("fixedIdentifier", "fixedIdentifier", Identifier, False, "fixed", False),
            ("fixedMoney", "fixedMoney", Money, False, "fixed", False),
            ("fixedPeriod", "fixedPeriod", Period, False, "fixed", False),
            ("fixedQuantity", "fixedQuantity", Quantity, False, "fixed", False),
            ("fixedRange", "fixedRange", Range, False, "fixed", False),
            ("fixedRatio", "fixedRatio", Ratio, False, "fixed", False),
            ("fixedReference", "fixedReference", FHIRReference, False, "fixed", False),
            ("fixedSampledData", "fixedSampledData", SampledData, False, "fixed", False),
            ("fixedSignature", "fixedSignature", Signature, False, "fixed", False),
            ("fixedTiming", "fixedTiming", Timing, False, "fixed", False),
            ("fixedContactDetail", "fixedContactDetail", ContactDetail, False, "fixed", False),
            ("fixedContributor", "fixedContributor", Contributor, False, "fixed", False),
            ("fixedDataRequirement", "fixedDataRequirement", DataRequirement, False, "fixed", False),
            ("fixedExpression", "fixedExpression", Expression, False, "fixed", False),
            ("fixedParameterDefinition", "fixedParameterDefinition", ParameterDefinition, False, "fixed", False),
            ("fixedRelatedArtifact", "fixedRelatedArtifact", RelatedArtifact, False, "fixed", False),
            ("fixedTriggerDefinition", "fixedTriggerDefinition", TriggerDefinition, False, "fixed", False),
            ("fixedUsageContext", "fixedUsageContext", UsageContext, False, "fixed", False),
            ("fixedDosage", "fixedDosage", Dosage, False, "fixed", False),
            ("patternBase64Binary", "patternBase64Binary", str, False, "pattern", False),
            ("patternBoolean", "patternBoolean", bool, False, "pattern", False),
            ("patternCanonical", "patternCanonical", str, False, "pattern", False),
            ("patternCode", "patternCode", str, False, "pattern", False),
            ("patternDate", "patternDate", FHIRDate, False, "pattern", False),
            ("patternDateTime", "patternDateTime", FHIRDate, False, "pattern", False),
            ("patternDecimal", "patternDecimal", float, False, "pattern", False),
            ("patternId", "patternId", str, False, "pattern", False),
            ("patternInstant", "patternInstant", FHIRDate, False, "pattern", False),
            ("patternInteger", "patternInteger", int, False, "pattern", False),
            ("patternMarkdown", "patternMarkdown", str, False, "pattern", False),
            ("patternOid", "patternOid", str, False, "pattern", False),
            ("patternPositiveInt", "patternPositiveInt", int, False, "pattern", False),
            ("patternString", "patternString", str, False, "pattern", False),
            ("patternTime", "patternTime", FHIRDate, False, "pattern", False),
            ("patternUnsignedInt", "patternUnsignedInt", int, False, "pattern", False),
            ("patternUri", "patternUri", str, False, "pattern", False),
            ("patternUrl", "patternUrl", str, False, "pattern", False),
            ("patternUuid", "patternUuid", str, False, "pattern", False),
            ("patternAddress", "patternAddress", Address, False, "pattern", False),
            ("patternAge", "patternAge", Age, False, "pattern", False),
            ("patternAnnotation", "patternAnnotation", Annotation, False, "pattern", False),
            ("patternAttachment", "patternAttachment", Attachment, False, "pattern", False),
            ("patternCodeableConcept", "patternCodeableConcept", CodeableConcept, False, "pattern", False),
            ("patternCoding", "patternCoding", Coding, False, "pattern", False),
            ("patternContactPoint", "patternContactPoint", ContactPoint, False, "pattern", False),
            ("patternCount", "patternCount", Count, False, "pattern", False),
            ("patternDistance", "patternDistance", Distance, False, "pattern", False),
            ("patternDuration", "patternDuration", Duration, False, "pattern", False),
            ("patternHumanName", "patternHumanName", HumanName, False, "pattern", False),
            ("patternIdentifier", "patternIdentifier", Identifier, False, "pattern", False),
            ("patternMoney", "patternMoney", Money, False, "pattern", False),
            ("patternPeriod", "patternPeriod", Period, False, "pattern", False),
            ("patternQuantity", "patternQuantity", Quantity, False, "pattern", False),
            ("patternRange", "patternRange", Range, False, "pattern", False),
            ("patternRatio", "patternRatio", Ratio, False, "pattern", False),
            ("patternReference", "patternReference", FHIRReference, False, "pattern", False),
            ("patternSampledData", "patternSampledData", SampledData, False, "pattern", False),
            ("patternSignature", "patternSignature", Signature, False, "pattern", False),
            ("patternTiming", "patternTiming", Timing, False, "pattern", False),
            ("patternContactDetail", "patternContactDetail", ContactDetail, False, "pattern", False),
            ("patternContributor", "patternContributor", Contributor, False, "pattern", False),
            ("patternDataRequirement", "patternDataRequirement", DataRequirement, False, "pattern", False),
            ("patternExpression", "patternExpression", Expression, False, "pattern", False),
            ("patternParameterDefinition", "patternParameterDefinition", ParameterDefinition, False, "pattern", False),
            ("patternRelatedArtifact", "patternRelatedArtifact", RelatedArtifact, False, "pattern", False),
            ("patternTriggerDefinition", "patternTriggerDefinition", TriggerDefinition, False, "pattern", False),
            ("patternUsageContext", "patternUsageContext", UsageContext, False, "pattern", False),
            ("patternDosage", "patternDosage", Dosage, False, "pattern", False),
            ("example", "example", ElementDefinitionExample, True, None, False),
            ("minValueDate", "minValueDate", FHIRDate, False, "minValue", False),
            ("minValueDateTime", "minValueDateTime", FHIRDate, False, "minValue", False),
            ("minValueInstant", "minValueInstant", FHIRDate, False, "minValue", False),
            ("minValueTime", "minValueTime", FHIRDate, False, "minValue", False),
            ("minValueDecimal", "minValueDecimal", float, False, "minValue", False),
            ("minValueInteger", "minValueInteger", int, False, "minValue", False),
            ("minValuePositiveInt", "minValuePositiveInt", int, False, "minValue", False),
            ("minValueUnsignedInt", "minValueUnsignedInt", int, False, "minValue", False),
            ("minValueQuantity", "minValueQuantity", Quantity, False, "minValue", False),
            ("maxValueDate", "maxValueDate", FHIRDate, False, "maxValue", False),
            ("maxValueDateTime", "maxValueDateTime", FHIRDate, False, "maxValue", False),
            ("maxValueInstant", "maxValueInstant", FHIRDate, False, "maxValue", False),
            ("maxValueTime", "maxValueTime", FHIRDate, False, "maxValue", False),
            ("maxValueDecimal", "maxValueDecimal", float, False, "maxValue", False),
            ("maxValueInteger", "maxValueInteger", int, False, "maxValue", False),
            ("maxValuePositiveInt", "maxValuePositiveInt", int, False, "maxValue", False),
            ("maxValueUnsignedInt", "maxValueUnsignedInt", int, False, "maxValue", False),
            ("maxValueQuantity", "maxValueQuantity", Quantity, False, "maxValue", False),
            ("maxLength", "maxLength", int, False, None, False),
            ("condition", "condition", str, True, None, False),
            ("constraint", "constraint", ElementDefinitionConstraint, True, None, False),
            ("mustSupport", "mustSupport", bool, False, None, False),
            ("isModifier", "isModifier", bool, False, None, False),
            ("isModifierReason", "isModifierReason", str, False, None, False),
            ("isSummary", "isSummary", bool, False, None, False),
            ("binding", "binding", ElementDefinitionBinding, False, None, False),
            ("mapping", "mapping", ElementDefinitionMapping, True, None, False),
        ])
        return js