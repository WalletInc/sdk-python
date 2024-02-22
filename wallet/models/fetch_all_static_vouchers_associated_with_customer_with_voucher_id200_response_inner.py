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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from wallet.models.fetch_all_static_vouchers_associated_with_customer_with_voucher_id200_response_inner_value_type import FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInnerValueType
from wallet.models.payment_design import PaymentDesign
from typing import Optional, Set
from typing_extensions import Self

class FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInner(BaseModel):
    """
    FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInner
    """ # noqa: E501
    payment_design: PaymentDesign = Field(alias="PaymentDesign")
    value_type: FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInnerValueType = Field(alias="ValueType")
    voucher_type: Union[StrictFloat, StrictInt] = Field(alias="VoucherType")
    expiration_date: datetime = Field(alias="ExpirationDate")
    start_date: datetime = Field(alias="StartDate")
    title: StrictStr = Field(alias="Title")
    is_redeemed: StrictBool = Field(alias="IsRedeemed")
    display_value: StrictStr = Field(alias="DisplayValue")
    offer_amount_cents_decimal: StrictStr = Field(alias="OfferAmountCents_decimal")
    offer_amount_cents: Union[StrictFloat, StrictInt] = Field(alias="OfferAmountCents")
    member_id: StrictStr = Field(alias="MemberID")
    cell_phone_number: StrictStr = Field(alias="CellPhoneNumber")
    id: StrictStr
    __properties: ClassVar[List[str]] = ["PaymentDesign", "ValueType", "VoucherType", "ExpirationDate", "StartDate", "Title", "IsRedeemed", "DisplayValue", "OfferAmountCents_decimal", "OfferAmountCents", "MemberID", "CellPhoneNumber", "id"]

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
        """Create an instance of FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of payment_design
        if self.payment_design:
            _dict['PaymentDesign'] = self.payment_design.to_dict()
        # override the default output from pydantic by calling `to_dict()` of value_type
        if self.value_type:
            _dict['ValueType'] = self.value_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "PaymentDesign": PaymentDesign.from_dict(obj["PaymentDesign"]) if obj.get("PaymentDesign") is not None else None,
            "ValueType": FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInnerValueType.from_dict(obj["ValueType"]) if obj.get("ValueType") is not None else None,
            "VoucherType": obj.get("VoucherType"),
            "ExpirationDate": obj.get("ExpirationDate"),
            "StartDate": obj.get("StartDate"),
            "Title": obj.get("Title"),
            "IsRedeemed": obj.get("IsRedeemed"),
            "DisplayValue": obj.get("DisplayValue"),
            "OfferAmountCents_decimal": obj.get("OfferAmountCents_decimal"),
            "OfferAmountCents": obj.get("OfferAmountCents"),
            "MemberID": obj.get("MemberID"),
            "CellPhoneNumber": obj.get("CellPhoneNumber"),
            "id": obj.get("id")
        })
        return _obj


