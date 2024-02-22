# WTMerchantUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** |  | 
**address1** | **str** |  | 
**address2** | **str** |  | 
**city** | **str** |  | 
**state** | **str** |  | 
**country** | **str** |  | 
**phone_number** | **str** |  | 
**zip** | **str** |  | 
**currency_abbreviation** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_merchant_update import WTMerchantUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WTMerchantUpdate from a JSON string
wt_merchant_update_instance = WTMerchantUpdate.from_json(json)
# print the JSON string representation of the object
print WTMerchantUpdate.to_json()

# convert the object into a dict
wt_merchant_update_dict = wt_merchant_update_instance.to_dict()
# create an instance of WTMerchantUpdate from a dict
wt_merchant_update_form_dict = wt_merchant_update.from_dict(wt_merchant_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


