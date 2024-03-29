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

from datetime import datetime
from pydantic import BaseModel, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from wallet.models.wt_membership_tier_id import WTMembershipTierId
from typing import Optional, Set
from typing_extensions import Self

class WTMembershipTier(BaseModel):
    """
    WTMembershipTier
    """ # noqa: E501
    tier_number: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The tier number as defined by the merchant", alias="tierNumber")
    tier_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The tier name as defined by the merchant", alias="tierName")
    tier_discount: Union[Annotated[float, Field(le=100, strict=True, ge=0)], Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(description="The provided discount as percentage", alias="tierDiscount")
    tier_design_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="tierDesignID")
    points_design_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="pointsDesignID")
    id: WTMembershipTierId
    merchant_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="merchantID")
    created_at: datetime = Field(description="The timestamp of when this resource was created", alias="createdAt")
    updated_at: datetime = Field(description="The timestamp of when this resource was updated", alias="updatedAt")
    is_active: StrictBool = Field(description="Denotes if this resource is active", alias="isActive")
    __properties: ClassVar[List[str]] = ["tierNumber", "tierName", "tierDiscount", "tierDesignID", "pointsDesignID", "id", "merchantID", "createdAt", "updatedAt", "isActive"]

    @field_validator('tier_design_id')
    def tier_design_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]+$/")
        return value

    @field_validator('points_design_id')
    def points_design_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]+$/")
        return value

    @field_validator('merchant_id')
    def merchant_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]+$/")
        return value

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
        """Create an instance of WTMembershipTier from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WTMembershipTier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tierNumber": obj.get("tierNumber"),
            "tierName": obj.get("tierName"),
            "tierDiscount": obj.get("tierDiscount"),
            "tierDesignID": obj.get("tierDesignID"),
            "pointsDesignID": obj.get("pointsDesignID"),
            "id": WTMembershipTierId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "merchantID": obj.get("merchantID"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "isActive": obj.get("isActive")
        })
        return _obj


