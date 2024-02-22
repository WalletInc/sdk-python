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
from wallet.models.pick_ss_outbound_message_log_exclude_keyof_ss_outbound_message_log_to_cell_phone_payment_object_broadcast_id import PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhonePaymentObjectBroadcastID
from wallet.models.pick_ss_outbound_message_log_exclude_keyof_ss_outbound_message_log_to_cell_phone_status import PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhoneStatus
from wallet.models.wt_wallet_page_view_id import WTWalletPageViewId
from typing import Optional, Set
from typing_extensions import Self

class OutboundSMS(BaseModel):
    """
    OutboundSMS
    """ # noqa: E501
    id: WTWalletPageViewId
    employee_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="employeeID")
    status: PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhoneStatus
    merchant_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="merchantID")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    is_active: StrictBool = Field(alias="isActive")
    body: StrictStr
    phone_number_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="phoneNumberID")
    media_urls: List[StrictStr] = Field(alias="mediaURLs")
    payment_object_broadcast_id: Optional[PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhonePaymentObjectBroadcastID] = Field(default=None, alias="paymentObjectBroadcastID")
    body_template: StrictStr = Field(alias="bodyTemplate")
    status_callback: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="statusCallback")
    is_sent: StrictBool = Field(alias="isSent")
    sent_at: Optional[datetime] = Field(default=None, alias="sentAt")
    delivered_at: Optional[datetime] = Field(default=None, alias="deliveredAt")
    message_sid: StrictStr = Field(alias="messageSid")
    num_segments: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="numSegments")
    num_media: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="numMedia")
    error_code: Optional[StrictStr] = Field(default=None, alias="errorCode")
    error_message: Optional[StrictStr] = Field(default=None, alias="errorMessage")
    to: StrictStr
    __properties: ClassVar[List[str]] = ["id", "employeeID", "status", "merchantID", "createdAt", "updatedAt", "isActive", "body", "phoneNumberID", "mediaURLs", "paymentObjectBroadcastID", "bodyTemplate", "statusCallback", "isSent", "sentAt", "deliveredAt", "messageSid", "numSegments", "numMedia", "errorCode", "errorMessage", "to"]

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
        """Create an instance of OutboundSMS from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_object_broadcast_id
        if self.payment_object_broadcast_id:
            _dict['paymentObjectBroadcastID'] = self.payment_object_broadcast_id.to_dict()
        # set to None if error_code (nullable) is None
        # and model_fields_set contains the field
        if self.error_code is None and "error_code" in self.model_fields_set:
            _dict['errorCode'] = None

        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict['errorMessage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OutboundSMS from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": WTWalletPageViewId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "employeeID": obj.get("employeeID"),
            "status": PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhoneStatus.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "merchantID": obj.get("merchantID"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "isActive": obj.get("isActive"),
            "body": obj.get("body"),
            "phoneNumberID": obj.get("phoneNumberID"),
            "mediaURLs": obj.get("mediaURLs"),
            "paymentObjectBroadcastID": PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhonePaymentObjectBroadcastID.from_dict(obj["paymentObjectBroadcastID"]) if obj.get("paymentObjectBroadcastID") is not None else None,
            "bodyTemplate": obj.get("bodyTemplate"),
            "statusCallback": obj.get("statusCallback"),
            "isSent": obj.get("isSent"),
            "sentAt": obj.get("sentAt"),
            "deliveredAt": obj.get("deliveredAt"),
            "messageSid": obj.get("messageSid"),
            "numSegments": obj.get("numSegments"),
            "numMedia": obj.get("numMedia"),
            "errorCode": obj.get("errorCode"),
            "errorMessage": obj.get("errorMessage"),
            "to": obj.get("to")
        })
        return _obj


