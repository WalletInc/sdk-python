# PaginatedWTMerchantCredits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[WTMerchantCredit]**](WTMerchantCredit.md) | Stores the results as an array | 
**length** | **int** | Denotes the length of the results array | 
**total** | **int** | Denotes the total number of records present in the database | 

## Example

```python
from wallet.models.paginated_wt_merchant_credits import PaginatedWTMerchantCredits

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedWTMerchantCredits from a JSON string
paginated_wt_merchant_credits_instance = PaginatedWTMerchantCredits.from_json(json)
# print the JSON string representation of the object
print PaginatedWTMerchantCredits.to_json()

# convert the object into a dict
paginated_wt_merchant_credits_dict = paginated_wt_merchant_credits_instance.to_dict()
# create an instance of PaginatedWTMerchantCredits from a dict
paginated_wt_merchant_credits_form_dict = paginated_wt_merchant_credits.from_dict(paginated_wt_merchant_credits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


