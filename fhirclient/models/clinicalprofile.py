#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ClinicalProfile) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class ClinicalProfileMedicationDosage(BackboneElement):
    """ Details of how medication was taken.
    """
    resource_type: ClassVar[str] = "ClinicalProfileMedicationDosage"
    text: Optional[str] = None
    site: Optional[List[CodeableConcept]] = empty_list()
    route: Optional[List[CodeableConcept]] = empty_list()
    method: Optional[List[CodeableConcept]] = empty_list()
    dose: Optional[List[Quantity]] = empty_list()
    rateRatio: Optional[Ratio] = None
    rateQuantity: Optional[Quantity] = None

    def elementProperties(self):
        js = super(ClinicalProfileMedicationDosage, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("site", "site", CodeableConcept, True, None, False),
            ("route", "route", CodeableConcept, True, None, False),
            ("method", "method", CodeableConcept, True, None, False),
            ("dose", "dose", Quantity, True, None, False),
            ("rateRatio", "rateRatio", Ratio, False, "rate", False),
            ("rateQuantity", "rateQuantity", Quantity, False, "rate", False),
        ])
        return js


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry(BackboneElement):
    """ Correlation entry.

    List of correlated phenotypes in descending order of the absolute value of
    the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry"
    code: CodeableConcept = None
    coefficient: float = None

    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("coefficient", "coefficient", float, False, None, True),
        ])
        return js


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry(BackboneElement):
    """ Correlation entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry"
    code: List[CodeableConcept] = empty_list()
    coefficient: float = None

    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, True, None, True),
            ("coefficient", "coefficient", float, False, None, True),
        ])
        return js


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntryMeds(BackboneElement):
    """ Medication code(s).
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntryMeds"
    medicationCodeableConcept: CodeableConcept = None
    medicationReference: FHIRReference = None

    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntryMeds, self).elementProperties()
        js.extend([
            ("medicationCodeableConcept", "medicationCodeableConcept", CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", FHIRReference, False, "medication", True),
        ])
        return js


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry(BackboneElement):
    """ Correlation entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry"
    meds: List[ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntryMeds] = empty_list()
    coefficient: float = None

    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry, self).elementProperties()
        js.extend([
            ("meds", "meds", ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntryMeds, True, None, True),
            ("coefficient", "coefficient", float, False, None, True),
        ])
        return js


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry(BackboneElement):
    """ Correlation entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry"
    code: CodeableConcept = None
    coefficient: float = None

    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("coefficient", "coefficient", float, False, None, True),
        ])
        return js


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedLabsEntry(BackboneElement):
    """ Correlated lab.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedLabsEntry"
    labcode: List[CodeableConcept] = empty_list()
    coefficient: float = None

    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedLabsEntry, self).elementProperties()
        js.extend([
            ("labcode", "labcode", CodeableConcept, True, None, True),
            ("coefficient", "coefficient", float, False, None, True),
        ])
        return js


@dataclass
class ClinicalProfileLabScalarDistributionDecile(BackboneElement):
    """ Decile partitions.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionDecile"
    nth: int = None
    value: float = None

    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionDecile, self).elementProperties()
        js.extend([
            ("nth", "nth", int, False, None, True),
            ("value", "value", float, False, None, True),
        ])
        return js


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedLabs(BackboneElement):
    """ Correlated laboratory tests.

    An ordered list of the laboratory tests  that are most closely correlated.
    This list can be limited by the top "n" labs and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedLabs"
    topn: Optional[int] = None
    abscorrelation: Optional[float] = None
    entry: Optional[List[ClinicalProfileLabScalarDistributionCorrelatedLabsEntry]] = empty_list()

    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedLabs, self).elementProperties()
        js.extend([
            ("topn", "topn", int, False, None, False),
            ("abscorrelation", "abscorrelation", float, False, None, False),
            ("entry", "entry", ClinicalProfileLabScalarDistributionCorrelatedLabsEntry, True, None, False),
        ])
        return js


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedDiagnoses(BackboneElement):
    """ Correlated diagnosies.

    An ordered list of  the diagnoses  that are most closely correlated.  This
    list can be limited by the top "n" diagnoses and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedDiagnoses"
    topn: Optional[int] = None
    abscorrelation: Optional[float] = None
    entry: Optional[List[ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry]] = empty_list()

    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedDiagnoses, self).elementProperties()
        js.extend([
            ("topn", "topn", int, False, None, False),
            ("abscorrelation", "abscorrelation", float, False, None, False),
            ("entry", "entry", ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry, True, None, False),
        ])
        return js


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedMedications(BackboneElement):
    """ Correlated medications.

    An ordered list of  the medications  that are most closely correlated.
    This list can be limited by the top "n" medications and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedMedications"
    topn: Optional[int] = None
    abscorrelation: Optional[float] = None
    entry: Optional[List[ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry]] = empty_list()

    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedMedications, self).elementProperties()
        js.extend([
            ("topn", "topn", int, False, None, False),
            ("abscorrelation", "abscorrelation", float, False, None, False),
            ("entry", "entry", ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry, True, None, False),
        ])
        return js


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedProcedures(BackboneElement):
    """ Correlated procedures.

    An ordered list of  the procedures  that are most closely correlated.  This
    list can be limited by the top "n" procedures and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedProcedures"
    topn: Optional[int] = None
    abscorrelation: Optional[float] = None
    entry: Optional[List[ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry]] = empty_list()

    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedProcedures, self).elementProperties()
        js.extend([
            ("topn", "topn", int, False, None, False),
            ("abscorrelation", "abscorrelation", float, False, None, False),
            ("entry", "entry", ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry, True, None, False),
        ])
        return js


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedPhenotypes(BackboneElement):
    """ Correlated phenotypes.

    An ordered list of  the phenotypes  that are most closely correlated.  This
    list can be limited by the top "n" phenotypes and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedPhenotypes"
    topn: Optional[int] = None
    abscorrelation: Optional[float] = None
    entry: Optional[List[ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry]] = empty_list()

    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedPhenotypes, self).elementProperties()
        js.extend([
            ("topn", "topn", int, False, None, False),
            ("abscorrelation", "abscorrelation", float, False, None, False),
            ("entry", "entry", ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry, True, None, False),
        ])
        return js


