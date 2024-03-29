#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 on 2019-08-06.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import medicinalproductdefinition
from .fhirdate import FHIRDate


class MedicinalProductDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductDefinition", js["resourceType"])
        return medicinalproductdefinition.MedicinalProductDefinition(js)
    
    def testMedicinalProductDefinition1(self):
        inst = self.instantiate_from("medicinalproductdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductDefinition instance")
        self.implMedicinalProductDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductDefinition", js["resourceType"])
        inst2 = medicinalproductdefinition.MedicinalProductDefinition(js)
        self.implMedicinalProductDefinition1(inst2)
    
    def implMedicinalProductDefinition1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://ema.europa.eu/example/MPID")
        self.assertEqual(inst.identifier[0].value, "{mpid}")
        self.assertEqual(inst.manufacturingBusinessOperation[0].authorisationReferenceNumber.system, "http://ema.europa.eu/example/manufacturingAuthorisationReferenceNumber")
        self.assertEqual(inst.manufacturingBusinessOperation[0].authorisationReferenceNumber.value, "1324TZ")
        self.assertEqual(inst.manufacturingBusinessOperation[0].effectiveDate.date, FHIRDate("2013-03-15").date)
        self.assertEqual(inst.manufacturingBusinessOperation[0].effectiveDate.as_json(), "2013-03-15")
        self.assertEqual(inst.manufacturingBusinessOperation[0].operationType.coding[0].code, "Batchrelease")
        self.assertEqual(inst.manufacturingBusinessOperation[0].operationType.coding[0].system, "http://ema.europa.eu/example/manufacturingOperationType")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].countryLanguage[0].country.coding[0].code, "EU")
        self.assertEqual(inst.name[0].countryLanguage[0].country.coding[0].system, "http://ema.europa.eu/example/countryCode")
        self.assertEqual(inst.name[0].countryLanguage[0].jurisdiction.coding[0].code, "EU")
        self.assertEqual(inst.name[0].countryLanguage[0].jurisdiction.coding[0].system, "http://ema.europa.eu/example/jurisdictionCode")
        self.assertEqual(inst.name[0].countryLanguage[0].language.coding[0].code, "EN")
        self.assertEqual(inst.name[0].countryLanguage[0].language.coding[0].system, "http://ema.europa.eu/example/languageCode")
        self.assertEqual(inst.name[0].namePart[0].part, "Equilidem")
        self.assertEqual(inst.name[0].namePart[0].type.code, "INV")
        self.assertEqual(inst.name[0].namePart[1].part, "2.5 mg")
        self.assertEqual(inst.name[0].namePart[1].type.code, "STR")
        self.assertEqual(inst.name[0].namePart[2].part, "film-coated tablets")
        self.assertEqual(inst.name[0].namePart[2].type.code, "FRM")
        self.assertEqual(inst.name[0].productName, "Equilidem 2.5 mg film-coated tablets")
        self.assertEqual(inst.productClassification[0].coding[0].code, "WHOAnatomicalTherapeuticChemicalATCClassificationSystem|B01AF02")
        self.assertEqual(inst.productClassification[0].coding[0].system, "http://ema.europa.eu/example/WHOAnatomicalTherapeuticChemicalATCClassificationSystem")
        self.assertEqual(inst.text.status, "generated")

