# WTMerchantCredit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** | The timestamp of when this resource was created | 
**updated_at** | **datetime** | The timestamp of when this resource was updated | 
**is_active** | **bool** | Denotes if this resource is active | 
**mobile_number** | **str** |  | 
**credit_amount** | **int** | The amount that needs to be credited to the member | 
**member_id** | **str** | MerchantCredit ID as represented by the merchant | [optional] 
**credit_amount_decimal** | **str** | The amount that needs to be credited to the member (fixed to 2 decimals) | 
**credit_amount_string** | **str** | The amount that needs to be credited to the member (in string) | 

## Example

```python
from wallet.models.wt_merchant_credit import WTMerchantCredit

# TODO update the JSON string below
json = "{}"
# create an instance of WTMerchantCredit from a JSON string
wt_merchant_credit_instance = WTMerchantCredit.from_json(json)
# print the JSON string representation of the object
print WTMerchantCredit.to_json()

# convert the object into a dict
wt_merchant_credit_dict = wt_merchant_credit_instance.to_dict()
# create an instance of WTMerchantCredit from a dict
wt_merchant_credit_form_dict = wt_merchant_credit.from_dict(wt_merchant_credit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