@dataclass
class ClinicalProfileLabScalarDistribution(BackboneElement):
    """ Scalar sample summary.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistribution"
    units: Quantity = None
    min: float = None
    max: float = None
    mean: float = None
    median: float = None
    stdDev: float = None
    decile: Optional[List[ClinicalProfileLabScalarDistributionDecile]] = empty_list()
    normalizedHigh: Optional[float] = None
    normalizedLow: Optional[float] = None
    fractionAboveNormal: Optional[float] = None
    fractionBelowNormal: Optional[float] = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None

    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistribution, self).elementProperties()
        js.extend([
            ("units", "units", Quantity, False, None, True),
            ("min", "min", float, False, None, True),
            ("max", "max", float, False, None, True),
            ("mean", "mean", float, False, None, True),
            ("median", "median", float, False, None, True),
            ("stdDev", "stdDev", float, False, None, True),
            ("decile", "decile", ClinicalProfileLabScalarDistributionDecile, True, None, False),
            ("normalizedHigh", "normalizedHigh", float, False, None, False),
            ("normalizedLow", "normalizedLow", float, False, None, False),
            ("fractionAboveNormal", "fractionAboveNormal", float, False, None, False),
            ("fractionBelowNormal", "fractionBelowNormal", float, False, None, False),
            ("correlatedLabs", "correlatedLabs", ClinicalProfileLabScalarDistributionCorrelatedLabs, False, None, False),
            ("correlatedDiagnoses", "correlatedDiagnoses", ClinicalProfileLabScalarDistributionCorrelatedDiagnoses, False, None, False),
            ("correlatedMedications", "correlatedMedications", ClinicalProfileLabScalarDistributionCorrelatedMedications, False, None, False),
            ("correlatedProcedures", "correlatedProcedures", ClinicalProfileLabScalarDistributionCorrelatedProcedures, False, None, False),
            ("correlatedPhenotypes", "correlatedPhenotypes", ClinicalProfileLabScalarDistributionCorrelatedPhenotypes, False, None, False),
        ])
        return js


@dataclass
class ClinicalProfileLab(BackboneElement):
    """ Laboratory profile entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLab"
    code: List[CodeableConcept] = empty_list()
    count: int = None
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: Optional[float] = None
    scalarDistribution: Optional[ClinicalProfileLabScalarDistribution] = None

    def elementProperties(self):
        js = super(ClinicalProfileLab, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, True, None, True),
            ("count", "count", int, False, None, True),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, False),
            ("scalarDistribution", "scalarDistribution", ClinicalProfileLabScalarDistribution, False, None, False),
        ])
        return js


@dataclass
class ClinicalProfileMedication(BackboneElement):
    """ Medication profile entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileMedication"
    category: Optional[CodeableConcept] = None
    medicationCodeableConcept: CodeableConcept = None
    medicationReference: FHIRReference = None
    dosage: Optional[ClinicalProfileMedicationDosage] = None
    treatementDuration: Optional[float] = None
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: float = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None

    def elementProperties(self):
        js = super(ClinicalProfileMedication, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", FHIRReference, False, "medication", True),
            ("dosage", "dosage", ClinicalProfileMedicationDosage, False, None, False),
            ("treatementDuration", "treatementDuration", float, False, None, False),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, True),
            ("correlatedLabs", "correlatedLabs", ClinicalProfileLabScalarDistributionCorrelatedLabs, False, None, False),
            ("correlatedDiagnoses", "correlatedDiagnoses", ClinicalProfileLabScalarDistributionCorrelatedDiagnoses, False, None, False),
            ("correlatedMedications", "correlatedMedications", ClinicalProfileLabScalarDistributionCorrelatedMedications, False, None, False),
            ("correlatedProcedures", "correlatedProcedures", ClinicalProfileLabScalarDistributionCorrelatedProcedures, False, None, False),
            ("correlatedPhenotypes", "correlatedPhenotypes", ClinicalProfileLabScalarDistributionCorrelatedPhenotypes, False, None, False),
        ])
        return js


@dataclass
class ClinicalProfileDiagnosis(BackboneElement):
    """ Diagnosis profile entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileDiagnosis"
    code: List[CodeableConcept] = empty_list()
    count: int = None
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: float = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None

    def elementProperties(self):
        js = super(ClinicalProfileDiagnosis, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, True, None, True),
            ("count", "count", int, False, None, True),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, True),
            ("correlatedLabs", "correlatedLabs", ClinicalProfileLabScalarDistributionCorrelatedLabs, False, None, False),
            ("correlatedDiagnoses", "correlatedDiagnoses", ClinicalProfileLabScalarDistributionCorrelatedDiagnoses, False, None, False),
            ("correlatedMedications", "correlatedMedications", ClinicalProfileLabScalarDistributionCorrelatedMedications, False, None, False),
            ("correlatedProcedures", "correlatedProcedures", ClinicalProfileLabScalarDistributionCorrelatedProcedures, False, None, False),
            ("correlatedPhenotypes", "correlatedPhenotypes", ClinicalProfileLabScalarDistributionCorrelatedPhenotypes, False, None, False),
        ])
        return js


