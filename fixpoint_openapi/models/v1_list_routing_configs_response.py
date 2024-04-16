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
from fixpoint_openapi.models.v1_routing_config import V1RoutingConfig
from typing import Optional, Set
from typing_extensions import Self

class V1ListRoutingConfigsResponse(BaseModel):
    """
    V1ListRoutingConfigsResponse
    """ # noqa: E501
    routing_configs: Optional[List[V1RoutingConfig]] = Field(default=None, alias="routingConfigs")
    next_page_token: Optional[StrictStr] = Field(default=None, alias="nextPageToken")
    __properties: ClassVar[List[str]] = ["routingConfigs", "nextPageToken"]

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
        """Create an instance of V1ListRoutingConfigsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in routing_configs (list)
        _items = []
        if self.routing_configs:
            for _item in self.routing_configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['routingConfigs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1ListRoutingConfigsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "routingConfigs": [V1RoutingConfig.from_dict(_item) for _item in obj["routingConfigs"]] if obj.get("routingConfigs") is not None else None,
            "nextPageToken": obj.get("nextPageToken")
        })
        return _obj


