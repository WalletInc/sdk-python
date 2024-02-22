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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from wallet.models.wt_employee import WTEmployee
from typing import Optional, Set
from typing_extensions import Self

class WTRole(BaseModel):
    """
    WTRole
    """ # noqa: E501
    id: Annotated[str, Field(min_length=10, strict=True, max_length=10)]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    employees: List[WTEmployee]
    roles: List[WTRole]
    employee_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="employeeID")
    merchant_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="merchantID")
    name: StrictStr
    display_name: StrictStr = Field(alias="displayName")
    is_public: StrictBool = Field(alias="isPublic")
    order_number: Union[StrictFloat, StrictInt] = Field(alias="orderNumber")
    is_system: StrictBool = Field(alias="isSystem")
    icons: List[StrictStr]
    category: StrictStr
    admin_page: StrictStr = Field(alias="adminPage")
    __properties: ClassVar[List[str]] = ["id", "createdAt", "updatedAt", "employees", "roles", "employeeID", "merchantID", "name", "displayName", "isPublic", "orderNumber", "isSystem", "icons", "category", "adminPage"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]+$/")
        return value

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
        """Create an instance of WTRole from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in employees (list)
        _items = []
        if self.employees:
            for _item in self.employees:
                if _item:
                    _items.append(_item.to_dict())
            _dict['employees'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WTRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "employees": [WTEmployee.from_dict(_item) for _item in obj["employees"]] if obj.get("employees") is not None else None,
            "roles": [WTRole.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None,
            "employeeID": obj.get("employeeID"),
            "merchantID": obj.get("merchantID"),
            "name": obj.get("name"),
            "displayName": obj.get("displayName"),
            "isPublic": obj.get("isPublic"),
            "orderNumber": obj.get("orderNumber"),
            "isSystem": obj.get("isSystem"),
            "icons": obj.get("icons"),
            "category": obj.get("category"),
            "adminPage": obj.get("adminPage")
        })
        return _obj

# TODO: Rewrite to not use raise_errors
WTRole.model_rebuild(raise_errors=False)

