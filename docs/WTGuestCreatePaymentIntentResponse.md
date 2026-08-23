# WTGuestCreatePaymentIntentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **object** |  | 
**reservation_id** | **object** |  | 
**charge_model** | **object** |  | 
**currency** | **object** |  | 
**client_secret** | **object** |  | 
**payment_intent_id** | **object** |  | 
**connected_account_id** | **object** |  | 
**publishable_key** | **object** |  | 
**amount_breakdown** | [**WTGuestAmountBreakdown**](WTGuestAmountBreakdown.md) |  | 

## Example

```python
from wallet.models.wt_guest_create_payment_intent_response import WTGuestCreatePaymentIntentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WTGuestCreatePaymentIntentResponse from a JSON string
wt_guest_create_payment_intent_response_instance = WTGuestCreatePaymentIntentResponse.from_json(json)
# print the JSON string representation of the object
print WTGuestCreatePaymentIntentResponse.to_json()

# convert the object into a dict
wt_guest_create_payment_intent_response_dict = wt_guest_create_payment_intent_response_instance.to_dict()
# create an instance of WTGuestCreatePaymentIntentResponse from a dict
wt_guest_create_payment_intent_response_form_dict = wt_guest_create_payment_intent_response.from_dict(wt_guest_create_payment_intent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


