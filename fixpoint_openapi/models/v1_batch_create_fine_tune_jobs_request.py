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
from fixpoint_openapi.models.v1_mode import V1Mode
from fixpoint_openapi.models.v1_tuning_configuration import V1TuningConfiguration
from typing import Optional, Set
from typing_extensions import Self

class V1BatchCreateFineTuneJobsRequest(BaseModel):
    """
    V1BatchCreateFineTuneJobsRequest
    """ # noqa: E501
    dataset_id: Optional[StrictStr] = Field(default=None, alias="datasetId")
    tuning_configs: Optional[List[V1TuningConfiguration]] = Field(default=None, alias="tuningConfigs")
    mode: Optional[V1Mode] = None
    __properties: ClassVar[List[str]] = ["datasetId", "tuningConfigs", "mode"]

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
        """Create an instance of V1BatchCreateFineTuneJobsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tuning_configs (list)
        _items = []
        if self.tuning_configs:
            for _item in self.tuning_configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tuningConfigs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1BatchCreateFineTuneJobsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "datasetId": obj.get("datasetId"),
            "tuningConfigs": [V1TuningConfiguration.from_dict(_item) for _item in obj["tuningConfigs"]] if obj.get("tuningConfigs") is not None else None,
            "mode": obj.get("mode")
        })
        return _obj


