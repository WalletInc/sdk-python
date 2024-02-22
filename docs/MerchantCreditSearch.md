# MerchantCreditSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_archive_included** | **bool** | Denotes if archived records should be included in the response payload | [optional] 
**page_size** | **int** | Denotes the number of records per page | [optional] 
**page_num** | **int** | Denotes the page number | [optional] 
**key** | **str** | The search key to be used | 

## Example

```python
from wallet.models.merchant_credit_search import MerchantCreditSearch

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantCreditSearch from a JSON string
merchant_credit_search_instance = MerchantCreditSearch.from_json(json)
# print the JSON string representation of the object
print MerchantCreditSearch.to_json()

# convert the object into a dict
merchant_credit_search_dict = merchant_credit_search_instance.to_dict()
# create an instance of MerchantCreditSearch from a dict
merchant_credit_search_form_dict = merchant_credit_search.from_dict(merchant_credit_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


