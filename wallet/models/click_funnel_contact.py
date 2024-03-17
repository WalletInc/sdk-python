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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wallet.models.click_funnel_contact_profile import ClickFunnelContactProfile
from typing import Optional, Set
from typing_extensions import Self

class ClickFunnelContact(BaseModel):
    """
    ClickFunnelContact
    """ # noqa: E501
    id: Union[StrictFloat, StrictInt]
    page_id: Union[StrictFloat, StrictInt]
    first_name: StrictStr
    last_name: StrictStr
    name: StrictStr
    address: StrictStr
    city: StrictStr
    country: StrictStr
    state: Optional[StrictStr] = None
    zip: StrictStr
    email: StrictStr
    phone: StrictStr
    webinar_at: Optional[Any] = None
    webinar_last_time: Optional[Any] = None
    webinar_ext: StrictStr
    created_at: datetime
    updated_at: datetime
    ip: StrictStr
    funnel_id: Union[StrictFloat, StrictInt]
    funnel_step_id: Union[StrictFloat, StrictInt]
    unsubscribed_at: Optional[Any] = None
    cf_uvid: StrictStr
    cart_affiliate_id: StrictStr
    shipping_address: StrictStr
    shipping_city: StrictStr
    shipping_country: StrictStr
    shipping_state: StrictStr
    shipping_zip: StrictStr
    vat_number: StrictStr
    affiliate_id: Optional[Any] = None
    aff_sub: StrictStr
    aff_sub2: StrictStr
    cf_affiliate_id: Optional[Any] = None
    contact_profile: Optional[ClickFunnelContactProfile] = None
    time_zone: Optional[StrictStr] = None
    company_name: StrictStr
    company_industry: StrictStr
    additional_info: Optional[Any] = None
    ga_client_id: Optional[StrictStr] = None
    ga_measurement_id: Optional[StrictStr] = None
    funnel_name: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "page_id", "first_name", "last_name", "name", "address", "city", "country", "state", "zip", "email", "phone", "webinar_at", "webinar_last_time", "webinar_ext", "created_at", "updated_at", "ip", "funnel_id", "funnel_step_id", "unsubscribed_at", "cf_uvid", "cart_affiliate_id", "shipping_address", "shipping_city", "shipping_country", "shipping_state", "shipping_zip", "vat_number", "affiliate_id", "aff_sub", "aff_sub2", "cf_affiliate_id", "contact_profile", "time_zone", "company_name", "company_industry", "additional_info", "ga_client_id", "ga_measurement_id", "funnel_name"]

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
        """Create an instance of ClickFunnelContact from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of contact_profile
        if self.contact_profile:
            _dict['contact_profile'] = self.contact_profile.to_dict()
        # set to None if webinar_at (nullable) is None
        # and model_fields_set contains the field
        if self.webinar_at is None and "webinar_at" in self.model_fields_set:
            _dict['webinar_at'] = None

        # set to None if webinar_last_time (nullable) is None
        # and model_fields_set contains the field
        if self.webinar_last_time is None and "webinar_last_time" in self.model_fields_set:
            _dict['webinar_last_time'] = None

        # set to None if unsubscribed_at (nullable) is None
        # and model_fields_set contains the field
        if self.unsubscribed_at is None and "unsubscribed_at" in self.model_fields_set:
            _dict['unsubscribed_at'] = None

        # set to None if affiliate_id (nullable) is None
        # and model_fields_set contains the field
        if self.affiliate_id is None and "affiliate_id" in self.model_fields_set:
            _dict['affiliate_id'] = None

        # set to None if cf_affiliate_id (nullable) is None
        # and model_fields_set contains the field
        if self.cf_affiliate_id is None and "cf_affiliate_id" in self.model_fields_set:
            _dict['cf_affiliate_id'] = None

        # set to None if time_zone (nullable) is None
        # and model_fields_set contains the field
        if self.time_zone is None and "time_zone" in self.model_fields_set:
            _dict['time_zone'] = None

        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additional_info'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClickFunnelContact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "page_id": obj.get("page_id"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "name": obj.get("name"),
            "address": obj.get("address"),
            "city": obj.get("city"),
            "country": obj.get("country"),
            "state": obj.get("state"),
            "zip": obj.get("zip"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "webinar_at": obj.get("webinar_at"),
            "webinar_last_time": obj.get("webinar_last_time"),
            "webinar_ext": obj.get("webinar_ext"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "ip": obj.get("ip"),
            "funnel_id": obj.get("funnel_id"),
            "funnel_step_id": obj.get("funnel_step_id"),
            "unsubscribed_at": obj.get("unsubscribed_at"),
            "cf_uvid": obj.get("cf_uvid"),
            "cart_affiliate_id": obj.get("cart_affiliate_id"),
            "shipping_address": obj.get("shipping_address"),
            "shipping_city": obj.get("shipping_city"),
            "shipping_country": obj.get("shipping_country"),
            "shipping_state": obj.get("shipping_state"),
            "shipping_zip": obj.get("shipping_zip"),
            "vat_number": obj.get("vat_number"),
            "affiliate_id": obj.get("affiliate_id"),
            "aff_sub": obj.get("aff_sub"),
            "aff_sub2": obj.get("aff_sub2"),
            "cf_affiliate_id": obj.get("cf_affiliate_id"),
            "contact_profile": ClickFunnelContactProfile.from_dict(obj["contact_profile"]) if obj.get("contact_profile") is not None else None,
            "time_zone": obj.get("time_zone"),
            "company_name": obj.get("company_name"),
            "company_industry": obj.get("company_industry"),
            "additional_info": obj.get("additional_info"),
            "ga_client_id": obj.get("ga_client_id"),
            "ga_measurement_id": obj.get("ga_measurement_id"),
            "funnel_name": obj.get("funnel_name")
        })
        return _obj


