# InboundSMS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**StaticVoucherId**](StaticVoucherId.md) |  | 
**automated_reply** | **object** |  | 
**automated_reply_additional_info** | **object** |  | 
**sms_sid** | **object** |  | 
**sms_message_sid** | **object** |  | 
**sms_status** | **object** |  | 
**messaging_service_sid** | **object** |  | [optional] 
**account_sid** | **object** |  | 
**message_sid** | **object** |  | 
**body** | **object** |  | 
**num_segments** | **object** |  | 
**to** | **object** |  | 
**to_city** | **object** |  | 
**to_state** | **object** |  | 
**to_zip** | **object** |  | 
**to_country** | **object** |  | 
**var_from** | **object** |  | 
**from_city** | **object** |  | 
**from_state** | **object** |  | 
**from_zip** | **object** |  | 
**from_country** | **object** |  | 
**media_urls** | **object** |  | [optional] 
**watson_intent** | **object** |  | [optional] 
**watson_intents** | **object** |  | [optional] 
**watson_context** | **object** |  | [optional] 
**watson_contexts** | **object** |  | [optional] 
**num_media** | **object** |  | 
**api_version** | **object** |  | 
**is_opt_in** | **object** |  | [optional] 
**is_help_desk_request** | **object** |  | [optional] 
**merchant_id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**body_lowercase** | **object** |  | 
**from_localized** | **object** |  | 

## Example

```python
from wallet.models.inbound_sms import InboundSMS

# TODO update the JSON string below
json = "{}"
# create an instance of InboundSMS from a JSON string
inbound_sms_instance = InboundSMS.from_json(json)
# print the JSON string representation of the object
print InboundSMS.to_json()

# convert the object into a dict
inbound_sms_dict = inbound_sms_instance.to_dict()
# create an instance of InboundSMS from a dict
inbound_sms_form_dict = inbound_sms.from_dict(inbound_sms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


