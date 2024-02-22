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
from wallet.models.pick_vs_campaign_update_params_exclude_keyof_vs_campaign_update_params_start_date_or_expiration_date_value_type import PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType
from wallet.models.wt_wallet_page_view_id import WTWalletPageViewId
from typing import Optional, Set
from typing_extensions import Self

class AdvertisementCredit(BaseModel):
    """
    AdvertisementCredit
    """ # noqa: E501
    title: Annotated[str, Field(min_length=1, strict=True)]
    value_type: PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType = Field(alias="valueType")
    payment_design_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="paymentDesignID")
    max_uses: Annotated[int, Field(strict=True, ge=0)] = Field(alias="maxUses")
    discount_value: Annotated[int, Field(strict=True, ge=0)] = Field(alias="discountValue")
    employee_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="employeeID")
    id: WTWalletPageViewId
    merchant_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="merchantID")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    is_active: StrictBool = Field(alias="isActive")
    discount_value_decimal: StrictStr = Field(alias="discountValue_decimal")
    discount_value_string: StrictStr = Field(alias="discountValue_string")
    __properties: ClassVar[List[str]] = ["title", "valueType", "paymentDesignID", "maxUses", "discountValue", "employeeID", "id", "merchantID", "createdAt", "updatedAt", "isActive", "discountValue_decimal", "discountValue_string"]

    @field_validator('payment_design_id')
    def payment_design_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]+$/")
        return value

    @field_validator('employee_id')
    def employee_id_validate_regular_expression(cls, value):
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
        """Create an instance of AdvertisementCredit from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of value_type
        if self.value_type:
            _dict['valueType'] = self.value_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdvertisementCredit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "valueType": PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType.from_dict(obj["valueType"]) if obj.get("valueType") is not None else None,
            "paymentDesignID": obj.get("paymentDesignID"),
            "maxUses": obj.get("maxUses"),
            "discountValue": obj.get("discountValue"),
            "employeeID": obj.get("employeeID"),
            "id": WTWalletPageViewId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "merchantID": obj.get("merchantID"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "isActive": obj.get("isActive"),
            "discountValue_decimal": obj.get("discountValue_decimal"),
            "discountValue_string": obj.get("discountValue_string")
        })
        return _obj


