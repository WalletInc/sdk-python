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


class TrustBundleStatuses(str, Enum):
    """
    TrustBundleStatuses
    """

    """
    allowed enum values
    """
    DRAFT = 'draft'
    PENDING_MINUS_REVIEW = 'pending-review'
    IN_MINUS_REVIEW = 'in-review'
    TWILIO_MINUS_REJECTED = 'twilio-rejected'
    TWILIO_MINUS_APPROVED = 'twilio-approved'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TrustBundleStatuses from a JSON string"""
        return cls(json.loads(json_str))


