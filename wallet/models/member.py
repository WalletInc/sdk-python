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
from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Member(BaseModel):
    """
    Member
    """ # noqa: E501
    id: Annotated[str, Field(min_length=12, strict=True, max_length=12)]
    merchant_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="merchantID")
    created_at: datetime = Field(description="The timestamp of when this resource was created", alias="createdAt")
    updated_at: datetime = Field(description="The timestamp of when this resource was updated", alias="updatedAt")
    is_active: StrictBool = Field(description="Denotes if this resource is active", alias="isActive")
    first_name: Optional[StrictStr] = Field(default=None, description="An optional first name of the member", alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, description="An optional last name of the member", alias="lastName")
    membership_tier_id: Annotated[str, Field(min_length=12, strict=True, max_length=12)] = Field(alias="membershipTierID")
    mobile_number: StrictStr = Field(alias="mobileNumber")
    email: StrictStr
    birthday: StrictStr = Field(description="Represents the date of birth of the member. Defaults to 0000-00-00, which represents that the date of birth has not been configured")
    points_accrued: Annotated[int, Field(strict=True, ge=0)] = Field(description="The number of points that the member has accrued", alias="pointsAccrued")
    member_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Member ID as represented by the merchant", alias="memberID")
    membership_tier_redeemable_id: Annotated[str, Field(min_length=12, strict=True, max_length=12)] = Field(alias="membershipTierRedeemableID")
    __properties: ClassVar[List[str]] = ["id", "merchantID", "createdAt", "updatedAt", "isActive", "firstName", "lastName", "membershipTierID", "mobileNumber", "email", "birthday", "pointsAccrued", "memberID", "membershipTierRedeemableID"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
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

    @field_validator('membership_tier_id')
    def membership_tier_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]+$/")
        return value

    @field_validator('member_id')
    def member_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]+$/")
        return value

    @field_validator('membership_tier_redeemable_id')
    def membership_tier_redeemable_id_validate_regular_expression(cls, value):
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
        """Create an instance of Member from a JSON string"""
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
        """Create an instance of Member from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "merchantID": obj.get("merchantID"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "isActive": obj.get("isActive"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "membershipTierID": obj.get("membershipTierID"),
            "mobileNumber": obj.get("mobileNumber"),
            "email": obj.get("email"),
            "birthday": obj.get("birthday"),
            "pointsAccrued": obj.get("pointsAccrued"),
            "memberID": obj.get("memberID"),
            "membershipTierRedeemableID": obj.get("membershipTierRedeemableID")
        })
        return _obj

