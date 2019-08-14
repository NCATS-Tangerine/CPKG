#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/Subscription) on 2019-08-06.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate


@dataclass
class SubscriptionChannel(BackboneElement):
    """ The channel on which to report matches to the criteria.

    Details where to send notifications when resources are received that meet
    the criteria.
    """
    resource_type: ClassVar[str] = "SubscriptionChannel"
    type: str = None
    endpoint: Optional[str] = None
    payload: Optional[str] = None
    header: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(SubscriptionChannel, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("endpoint", "endpoint", str, False, None, False),
            ("payload", "payload", str, False, None, False),
            ("header", "header", str, True, None, False),
        ])
        return js


@dataclass
class Subscription(DomainResource):
    """ Server push subscription criteria.

    The subscription resource is used to define a push-based subscription from
    a server to another system. Once a subscription is registered with the
    server, the server checks every resource that is created or updated, and if
    the resource matches the given criteria, it sends a message on the defined
    "channel" so that another system can take an appropriate action.
    """
    resource_type: ClassVar[str] = "Subscription"
    status: str = None
    contact: Optional[List[ContactPoint]] = empty_list()
    end: Optional[FHIRDate] = None
    reason: str = None
    criteria: str = None
    error: Optional[str] = None
    channel: SubscriptionChannel = None

    def elementProperties(self):
        js = super(Subscription, self).elementProperties()
        js.extend([
            ("status", "status", str, False, None, True),
            ("contact", "contact", ContactPoint, True, None, False),
            ("end", "end", FHIRDate, False, None, False),
            ("reason", "reason", str, False, None, True),
            ("criteria", "criteria", str, False, None, True),
            ("error", "error", str, False, None, False),
            ("channel", "channel", SubscriptionChannel, False, None, True),
        ])
        return js