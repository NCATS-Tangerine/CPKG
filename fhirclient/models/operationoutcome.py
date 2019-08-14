#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/OperationOutcome) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource


@dataclass
class OperationOutcomeIssue(BackboneElement):
    """ A single issue associated with the action.

    An error, warning, or information message that results from a system
    action.
    """
    resource_type: ClassVar[str] = "OperationOutcomeIssue"
    severity: str = None
    code: str = None
    details: Optional[CodeableConcept] = None
    diagnostics: Optional[str] = None
    location: Optional[List[str]] = empty_list()
    expression: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(OperationOutcomeIssue, self).elementProperties()
        js.extend([
            ("severity", "severity", str, False, None, True),
            ("code", "code", str, False, None, True),
            ("details", "details", CodeableConcept, False, None, False),
            ("diagnostics", "diagnostics", str, False, None, False),
            ("location", "location", str, True, None, False),
            ("expression", "expression", str, True, None, False),
        ])
        return js


@dataclass
class OperationOutcome(DomainResource):
    """ Information about the success/failure of an action.

    A collection of error, warning, or information messages that result from a
    system action.
    """
    resource_type: ClassVar[str] = "OperationOutcome"
    issue: List[OperationOutcomeIssue] = empty_list()

    def elementProperties(self):
        js = super(OperationOutcome, self).elementProperties()
        js.extend([
            ("issue", "issue", OperationOutcomeIssue, True, None, True),
        ])
        return js