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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallet.models.ms_member_redemption_transaction_type import MSMemberRedemptionTransactionType
from wallet.models.pick_vs_static_voucher_exclude_keyof_vs_static_voucher_redeemed_at_or_refunded_at_or_last_viewed_at_register_id import PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID
from typing import Optional, Set
from typing_extensions import Self

class MSMerchantCreditRedemption(BaseModel):
    """
    MSMerchantCreditRedemption
    """ # noqa: E501
    transaction_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The transaction ID at the POS", alias="transactionID")
    transaction_type: MSMemberRedemptionTransactionType = Field(alias="transactionType")
    amount: Annotated[int, Field(strict=True, ge=0)] = Field(description="The number of amount involved in this transaction")
    register_id: Optional[PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID] = Field(default=None, alias="registerID")
    terminal_type: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The type of the terminal", alias="terminalType")
    id: Annotated[str, Field(min_length=36, strict=True, max_length=36)] = Field(description="The UUID of this record")
    merchant_credit_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="merchantCreditID")
    merchant_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="merchantID")
    created_at: datetime = Field(description="The timestamp of when this resource was created", alias="createdAt")
    is_active: StrictBool = Field(description="Denotes if this resource is active", alias="isActive")
    __properties: ClassVar[List[str]] = ["transactionID", "transactionType", "amount", "registerID", "terminalType", "id", "merchantCreditID", "merchantID", "createdAt", "isActive"]

    @field_validator('merchant_credit_id')
    def merchant_credit_id_validate_regular_expression(cls, value):
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
        """Create an instance of MSMerchantCreditRedemption from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MSMerchantCreditRedemption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transactionID": obj.get("transactionID"),
            "transactionType": MSMemberRedemptionTransactionType.from_dict(obj["transactionType"]) if obj.get("transactionType") is not None else None,
            "amount": obj.get("amount"),
            "registerID": PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID.from_dict(obj["registerID"]) if obj.get("registerID") is not None else None,
            "terminalType": obj.get("terminalType"),
            "id": obj.get("id"),
            "merchantCreditID": obj.get("merchantCreditID"),
            "merchantID": obj.get("merchantID"),
            "createdAt": obj.get("createdAt"),
            "isActive": obj.get("isActive")
        })
        return _obj


