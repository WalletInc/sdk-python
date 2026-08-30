# WTGuestCreatePaymentIntentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_verification_token** | **object** |  | 
**object_id** | **object** |  | 
**credit_id** | **object** |  | [optional] 
**tip_cents** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_guest_create_payment_intent_request import WTGuestCreatePaymentIntentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTGuestCreatePaymentIntentRequest from a JSON string
wt_guest_create_payment_intent_request_instance = WTGuestCreatePaymentIntentRequest.from_json(json)
# print the JSON string representation of the object
print WTGuestCreatePaymentIntentRequest.to_json()

# convert the object into a dict
wt_guest_create_payment_intent_request_dict = wt_guest_create_payment_intent_request_instance.to_dict()
# create an instance of WTGuestCreatePaymentIntentRequest from a dict
wt_guest_create_payment_intent_request_form_dict = wt_guest_create_payment_intent_request.from_dict(wt_guest_create_payment_intent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


