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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from wallet.models.wallet_configuration_sms_opt_in_source_id import WalletConfigurationSmsOptInSourceID
from typing import Optional, Set
from typing_extensions import Self

class WalletConfiguration(BaseModel):
    """
    WalletConfiguration
    """ # noqa: E501
    header_background_color: StrictStr = Field(alias="headerBackgroundColor")
    header_button_color: StrictStr = Field(alias="headerButtonColor")
    left_menu_header_background_color: StrictStr = Field(alias="leftMenuHeaderBackgroundColor")
    left_menu_header_font_color: StrictStr = Field(alias="leftMenuHeaderFontColor")
    left_menu_section_background_color: StrictStr = Field(alias="leftMenuSectionBackgroundColor")
    left_menu_section_font_color: StrictStr = Field(alias="leftMenuSectionFontColor")
    company_logo_url: StrictStr = Field(alias="companyLogoURL")
    header_image_url: Optional[StrictStr] = Field(default=None, alias="headerImageURL")
    header_custom_icon: Optional[StrictStr] = Field(default=None, alias="headerCustomIcon")
    welcome_message: StrictStr = Field(alias="welcomeMessage")
    is_apple_enabled: StrictBool = Field(alias="isAppleEnabled")
    is_google_enabled: StrictBool = Field(alias="isGoogleEnabled")
    is_samsung_enabled: StrictBool = Field(alias="isSamsungEnabled")
    is_ad_credits: StrictBool = Field(alias="isAdCredits")
    is_static_vouchers: StrictBool = Field(alias="isStaticVouchers")
    is_dynamic_vouchers: StrictBool = Field(alias="isDynamicVouchers")
    is_membership_tier: StrictBool = Field(alias="isMembershipTier")
    is_membership_points: StrictBool = Field(alias="isMembershipPoints")
    is_membership_level: StrictBool = Field(alias="isMembershipLevel")
    is_gift_cards: StrictBool = Field(alias="isGiftCards")
    is_gift_certificates: StrictBool = Field(alias="isGiftCertificates")
    is_promotions: StrictBool = Field(alias="isPromotions")
    is_merchant_credit: StrictBool = Field(alias="isMerchantCredit")
    is_tickets: Optional[StrictBool] = Field(default=None, alias="isTickets")
    is_news_articles: StrictBool = Field(alias="isNewsArticles")
    is_performances: StrictBool = Field(alias="isPerformances")
    is_messages: StrictBool = Field(alias="isMessages")
    is_call: StrictBool = Field(alias="isCall")
    is_representatives: StrictBool = Field(alias="isRepresentatives")
    is_products: StrictBool = Field(alias="isProducts")
    is_services: StrictBool = Field(alias="isServices")
    is_room_rates: StrictBool = Field(alias="isRoomRates")
    is_amenities: StrictBool = Field(alias="isAmenities")
    is_gaming: StrictBool = Field(alias="isGaming")
    is_dining: StrictBool = Field(alias="isDining")
    is_lounges: StrictBool = Field(alias="isLounges")
    is_map_directions: StrictBool = Field(alias="isMapDirections")
    is_link_book: StrictBool = Field(alias="isLinkBook")
    is_image_grid: StrictBool = Field(alias="isImageGrid")
    is_videos: StrictBool = Field(alias="isVideos")
    is_transaction_history: StrictBool = Field(alias="isTransactionHistory")
    is_profile: StrictBool = Field(alias="isProfile")
    is_settings: StrictBool = Field(alias="isSettings")
    is_chat_room: StrictBool = Field(alias="isChatRoom")
    is_sms_opt_in: StrictBool = Field(alias="isSmsOptIn")
    sms_opt_in_source_id: Optional[WalletConfigurationSmsOptInSourceID] = Field(default=None, alias="smsOptInSourceID")
    is_email_subscriber: StrictBool = Field(alias="isEmailSubscriber")
    google_analytics_id: Optional[StrictStr] = Field(default=None, alias="googleAnalyticsID")
    facebook_pixel_id: Optional[StrictStr] = Field(default=None, alias="facebookPixelID")
    public_chat_room_channel_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="publicChatRoomChannelID")
    vanity_handle: Optional[StrictStr] = Field(default=None, alias="vanityHandle")
    vanity_page_wallet_prefix: Optional[StrictStr] = Field(default=None, alias="vanityPageWalletPrefix")
    merchant_credit_payment_design_id: Optional[StrictStr] = Field(default=None, alias="merchantCreditPaymentDesignID")
    custom_domain: Optional[StrictStr] = Field(default=None, alias="customDomain")
    is_claimed: Optional[StrictBool] = Field(default=None, alias="isClaimed")
    mobile_app_icon_url: Optional[StrictStr] = Field(default=None, alias="mobileAppIconURL")
    is_age_gate: Optional[StrictBool] = Field(default=None, alias="isAgeGate")
    age_gate_minimum: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ageGateMinimum")
    age_gate_decline_url: Optional[StrictStr] = Field(default=None, alias="ageGateDeclineURL")
    social_instagram_url: Optional[StrictStr] = Field(default=None, alias="socialInstagramURL")
    social_facebook_url: Optional[StrictStr] = Field(default=None, alias="socialFacebookURL")
    social_you_tube_url: Optional[StrictStr] = Field(default=None, alias="socialYouTubeURL")
    social_twitter_url: Optional[StrictStr] = Field(default=None, alias="socialTwitterURL")
    social_linked_in_url: Optional[StrictStr] = Field(default=None, alias="socialLinkedInURL")
    social_background_color: Optional[StrictStr] = Field(default=None, alias="socialBackgroundColor")
    social_font_color: Optional[StrictStr] = Field(default=None, alias="socialFontColor")
    primary_phone_number: Optional[StrictStr] = Field(default=None, alias="primaryPhoneNumber")
    primary_whats_app: Optional[StrictStr] = Field(default=None, alias="primaryWhatsApp")
    primary_email_address: Optional[StrictStr] = Field(default=None, alias="primaryEmailAddress")
    custom_js: Optional[StrictStr] = Field(default=None, alias="customJS")
    custom_css: Optional[StrictStr] = Field(default=None, alias="customCSS")
    non_mobile_redirect_url: Optional[StrictStr] = Field(default=None, alias="nonMobileRedirectURL")
    apple_app_store_url: Optional[StrictStr] = Field(default=None, alias="appleAppStoreURL")
    google_play_store_url: Optional[StrictStr] = Field(default=None, alias="googlePlayStoreURL")
    id: Annotated[str, Field(min_length=10, strict=True, max_length=10)]
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    merchant_id: Annotated[str, Field(min_length=10, strict=True, max_length=10)] = Field(alias="merchantID")
    __properties: ClassVar[List[str]] = ["headerBackgroundColor", "headerButtonColor", "leftMenuHeaderBackgroundColor", "leftMenuHeaderFontColor", "leftMenuSectionBackgroundColor", "leftMenuSectionFontColor", "companyLogoURL", "headerImageURL", "headerCustomIcon", "welcomeMessage", "isAppleEnabled", "isGoogleEnabled", "isSamsungEnabled", "isAdCredits", "isStaticVouchers", "isDynamicVouchers", "isMembershipTier", "isMembershipPoints", "isMembershipLevel", "isGiftCards", "isGiftCertificates", "isPromotions", "isMerchantCredit", "isTickets", "isNewsArticles", "isPerformances", "isMessages", "isCall", "isRepresentatives", "isProducts", "isServices", "isRoomRates", "isAmenities", "isGaming", "isDining", "isLounges", "isMapDirections", "isLinkBook", "isImageGrid", "isVideos", "isTransactionHistory", "isProfile", "isSettings", "isChatRoom", "isSmsOptIn", "smsOptInSourceID", "isEmailSubscriber", "googleAnalyticsID", "facebookPixelID", "publicChatRoomChannelID", "vanityHandle", "vanityPageWalletPrefix", "merchantCreditPaymentDesignID", "customDomain", "isClaimed", "mobileAppIconURL", "isAgeGate", "ageGateMinimum", "ageGateDeclineURL", "socialInstagramURL", "socialFacebookURL", "socialYouTubeURL", "socialTwitterURL", "socialLinkedInURL", "socialBackgroundColor", "socialFontColor", "primaryPhoneNumber", "primaryWhatsApp", "primaryEmailAddress", "customJS", "customCSS", "nonMobileRedirectURL", "appleAppStoreURL", "googlePlayStoreURL", "id", "createdAt", "updatedAt", "merchantID"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
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
        """Create an instance of WalletConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sms_opt_in_source_id
        if self.sms_opt_in_source_id:
            _dict['smsOptInSourceID'] = self.sms_opt_in_source_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WalletConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "headerBackgroundColor": obj.get("headerBackgroundColor"),
            "headerButtonColor": obj.get("headerButtonColor"),
            "leftMenuHeaderBackgroundColor": obj.get("leftMenuHeaderBackgroundColor"),
            "leftMenuHeaderFontColor": obj.get("leftMenuHeaderFontColor"),
            "leftMenuSectionBackgroundColor": obj.get("leftMenuSectionBackgroundColor"),
            "leftMenuSectionFontColor": obj.get("leftMenuSectionFontColor"),
            "companyLogoURL": obj.get("companyLogoURL"),
            "headerImageURL": obj.get("headerImageURL"),
            "headerCustomIcon": obj.get("headerCustomIcon"),
            "welcomeMessage": obj.get("welcomeMessage"),
            "isAppleEnabled": obj.get("isAppleEnabled"),
            "isGoogleEnabled": obj.get("isGoogleEnabled"),
            "isSamsungEnabled": obj.get("isSamsungEnabled"),
            "isAdCredits": obj.get("isAdCredits"),
            "isStaticVouchers": obj.get("isStaticVouchers"),
            "isDynamicVouchers": obj.get("isDynamicVouchers"),
            "isMembershipTier": obj.get("isMembershipTier"),
            "isMembershipPoints": obj.get("isMembershipPoints"),
            "isMembershipLevel": obj.get("isMembershipLevel"),
            "isGiftCards": obj.get("isGiftCards"),
            "isGiftCertificates": obj.get("isGiftCertificates"),
            "isPromotions": obj.get("isPromotions"),
            "isMerchantCredit": obj.get("isMerchantCredit"),
            "isTickets": obj.get("isTickets"),
            "isNewsArticles": obj.get("isNewsArticles"),
            "isPerformances": obj.get("isPerformances"),
            "isMessages": obj.get("isMessages"),
            "isCall": obj.get("isCall"),
            "isRepresentatives": obj.get("isRepresentatives"),
            "isProducts": obj.get("isProducts"),
            "isServices": obj.get("isServices"),
            "isRoomRates": obj.get("isRoomRates"),
            "isAmenities": obj.get("isAmenities"),
            "isGaming": obj.get("isGaming"),
            "isDining": obj.get("isDining"),
            "isLounges": obj.get("isLounges"),
            "isMapDirections": obj.get("isMapDirections"),
            "isLinkBook": obj.get("isLinkBook"),
            "isImageGrid": obj.get("isImageGrid"),
            "isVideos": obj.get("isVideos"),
            "isTransactionHistory": obj.get("isTransactionHistory"),
            "isProfile": obj.get("isProfile"),
            "isSettings": obj.get("isSettings"),
            "isChatRoom": obj.get("isChatRoom"),
            "isSmsOptIn": obj.get("isSmsOptIn"),
            "smsOptInSourceID": WalletConfigurationSmsOptInSourceID.from_dict(obj["smsOptInSourceID"]) if obj.get("smsOptInSourceID") is not None else None,
            "isEmailSubscriber": obj.get("isEmailSubscriber"),
            "googleAnalyticsID": obj.get("googleAnalyticsID"),
            "facebookPixelID": obj.get("facebookPixelID"),
            "publicChatRoomChannelID": obj.get("publicChatRoomChannelID"),
            "vanityHandle": obj.get("vanityHandle"),
            "vanityPageWalletPrefix": obj.get("vanityPageWalletPrefix"),
            "merchantCreditPaymentDesignID": obj.get("merchantCreditPaymentDesignID"),
            "customDomain": obj.get("customDomain"),
            "isClaimed": obj.get("isClaimed"),
            "mobileAppIconURL": obj.get("mobileAppIconURL"),
            "isAgeGate": obj.get("isAgeGate"),
            "ageGateMinimum": obj.get("ageGateMinimum"),
            "ageGateDeclineURL": obj.get("ageGateDeclineURL"),
            "socialInstagramURL": obj.get("socialInstagramURL"),
            "socialFacebookURL": obj.get("socialFacebookURL"),
            "socialYouTubeURL": obj.get("socialYouTubeURL"),
            "socialTwitterURL": obj.get("socialTwitterURL"),
            "socialLinkedInURL": obj.get("socialLinkedInURL"),
            "socialBackgroundColor": obj.get("socialBackgroundColor"),
            "socialFontColor": obj.get("socialFontColor"),
            "primaryPhoneNumber": obj.get("primaryPhoneNumber"),
            "primaryWhatsApp": obj.get("primaryWhatsApp"),
            "primaryEmailAddress": obj.get("primaryEmailAddress"),
            "customJS": obj.get("customJS"),
            "customCSS": obj.get("customCSS"),
            "nonMobileRedirectURL": obj.get("nonMobileRedirectURL"),
            "appleAppStoreURL": obj.get("appleAppStoreURL"),
            "googlePlayStoreURL": obj.get("googlePlayStoreURL"),
            "id": obj.get("id"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "merchantID": obj.get("merchantID")
        })
        return _obj


