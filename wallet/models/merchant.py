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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Merchant(BaseModel):
    """
    Merchant
    """ # noqa: E501
    company_name: StrictStr = Field(alias="companyName")
    address1: StrictStr
    address2: StrictStr
    city: StrictStr
    state: StrictStr
    country: StrictStr
    phone_number: StrictStr = Field(alias="phoneNumber")
    zip: StrictStr
    currency_abbreviation: Optional[StrictStr] = Field(default=None, alias="currencyAbbreviation")
    id: Annotated[str, Field(min_length=10, strict=True, max_length=10)]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    industry: StrictStr
    industry_name: StrictStr = Field(alias="industryName")
    info_genesis_property_id: StrictStr = Field(alias="infoGenesisPropertyID")
    is_frozen: StrictBool = Field(alias="isFrozen")
    billing_contact_employee_id: StrictStr = Field(alias="billingContactEmployeeID")
    marketing_contact_employee_id: StrictStr = Field(alias="marketingContactEmployeeID")
    technical_contact_employee_id: StrictStr = Field(alias="technicalContactEmployeeID")
    customer_service_contact_employee_id: StrictStr = Field(alias="customerServiceContactEmployeeID")
    stripe_customer_id: StrictStr = Field(alias="stripeCustomerID")
    is_payment_method_provided: StrictBool = Field(alias="isPaymentMethodProvided")
    plan_nickname: StrictStr = Field(alias="planNickname")
    max_sms_count: Union[StrictFloat, StrictInt] = Field(alias="maxSMSCount")
    is_sms_agreement: Optional[StrictBool] = Field(default=None, alias="isSmsAgreement")
    is_white_labeled: Optional[StrictBool] = Field(default=None, alias="isWhiteLabeled")
    is_featured: Optional[StrictBool] = Field(default=None, alias="isFeatured")
    __properties: ClassVar[List[str]] = ["companyName", "address1", "address2", "city", "state", "country", "phoneNumber", "zip", "currencyAbbreviation", "id", "createdAt", "updatedAt", "industry", "industryName", "infoGenesisPropertyID", "isFrozen", "billingContactEmployeeID", "marketingContactEmployeeID", "technicalContactEmployeeID", "customerServiceContactEmployeeID", "stripeCustomerID", "isPaymentMethodProvided", "planNickname", "maxSMSCount", "isSmsAgreement", "isWhiteLabeled", "isFeatured"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
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
        """Create an instance of Merchant from a JSON string"""
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
        """Create an instance of Merchant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "companyName": obj.get("companyName"),
            "address1": obj.get("address1"),
            "address2": obj.get("address2"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "country": obj.get("country"),
            "phoneNumber": obj.get("phoneNumber"),
            "zip": obj.get("zip"),
            "currencyAbbreviation": obj.get("currencyAbbreviation"),
            "id": obj.get("id"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "industry": obj.get("industry"),
            "industryName": obj.get("industryName"),
            "infoGenesisPropertyID": obj.get("infoGenesisPropertyID"),
            "isFrozen": obj.get("isFrozen"),
            "billingContactEmployeeID": obj.get("billingContactEmployeeID"),
            "marketingContactEmployeeID": obj.get("marketingContactEmployeeID"),
            "technicalContactEmployeeID": obj.get("technicalContactEmployeeID"),
            "customerServiceContactEmployeeID": obj.get("customerServiceContactEmployeeID"),
            "stripeCustomerID": obj.get("stripeCustomerID"),
            "isPaymentMethodProvided": obj.get("isPaymentMethodProvided"),
            "planNickname": obj.get("planNickname"),
            "maxSMSCount": obj.get("maxSMSCount"),
            "isSmsAgreement": obj.get("isSmsAgreement"),
            "isWhiteLabeled": obj.get("isWhiteLabeled"),
            "isFeatured": obj.get("isFeatured")
        })
        return _obj