@dataclass
class ClinicalProfileProcedure(BackboneElement):
    """ Procedure profile entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileProcedure"
    code: List[CodeableConcept] = empty_list()
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: float = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None

    def elementProperties(self):
        js = super(ClinicalProfileProcedure, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, True, None, True),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, True),
            ("correlatedLabs", "correlatedLabs", ClinicalProfileLabScalarDistributionCorrelatedLabs, False, None, False),
            ("correlatedDiagnoses", "correlatedDiagnoses", ClinicalProfileLabScalarDistributionCorrelatedDiagnoses, False, None, False),
            ("correlatedMedications", "correlatedMedications", ClinicalProfileLabScalarDistributionCorrelatedMedications, False, None, False),
            ("correlatedProcedures", "correlatedProcedures", ClinicalProfileLabScalarDistributionCorrelatedProcedures, False, None, False),
            ("correlatedPhenotypes", "correlatedPhenotypes", ClinicalProfileLabScalarDistributionCorrelatedPhenotypes, False, None, False),
        ])
        return js


@dataclass
class ClinicalProfileHpo(BackboneElement):
    """ HPO Profile Entry.

    Phenotypic description.
    """
    resource_type: ClassVar[str] = "ClinicalProfileHpo"
    code: List[CodeableConcept] = empty_list()
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: float = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None

    def elementProperties(self):
        js = super(ClinicalProfileHpo, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, True, None, True),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, True),
            ("correlatedLabs", "correlatedLabs", ClinicalProfileLabScalarDistributionCorrelatedLabs, False, None, False),
            ("correlatedDiagnoses", "correlatedDiagnoses", ClinicalProfileLabScalarDistributionCorrelatedDiagnoses, False, None, False),
            ("correlatedMedications", "correlatedMedications", ClinicalProfileLabScalarDistributionCorrelatedMedications, False, None, False),
            ("correlatedProcedures", "correlatedProcedures", ClinicalProfileLabScalarDistributionCorrelatedProcedures, False, None, False),
            ("correlatedPhenotypes", "correlatedPhenotypes", ClinicalProfileLabScalarDistributionCorrelatedPhenotypes, False, None, False),
        ])
        return js


@dataclass
class ClinicalProfile(DomainResource):
    """ Results of a measure evaluation.

    Clinical Profiles summarize and demonstrate the features of a population.
    """
    resource_type: ClassVar[str] = "ClinicalProfile"
    identifier: Optional[List[Identifier]] = empty_list()
    status: str = None
    population: FHIRReference = None
    cohort: FHIRReference = None
    date: Optional[FHIRDate] = None
    source: Optional[List[Identifier]] = empty_list()
    reporter: FHIRReference = None
    lab: Optional[List[ClinicalProfileLab]] = empty_list()
    medication: Optional[List[ClinicalProfileMedication]] = empty_list()
    diagnosis: Optional[List[ClinicalProfileDiagnosis]] = empty_list()
    procedure: Optional[List[ClinicalProfileProcedure]] = empty_list()
    hpo: Optional[List[ClinicalProfileHpo]] = empty_list()

    def elementProperties(self):
        js = super(ClinicalProfile, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("population", "population", FHIRReference, False, None, True),
            ("cohort", "cohort", FHIRReference, False, None, True),
            ("date", "date", FHIRDate, False, None, False),
            ("source", "source", Identifier, True, None, False),
            ("reporter", "reporter", FHIRReference, False, None, True),
            ("lab", "lab", ClinicalProfileLab, True, None, False),
            ("medication", "medication", ClinicalProfileMedication, True, None, False),
            ("diagnosis", "diagnosis", ClinicalProfileDiagnosis, True, None, False),
            ("procedure", "procedure", ClinicalProfileProcedure, True, None, False),
            ("hpo", "hpo", ClinicalProfileHpo, True, None, False),
        ])
        return js