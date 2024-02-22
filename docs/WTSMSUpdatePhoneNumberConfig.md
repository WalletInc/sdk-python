# WTSMSUpdatePhoneNumberConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** |  | 
**privacy_policy_url** | **str** |  | [optional] 
**terms_of_service_url** | **str** |  | [optional] 
**message_footer** | **str** |  | 
**stop_response** | **str** |  | 
**help_response** | **str** |  | 
**help_desk_keyword** | **str** |  | 
**help_desk_queue_response** | **str** |  | 
**is_connected_to_watson** | **bool** |  | [optional] 
**watson_username** | **str** |  | [optional] 
**watson_password** | **str** |  | [optional] 
**watson_conversation_workplace_id** | **str** |  | [optional] 

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


