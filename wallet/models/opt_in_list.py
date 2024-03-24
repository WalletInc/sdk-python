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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from wallet.models.wt_wallet_page_view_id import WTWalletPageViewId
from typing import Optional, Set
from typing_extensions import Self

class OptInList(BaseModel):
    """
    OptInList
    """ # noqa: E501
    employee_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="employeeID")
    is_active: StrictBool = Field(alias="isActive")
    list_name: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="listName")
    phone_number_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="phoneNumberID")
    estimated_messages_per_month: Annotated[int, Field(strict=True, ge=0)] = Field(alias="estimatedMessagesPerMonth")
    opt_in_keyword: Annotated[str, Field(min_length=4, strict=True, max_length=30)] = Field(alias="optInKeyword")
    opt_out_keyword: Annotated[str, Field(min_length=4, strict=True, max_length=34)] = Field(alias="optOutKeyword")
    opt_in_confirmed_response: StrictStr = Field(alias="optInConfirmedResponse")
    opt_out_confirmed_response: StrictStr = Field(alias="optOutConfirmedResponse")
    opt_in_confirmed_customer_receives: StrictStr = Field(alias="optInConfirmedCustomerReceives")
    opt_out_confirmed_customer_receives: StrictStr = Field(alias="optOutConfirmedCustomerReceives")
    opt_in_confirmed_media_urls: List[StrictStr] = Field(alias="optInConfirmedMediaURLs")
    opt_out_confirmed_media_urls: List[StrictStr] = Field(alias="optOutConfirmedMediaURLs")
    is_over21_required: StrictBool = Field(alias="isOver21Required")
    id: WTWalletPageViewId
    merchant_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="merchantID")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    __properties: ClassVar[List[str]] = ["employeeID", "isActive", "listName", "phoneNumberID", "estimatedMessagesPerMonth", "optInKeyword", "optOutKeyword", "optInConfirmedResponse", "optOutConfirmedResponse", "optInConfirmedCustomerReceives", "optOutConfirmedCustomerReceives", "optInConfirmedMediaURLs", "optOutConfirmedMediaURLs", "isOver21Required", "id", "merchantID", "createdAt", "updatedAt"]

    @field_validator('employee_id')
    def employee_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]+$/")
        return value

    @field_validator('phone_number_id')
    def phone_number_id_validate_regular_expression(cls, value):
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
        """Create an instance of OptInList from a JSON string"""
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
        """Create an instance of OptInList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "employeeID": obj.get("employeeID"),
            "isActive": obj.get("isActive"),
            "listName": obj.get("listName"),
            "phoneNumberID": obj.get("phoneNumberID"),
            "estimatedMessagesPerMonth": obj.get("estimatedMessagesPerMonth"),
            "optInKeyword": obj.get("optInKeyword"),
            "optOutKeyword": obj.get("optOutKeyword"),
            "optInConfirmedResponse": obj.get("optInConfirmedResponse"),
            "optOutConfirmedResponse": obj.get("optOutConfirmedResponse"),
            "optInConfirmedCustomerReceives": obj.get("optInConfirmedCustomerReceives"),
            "optOutConfirmedCustomerReceives": obj.get("optOutConfirmedCustomerReceives"),
            "optInConfirmedMediaURLs": obj.get("optInConfirmedMediaURLs"),
            "optOutConfirmedMediaURLs": obj.get("optOutConfirmedMediaURLs"),
            "isOver21Required": obj.get("isOver21Required"),
            "id": WTWalletPageViewId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "merchantID": obj.get("merchantID"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj

