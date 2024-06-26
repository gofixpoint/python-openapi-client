# coding: utf-8

"""
    fixpoint/v1/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AppLogLevelType(str, Enum):
    """
    AppLogLevelType
    """

    """
    allowed enum values
    """
    TRACE = 'TRACE'
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'
    FATAL = 'FATAL'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AppLogLevelType from a JSON string"""
        return cls(json.loads(json_str))


