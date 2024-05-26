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

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PickMSMemberCreationParamsExcludeKeyofMSMemberCreationParamsMemberIdentifier(BaseModel):
    """
    From T, pick a set of properties whose keys are in the union K
    """ # noqa: E501
    mobile_number: StrictStr = Field(alias="mobileNumber")
    first_name: Optional[StrictStr] = Field(default=None, description="An optional first name of the member", alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, description="An optional last name of the member", alias="lastName")
    membership_tier_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="membershipTierID")
    email: StrictStr
    birthday: StrictStr = Field(description="Represents the date of birth of the member. Defaults to 0000-00-00, which represents that the date of birth has not been configured")
    points_accrued: Annotated[int, Field(strict=True, ge=0)] = Field(description="The number of points that the member has accrued", alias="pointsAccrued")
    __properties: ClassVar[List[str]] = ["mobileNumber", "firstName", "lastName", "membershipTierID", "email", "birthday", "pointsAccrued"]

    @field_validator('membership_tier_id')
    def membership_tier_id_validate_regular_expression(cls, value):
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
        """Create an instance of PickMSMemberCreationParamsExcludeKeyofMSMemberCreationParamsMemberIdentifier from a JSON string"""
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
        """Create an instance of PickMSMemberCreationParamsExcludeKeyofMSMemberCreationParamsMemberIdentifier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mobileNumber": obj.get("mobileNumber"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "membershipTierID": obj.get("membershipTierID"),
            "email": obj.get("email"),
            "birthday": obj.get("birthday"),
            "pointsAccrued": obj.get("pointsAccrued")
        })
        return _obj


