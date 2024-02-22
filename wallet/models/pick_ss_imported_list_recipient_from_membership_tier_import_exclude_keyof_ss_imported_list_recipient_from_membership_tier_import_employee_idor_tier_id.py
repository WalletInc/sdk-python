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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PickSSImportedListRecipientFromMembershipTierImportExcludeKeyofSSImportedListRecipientFromMembershipTierImportEmployeeIDOrTierID(BaseModel):
    """
    From T, pick a set of properties whose keys are in the union K
    """ # noqa: E501
    list_name: StrictStr = Field(alias="listName")
    phone_number_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="phoneNumberID")
    __properties: ClassVar[List[str]] = ["listName", "phoneNumberID"]

    @field_validator('phone_number_id')
    def phone_number_id_validate_regular_expression(cls, value):
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
        """Create an instance of PickSSImportedListRecipientFromMembershipTierImportExcludeKeyofSSImportedListRecipientFromMembershipTierImportEmployeeIDOrTierID from a JSON string"""
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
        """Create an instance of PickSSImportedListRecipientFromMembershipTierImportExcludeKeyofSSImportedListRecipientFromMembershipTierImportEmployeeIDOrTierID from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "listName": obj.get("listName"),
            "phoneNumberID": obj.get("phoneNumberID")
        })
        return _obj


