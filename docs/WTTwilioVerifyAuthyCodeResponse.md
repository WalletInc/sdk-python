# WTTwilioVerifyAuthyCodeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | [optional] 
**token** | **str** |  | 
**chat_user_id** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_twilio_verify_authy_code_response import WTTwilioVerifyAuthyCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WTTwilioVerifyAuthyCodeResponse from a JSON string
wt_twilio_verify_authy_code_response_instance = WTTwilioVerifyAuthyCodeResponse.from_json(json)
# print the JSON string representation of the object
print WTTwilioVerifyAuthyCodeResponse.to_json()

# convert the object into a dict
wt_twilio_verify_authy_code_response_dict = wt_twilio_verify_authy_code_response_instance.to_dict()
# create an instance of WTTwilioVerifyAuthyCodeResponse from a dict
wt_twilio_verify_authy_code_response_form_dict = wt_twilio_verify_authy_code_response.from_dict(wt_twilio_verify_authy_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


