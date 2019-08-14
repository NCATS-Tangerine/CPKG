#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 on 2019-08-06.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import regulatedadministrableproduct
from .fhirdate import FHIRDate


class RegulatedAdministrableProductTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("RegulatedAdministrableProduct", js["resourceType"])
        return regulatedadministrableproduct.RegulatedAdministrableProduct(js)
    
    def testRegulatedAdministrableProduct1(self):
        inst = self.instantiate_from("administrableproductdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a RegulatedAdministrableProduct instance")
        self.implRegulatedAdministrableProduct1(inst)
        
        js = inst.as_json()
        self.assertEqual("RegulatedAdministrableProduct", js["resourceType"])
        inst2 = regulatedadministrableproduct.RegulatedAdministrableProduct(js)
        self.implRegulatedAdministrableProduct1(inst2)
    
    def implRegulatedAdministrableProduct1(self, inst):
        self.assertEqual(inst.administrableDoseForm.coding[0].code, "Film-coatedtablet")
        self.assertEqual(inst.administrableDoseForm.coding[0].system, "http://ema.europa.eu/example/administrabledoseform")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://ema.europa.eu/example/phpididentifiersets")
        self.assertEqual(inst.identifier[0].value, "{PhPID}")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.routeOfAdministration[0].code.coding[0].code, "OralUse")
        self.assertEqual(inst.routeOfAdministration[0].code.coding[0].system, "http://ema.europa.eu/example/routeofadministration")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.unitOfPresentation.coding[0].code, "Tablet")
        self.assertEqual(inst.unitOfPresentation.coding[0].system, "http://ema.europa.eu/example/unitofpresentation")
    
    def testRegulatedAdministrableProduct2(self):
        inst = self.instantiate_from("regulatedadministrableproduct-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a RegulatedAdministrableProduct instance")
        self.implRegulatedAdministrableProduct2(inst)
        
        js = inst.as_json()
        self.assertEqual("RegulatedAdministrableProduct", js["resourceType"])
        inst2 = regulatedadministrableproduct.RegulatedAdministrableProduct(js)
        self.implRegulatedAdministrableProduct2(inst2)
    
    def implRegulatedAdministrableProduct2(self, inst):
        self.assertEqual(inst.administrableDoseForm.coding[0].code, "Film-coatedtablet")
        self.assertEqual(inst.administrableDoseForm.coding[0].system, "http://ema.europa.eu/example/administrabledoseform")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://ema.europa.eu/example/phpididentifiersets")
        self.assertEqual(inst.identifier[0].value, "{PhPID}")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.routeOfAdministration[0].code.coding[0].code, "OralUse")
        self.assertEqual(inst.routeOfAdministration[0].code.coding[0].system, "http://ema.europa.eu/example/routeofadministration")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.unitOfPresentation.coding[0].code, "Tablet")
        self.assertEqual(inst.unitOfPresentation.coding[0].system, "http://ema.europa.eu/example/unitofpresentation")

