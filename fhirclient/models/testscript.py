#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/TestScript) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .usagecontext import UsageContext


@dataclass
class TestScriptTeardownAction(BackboneElement):
    """ One or more teardown operations to perform.

    The teardown action will only contain an operation.
    """
    resource_type: ClassVar[str] = "TestScriptTeardownAction"
    operation: "TestScriptSetupActionOperation" = None

    def elementProperties(self):
        js = super(TestScriptTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestScriptSetupActionOperation, False, None, True),
        ])
        return js


@dataclass
class TestScriptTestAction(BackboneElement):
    """ A test operation or assert to perform.

    Action would contain either an operation or an assertion.
    """
    resource_type: ClassVar[str] = "TestScriptTestAction"
    operation: Optional["TestScriptSetupActionOperation"] = None
    assert_fhir: Optional["TestScriptSetupActionAssert"] = None

    def elementProperties(self):
        js = super(TestScriptTestAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
            ("assert_fhir", "assert", TestScriptSetupActionAssert, False, None, False),
        ])
        return js


@dataclass
class TestScriptSetupActionOperationRequestHeader(BackboneElement):
    """ Each operation can have one or more header elements.

    Header elements would be used to set HTTP headers.
    """
    resource_type: ClassVar[str] = "TestScriptSetupActionOperationRequestHeader"
    field: str = None
    value: str = None

    def elementProperties(self):
        js = super(TestScriptSetupActionOperationRequestHeader, self).elementProperties()
        js.extend([
            ("field", "field", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


@dataclass
class TestScriptSetupActionOperation(BackboneElement):
    """ The setup operation to perform.

    The operation to perform.
    """
    resource_type: ClassVar[str] = "TestScriptSetupActionOperation"
    type: Optional[Coding] = None
    resource: Optional[str] = None
    label: Optional[str] = None
    description: Optional[str] = None
    accept: Optional[str] = None
    contentType: Optional[str] = None
    destination: Optional[int] = None
    encodeRequestUrl: bool = None
    method: Optional[str] = None
    origin: Optional[int] = None
    params: Optional[str] = None
    requestHeader: Optional[List[TestScriptSetupActionOperationRequestHeader]] = empty_list()
    requestId: Optional[str] = None
    responseId: Optional[str] = None
    sourceId: Optional[str] = None
    targetId: Optional[str] = None
    url: Optional[str] = None

    def elementProperties(self):
        js = super(TestScriptSetupActionOperation, self).elementProperties()
        js.extend([
            ("type", "type", Coding, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("label", "label", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("accept", "accept", str, False, None, False),
            ("contentType", "contentType", str, False, None, False),
            ("destination", "destination", int, False, None, False),
            ("encodeRequestUrl", "encodeRequestUrl", bool, False, None, True),
            ("method", "method", str, False, None, False),
            ("origin", "origin", int, False, None, False),
            ("params", "params", str, False, None, False),
            ("requestHeader", "requestHeader", TestScriptSetupActionOperationRequestHeader, True, None, False),
            ("requestId", "requestId", str, False, None, False),
            ("responseId", "responseId", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("targetId", "targetId", str, False, None, False),
            ("url", "url", str, False, None, False),
        ])
        return js


@dataclass
class TestScriptSetupActionAssert(BackboneElement):
    """ The assertion to perform.

    Evaluates the results of previous operations to determine if the server
    under test behaves appropriately.
    """
    resource_type: ClassVar[str] = "TestScriptSetupActionAssert"
    label: Optional[str] = None
    description: Optional[str] = None
    direction: Optional[str] = None
    compareToSourceId: Optional[str] = None
    compareToSourceExpression: Optional[str] = None
    compareToSourcePath: Optional[str] = None
    contentType: Optional[str] = None
    expression: Optional[str] = None
    headerField: Optional[str] = None
    minimumId: Optional[str] = None
    navigationLinks: Optional[bool] = None
    operator: Optional[str] = None
    path: Optional[str] = None
    requestMethod: Optional[str] = None
    requestURL: Optional[str] = None
    resource: Optional[str] = None
    response: Optional[str] = None
    responseCode: Optional[str] = None
    sourceId: Optional[str] = None
    validateProfileId: Optional[str] = None
    value: Optional[str] = None
    warningOnly: bool = None

    def elementProperties(self):
        js = super(TestScriptSetupActionAssert, self).elementProperties()
        js.extend([
            ("label", "label", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("direction", "direction", str, False, None, False),
            ("compareToSourceId", "compareToSourceId", str, False, None, False),
            ("compareToSourceExpression", "compareToSourceExpression", str, False, None, False),
            ("compareToSourcePath", "compareToSourcePath", str, False, None, False),
            ("contentType", "contentType", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("headerField", "headerField", str, False, None, False),
            ("minimumId", "minimumId", str, False, None, False),
            ("navigationLinks", "navigationLinks", bool, False, None, False),
            ("operator", "operator", str, False, None, False),
            ("path", "path", str, False, None, False),
            ("requestMethod", "requestMethod", str, False, None, False),
            ("requestURL", "requestURL", str, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("response", "response", str, False, None, False),
            ("responseCode", "responseCode", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("validateProfileId", "validateProfileId", str, False, None, False),
            ("value", "value", str, False, None, False),
            ("warningOnly", "warningOnly", bool, False, None, True),
        ])
        return js


@dataclass
class TestScriptSetupAction(BackboneElement):
    """ A setup operation or assert to perform.

    Action would contain either an operation or an assertion.
    """
    resource_type: ClassVar[str] = "TestScriptSetupAction"
    operation: Optional[TestScriptSetupActionOperation] = None
    assert_fhir: Optional[TestScriptSetupActionAssert] = None

    def elementProperties(self):
        js = super(TestScriptSetupAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
            ("assert_fhir", "assert", TestScriptSetupActionAssert, False, None, False),
        ])
        return js


@dataclass
class TestScriptMetadataLink(BackboneElement):
    """ Links to the FHIR specification.

    A link to the FHIR specification that this test is covering.
    """
    resource_type: ClassVar[str] = "TestScriptMetadataLink"
    url: str = None
    description: Optional[str] = None

    def elementProperties(self):
        js = super(TestScriptMetadataLink, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("description", "description", str, False, None, False),
        ])
        return js


@dataclass
class TestScriptMetadataCapability(BackboneElement):
    """ Capabilities  that are assumed to function correctly on the FHIR server
    being tested.

    Capabilities that must exist and are assumed to function correctly on the
    FHIR server being tested.
    """
    resource_type: ClassVar[str] = "TestScriptMetadataCapability"
    required: bool = None
    validated: bool = None
    description: Optional[str] = None
    origin: Optional[List[int]] = empty_list()
    destination: Optional[int] = None
    link: Optional[List[str]] = empty_list()
    capabilities: str = None

    def elementProperties(self):
        js = super(TestScriptMetadataCapability, self).elementProperties()
        js.extend([
            ("required", "required", bool, False, None, True),
            ("validated", "validated", bool, False, None, True),
            ("description", "description", str, False, None, False),
            ("origin", "origin", int, True, None, False),
            ("destination", "destination", int, False, None, False),
            ("link", "link", str, True, None, False),
            ("capabilities", "capabilities", str, False, None, True),
        ])
        return js


@dataclass
class TestScriptOrigin(BackboneElement):
    """ An abstract server representing a client or sender in a message exchange.

    An abstract server used in operations within this test script in the origin
    element.
    """
    resource_type: ClassVar[str] = "TestScriptOrigin"
    index: int = None
    profile: Coding = None

    def elementProperties(self):
        js = super(TestScriptOrigin, self).elementProperties()
        js.extend([
            ("index", "index", int, False, None, True),
            ("profile", "profile", Coding, False, None, True),
        ])
        return js


@dataclass
class TestScriptDestination(BackboneElement):
    """ An abstract server representing a destination or receiver in a message
    exchange.

    An abstract server used in operations within this test script in the
    destination element.
    """
    resource_type: ClassVar[str] = "TestScriptDestination"
    index: int = None
    profile: Coding = None

    def elementProperties(self):
        js = super(TestScriptDestination, self).elementProperties()
        js.extend([
            ("index", "index", int, False, None, True),
            ("profile", "profile", Coding, False, None, True),
        ])
        return js


@dataclass
class TestScriptMetadata(BackboneElement):
    """ Required capability that is assumed to function correctly on the FHIR
    server being tested.

    The required capability must exist and are assumed to function correctly on
    the FHIR server being tested.
    """
    resource_type: ClassVar[str] = "TestScriptMetadata"
    link: Optional[List[TestScriptMetadataLink]] = empty_list()
    capability: List[TestScriptMetadataCapability] = empty_list()

    def elementProperties(self):
        js = super(TestScriptMetadata, self).elementProperties()
        js.extend([
            ("link", "link", TestScriptMetadataLink, True, None, False),
            ("capability", "capability", TestScriptMetadataCapability, True, None, True),
        ])
        return js


@dataclass
class TestScriptFixture(BackboneElement):
    """ Fixture in the test script - by reference (uri).

    Fixture in the test script - by reference (uri). All fixtures are required
    for the test script to execute.
    """
    resource_type: ClassVar[str] = "TestScriptFixture"
    autocreate: bool = None
    autodelete: bool = None
    resource: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(TestScriptFixture, self).elementProperties()
        js.extend([
            ("autocreate", "autocreate", bool, False, None, True),
            ("autodelete", "autodelete", bool, False, None, True),
            ("resource", "resource", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class TestScriptVariable(BackboneElement):
    """ Placeholder for evaluated elements.

    Variable is set based either on element value in response body or on header
    field value in the response headers.
    """
    resource_type: ClassVar[str] = "TestScriptVariable"
    name: str = None
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    expression: Optional[str] = None
    headerField: Optional[str] = None
    hint: Optional[str] = None
    path: Optional[str] = None
    sourceId: Optional[str] = None

    def elementProperties(self):
        js = super(TestScriptVariable, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("defaultValue", "defaultValue", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("headerField", "headerField", str, False, None, False),
            ("hint", "hint", str, False, None, False),
            ("path", "path", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
        ])
        return js


@dataclass
class TestScriptSetup(BackboneElement):
    """ A series of required setup operations before tests are executed.
    """
    resource_type: ClassVar[str] = "TestScriptSetup"
    action: List[TestScriptSetupAction] = empty_list()

    def elementProperties(self):
        js = super(TestScriptSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptSetupAction, True, None, True),
        ])
        return js


@dataclass
class TestScriptTest(BackboneElement):
    """ A test in this script.
    """
    resource_type: ClassVar[str] = "TestScriptTest"
    name: Optional[str] = None
    description: Optional[str] = None
    action: List[TestScriptTestAction] = empty_list()

    def elementProperties(self):
        js = super(TestScriptTest, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("action", "action", TestScriptTestAction, True, None, True),
        ])
        return js


@dataclass
class TestScriptTeardown(BackboneElement):
    """ A series of required clean up steps.

    A series of operations required to clean up after all the tests are
    executed (successfully or otherwise).
    """
    resource_type: ClassVar[str] = "TestScriptTeardown"
    action: List[TestScriptTeardownAction] = empty_list()

    def elementProperties(self):
        js = super(TestScriptTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptTeardownAction, True, None, True),
        ])
        return js


@dataclass
class TestScript(DomainResource):
    """ Describes a set of tests.

    A structured set of tests against a FHIR server or client implementation to
    determine compliance against the FHIR specification.
    """
    resource_type: ClassVar[str] = "TestScript"
    url: str = None
    identifier: Optional[Identifier] = None
    version: Optional[str] = None
    name: str = None
    title: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    origin: Optional[List[TestScriptOrigin]] = empty_list()
    destination: Optional[List[TestScriptDestination]] = empty_list()
    metadata: Optional[TestScriptMetadata] = None
    fixture: Optional[List[TestScriptFixture]] = empty_list()
    profile: Optional[List[FHIRReference]] = empty_list()
    variable: Optional[List[TestScriptVariable]] = empty_list()
    setup: Optional[TestScriptSetup] = None
    test: Optional[List[TestScriptTest]] = empty_list()
    teardown: Optional[TestScriptTeardown] = None

    def elementProperties(self):
        js = super(TestScript, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("identifier", "identifier", Identifier, False, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("origin", "origin", TestScriptOrigin, True, None, False),
            ("destination", "destination", TestScriptDestination, True, None, False),
            ("metadata", "metadata", TestScriptMetadata, False, None, False),
            ("fixture", "fixture", TestScriptFixture, True, None, False),
            ("profile", "profile", FHIRReference, True, None, False),
            ("variable", "variable", TestScriptVariable, True, None, False),
            ("setup", "setup", TestScriptSetup, False, None, False),
            ("test", "test", TestScriptTest, True, None, False),
            ("teardown", "teardown", TestScriptTeardown, False, None, False),
        ])
        return js