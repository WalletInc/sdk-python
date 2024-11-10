# WTWalletConfigurationSaveWalletRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_background_color** | **str** |  | 
**header_button_color** | **str** |  | 
**left_menu_header_background_color** | **str** |  | 
**left_menu_header_font_color** | **str** |  | 
**left_menu_section_background_color** | **str** |  | 
**left_menu_section_font_color** | **str** |  | 
**company_logo_url** | **str** |  | 
**header_image_url** | **str** |  | [optional] 
**header_custom_icon** | **str** |  | [optional] 
**welcome_message** | **str** |  | 
**is_apple_enabled** | **bool** |  | 
**is_google_enabled** | **bool** |  | 
**is_samsung_enabled** | **bool** |  | 
**is_ad_credits** | **bool** |  | 
**is_static_vouchers** | **bool** |  | 
**is_dynamic_vouchers** | **bool** |  | 
**is_membership_tier** | **bool** |  | 
**is_membership_points** | **bool** |  | 
**is_membership_level** | **bool** |  | 
**is_gift_cards** | **bool** |  | 
**is_gift_certificates** | **bool** |  | 
**is_promotions** | **bool** |  | 
**is_merchant_credit** | **bool** |  | 
**is_tickets** | **bool** |  | [optional] 
**is_news_articles** | **bool** |  | 
**is_performances** | **bool** |  | 
**is_messages** | **bool** |  | 
**is_call** | **bool** |  | 
**is_representatives** | **bool** |  | 
**is_products** | **bool** |  | 
**is_services** | **bool** |  | 
**is_room_rates** | **bool** |  | 
**is_amenities** | **bool** |  | 
**is_gaming** | **bool** |  | 
**is_dining** | **bool** |  | 
**is_lounges** | **bool** |  | 
**is_map_directions** | **bool** |  | 
**is_link_book** | **bool** |  | 
**is_image_grid** | **bool** |  | 
**is_videos** | **bool** |  | 
**is_transaction_history** | **bool** |  | 
**is_profile** | **bool** |  | 
**is_settings** | **bool** |  | 
**is_chat_room** | **bool** |  | 
**is_sms_opt_in** | **bool** |  | 
**sms_opt_in_source_id** | [**WalletConfigurationSmsOptInSourceID**](WalletConfigurationSmsOptInSourceID.md) |  | [optional] 
**is_email_subscriber** | **bool** |  | 
**google_analytics_id** | **str** |  | [optional] 
**facebook_pixel_id** | **str** |  | [optional] 
**public_chat_room_channel_id** | **float** |  | [optional] 
**vanity_handle** | **str** |  | [optional] 
**vanity_page_wallet_prefix** | **str** |  | [optional] 
**merchant_credit_payment_design_id** | **str** |  | [optional] 
**custom_domain** | **str** |  | [optional] 
**is_claimed** | **bool** |  | [optional] 
**mobile_app_icon_url** | **str** |  | [optional] 
**is_age_gate** | **bool** |  | [optional] 
**age_gate_minimum** | **float** |  | [optional] 
**age_gate_decline_url** | **str** |  | [optional] 
**social_instagram_url** | **str** |  | [optional] 
**social_facebook_url** | **str** |  | [optional] 
**social_you_tube_url** | **str** |  | [optional] 
**social_twitter_url** | **str** |  | [optional] 
**social_linked_in_url** | **str** |  | [optional] 
**social_background_color** | **str** |  | [optional] 
**social_font_color** | **str** |  | [optional] 
**primary_phone_number** | **str** |  | [optional] 
**primary_whats_app** | **str** |  | [optional] 
**primary_email_address** | **str** |  | [optional] 
**custom_js** | **str** |  | [optional] 
**custom_css** | **str** |  | [optional] 
**non_mobile_redirect_url** | **str** |  | [optional] 
**apple_app_store_url** | **str** |  | [optional] 
**google_play_store_url** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_wallet_configuration_save_wallet_record import WTWalletConfigurationSaveWalletRecord

# TODO update the JSON string below
json = "{}"
# create an instance of WTWalletConfigurationSaveWalletRecord from a JSON string
wt_wallet_configuration_save_wallet_record_instance = WTWalletConfigurationSaveWalletRecord.from_json(json)
# print the JSON string representation of the object
print WTWalletConfigurationSaveWalletRecord.to_json()

# convert the object into a dict
wt_wallet_configuration_save_wallet_record_dict = wt_wallet_configuration_save_wallet_record_instance.to_dict()
# create an instance of WTWalletConfigurationSaveWalletRecord from a dict
wt_wallet_configuration_save_wallet_record_form_dict = wt_wallet_configuration_save_wallet_record.from_dict(wt_wallet_configuration_save_wallet_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


