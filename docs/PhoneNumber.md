# PhoneNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_footer** | **str** |  | 
**help_response** | **str** |  | 
**stop_response** | **str** |  | 
**company_name** | **str** |  | 
**privacy_policy_url** | **str** |  | 
**terms_of_service_url** | **str** |  | 
**help_desk_keyword** | **str** |  | 
**help_desk_queue_response** | **str** |  | 
**is_connected_to_watson** | **bool** |  | 
**watson_conversation_workplace_id** | **str** |  | 
**watson_username** | **str** |  | 
**watson_password** | **str** |  | 
**mobile_number** | **str** |  | 
**is_short_code** | **bool** |  | 
**twilio_sid** | **str** |  | 
**twilio_account_sid** | **str** |  | 
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**is_approved** | **bool** |  | 

## Example

```python
from wallet.models.phone_number import PhoneNumber

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumber from a JSON string
phone_number_instance = PhoneNumber.from_json(json)
# print the JSON string representation of the object
print PhoneNumber.to_json()

# convert the object into a dict
phone_number_dict = phone_number_instance.to_dict()
# create an instance of PhoneNumber from a dict
phone_number_form_dict = phone_number.from_dict(phone_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


