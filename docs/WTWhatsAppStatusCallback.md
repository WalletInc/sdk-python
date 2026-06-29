# WTWhatsAppStatusCallback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sms_sid** | **str** |  | 
**sms_status** | **str** |  | 
**message_status** | **str** |  | 
**to** | **str** |  | 
**message_sid** | **str** |  | 
**account_sid** | **str** |  | 
**var_from** | **str** |  | 
**api_version** | **str** |  | 
**num_media** | **object** |  | [optional] 
**error_code** | **object** |  | [optional] 
**error_message** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_whats_app_status_callback import WTWhatsAppStatusCallback

# TODO update the JSON string below
json = "{}"
# create an instance of WTWhatsAppStatusCallback from a JSON string
wt_whats_app_status_callback_instance = WTWhatsAppStatusCallback.from_json(json)
# print the JSON string representation of the object
print WTWhatsAppStatusCallback.to_json()

# convert the object into a dict
wt_whats_app_status_callback_dict = wt_whats_app_status_callback_instance.to_dict()
# create an instance of WTWhatsAppStatusCallback from a dict
wt_whats_app_status_callback_form_dict = wt_whats_app_status_callback.from_dict(wt_whats_app_status_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


