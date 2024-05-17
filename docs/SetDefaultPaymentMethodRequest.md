# SetDefaultPaymentMethodRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_id** | **str** |  | 

## Example

```python
from wallet.models.set_default_payment_method_request import SetDefaultPaymentMethodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDefaultPaymentMethodRequest from a JSON string
set_default_payment_method_request_instance = SetDefaultPaymentMethodRequest.from_json(json)
# print the JSON string representation of the object
print SetDefaultPaymentMethodRequest.to_json()

# convert the object into a dict
set_default_payment_method_request_dict = set_default_payment_method_request_instance.to_dict()
# create an instance of SetDefaultPaymentMethodRequest from a dict
set_default_payment_method_request_form_dict = set_default_payment_method_request.from_dict(set_default_payment_method_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


