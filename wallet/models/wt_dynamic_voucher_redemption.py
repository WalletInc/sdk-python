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
from wallet.models.pick_vs_static_voucher_exclude_keyof_vs_static_voucher_redeemed_at_or_refunded_at_or_last_viewed_at_register_id import PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID
from wallet.models.vs_dynamic_voucher_status import VSDynamicVoucherStatus
from wallet.models.wt_dynamic_voucher_redemption_transaction_type import WTDynamicVoucherRedemptionTransactionType
from wallet.models.wt_wallet_page_view_id import WTWalletPageViewId
from typing import Optional, Set
from typing_extensions import Self

class WTDynamicVoucherRedemption(BaseModel):
    """
    WTDynamicVoucherRedemption
    """ # noqa: E501
    session_key: Annotated[str, Field(strict=True)] = Field(alias="sessionKey")
    redeemed_amount: Annotated[int, Field(strict=True, ge=0)] = Field(alias="redeemedAmount")
    dynamic_voucher_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="dynamicVoucherID")
    redeemed_source: StrictStr = Field(alias="redeemedSource")
    redeemed_transaction_id: StrictStr = Field(alias="redeemedTransactionID")
    transaction_type: WTDynamicVoucherRedemptionTransactionType = Field(alias="transactionType")
    register_id: PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID = Field(alias="registerID")
    id: WTWalletPageViewId
    merchant_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="merchantID")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    is_active: StrictBool = Field(alias="isActive")
    redeemed_at: Optional[datetime] = Field(default=None, alias="redeemedAt")
    refunded_at: Optional[datetime] = Field(default=None, alias="refundedAt")
    refunded_transaction_id: StrictStr = Field(alias="refundedTransactionID")
    refunded_amount: Annotated[int, Field(strict=True, ge=0)] = Field(alias="refundedAmount")
    status: VSDynamicVoucherStatus
    redeemed_amount_decimal: StrictStr = Field(alias="redeemedAmount_decimal")
    redeemed_amount_string: StrictStr = Field(alias="redeemedAmount_string")
    discount_received: StrictStr = Field(alias="discountReceived")
    meta_value: StrictStr = Field(alias="metaValue")
    parent_object_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="parentObjectID")
    __properties: ClassVar[List[str]] = ["sessionKey", "redeemedAmount", "dynamicVoucherID", "redeemedSource", "redeemedTransactionID", "transactionType", "registerID", "id", "merchantID", "createdAt", "updatedAt", "isActive", "redeemedAt", "refundedAt", "refundedTransactionID", "refundedAmount", "status", "redeemedAmount_decimal", "redeemedAmount_string", "discountReceived", "metaValue", "parentObjectID"]

    @field_validator('dynamic_voucher_id')
    def dynamic_voucher_id_validate_regular_expression(cls, value):
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

    @field_validator('parent_object_id')
    def parent_object_id_validate_regular_expression(cls, value):
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
        """Create an instance of WTDynamicVoucherRedemption from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of transaction_type
        if self.transaction_type:
            _dict['transactionType'] = self.transaction_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of register_id
        if self.register_id:
            _dict['registerID'] = self.register_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # set to None if redeemed_at (nullable) is None
        # and model_fields_set contains the field
        if self.redeemed_at is None and "redeemed_at" in self.model_fields_set:
            _dict['redeemedAt'] = None

        # set to None if refunded_at (nullable) is None
        # and model_fields_set contains the field
        if self.refunded_at is None and "refunded_at" in self.model_fields_set:
            _dict['refundedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WTDynamicVoucherRedemption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sessionKey": obj.get("sessionKey"),
            "redeemedAmount": obj.get("redeemedAmount"),
            "dynamicVoucherID": obj.get("dynamicVoucherID"),
            "redeemedSource": obj.get("redeemedSource"),
            "redeemedTransactionID": obj.get("redeemedTransactionID"),
            "transactionType": WTDynamicVoucherRedemptionTransactionType.from_dict(obj["transactionType"]) if obj.get("transactionType") is not None else None,
            "registerID": PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID.from_dict(obj["registerID"]) if obj.get("registerID") is not None else None,
            "id": WTWalletPageViewId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "merchantID": obj.get("merchantID"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "isActive": obj.get("isActive"),
            "redeemedAt": obj.get("redeemedAt"),
            "refundedAt": obj.get("refundedAt"),
            "refundedTransactionID": obj.get("refundedTransactionID"),
            "refundedAmount": obj.get("refundedAmount"),
            "status": VSDynamicVoucherStatus.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "redeemedAmount_decimal": obj.get("redeemedAmount_decimal"),
            "redeemedAmount_string": obj.get("redeemedAmount_string"),
            "discountReceived": obj.get("discountReceived"),
            "metaValue": obj.get("metaValue"),
            "parentObjectID": obj.get("parentObjectID")
        })
        return _obj


