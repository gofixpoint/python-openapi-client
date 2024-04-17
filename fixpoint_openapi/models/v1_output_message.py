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
from fixpoint_openapi.models.v1_tool_call import V1ToolCall
from typing import Optional, Set
from typing_extensions import Self

class V1OutputMessage(BaseModel):
    """
    V1OutputMessage
    """ # noqa: E501
    role: StrictStr
    content: Optional[StrictStr] = Field(default=None, description="If the model produced a plain text completion, this will be set. If the model only made tool calls, this will be empty.")
    tool_calls: Optional[List[V1ToolCall]] = Field(default=None, description="Optional tool calls, if the model called any.", alias="toolCalls")
    __properties: ClassVar[List[str]] = ["role", "content", "toolCalls"]

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
        """Create an instance of V1OutputMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tool_calls (list)
        _items = []
        if self.tool_calls:
            for _item in self.tool_calls:
                if _item:
                    _items.append(_item.to_dict())
            _dict['toolCalls'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1OutputMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "role": obj.get("role"),
            "content": obj.get("content"),
            "toolCalls": [V1ToolCall.from_dict(_item) for _item in obj["toolCalls"]] if obj.get("toolCalls") is not None else None
        })
        return _obj


