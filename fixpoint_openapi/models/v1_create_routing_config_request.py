# coding: utf-8

"""
    fixpoint/v1/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fixpoint_openapi.models.fixpointv1_model import Fixpointv1Model
from fixpoint_openapi.models.v1_fallback_strategy import V1FallbackStrategy
from fixpoint_openapi.models.v1_terminal_state import V1TerminalState
from typing import Optional, Set
from typing_extensions import Self

class V1CreateRoutingConfigRequest(BaseModel):
    """
    V1CreateRoutingConfigRequest
    """ # noqa: E501
    models: Optional[List[Fixpointv1Model]] = None
    description: Optional[StrictStr] = None
    fallback_strategy: Optional[V1FallbackStrategy] = Field(default=None, alias="fallbackStrategy")
    terminal_state: Optional[V1TerminalState] = Field(default=None, alias="terminalState")
    __properties: ClassVar[List[str]] = ["models", "description", "fallbackStrategy", "terminalState"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V1CreateRoutingConfigRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in models (list)
        _items = []
        if self.models:
            for _item in self.models:
                if _item:
                    _items.append(_item.to_dict())
            _dict['models'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1CreateRoutingConfigRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "models": [Fixpointv1Model.from_dict(_item) for _item in obj["models"]] if obj.get("models") is not None else None,
            "description": obj.get("description"),
            "fallbackStrategy": obj.get("fallbackStrategy"),
            "terminalState": obj.get("terminalState")
        })
        return _obj


