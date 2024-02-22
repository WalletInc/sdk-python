# WTMerchantURLUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nickname** | **str** |  | 
**destination_url** | **str** |  | 

## Example

```python
from wallet.models.wt_merchant_url_update import WTMerchantURLUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WTMerchantURLUpdate from a JSON string
wt_merchant_url_update_instance = WTMerchantURLUpdate.from_json(json)
# print the JSON string representation of the object
print WTMerchantURLUpdate.to_json()

# convert the object into a dict
wt_merchant_url_update_dict = wt_merchant_url_update_instance.to_dict()
# create an instance of WTMerchantURLUpdate from a dict
wt_merchant_url_update_form_dict = wt_merchant_url_update.from_dict(wt_merchant_url_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


