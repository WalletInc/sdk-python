# WTStaticVoucherCampaignPreviewMessagesByPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**locale** | **str** |  | 
**timezone** | **str** |  | 
**page_num** | **float** |  | 
**page_size** | **float** |  | 

## Example

```python
from wallet.models.wt_static_voucher_campaign_preview_messages_by_page import WTStaticVoucherCampaignPreviewMessagesByPage

# TODO update the JSON string below
json = "{}"
# create an instance of WTStaticVoucherCampaignPreviewMessagesByPage from a JSON string
wt_static_voucher_campaign_preview_messages_by_page_instance = WTStaticVoucherCampaignPreviewMessagesByPage.from_json(json)
# print the JSON string representation of the object
print WTStaticVoucherCampaignPreviewMessagesByPage.to_json()

# convert the object into a dict
wt_static_voucher_campaign_preview_messages_by_page_dict = wt_static_voucher_campaign_preview_messages_by_page_instance.to_dict()
# create an instance of WTStaticVoucherCampaignPreviewMessagesByPage from a dict
wt_static_voucher_campaign_preview_messages_by_page_form_dict = wt_static_voucher_campaign_preview_messages_by_page.from_dict(wt_static_voucher_campaign_preview_messages_by_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


