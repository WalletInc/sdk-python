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

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wallet.models.portal_page import PortalPage
from wallet.models.subscription_feature import SubscriptionFeature
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionProduct(BaseModel):
    """
    SubscriptionProduct
    """ # noqa: E501
    id: StrictStr
    title: StrictStr
    title_full: StrictStr = Field(alias="titleFull")
    category: StrictStr
    volume: Optional[Union[StrictFloat, StrictInt]] = None
    value: Optional[Union[StrictFloat, StrictInt]] = None
    features: List[SubscriptionFeature]
    pages: List[PortalPage]
    icon_name: StrictStr = Field(alias="iconName")
    description: StrictStr
    is_hourly: Optional[StrictBool] = Field(default=None, alias="isHourly")
    release_status: Optional[StrictStr] = Field(default=None, alias="releaseStatus")
    __properties: ClassVar[List[str]] = ["id", "title", "titleFull", "category", "volume", "value", "features", "pages", "iconName", "description", "isHourly", "releaseStatus"]

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
        """Create an instance of SubscriptionProduct from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in features (list)
        _items = []
        if self.features:
            for _item in self.features:
                if _item:
                    _items.append(_item.to_dict())
            _dict['features'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "titleFull": obj.get("titleFull"),
            "category": obj.get("category"),
            "volume": obj.get("volume"),
            "value": obj.get("value"),
            "features": [SubscriptionFeature.from_dict(_item) for _item in obj["features"]] if obj.get("features") is not None else None,
            "pages": obj.get("pages"),
            "iconName": obj.get("iconName"),
            "description": obj.get("description"),
            "isHourly": obj.get("isHourly"),
            "releaseStatus": obj.get("releaseStatus")
        })
        return _obj


