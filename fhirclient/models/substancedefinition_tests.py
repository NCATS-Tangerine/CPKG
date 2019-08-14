#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 on 2019-08-06.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import substancedefinition
from .fhirdate import FHIRDate


class SubstanceDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SubstanceDefinition", js["resourceType"])
        return substancedefinition.SubstanceDefinition(js)
    
    def testSubstanceDefinition1(self):
        inst = self.instantiate_from("substancedefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SubstanceDefinition instance")
        self.implSubstanceDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("SubstanceDefinition", js["resourceType"])
        inst2 = substancedefinition.SubstanceDefinition(js)
        self.implSubstanceDefinition1(inst2)
    
    def implSubstanceDefinition1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p></div>")
        self.assertEqual(inst.text.status, "generated")

