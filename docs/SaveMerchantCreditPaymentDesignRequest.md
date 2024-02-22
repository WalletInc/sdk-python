# SaveMerchantCreditPaymentDesignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_design_id** | **str** |  | 

## Example

```python
from wallet.models.save_merchant_credit_payment_design_request import SaveMerchantCreditPaymentDesignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveMerchantCreditPaymentDesignRequest from a JSON string
save_merchant_credit_payment_design_request_instance = SaveMerchantCreditPaymentDesignRequest.from_json(json)
# print the JSON string representation of the object
print SaveMerchantCreditPaymentDesignRequest.to_json()

# convert the object into a dict
save_merchant_credit_payment_design_request_dict = save_merchant_credit_payment_design_request_instance.to_dict()
# create an instance of SaveMerchantCreditPaymentDesignRequest from a dict
save_merchant_credit_payment_design_request_form_dict = save_merchant_credit_payment_design_request.from_dict(save_merchant_credit_payment_design_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


