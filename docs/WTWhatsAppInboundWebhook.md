# WTWhatsAppInboundWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sms_message_sid** | **str** |  | 
**num_media** | **object** |  | 
**profile_name** | **str** |  | 
**sms_sid** | **str** |  | 
**wa_id** | **str** |  | 
**sms_status** | **str** |  | 
**body** | **str** |  | 
**to** | **str** |  | 
**num_segments** | **object** |  | 
**message_sid** | **str** |  | 
**account_sid** | **str** |  | 
**var_from** | **str** |  | 
**api_version** | **str** |  | 
**media_urls** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_whats_app_inbound_webhook import WTWhatsAppInboundWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of WTWhatsAppInboundWebhook from a JSON string
wt_whats_app_inbound_webhook_instance = WTWhatsAppInboundWebhook.from_json(json)
# print the JSON string representation of the object
print WTWhatsAppInboundWebhook.to_json()

# convert the object into a dict
wt_whats_app_inbound_webhook_dict = wt_whats_app_inbound_webhook_instance.to_dict()
# create an instance of WTWhatsAppInboundWebhook from a dict
wt_whats_app_inbound_webhook_form_dict = wt_whats_app_inbound_webhook.from_dict(wt_whats_app_inbound_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


