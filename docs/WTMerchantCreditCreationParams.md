# WTMerchantCreditCreationParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile_number** | **str** |  | 
**credit_amount** | **int** | The amount that needs to be credited to the member | 
**member_id** | **str** | MerchantCredit ID as represented by the merchant | [optional] 

## Example

```python
from wallet.models.wt_merchant_credit_creation_params import WTMerchantCreditCreationParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTMerchantCreditCreationParams from a JSON string
wt_merchant_credit_creation_params_instance = WTMerchantCreditCreationParams.from_json(json)
# print the JSON string representation of the object
print WTMerchantCreditCreationParams.to_json()

# convert the object into a dict
wt_merchant_credit_creation_params_dict = wt_merchant_credit_creation_params_instance.to_dict()
# create an instance of WTMerchantCreditCreationParams from a dict
wt_merchant_credit_creation_params_form_dict = wt_merchant_credit_creation_params.from_dict(wt_merchant_credit_creation_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


