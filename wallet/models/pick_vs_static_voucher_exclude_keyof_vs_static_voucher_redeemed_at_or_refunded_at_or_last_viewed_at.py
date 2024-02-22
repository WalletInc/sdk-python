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
from wallet.models.pick_vs_static_voucher_exclude_keyof_vs_static_voucher_redeemed_at_or_refunded_at_or_last_viewed_at_transaction_type import PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtTransactionType
from wallet.models.status import Status
from typing import Optional, Set
from typing_extensions import Self

class PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAt(BaseModel):
    """
    From T, pick a set of properties whose keys are in the union K
    """ # noqa: E501
    id: Annotated[str, Field(min_length=10, strict=True, max_length=10)]
    campaign_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="campaignID")
    member_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="memberID")
    cell_phone_number: Optional[StrictStr] = Field(default=None, alias="cellPhoneNumber")
    offer_amount_cents: Annotated[int, Field(strict=True, ge=0)] = Field(alias="offerAmountCents")
    order_number: Annotated[int, Field(strict=True, ge=0)] = Field(alias="orderNumber")
    transaction_type: PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtTransactionType = Field(alias="transactionType")
    register_id: PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID = Field(alias="registerID")
    redeemed_source: StrictStr = Field(alias="redeemedSource")
    redeemed_transaction_id: StrictStr = Field(alias="redeemedTransactionID")
    redeemed_amount: Annotated[int, Field(strict=True, ge=0)] = Field(alias="redeemedAmount")
    is_redeemed: StrictBool = Field(alias="isRedeemed")
    refunded_transaction_id: StrictStr = Field(alias="refundedTransactionID")
    refunded_amount: Annotated[int, Field(strict=True, ge=0)] = Field(alias="refundedAmount")
    status: Status
    customer_id: Optional[StrictStr] = Field(default=None, alias="customerID")
    authorized_against_check_number: StrictStr = Field(alias="authorizedAgainstCheckNumber")
    authorized_amount: Annotated[int, Field(strict=True, ge=0)] = Field(alias="authorizedAmount")
    merchant_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="merchantID")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    is_active: StrictBool = Field(alias="isActive")
    __properties: ClassVar[List[str]] = ["id", "campaignID", "memberID", "cellPhoneNumber", "offerAmountCents", "orderNumber", "transactionType", "registerID", "redeemedSource", "redeemedTransactionID", "redeemedAmount", "isRedeemed", "refundedTransactionID", "refundedAmount", "status", "customerID", "authorizedAgainstCheckNumber", "authorizedAmount", "merchantID", "createdAt", "updatedAt", "isActive"]

    @field_validator('campaign_id')
    def campaign_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]+$/")
        return value

    @field_validator('member_id')
    def member_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]*$/")
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
        """Create an instance of PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAt from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "campaignID": obj.get("campaignID"),
            "memberID": obj.get("memberID"),
            "cellPhoneNumber": obj.get("cellPhoneNumber"),
            "offerAmountCents": obj.get("offerAmountCents"),
            "orderNumber": obj.get("orderNumber"),
            "transactionType": PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtTransactionType.from_dict(obj["transactionType"]) if obj.get("transactionType") is not None else None,
            "registerID": PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID.from_dict(obj["registerID"]) if obj.get("registerID") is not None else None,
            "redeemedSource": obj.get("redeemedSource"),
            "redeemedTransactionID": obj.get("redeemedTransactionID"),
            "redeemedAmount": obj.get("redeemedAmount"),
            "isRedeemed": obj.get("isRedeemed"),
            "refundedTransactionID": obj.get("refundedTransactionID"),
            "refundedAmount": obj.get("refundedAmount"),
            "status": Status.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "customerID": obj.get("customerID"),
            "authorizedAgainstCheckNumber": obj.get("authorizedAgainstCheckNumber"),
            "authorizedAmount": obj.get("authorizedAmount"),
            "merchantID": obj.get("merchantID"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "isActive": obj.get("isActive")
        })
        return _obj


