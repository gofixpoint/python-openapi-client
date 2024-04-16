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


class V1TerminalState(str, Enum):
    """
    - TERMINAL_STATE_ERROR: Error out if a spend cap is met for the last model in the sequence  - TERMINAL_STATE_IGNORE_CAP: Ignore the spend cap on the last model in the sequence
    """

    """
    allowed enum values
    """
    TERMINAL_STATE_UNSPECIFIED = 'TERMINAL_STATE_UNSPECIFIED'
    TERMINAL_STATE_ERROR = 'TERMINAL_STATE_ERROR'
    TERMINAL_STATE_IGNORE_CAP = 'TERMINAL_STATE_IGNORE_CAP'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V1TerminalState from a JSON string"""
        return cls(json.loads(json_str))


