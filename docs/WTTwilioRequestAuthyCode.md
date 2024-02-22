# WTTwilioRequestAuthyCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | 
**phone_number** | **str** |  | 

## Example

```python
from wallet.models.wt_twilio_request_authy_code import WTTwilioRequestAuthyCode

# TODO update the JSON string below
json = "{}"
# create an instance of WTTwilioRequestAuthyCode from a JSON string
wt_twilio_request_authy_code_instance = WTTwilioRequestAuthyCode.from_json(json)
# print the JSON string representation of the object
print WTTwilioRequestAuthyCode.to_json()

# convert the object into a dict
wt_twilio_request_authy_code_dict = wt_twilio_request_authy_code_instance.to_dict()
# create an instance of WTTwilioRequestAuthyCode from a dict
wt_twilio_request_authy_code_form_dict = wt_twilio_request_authy_code.from_dict(wt_twilio_request_authy_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


