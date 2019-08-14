#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/TestReport) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class TestReportTeardownAction(BackboneElement):
    """ One or more teardown operations performed.

    The teardown action will only contain an operation.
    """
    resource_type: ClassVar[str] = "TestReportTeardownAction"
    operation: "TestReportSetupActionOperation" = None

    def elementProperties(self):
        js = super(TestReportTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestReportSetupActionOperation, False, None, True),
        ])
        return js


@dataclass
class TestReportTestAction(BackboneElement):
    """ A test operation or assert that was performed.

    Action would contain either an operation or an assertion.
    """
    resource_type: ClassVar[str] = "TestReportTestAction"
    operation: Optional["TestReportSetupActionOperation"] = None
    assert_fhir: Optional["TestReportSetupActionAssert"] = None

    def elementProperties(self):
        js = super(TestReportTestAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestReportSetupActionOperation, False, None, False),
            ("assert_fhir", "assert", TestReportSetupActionAssert, False, None, False),
        ])
        return js


@dataclass
class TestReportSetupActionOperation(BackboneElement):
    """ The operation to perform.

    The operation performed.
    """
    resource_type: ClassVar[str] = "TestReportSetupActionOperation"
    result: str = None
    message: Optional[str] = None
    detail: Optional[str] = None

    def elementProperties(self):
        js = super(TestReportSetupActionOperation, self).elementProperties()
        js.extend([
            ("result", "result", str, False, None, True),
            ("message", "message", str, False, None, False),
            ("detail", "detail", str, False, None, False),
        ])
        return js


@dataclass
class TestReportSetupActionAssert(BackboneElement):
    """ The assertion to perform.

    The results of the assertion performed on the previous operations.
    """
    resource_type: ClassVar[str] = "TestReportSetupActionAssert"
    result: str = None
    message: Optional[str] = None
    detail: Optional[str] = None

    def elementProperties(self):
        js = super(TestReportSetupActionAssert, self).elementProperties()
        js.extend([
            ("result", "result", str, False, None, True),
            ("message", "message", str, False, None, False),
            ("detail", "detail", str, False, None, False),
        ])
        return js


@dataclass
class TestReportSetupAction(BackboneElement):
    """ A setup operation or assert that was executed.

    Action would contain either an operation or an assertion.
    """
    resource_type: ClassVar[str] = "TestReportSetupAction"
    operation: Optional[TestReportSetupActionOperation] = None
    assert_fhir: Optional[TestReportSetupActionAssert] = None

    def elementProperties(self):
        js = super(TestReportSetupAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestReportSetupActionOperation, False, None, False),
            ("assert_fhir", "assert", TestReportSetupActionAssert, False, None, False),
        ])
        return js


@dataclass
class TestReportParticipant(BackboneElement):
    """ A participant in the test execution, either the execution engine, a client,
    or a server.
    """
    resource_type: ClassVar[str] = "TestReportParticipant"
    type: str = None
    uri: str = None
    display: Optional[str] = None

    def elementProperties(self):
        js = super(TestReportParticipant, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("uri", "uri", str, False, None, True),
            ("display", "display", str, False, None, False),
        ])
        return js


@dataclass
class TestReportSetup(BackboneElement):
    """ The results of the series of required setup operations before the tests
    were executed.
    """
    resource_type: ClassVar[str] = "TestReportSetup"
    action: List[TestReportSetupAction] = empty_list()

    def elementProperties(self):
        js = super(TestReportSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestReportSetupAction, True, None, True),
        ])
        return js


@dataclass
class TestReportTest(BackboneElement):
    """ A test executed from the test script.
    """
    resource_type: ClassVar[str] = "TestReportTest"
    name: Optional[str] = None
    description: Optional[str] = None
    action: List[TestReportTestAction] = empty_list()

    def elementProperties(self):
        js = super(TestReportTest, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("action", "action", TestReportTestAction, True, None, True),
        ])
        return js


@dataclass
class TestReportTeardown(BackboneElement):
    """ The results of running the series of required clean up steps.

    The results of the series of operations required to clean up after all the
    tests were executed (successfully or otherwise).
    """
    resource_type: ClassVar[str] = "TestReportTeardown"
    action: List[TestReportTeardownAction] = empty_list()

    def elementProperties(self):
        js = super(TestReportTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestReportTeardownAction, True, None, True),
        ])
        return js


@dataclass
class TestReport(DomainResource):
    """ Describes the results of a TestScript execution.

    A summary of information based on the results of executing a TestScript.
    """
    resource_type: ClassVar[str] = "TestReport"
    identifier: Optional[Identifier] = None
    name: Optional[str] = None
    status: str = None
    testScript: FHIRReference = None
    result: str = None
    score: Optional[float] = None
    tester: Optional[str] = None
    issued: Optional[FHIRDate] = None
    participant: Optional[List[TestReportParticipant]] = empty_list()
    setup: Optional[TestReportSetup] = None
    test: Optional[List[TestReportTest]] = empty_list()
    teardown: Optional[TestReportTeardown] = None

    def elementProperties(self):
        js = super(TestReport, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("name", "name", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("testScript", "testScript", FHIRReference, False, None, True),
            ("result", "result", str, False, None, True),
            ("score", "score", float, False, None, False),
            ("tester", "tester", str, False, None, False),
            ("issued", "issued", FHIRDate, False, None, False),
            ("participant", "participant", TestReportParticipant, True, None, False),
            ("setup", "setup", TestReportSetup, False, None, False),
            ("test", "test", TestReportTest, True, None, False),
            ("teardown", "teardown", TestReportTeardown, False, None, False),
        ])
        return js