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

from pydantic import BaseModel, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallet.models.wt_wallet_page_view_id import WTWalletPageViewId
from typing import Optional, Set
from typing_extensions import Self

class WTStaticVoucherCreateParams(BaseModel):
    """
    WTStaticVoucherCreateParams
    """ # noqa: E501
    offer_amount_cents: Annotated[int, Field(strict=True, ge=0)] = Field(alias="offerAmountCents")
    member_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="memberID")
    cell_phone: Annotated[str, Field(min_length=10, strict=True)] = Field(alias="cellPhone")
    campaign_id: WTWalletPageViewId = Field(alias="campaignID")
    __properties: ClassVar[List[str]] = ["offerAmountCents", "memberID", "cellPhone", "campaignID"]

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
        """Create an instance of WTStaticVoucherCreateParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of campaign_id
        if self.campaign_id:
            _dict['campaignID'] = self.campaign_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WTStaticVoucherCreateParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "offerAmountCents": obj.get("offerAmountCents"),
            "memberID": obj.get("memberID"),
            "cellPhone": obj.get("cellPhone"),
            "campaignID": WTWalletPageViewId.from_dict(obj["campaignID"]) if obj.get("campaignID") is not None else None
        })
        return _obj


