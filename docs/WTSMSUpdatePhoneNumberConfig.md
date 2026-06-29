# WTSMSUpdatePhoneNumberConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **object** |  | 
**privacy_policy_url** | **object** |  | [optional] 
**terms_of_service_url** | **object** |  | [optional] 
**message_footer** | **object** |  | 
**stop_response** | **object** |  | 
**help_response** | **object** |  | 
**help_desk_keyword** | **object** |  | 
**help_desk_queue_response** | **object** |  | 
**is_connected_to_watson** | **object** |  | [optional] 
**watson_username** | **object** |  | [optional] 
**watson_password** | **object** |  | [optional] 
**watson_conversation_workplace_id** | **object** |  | [optional] 

## Example

```python
from wallet.models.wtsms_update_phone_number_config import WTSMSUpdatePhoneNumberConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WTSMSUpdatePhoneNumberConfig from a JSON string
wtsms_update_phone_number_config_instance = WTSMSUpdatePhoneNumberConfig.from_json(json)
# print the JSON string representation of the object
print WTSMSUpdatePhoneNumberConfig.to_json()

# convert the object into a dict
wtsms_update_phone_number_config_dict = wtsms_update_phone_number_config_instance.to_dict()
# create an instance of WTSMSUpdatePhoneNumberConfig from a dict
wtsms_update_phone_number_config_form_dict = wtsms_update_phone_number_config.from_dict(wtsms_update_phone_number_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


