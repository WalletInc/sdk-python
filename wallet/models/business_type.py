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
import json
from enum import Enum
from typing_extensions import Self


class BusinessType(str, Enum):
    """
    BusinessType
    """

    """
    allowed enum values
    """
    PARTNERSHIP = 'Partnership'
    LIMITED_LIABILITY_CORPORATION = 'Limited Liability Corporation'
    CO_MINUS_OPERATIVE = 'Co-operative'
    NON_MINUS_PROFIT_CORPORATION = 'Non-profit Corporation'
    CORPORATION = 'Corporation'
    SOLE_PROPRIETORSHIP = 'Sole Proprietorship'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BusinessType from a JSON string"""
        return cls(json.loads(json_str))


