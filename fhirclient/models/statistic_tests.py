#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 on 2019-08-06.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import statistic
from .fhirdate import FHIRDate


class StatisticTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Statistic", js["resourceType"])
        return statistic.Statistic(js)
    
    def testStatistic1(self):
        inst = self.instantiate_from("statistic-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Statistic instance")
        self.implStatistic1(inst)
        
        js = inst.as_json()
        self.assertEqual("Statistic", js["resourceType"])
        inst2 = statistic.Statistic(js)
        self.implStatistic1(inst2)
    
    def implStatistic1(self, inst):
        self.assertEqual(inst.certainty[0].certaintySubcomponent[0].rating[0].coding[0].code, "no-concern")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[0].rating[0].coding[0].display, "no serious concern")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[0].type[0].coding[0].code, "RiskOfBias")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[0].type[0].coding[0].display, "Risk of bias")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[1].note[0].text, "No explanation was provided")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[1].rating[0].coding[0].code, "serious-concern")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[1].rating[0].coding[0].display, "serious concern")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[1].type[0].coding[0].code, "Inconsistency")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[1].type[0].coding[0].display, "Inconsistency")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[2].rating[0].coding[0].code, "no-concern")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[2].rating[0].coding[0].display, "no serious concern")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[2].type[0].coding[0].code, "Indirectness")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[2].type[0].coding[0].display, "Indirectness")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[3].rating[0].coding[0].code, "no-concern")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[3].rating[0].coding[0].display, "no serious concern")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[3].type[0].coding[0].code, "Imprecision")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[3].type[0].coding[0].display, "Imprecision")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[4].rating[0].coding[0].code, "no-concern")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[4].rating[0].coding[0].display, "no serious concern")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[4].type[0].coding[0].code, "PublicationBias")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[4].type[0].coding[0].display, "Publication bias")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[5].rating[0].coding[0].code, "absent")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[5].rating[0].coding[0].display, "absent")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[5].type[0].coding[0].code, "DoseResponseGradient")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[5].type[0].coding[0].display, "Dose response gradient")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[6].rating[0].coding[0].code, "absent")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[6].rating[0].coding[0].display, "absent")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[6].type[0].coding[0].code, "PlausibleConfounding")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[6].type[0].coding[0].display, "Plausible confounding")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[7].rating[0].coding[0].code, "absent")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[7].rating[0].coding[0].display, "absent")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[7].type[0].coding[0].code, "LargeEffect")
        self.assertEqual(inst.certainty[0].certaintySubcomponent[7].type[0].coding[0].display, "Large effect")
        self.assertEqual(inst.certainty[0].rating[0].coding[0].code, "3")
        self.assertEqual(inst.certainty[0].rating[0].coding[0].display, "Moderate")
        self.assertEqual(inst.contributor[0].contact[0].name, "Jan L. Brozek")
        self.assertEqual(inst.contributor[0].name, "Jan L. Brozek")
        self.assertEqual(inst.contributor[0].type, "author")
        self.assertEqual(inst.date.date, FHIRDate("2017-01-05T17:18:19+01:00").date)
        self.assertEqual(inst.date.as_json(), "2017-01-05T17:18:19+01:00")
        self.assertEqual(inst.id, "Statistic-example-1")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2019-04-23T14:47:57.773+00:00").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2019-04-23T14:47:57.773+00:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.meta.versionId, "1")
        self.assertEqual(inst.pValue[0].quantity.comparator, "<")
        self.assertEqual(inst.pValue[0].quantity.value, 0.05)
        self.assertEqual(inst.precisionEstimate[0].from_fhir, -0.46)
        self.assertEqual(inst.precisionEstimate[0].level, 0.95)
        self.assertEqual(inst.precisionEstimate[0].to, -0.26)
        self.assertEqual(inst.precisionEstimate[0].type.coding[0].code, "CI")
        self.assertEqual(inst.precisionEstimate[0].type.coding[0].display, "confidence interval")
        self.assertEqual(inst.precisionEstimate[0].type.coding[0].system, "http://build.fhir.org/valueset-precision-estimate-type.html")
        self.assertEqual(inst.quantity.code, "score")
        self.assertEqual(inst.quantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.quantity.unit, "points")
        self.assertEqual(inst.quantity.value, -0.36)
        self.assertEqual(inst.sampleSize.numberOfParticipants, 1658)
        self.assertEqual(inst.sampleSize.numberOfStudies, 6)
        self.assertEqual(inst.statisticPublisher[0].name, "Cochrane")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.studyType.coding[0].code, "RCT")
        self.assertEqual(inst.synthesisType.coding[0].code, "std-MA")
        self.assertEqual(inst.text.status, "generated")

