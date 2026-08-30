# WTPublicVanityPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**vanity_page_wallet_prefix** | **str** |  | [optional] 
**company_logo_url** | **str** |  | [optional] 
**header_background_color** | **str** |  | [optional] 
**mobile_app_icon_url** | **str** |  | [optional] 
**android_sha256_fingerprint** | **object** |  | [optional] 
**is_call** | **bool** |  | [optional] 
**is_promotions** | **bool** |  | [optional] 
**is_news_articles** | **bool** |  | [optional] 
**is_performances** | **bool** |  | [optional] 
**is_representatives** | **bool** |  | [optional] 
**is_products** | **bool** |  | [optional] 
**is_services** | **bool** |  | [optional] 
**is_room_rates** | **bool** |  | [optional] 
**is_amenities** | **bool** |  | [optional] 
**is_gaming** | **bool** |  | [optional] 
**is_dining** | **bool** |  | [optional] 
**is_lounges** | **bool** |  | [optional] 
**is_link_book** | **bool** |  | [optional] 
**is_image_grid** | **bool** |  | [optional] 
**merchant** | [**WTPublicVanityPageMerchant**](WTPublicVanityPageMerchant.md) | Whitelisted slice of the attached Merchant: only id + companyName, never the full PII record. | [optional] 

## Example

```python
from wallet.models.wt_public_vanity_page import WTPublicVanityPage

# TODO update the JSON string below
json = "{}"
# create an instance of WTPublicVanityPage from a JSON string
wt_public_vanity_page_instance = WTPublicVanityPage.from_json(json)
# print the JSON string representation of the object
print WTPublicVanityPage.to_json()

# convert the object into a dict
wt_public_vanity_page_dict = wt_public_vanity_page_instance.to_dict()
# create an instance of WTPublicVanityPage from a dict
wt_public_vanity_page_form_dict = wt_public_vanity_page.from_dict(wt_public_vanity_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


