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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wallet.models.click_funnel_amount import ClickFunnelAmount
from typing import Optional, Set
from typing_extensions import Self

class ClickFunnelProduct(BaseModel):
    """
    ClickFunnelProduct
    """ # noqa: E501
    id: Union[StrictFloat, StrictInt]
    name: StrictStr
    stripe_plan: StrictStr
    amount: ClickFunnelAmount
    amount_currency: StrictStr
    created_at: datetime
    updated_at: datetime
    subject: StrictStr
    html_body: StrictStr
    thank_you_page_id: Union[StrictFloat, StrictInt]
    stripe_cancel_after_payments: Optional[Any] = None
    bump: StrictBool
    cart_product_id: Optional[Any] = None
    billing_integration: StrictStr
    infusionsoft_product_id: Optional[Any] = None
    infusionsoft_subscription_id: Optional[Any] = None
    ontraport_product_id: Optional[Any] = None
    ontraport_payment_count: Optional[Any] = None
    ontraport_payment_type: Optional[Any] = None
    ontraport_unit: Optional[Any] = None
    ontraport_gateway_id: Optional[Any] = None
    ontraport_invoice_id: Optional[Any] = None
    commissionable: StrictBool
    statement_descriptor: StrictStr
    netsuite_id: Optional[Any] = None
    netsuite_tag: Optional[Any] = None
    netsuite_class: Optional[Any] = None
    description: StrictStr
    __properties: ClassVar[List[str]] = ["id", "name", "stripe_plan", "amount", "amount_currency", "created_at", "updated_at", "subject", "html_body", "thank_you_page_id", "stripe_cancel_after_payments", "bump", "cart_product_id", "billing_integration", "infusionsoft_product_id", "infusionsoft_subscription_id", "ontraport_product_id", "ontraport_payment_count", "ontraport_payment_type", "ontraport_unit", "ontraport_gateway_id", "ontraport_invoice_id", "commissionable", "statement_descriptor", "netsuite_id", "netsuite_tag", "netsuite_class", "description"]

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
        """Create an instance of ClickFunnelProduct from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # set to None if stripe_cancel_after_payments (nullable) is None
        # and model_fields_set contains the field
        if self.stripe_cancel_after_payments is None and "stripe_cancel_after_payments" in self.model_fields_set:
            _dict['stripe_cancel_after_payments'] = None

        # set to None if cart_product_id (nullable) is None
        # and model_fields_set contains the field
        if self.cart_product_id is None and "cart_product_id" in self.model_fields_set:
            _dict['cart_product_id'] = None

        # set to None if infusionsoft_product_id (nullable) is None
        # and model_fields_set contains the field
        if self.infusionsoft_product_id is None and "infusionsoft_product_id" in self.model_fields_set:
            _dict['infusionsoft_product_id'] = None

        # set to None if infusionsoft_subscription_id (nullable) is None
        # and model_fields_set contains the field
        if self.infusionsoft_subscription_id is None and "infusionsoft_subscription_id" in self.model_fields_set:
            _dict['infusionsoft_subscription_id'] = None

        # set to None if ontraport_product_id (nullable) is None
        # and model_fields_set contains the field
        if self.ontraport_product_id is None and "ontraport_product_id" in self.model_fields_set:
            _dict['ontraport_product_id'] = None

        # set to None if ontraport_payment_count (nullable) is None
        # and model_fields_set contains the field
        if self.ontraport_payment_count is None and "ontraport_payment_count" in self.model_fields_set:
            _dict['ontraport_payment_count'] = None

        # set to None if ontraport_payment_type (nullable) is None
        # and model_fields_set contains the field
        if self.ontraport_payment_type is None and "ontraport_payment_type" in self.model_fields_set:
            _dict['ontraport_payment_type'] = None

        # set to None if ontraport_unit (nullable) is None
        # and model_fields_set contains the field
        if self.ontraport_unit is None and "ontraport_unit" in self.model_fields_set:
            _dict['ontraport_unit'] = None

        # set to None if ontraport_gateway_id (nullable) is None
        # and model_fields_set contains the field
        if self.ontraport_gateway_id is None and "ontraport_gateway_id" in self.model_fields_set:
            _dict['ontraport_gateway_id'] = None

        # set to None if ontraport_invoice_id (nullable) is None
        # and model_fields_set contains the field
        if self.ontraport_invoice_id is None and "ontraport_invoice_id" in self.model_fields_set:
            _dict['ontraport_invoice_id'] = None

        # set to None if netsuite_id (nullable) is None
        # and model_fields_set contains the field
        if self.netsuite_id is None and "netsuite_id" in self.model_fields_set:
            _dict['netsuite_id'] = None

        # set to None if netsuite_tag (nullable) is None
        # and model_fields_set contains the field
        if self.netsuite_tag is None and "netsuite_tag" in self.model_fields_set:
            _dict['netsuite_tag'] = None

        # set to None if netsuite_class (nullable) is None
        # and model_fields_set contains the field
        if self.netsuite_class is None and "netsuite_class" in self.model_fields_set:
            _dict['netsuite_class'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClickFunnelProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "stripe_plan": obj.get("stripe_plan"),
            "amount": ClickFunnelAmount.from_dict(obj["amount"]) if obj.get("amount") is not None else None,
            "amount_currency": obj.get("amount_currency"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "subject": obj.get("subject"),
            "html_body": obj.get("html_body"),
            "thank_you_page_id": obj.get("thank_you_page_id"),
            "stripe_cancel_after_payments": obj.get("stripe_cancel_after_payments"),
            "bump": obj.get("bump"),
            "cart_product_id": obj.get("cart_product_id"),
            "billing_integration": obj.get("billing_integration"),
            "infusionsoft_product_id": obj.get("infusionsoft_product_id"),
            "infusionsoft_subscription_id": obj.get("infusionsoft_subscription_id"),
            "ontraport_product_id": obj.get("ontraport_product_id"),
            "ontraport_payment_count": obj.get("ontraport_payment_count"),
            "ontraport_payment_type": obj.get("ontraport_payment_type"),
            "ontraport_unit": obj.get("ontraport_unit"),
            "ontraport_gateway_id": obj.get("ontraport_gateway_id"),
            "ontraport_invoice_id": obj.get("ontraport_invoice_id"),
            "commissionable": obj.get("commissionable"),
            "statement_descriptor": obj.get("statement_descriptor"),
            "netsuite_id": obj.get("netsuite_id"),
            "netsuite_tag": obj.get("netsuite_tag"),
            "netsuite_class": obj.get("netsuite_class"),
            "description": obj.get("description")
        })
        return _obj


