# PhoneNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_footer** | **object** |  | 
**help_response** | **object** |  | 
**stop_response** | **object** |  | 
**company_name** | **object** |  | 
**privacy_policy_url** | **object** |  | 
**terms_of_service_url** | **object** |  | 
**help_desk_keyword** | **object** |  | 
**help_desk_queue_response** | **object** |  | 
**is_connected_to_watson** | **object** |  | 
**watson_conversation_workplace_id** | **object** |  | 
**watson_username** | **object** |  | 
**watson_password** | **object** |  | 
**mobile_number** | **object** |  | 
**is_short_code** | **object** |  | 
**twilio_sid** | **object** |  | 
**twilio_account_sid** | **object** |  | 
**id** | [**StaticVoucherId**](StaticVoucherId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**is_approved** | **object** |  | 

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


