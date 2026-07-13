# WalletConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_background_color** | **object** |  | 
**header_button_color** | **object** |  | 
**left_menu_header_background_color** | **object** |  | 
**left_menu_header_font_color** | **object** |  | 
**left_menu_section_background_color** | **object** |  | 
**left_menu_section_font_color** | **object** |  | 
**company_logo_url** | **object** |  | 
**header_image_url** | **object** |  | [optional] 
**header_custom_icon** | **object** |  | [optional] 
**welcome_message** | **object** |  | 
**is_apple_enabled** | **object** |  | 
**is_google_enabled** | **object** |  | 
**is_samsung_enabled** | **object** |  | 
**is_ad_credits** | **object** |  | 
**is_static_vouchers** | **object** |  | 
**is_dynamic_vouchers** | **object** |  | 
**is_membership_tier** | **object** |  | 
**is_membership_points** | **object** |  | 
**is_membership_level** | **object** |  | 
**is_gift_cards** | **object** |  | 
**is_gift_certificates** | **object** |  | 
**is_promotions** | **object** |  | 
**is_merchant_credit** | **object** |  | 
**is_tickets** | **object** |  | [optional] 
**is_news_articles** | **object** |  | 
**is_performances** | **object** |  | 
**is_messages** | **object** |  | 
**is_call** | **object** |  | 
**is_representatives** | **object** |  | 
**is_products** | **object** |  | 
**is_services** | **object** |  | 
**is_room_rates** | **object** |  | 
**is_amenities** | **object** |  | 
**is_gaming** | **object** |  | 
**is_dining** | **object** |  | 
**is_lounges** | **object** |  | 
**is_map_directions** | **object** |  | 
**is_link_book** | **object** |  | 
**is_image_grid** | **object** |  | 
**is_videos** | **object** |  | 
**is_transaction_history** | **object** |  | 
**is_profile** | **object** |  | 
**is_settings** | **object** |  | 
**is_chat_room** | **object** |  | 
**is_sms_opt_in** | **object** |  | 
**sms_opt_in_source_id** | [**WTWalletConfigurationSaveWalletRecordSmsOptInSourceID**](WTWalletConfigurationSaveWalletRecordSmsOptInSourceID.md) |  | [optional] 
**is_email_subscriber** | **object** |  | 
**google_analytics_id** | **object** |  | [optional] 
**facebook_pixel_id** | **object** |  | [optional] 
**public_chat_room_channel_id** | **object** |  | [optional] 
**vanity_handle** | **object** |  | [optional] 
**vanity_page_wallet_prefix** | **object** |  | [optional] 
**merchant_credit_payment_design_id** | **object** |  | [optional] 
**custom_domain** | **object** |  | [optional] 
**is_claimed** | **object** |  | [optional] 
**mobile_app_icon_url** | **object** |  | [optional] 
**is_age_gate** | **object** |  | [optional] 
**is_flip_required_for_qr** | **object** |  | [optional] 
**age_gate_minimum** | **object** |  | [optional] 
**age_gate_decline_url** | **object** |  | [optional] 
**social_instagram_url** | **object** |  | [optional] 
**social_facebook_url** | **object** |  | [optional] 
**social_you_tube_url** | **object** |  | [optional] 
**social_twitter_url** | **object** |  | [optional] 
**social_linked_in_url** | **object** |  | [optional] 
**social_background_color** | **object** |  | [optional] 
**social_font_color** | **object** |  | [optional] 
**primary_phone_number** | **object** |  | [optional] 
**primary_whats_app** | **object** |  | [optional] 
**primary_email_address** | **object** |  | [optional] 
**custom_js** | **object** |  | [optional] 
**custom_css** | **object** |  | [optional] 
**non_mobile_redirect_url** | **object** |  | [optional] 
**apple_app_store_url** | **object** |  | [optional] 
**google_play_store_url** | **object** |  | [optional] 
**pass_brand_kit** | [**WTWalletConfigurationSaveWalletRecordPassBrandKit**](WTWalletConfigurationSaveWalletRecordPassBrandKit.md) |  | [optional] 
**id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**merchant_id** | **str** |  | 
**android_sha256_fingerprint** | **object** | SHA-256 fingerprint of the merchant&#39;s Android signing certificate, in Android&#39;s colon-separated uppercase hex format (e.g. \&quot;A1:B2:C3:...\&quot;). Populated by the POST /v2/wallet/android/keystore endpoint and consumed by the assetlinks.json endpoint so Google can verify the merchant&#39;s TWA ownership. | [optional] 

## Example

```python
from wallet.models.wallet_configuration import WalletConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of WalletConfiguration from a JSON string
wallet_configuration_instance = WalletConfiguration.from_json(json)
# print the JSON string representation of the object
print WalletConfiguration.to_json()

# convert the object into a dict
wallet_configuration_dict = wallet_configuration_instance.to_dict()
# create an instance of WalletConfiguration from a dict
wallet_configuration_form_dict = wallet_configuration.from_dict(wallet_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


