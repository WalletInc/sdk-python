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

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallet.models.pick_vs_payment_design_update_params_exclude_keyof_vs_payment_design_update_params_id_border_style_type import PickVSPaymentDesignUpdateParamsExcludeKeyofVSPaymentDesignUpdateParamsIdBorderStyleType
from typing import Optional, Set
from typing_extensions import Self

class PickVSPaymentDesignCreateParamsExcludeKeyofVSPaymentDesignCreateParamsEmployeeID(BaseModel):
    """
    From T, pick a set of properties whose keys are in the union K
    """ # noqa: E501
    border_color: Annotated[str, Field(strict=True)] = Field(alias="borderColor")
    border_style_type: PickVSPaymentDesignUpdateParamsExcludeKeyofVSPaymentDesignUpdateParamsIdBorderStyleType = Field(alias="borderStyleType")
    border_size: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="borderSize")
    border_radius: Annotated[int, Field(le=20, strict=True, ge=0)] = Field(alias="borderRadius")
    font_color: Annotated[str, Field(strict=True)] = Field(alias="fontColor")
    font_type: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="fontType")
    abbreviation: Annotated[str, Field(min_length=1, strict=True)]
    acronym: Annotated[str, Field(min_length=1, strict=True)]
    icon: Annotated[str, Field(min_length=1, strict=True)]
    design_name: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="designName")
    display_name: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="displayName")
    background_image_url: Optional[StrictStr] = Field(default=None, alias="backgroundImageURL")
    company_logo_url: Optional[StrictStr] = Field(default=None, alias="companyLogoURL")
    __properties: ClassVar[List[str]] = ["borderColor", "borderStyleType", "borderSize", "borderRadius", "fontColor", "fontType", "abbreviation", "acronym", "icon", "designName", "displayName", "backgroundImageURL", "companyLogoURL"]

    @field_validator('border_color')
    def border_color_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", value):
            raise ValueError(r"must validate the regular expression /^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/")
        return value

    @field_validator('font_color')
    def font_color_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", value):
            raise ValueError(r"must validate the regular expression /^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/")
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
        """Create an instance of PickVSPaymentDesignCreateParamsExcludeKeyofVSPaymentDesignCreateParamsEmployeeID from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of border_style_type
        if self.border_style_type:
            _dict['borderStyleType'] = self.border_style_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PickVSPaymentDesignCreateParamsExcludeKeyofVSPaymentDesignCreateParamsEmployeeID from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "borderColor": obj.get("borderColor"),
            "borderStyleType": PickVSPaymentDesignUpdateParamsExcludeKeyofVSPaymentDesignUpdateParamsIdBorderStyleType.from_dict(obj["borderStyleType"]) if obj.get("borderStyleType") is not None else None,
            "borderSize": obj.get("borderSize"),
            "borderRadius": obj.get("borderRadius"),
            "fontColor": obj.get("fontColor"),
            "fontType": obj.get("fontType"),
            "abbreviation": obj.get("abbreviation"),
            "acronym": obj.get("acronym"),
            "icon": obj.get("icon"),
            "designName": obj.get("designName"),
            "displayName": obj.get("displayName"),
            "backgroundImageURL": obj.get("backgroundImageURL"),
            "companyLogoURL": obj.get("companyLogoURL")
        })
        return _obj


