# WTMerchantURLCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nickname** | **str** |  | 
**destination_url** | **str** |  | 

## Example

```python
from wallet.models.wt_merchant_url_create import WTMerchantURLCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WTMerchantURLCreate from a JSON string
wt_merchant_url_create_instance = WTMerchantURLCreate.from_json(json)
# print the JSON string representation of the object
print WTMerchantURLCreate.to_json()

# convert the object into a dict
wt_merchant_url_create_dict = wt_merchant_url_create_instance.to_dict()
# create an instance of WTMerchantURLCreate from a dict
wt_merchant_url_create_form_dict = wt_merchant_url_create.from_dict(wt_merchant_url_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


