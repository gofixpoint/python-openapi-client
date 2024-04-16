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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from fixpoint_openapi.models.v1_input_message import V1InputMessage
from typing import Optional, Set
from typing_extensions import Self

class V1OpenAIChatInputLog(BaseModel):
    """
    V1OpenAIChatInputLog
    """ # noqa: E501
    name: Optional[StrictStr] = None
    model_name: Optional[StrictStr] = Field(default=None, alias="modelName")
    session_name: Optional[StrictStr] = Field(default=None, alias="sessionName")
    messages: Optional[List[V1InputMessage]] = None
    temperature: Optional[Union[StrictFloat, StrictInt]] = None
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    trace_id: Optional[StrictStr] = Field(default=None, alias="traceId")
    __properties: ClassVar[List[str]] = ["name", "modelName", "sessionName", "messages", "temperature", "createdAt", "traceId"]

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
        """Create an instance of V1OpenAIChatInputLog from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in messages (list)
        _items = []
        if self.messages:
            for _item in self.messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['messages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1OpenAIChatInputLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "modelName": obj.get("modelName"),
            "sessionName": obj.get("sessionName"),
            "messages": [V1InputMessage.from_dict(_item) for _item in obj["messages"]] if obj.get("messages") is not None else None,
            "temperature": obj.get("temperature"),
            "createdAt": obj.get("createdAt"),
            "traceId": obj.get("traceId")
        })
        return _obj


