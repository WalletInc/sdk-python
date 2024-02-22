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
from wallet.models.save_ticket_settings_request_payment_design_id import SaveTicketSettingsRequestPaymentDesignID
from typing import Optional, Set
from typing_extensions import Self

class Service(BaseModel):
    """
    Service
    """ # noqa: E501
    title: Annotated[str, Field(min_length=1, strict=True)]
    description: Annotated[str, Field(min_length=1, strict=True)]
    displayed_price: Optional[StrictStr] = Field(default=None, alias="displayedPrice")
    order_number: Annotated[int, Field(strict=True, ge=1)] = Field(alias="orderNumber")
    media_url: Optional[StrictStr] = Field(default=None, alias="mediaURL")
    additional_info_url: Optional[StrictStr] = Field(default=None, alias="additionalInfoURL")
    id: SaveTicketSettingsRequestPaymentDesignID
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    is_active: StrictBool = Field(alias="isActive")
    merchant_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="merchantID")
    __properties: ClassVar[List[str]] = ["title", "description", "displayedPrice", "orderNumber", "mediaURL", "additionalInfoURL", "id", "createdAt", "updatedAt", "isActive", "merchantID"]

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
        """Create an instance of Service from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Service from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "description": obj.get("description"),
            "displayedPrice": obj.get("displayedPrice"),
            "orderNumber": obj.get("orderNumber"),
            "mediaURL": obj.get("mediaURL"),
            "additionalInfoURL": obj.get("additionalInfoURL"),
            "id": SaveTicketSettingsRequestPaymentDesignID.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "isActive": obj.get("isActive"),
            "merchantID": obj.get("merchantID")
        })
        return _obj


