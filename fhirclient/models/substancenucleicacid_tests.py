#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 on 2019-08-06.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import substancenucleicacid
from .fhirdate import FHIRDate


class SubstanceNucleicAcidTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SubstanceNucleicAcid", js["resourceType"])
        return substancenucleicacid.SubstanceNucleicAcid(js)
    
    def testSubstanceNucleicAcid1(self):
        inst = self.instantiate_from("substancenucleicacid-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SubstanceNucleicAcid instance")
        self.implSubstanceNucleicAcid1(inst)
        
        js = inst.as_json()
        self.assertEqual("SubstanceNucleicAcid", js["resourceType"])
        inst2 = substancenucleicacid.SubstanceNucleicAcid(js)
        self.implSubstanceNucleicAcid1(inst2)
    
    def implSubstanceNucleicAcid1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p></div>")
        self.assertEqual(inst.text.status, "generated")

