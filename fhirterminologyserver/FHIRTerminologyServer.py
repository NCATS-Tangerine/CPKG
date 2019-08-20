#!/usr/bin/env python
# coding: utf-8

# # FHIR Terminology Services

import sys
from typing import Optional, Union, Dict, List
import requests
from jsonasobj import JsonObj, loads, as_json
import getpass


class FHIRServer:
    """ FHIR server wrapper """

    def __init__(self, url: str,
                 user: Optional[str] = None,
                 password: Optional[str] = None,
                 default_format: str = "json",
                 show_urls: bool = False) -> None:
        """
        Initialize the server
        :param url: Server base URL
        :param user: User id if needed
        :param password: User password if needed
        :param default_format: Default format
        :param show_urls: True means show diagnostic URLs
        """

        self.url = url + ('' if url.endswith('/') or url.endswith('#') else '/')
        self.format = default_format
        self._user = user
        self._password = password
        self.metadata = self.get('metadata')
        self.ok = self.metadata is not None
        self.show_urls = show_urls
        self.codesystems = self._eval_codesystems()
        self.codesystemmaps = self._codesystem_maps()

    def _eval_codesystems(self) -> List[str]:
        return ['https://loinc.org', 'http://loinc.org']

    def _codesystem_maps(self) -> Dict[str, str]:
        return {'https://loinc.org': 'http://loinc.org'}

    @staticmethod
    def logon(url: str, show_urls: bool = False) -> Optional["FHIRServer"]:
        """ Prompt for a user and password and return a server """
        server = None
        while server is None:
            user = input(f"User id: ")
            if not user:
                return None
            else:
                password = getpass.getpass(f"Password: ")
            server = FHIRServer(url, user, password, show_urls=show_urls)
        return server

    def __getitem__(self, item: str) -> "FHIRReader":
        """ Convert item to a URI """
        return FHIRReader(item, self)

    def __getattr__(self, item: str) -> Union[object, Optional[JsonObj]]:
        if item.startswith('_'):
            return super().__getattribute__(item)
        else:
            return FHIRReader(item, self)

    def get(self, relurl: Optional[str], params: Optional[Dict[str, str]] = None) -> Optional[JsonObj]:
        url = self.url + relurl
        resp = requests.get(url, params=params, auth=(self._user, self._password) if self._user else None)
        if self.show_urls:
            print(f"GET {resp.url}")
        if resp.ok:
            return loads(resp.text)
        else:
            print(f"{resp.url}: Error: {resp.reason}", file=sys.stderr)
            return None


class FHIRReader:
    def __init__(self, resource: str, server: FHIRServer) -> None:
        """
        FHIR Resource reader
        :param resource: resource type
        :param server: FHIR server
        """
        self._resource = resource
        self._server = server

    def __getitem__(self, item: str) -> Optional[JsonObj]:
        """ Return <resource>[item] """
        return self._server.get(self._resource + ('/' + item if item != '*' else ''))

    def __getattr__(self, item: str) -> Union[object, Optional[JsonObj]]:
        """ Return <resource>.<item> """
        return super().__getattribute__(item) if item.startswith('_') else self.__getitem__(item)

    def lookup(self, **kwargs) -> Optional[JsonObj]:
        params = dict(kwargs)
        if 'system' not in kwargs or kwargs['system'] not in self._server.codesystems:
            return None
        params['system'] = self._server.codesystemmaps.get(kwargs['system'], kwargs['system'])
        return self._server.get(self._resource + '/$lookup', params=params)
