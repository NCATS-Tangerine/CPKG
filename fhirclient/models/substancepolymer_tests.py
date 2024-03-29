#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 on 2019-08-06.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import substancepolymer
from .fhirdate import FHIRDate


class SubstancePolymerTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SubstancePolymer", js["resourceType"])
        return substancepolymer.SubstancePolymer(js)
    
    def testSubstancePolymer1(self):
        inst = self.instantiate_from("substancepolymer-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SubstancePolymer instance")
        self.implSubstancePolymer1(inst)
        
        js = inst.as_json()
        self.assertEqual("SubstancePolymer", js["resourceType"])
        inst2 = substancepolymer.SubstancePolymer(js)
        self.implSubstancePolymer1(inst2)
    
    def implSubstancePolymer1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p></div>")
        self.assertEqual(inst.text.status, "generated")

