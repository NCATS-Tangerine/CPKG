#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/MedicationUsage) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .dosage import Dosage
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class MedicationUsage(DomainResource):
    """ Record of medication being taken by a patient.

    A record of a medication that is being consumed by a patient.   A
    MedicationUsage may indicate that the patient may be taking the medication
    now or has taken the medication in the past or will be taking the
    medication in the future.  The source of this information can be the
    patient, significant other (such as a family member or spouse), or a
    clinician.  A common scenario where this information is captured is during
    the history taking process during a patient visit or stay.   The medication
    information may come from sources such as the patient's memory, from a
    prescription bottle,  or from a list of medications the patient, clinician
    or other party maintains.
    
    The primary difference between a medicationusage and a
    medicationadministration is that the medication administration has complete
    administration information and is based on actual administration
    information from the person who administered the medication.  A
    medicationusage is often, if not always, less specific.  There is no
    required date/time when the medication was administered, in fact we only
    know that a source has reported the patient is taking this medication,
    where details such as time, quantity, or rate or even medication product
    may be incomplete or missing or less precise.  As stated earlier, the
    Medication Usage information may come from the patient's memory, from a
    prescription bottle or from a list of medications the patient, clinician or
    other party maintains.  Medication administration is more formal and is not
    missing detailed information.
    """
    resource_type: ClassVar[str] = "MedicationUsage"
    identifier: Optional[List[Identifier]] = empty_list()
    basedOn: Optional[List[FHIRReference]] = empty_list()
    partOf: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    statusReason: Optional[List[CodeableConcept]] = empty_list()
    category: Optional[List[CodeableConcept]] = empty_list()
    medicationCodeableConcept: CodeableConcept = None
    medicationReference: FHIRReference = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    effectiveDateTime: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    dateAsserted: Optional[FHIRDate] = None
    informationSource: Optional[FHIRReference] = None
    derivedFrom: Optional[List[FHIRReference]] = empty_list()
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    dosage: Optional[List[Dosage]] = empty_list()
    takenAsOrdered: Optional[bool] = None

    def elementProperties(self):
        js = super(MedicationUsage, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", CodeableConcept, True, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", FHIRReference, False, "medication", True),
            ("subject", "subject", FHIRReference, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", Period, False, "effective", False),
            ("dateAsserted", "dateAsserted", FHIRDate, False, None, False),
            ("informationSource", "informationSource", FHIRReference, False, None, False),
            ("derivedFrom", "derivedFrom", FHIRReference, True, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("dosage", "dosage", Dosage, True, None, False),
            ("takenAsOrdered", "takenAsOrdered", bool, False, None, False),
        ])
        return js