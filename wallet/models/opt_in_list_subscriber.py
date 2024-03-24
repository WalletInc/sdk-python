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
from wallet.models.pick_ss_opt_in_list_member_update_params_exclude_keyof_ss_opt_in_list_member_update_params_merchant_created_at_or_max_sms_count_opt_in_source_id import PickSSOptInListMemberUpdateParamsExcludeKeyofSSOptInListMemberUpdateParamsMerchantCreatedAtOrMaxSMSCountOptInSourceID
from wallet.models.ss_opt_in_source import SSOptInSource
from wallet.models.wt_wallet_page_view_id import WTWalletPageViewId
from typing import Optional, Set
from typing_extensions import Self

class OptInListSubscriber(BaseModel):
    """
    OptInListSubscriber
    """ # noqa: E501
    caller_name: Optional[StrictStr] = Field(default=None, alias="callerName")
    caller_type: Optional[StrictStr] = Field(default=None, alias="callerType")
    opt_in_list_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="optInListID")
    opt_in_source_id: PickSSOptInListMemberUpdateParamsExcludeKeyofSSOptInListMemberUpdateParamsMerchantCreatedAtOrMaxSMSCountOptInSourceID = Field(alias="optInSourceID")
    is_subscribed: StrictBool = Field(alias="isSubscribed")
    is_pending_age21_verification: StrictBool = Field(alias="isPendingAge21Verification")
    mobile_phone_number: StrictStr = Field(alias="mobilePhoneNumber")
    referring_url: Annotated[str, Field(min_length=0, strict=True)] = Field(alias="referringURL")
    id: WTWalletPageViewId
    merchant_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="merchantID")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    is_active: StrictBool = Field(alias="isActive")
    opted_status: Optional[StrictBool] = Field(default=None, alias="optedStatus")
    source: Optional[SSOptInSource] = Field(default=None, alias="Source")
    __properties: ClassVar[List[str]] = ["callerName", "callerType", "optInListID", "optInSourceID", "isSubscribed", "isPendingAge21Verification", "mobilePhoneNumber", "referringURL", "id", "merchantID", "createdAt", "updatedAt", "isActive", "optedStatus", "Source"]

    @field_validator('opt_in_list_id')
    def opt_in_list_id_validate_regular_expression(cls, value):
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
        """Create an instance of OptInListSubscriber from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of opt_in_source_id
        if self.opt_in_source_id:
            _dict['optInSourceID'] = self.opt_in_source_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['Source'] = self.source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OptInListSubscriber from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "callerName": obj.get("callerName"),
            "callerType": obj.get("callerType"),
            "optInListID": obj.get("optInListID"),
            "optInSourceID": PickSSOptInListMemberUpdateParamsExcludeKeyofSSOptInListMemberUpdateParamsMerchantCreatedAtOrMaxSMSCountOptInSourceID.from_dict(obj["optInSourceID"]) if obj.get("optInSourceID") is not None else None,
            "isSubscribed": obj.get("isSubscribed"),
            "isPendingAge21Verification": obj.get("isPendingAge21Verification"),
            "mobilePhoneNumber": obj.get("mobilePhoneNumber"),
            "referringURL": obj.get("referringURL"),
            "id": WTWalletPageViewId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "merchantID": obj.get("merchantID"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "isActive": obj.get("isActive"),
            "optedStatus": obj.get("optedStatus"),
            "Source": SSOptInSource.from_dict(obj["Source"]) if obj.get("Source") is not None else None
        })
        return _obj

