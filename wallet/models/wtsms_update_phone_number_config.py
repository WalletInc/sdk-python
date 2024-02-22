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
from typing import Optional, Set
from typing_extensions import Self

class WTSMSUpdatePhoneNumberConfig(BaseModel):
    """
    WTSMSUpdatePhoneNumberConfig
    """ # noqa: E501
    company_name: StrictStr = Field(alias="companyName")
    privacy_policy_url: Optional[StrictStr] = Field(default=None, alias="privacyPolicyURL")
    terms_of_service_url: Optional[StrictStr] = Field(default=None, alias="termsOfServiceURL")
    message_footer: StrictStr = Field(alias="messageFooter")
    stop_response: StrictStr = Field(alias="stopResponse")
    help_response: StrictStr = Field(alias="helpResponse")
    help_desk_keyword: StrictStr = Field(alias="helpDeskKeyword")
    help_desk_queue_response: StrictStr = Field(alias="helpDeskQueueResponse")
    is_connected_to_watson: Optional[StrictBool] = Field(default=None, alias="isConnectedToWatson")
    watson_username: Optional[StrictStr] = Field(default=None, alias="watsonUsername")
    watson_password: Optional[StrictStr] = Field(default=None, alias="watsonPassword")
    watson_conversation_workplace_id: Optional[StrictStr] = Field(default=None, alias="watsonConversationWorkplaceID")
    __properties: ClassVar[List[str]] = ["companyName", "privacyPolicyURL", "termsOfServiceURL", "messageFooter", "stopResponse", "helpResponse", "helpDeskKeyword", "helpDeskQueueResponse", "isConnectedToWatson", "watsonUsername", "watsonPassword", "watsonConversationWorkplaceID"]

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
        """Create an instance of WTSMSUpdatePhoneNumberConfig from a JSON string"""
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
        """Create an instance of WTSMSUpdatePhoneNumberConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "companyName": obj.get("companyName"),
            "privacyPolicyURL": obj.get("privacyPolicyURL"),
            "termsOfServiceURL": obj.get("termsOfServiceURL"),
            "messageFooter": obj.get("messageFooter"),
            "stopResponse": obj.get("stopResponse"),
            "helpResponse": obj.get("helpResponse"),
            "helpDeskKeyword": obj.get("helpDeskKeyword"),
            "helpDeskQueueResponse": obj.get("helpDeskQueueResponse"),
            "isConnectedToWatson": obj.get("isConnectedToWatson"),
            "watsonUsername": obj.get("watsonUsername"),
            "watsonPassword": obj.get("watsonPassword"),
            "watsonConversationWorkplaceID": obj.get("watsonConversationWorkplaceID")
        })
        return _obj


