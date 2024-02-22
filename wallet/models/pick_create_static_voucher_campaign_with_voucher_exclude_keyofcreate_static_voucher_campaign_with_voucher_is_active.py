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
from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallet.models.pick_vs_campaign_update_params_exclude_keyof_vs_campaign_update_params_start_date_or_expiration_date_value_type import PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType
from typing import Optional, Set
from typing_extensions import Self

class PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherIsActive(BaseModel):
    """
    From T, pick a set of properties whose keys are in the union K
    """ # noqa: E501
    title: Annotated[str, Field(min_length=1, strict=True)]
    notes: StrictStr
    value_type: PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType = Field(alias="valueType")
    display_value: Optional[StrictStr] = Field(default=None, alias="displayValue")
    merchants_reference_id: Optional[StrictStr] = Field(default=None, alias="merchantsReferenceID")
    valid_only_at_pos_register_ids: Optional[List[StrictStr]] = Field(default=None, alias="validOnlyAtPOSRegisterIDs")
    payment_design_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="paymentDesignID")
    start_date_time: datetime = Field(alias="startDateTime")
    expiration_date_time: datetime = Field(alias="expirationDateTime")
    source_id: StrictInt = Field(alias="sourceID")
    member_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="memberID")
    offer_amount_cents: Annotated[int, Field(strict=True, ge=0)] = Field(alias="offerAmountCents")
    cell_phone: Optional[StrictStr] = Field(default=None, alias="cellPhone")
    __properties: ClassVar[List[str]] = ["title", "notes", "valueType", "displayValue", "merchantsReferenceID", "validOnlyAtPOSRegisterIDs", "paymentDesignID", "startDateTime", "expirationDateTime", "sourceID", "memberID", "offerAmountCents", "cellPhone"]

    @field_validator('payment_design_id')
    def payment_design_id_validate_regular_expression(cls, value):
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
        """Create an instance of PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherIsActive from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherIsActive from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "notes": obj.get("notes"),
            "valueType": PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType.from_dict(obj["valueType"]) if obj.get("valueType") is not None else None,
            "displayValue": obj.get("displayValue"),
            "merchantsReferenceID": obj.get("merchantsReferenceID"),
            "validOnlyAtPOSRegisterIDs": obj.get("validOnlyAtPOSRegisterIDs"),
            "paymentDesignID": obj.get("paymentDesignID"),
            "startDateTime": obj.get("startDateTime"),
            "expirationDateTime": obj.get("expirationDateTime"),
            "sourceID": obj.get("sourceID"),
            "memberID": obj.get("memberID"),
            "offerAmountCents": obj.get("offerAmountCents"),
            "cellPhone": obj.get("cellPhone")
        })
        return _obj


