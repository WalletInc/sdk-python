# coding: utf-8

"""
    wallet-api

    API

    The version of the OpenAPI document: 2.1.600
    Contact: development@wallet.inc
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class WTPosMachineCreateParams(BaseModel):
    """
    WTPosMachineCreateParams
    """ # noqa: E501
    register_id: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="registerID")
    register_name: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="registerName")
    outlet_name: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="outletName")
    outlet_number: StrictInt = Field(description="Stores the outlet number", alias="outletNumber")
    profit_center: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="profitCenter")
    __properties: ClassVar[List[str]] = ["registerID", "registerName", "outletName", "outletNumber", "profitCenter"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WTPosMachineCreateParams from a JSON string"""
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
        """Create an instance of WTPosMachineCreateParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "registerID": obj.get("registerID"),
            "registerName": obj.get("registerName"),
            "outletName": obj.get("outletName"),
            "outletNumber": obj.get("outletNumber"),
            "profitCenter": obj.get("profitCenter")
        })
        return _obj

