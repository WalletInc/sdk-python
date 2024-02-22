# InboundSMS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
**automated_reply** | **str** |  | 
**automated_reply_additional_info** | **str** |  | 
**sms_sid** | **str** |  | 
**sms_message_sid** | **str** |  | 
**sms_status** | **str** |  | 
**messaging_service_sid** | **str** |  | [optional] 
**account_sid** | **str** |  | 
**message_sid** | **str** |  | 
**body** | **str** |  | 
**num_segments** | **int** |  | 
**to** | **str** |  | 
**to_city** | **str** |  | 
**to_state** | **str** |  | 
**to_zip** | **str** |  | 
**to_country** | **str** |  | 
**var_from** | **str** |  | 
**from_city** | **str** |  | 
**from_state** | **str** |  | 
**from_zip** | **str** |  | 
**from_country** | **str** |  | 
**media_urls** | **List[str]** |  | [optional] 
**watson_intent** | **str** |  | [optional] 
**watson_intents** | **str** |  | [optional] 
**watson_context** | **str** |  | [optional] 
**watson_contexts** | **str** |  | [optional] 
**num_media** | **int** |  | 
**api_version** | **str** |  | 
**is_opt_in** | **bool** |  | [optional] 
**is_help_desk_request** | **bool** |  | [optional] 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**body_lowercase** | **str** |  | 
**from_localized** | **str** |  | 

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


