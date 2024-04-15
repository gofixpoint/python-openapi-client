# coding: utf-8

"""
    fixpoint/llmproxy/v1/service.proto

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
from openapi_client.models.v1_origin_type import V1OriginType
from openapi_client.models.v1_thumbs_reaction import V1ThumbsReaction
from typing import Optional, Set
from typing_extensions import Self

class V1LikeIngest(BaseModel):
    """
    V1LikeIngest
    """ # noqa: E501
    log_name: Optional[StrictStr] = Field(default=None, alias="logName")
    thumbs_reaction: Optional[V1ThumbsReaction] = Field(default=None, alias="thumbsReaction")
    user_id: Optional[StrictStr] = Field(default=None, alias="userId")
    origin: Optional[V1OriginType] = None
    __properties: ClassVar[List[str]] = ["logName", "thumbsReaction", "userId", "origin"]

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
        """Create an instance of V1LikeIngest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1LikeIngest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "logName": obj.get("logName"),
            "thumbsReaction": obj.get("thumbsReaction"),
            "userId": obj.get("userId"),
            "origin": obj.get("origin")
        })
        return _obj


