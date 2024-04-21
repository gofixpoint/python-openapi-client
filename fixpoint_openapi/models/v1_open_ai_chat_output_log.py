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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fixpoint_openapi.models.v1_open_ai_chat_output_log_choice import V1OpenAIChatOutputLogChoice
from fixpoint_openapi.models.v1_open_ai_chat_output_log_usage import V1OpenAIChatOutputLogUsage
from fixpoint_openapi.models.v1_tracing import V1Tracing
from typing import Optional, Set
from typing_extensions import Self

class V1OpenAIChatOutputLog(BaseModel):
    """
    V1OpenAIChatOutputLog
    """ # noqa: E501
    name: Optional[StrictStr] = None
    input_name: Optional[StrictStr] = Field(default=None, alias="inputName")
    openai_id: Optional[StrictStr] = Field(default=None, alias="openaiId")
    model_name: Optional[StrictStr] = Field(default=None, alias="modelName")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    tracing: Optional[V1Tracing] = None
    choices: Optional[List[V1OpenAIChatOutputLogChoice]] = None
    usage: Optional[V1OpenAIChatOutputLogUsage] = None
    __properties: ClassVar[List[str]] = ["name", "inputName", "openaiId", "modelName", "createdAt", "tracing", "choices", "usage"]

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
        """Create an instance of V1OpenAIChatOutputLog from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tracing
        if self.tracing:
            _dict['tracing'] = self.tracing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in choices (list)
        _items = []
        if self.choices:
            for _item in self.choices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['choices'] = _items
        # override the default output from pydantic by calling `to_dict()` of usage
        if self.usage:
            _dict['usage'] = self.usage.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1OpenAIChatOutputLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "inputName": obj.get("inputName"),
            "openaiId": obj.get("openaiId"),
            "modelName": obj.get("modelName"),
            "createdAt": obj.get("createdAt"),
            "tracing": V1Tracing.from_dict(obj["tracing"]) if obj.get("tracing") is not None else None,
            "choices": [V1OpenAIChatOutputLogChoice.from_dict(_item) for _item in obj["choices"]] if obj.get("choices") is not None else None,
            "usage": V1OpenAIChatOutputLogUsage.from_dict(obj["usage"]) if obj.get("usage") is not None else None
        })
        return _obj


