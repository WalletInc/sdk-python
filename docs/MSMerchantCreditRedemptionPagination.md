# MSMerchantCreditRedemptionPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[MSMerchantCreditRedemption]**](MSMerchantCreditRedemption.md) | Stores the results as an array | 
**length** | **int** | Denotes the length of the results array | 
**total** | **int** | Denotes the total number of records present in the database | 

## Example

```python
from wallet.models.ms_merchant_credit_redemption_pagination import MSMerchantCreditRedemptionPagination

# TODO update the JSON string below
json = "{}"
# create an instance of MSMerchantCreditRedemptionPagination from a JSON string
ms_merchant_credit_redemption_pagination_instance = MSMerchantCreditRedemptionPagination.from_json(json)
# print the JSON string representation of the object
print MSMerchantCreditRedemptionPagination.to_json()

# convert the object into a dict
ms_merchant_credit_redemption_pagination_dict = ms_merchant_credit_redemption_pagination_instance.to_dict()
# create an instance of MSMerchantCreditRedemptionPagination from a dict
ms_merchant_credit_redemption_pagination_form_dict = ms_merchant_credit_redemption_pagination.from_dict(ms_merchant_credit_redemption_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


