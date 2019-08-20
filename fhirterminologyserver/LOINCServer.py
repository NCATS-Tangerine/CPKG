from typing import Optional

from fhirclient.models.coding import Coding
from fhirterminologyserver.FHIRTerminologyServer import FHIRServer


def LOINCServer(**kwargs) -> Optional[FHIRServer]:
    return FHIRServer(url='https://fhir.loinc.org/', **kwargs)


def prefname(code: Coding, server: FHIRServer) -> str:
    """ Return the preferred name for the concept in Coding """
    rval = getattr(code, 'display', None)
    if not rval:
        concept = server.CodeSystem.lookup(system=code.system, code=code.code)
        if concept:
            for p in concept.parameter:
                if p.name == 'display':
                    rval = p.valueString
                    break
    if not rval:
        rval = f"System: {code.system} Code: {code.code} not found"
    return rval
