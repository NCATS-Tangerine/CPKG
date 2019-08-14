#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 on 2019-08-06.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import manufactureditemdefinition
from .fhirdate import FHIRDate


class ManufacturedItemDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ManufacturedItemDefinition", js["resourceType"])
        return manufactureditemdefinition.ManufacturedItemDefinition(js)
    
    def testManufacturedItemDefinition1(self):
        inst = self.instantiate_from("manufactureditemdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ManufacturedItemDefinition instance")
        self.implManufacturedItemDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ManufacturedItemDefinition", js["resourceType"])
        inst2 = manufactureditemdefinition.ManufacturedItemDefinition(js)
        self.implManufacturedItemDefinition1(inst2)
    
    def implManufacturedItemDefinition1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.manufacturedDoseForm.coding[0].code, "Film-coatedtablet")
        self.assertEqual(inst.manufacturedDoseForm.coding[0].system, "http://ema.europa.eu/example/manufactureddoseform")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.physicalCharacteristics.color[0], "Pink")
        self.assertEqual(inst.physicalCharacteristics.imprint[0], "894")
        self.assertEqual(inst.physicalCharacteristics.shape, "Oval")
        self.assertEqual(inst.quantity.unit, "1")
        self.assertEqual(inst.quantity.value, 10)
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.unitOfPresentation.coding[0].code, "Tablet")
        self.assertEqual(inst.unitOfPresentation.coding[0].system, "http://ema.europa.eu/example/unitofpresentation")

