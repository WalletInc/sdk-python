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

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class WTQRCodeDesignCreateParams(BaseModel):
    """
    WTQRCodeDesignCreateParams
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True)]
    size: Annotated[int, Field(strict=True, ge=1)]
    margin: Annotated[int, Field(strict=True, ge=0)]
    is_margin_white: StrictBool = Field(alias="isMarginWhite")
    corner_radius: Annotated[int, Field(strict=True, ge=0)] = Field(alias="cornerRadius")
    color_dark_hex: Annotated[str, Field(min_length=0, strict=True)] = Field(alias="colorDarkHex")
    color_light_hex: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="colorLightHex")
    background_dimming_hex: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="backgroundDimmingHex")
    logo_image_url: Optional[StrictStr] = Field(default=None, alias="logoImageURL")
    background_image_url: Optional[StrictStr] = Field(default=None, alias="backgroundImageURL")
    animated_gif_background_url: Optional[StrictStr] = Field(default=None, alias="animatedGifBackgroundURL")
    __properties: ClassVar[List[str]] = ["name", "size", "margin", "isMarginWhite", "cornerRadius", "colorDarkHex", "colorLightHex", "backgroundDimmingHex", "logoImageURL", "backgroundImageURL", "animatedGifBackgroundURL"]

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
        """Create an instance of WTQRCodeDesignCreateParams from a JSON string"""
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
        """Create an instance of WTQRCodeDesignCreateParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "size": obj.get("size"),
            "margin": obj.get("margin"),
            "isMarginWhite": obj.get("isMarginWhite"),
            "cornerRadius": obj.get("cornerRadius"),
            "colorDarkHex": obj.get("colorDarkHex"),
            "colorLightHex": obj.get("colorLightHex"),
            "backgroundDimmingHex": obj.get("backgroundDimmingHex"),
            "logoImageURL": obj.get("logoImageURL"),
            "backgroundImageURL": obj.get("backgroundImageURL"),
            "animatedGifBackgroundURL": obj.get("animatedGifBackgroundURL")
        })
        return _obj


