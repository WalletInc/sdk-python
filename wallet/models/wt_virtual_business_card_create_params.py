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

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class WTVirtualBusinessCardCreateParams(BaseModel):
    """
    WTVirtualBusinessCardCreateParams
    """ # noqa: E501
    first_name: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="firstName")
    last_name: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="lastName")
    email_address: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="emailAddress")
    designation: Annotated[str, Field(min_length=1, strict=True)]
    phone_number: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="phoneNumber")
    introduction: Optional[Annotated[str, Field(min_length=0, strict=True)]] = None
    instagram: Optional[Annotated[str, Field(strict=True)]] = None
    facebook: Optional[Annotated[str, Field(strict=True)]] = None
    you_tube: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="youTube")
    twitter: Optional[Annotated[str, Field(strict=True)]] = None
    linked_in: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="linkedIn")
    whats_app: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="whatsApp")
    avatar_url: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="avatarURL")
    __properties: ClassVar[List[str]] = ["firstName", "lastName", "emailAddress", "designation", "phoneNumber", "introduction", "instagram", "facebook", "youTube", "twitter", "linkedIn", "whatsApp", "avatarURL"]

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
        """Create an instance of WTVirtualBusinessCardCreateParams from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WTVirtualBusinessCardCreateParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "emailAddress": obj.get("emailAddress"),
            "designation": obj.get("designation"),
            "phoneNumber": obj.get("phoneNumber"),
            "introduction": obj.get("introduction"),
            "instagram": obj.get("instagram"),
            "facebook": obj.get("facebook"),
            "youTube": obj.get("youTube"),
            "twitter": obj.get("twitter"),
            "linkedIn": obj.get("linkedIn"),
            "whatsApp": obj.get("whatsApp"),
            "avatarURL": obj.get("avatarURL")
        })
        return _obj


