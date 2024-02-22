# WTBillingSavePaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_id** | **str** |  | 

## Example

```python
from wallet.models.wt_billing_save_payment_method import WTBillingSavePaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of WTBillingSavePaymentMethod from a JSON string
wt_billing_save_payment_method_instance = WTBillingSavePaymentMethod.from_json(json)
# print the JSON string representation of the object
print WTBillingSavePaymentMethod.to_json()

# convert the object into a dict
wt_billing_save_payment_method_dict = wt_billing_save_payment_method_instance.to_dict()
# create an instance of WTBillingSavePaymentMethod from a dict
wt_billing_save_payment_method_form_dict = wt_billing_save_payment_method.from_dict(wt_billing_save_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


