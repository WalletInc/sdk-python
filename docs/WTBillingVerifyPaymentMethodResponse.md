# WTBillingVerifyPaymentMethodResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_payment_method_provided** | **bool** |  | 
**subscription** | [**SubscriptionPlan**](SubscriptionPlan.md) |  | 

## Example

```python
from wallet.models.wt_billing_verify_payment_method_response import WTBillingVerifyPaymentMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WTBillingVerifyPaymentMethodResponse from a JSON string
wt_billing_verify_payment_method_response_instance = WTBillingVerifyPaymentMethodResponse.from_json(json)
# print the JSON string representation of the object
print WTBillingVerifyPaymentMethodResponse.to_json()

# convert the object into a dict
wt_billing_verify_payment_method_response_dict = wt_billing_verify_payment_method_response_instance.to_dict()
# create an instance of WTBillingVerifyPaymentMethodResponse from a dict
wt_billing_verify_payment_method_response_form_dict = wt_billing_verify_payment_method_response.from_dict(wt_billing_verify_payment_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


