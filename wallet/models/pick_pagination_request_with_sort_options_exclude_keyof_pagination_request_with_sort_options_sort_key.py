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

from pydantic import BaseModel, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from wallet.models.pagination_request_with_sort_options_sort_order import PaginationRequestWithSortOptionsSortOrder
from typing import Optional, Set
from typing_extensions import Self

class PickPaginationRequestWithSortOptionsExcludeKeyofPaginationRequestWithSortOptionsSortKey(BaseModel):
    """
    From T, pick a set of properties whose keys are in the union K
    """ # noqa: E501
    is_archive_included: Optional[StrictBool] = Field(default=None, description="Denotes if archived records should be included in the response payload", alias="isArchiveIncluded")
    page_size: Optional[StrictInt] = Field(default=None, description="Denotes the number of records per page", alias="pageSize")
    page_num: Optional[StrictInt] = Field(default=None, description="Denotes the page number", alias="pageNum")
    sort_order: Optional[PaginationRequestWithSortOptionsSortOrder] = Field(default=None, alias="sortOrder")
    __properties: ClassVar[List[str]] = ["isArchiveIncluded", "pageSize", "pageNum", "sortOrder"]

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
        """Create an instance of PickPaginationRequestWithSortOptionsExcludeKeyofPaginationRequestWithSortOptionsSortKey from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sort_order
        if self.sort_order:
            _dict['sortOrder'] = self.sort_order.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PickPaginationRequestWithSortOptionsExcludeKeyofPaginationRequestWithSortOptionsSortKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isArchiveIncluded": obj.get("isArchiveIncluded"),
            "pageSize": obj.get("pageSize"),
            "pageNum": obj.get("pageNum"),
            "sortOrder": PaginationRequestWithSortOptionsSortOrder.from_dict(obj["sortOrder"]) if obj.get("sortOrder") is not None else None
        })
        return _obj


