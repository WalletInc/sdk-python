# MSMerchantCreditHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_identifier** | **str** | Optional Member ID as represented by the merchant | [optional] 
**mobile_number** | **str** |  | 
**credit_amount** | **int** | The amount that needs to be credited to the member | 
**id** | **str** | The UUID of this record | 
**merchant_credit_id** | **str** |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** | The timestamp of when this resource was created | 
**is_active** | **bool** | Denotes if this resource is active | 

## Example

```python
from wallet.models.ms_merchant_credit_history import MSMerchantCreditHistory

# TODO update the JSON string below
json = "{}"
# create an instance of MSMerchantCreditHistory from a JSON string
ms_merchant_credit_history_instance = MSMerchantCreditHistory.from_json(json)
# print the JSON string representation of the object
print MSMerchantCreditHistory.to_json()

# convert the object into a dict
ms_merchant_credit_history_dict = ms_merchant_credit_history_instance.to_dict()
# create an instance of MSMerchantCreditHistory from a dict
ms_merchant_credit_history_form_dict = ms_merchant_credit_history.from_dict(ms_merchant_credit_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


