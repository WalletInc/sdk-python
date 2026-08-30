# WTPublicVanityPageMerchant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_public_vanity_page_merchant import WTPublicVanityPageMerchant

# TODO update the JSON string below
json = "{}"
# create an instance of WTPublicVanityPageMerchant from a JSON string
wt_public_vanity_page_merchant_instance = WTPublicVanityPageMerchant.from_json(json)
# print the JSON string representation of the object
print WTPublicVanityPageMerchant.to_json()

# convert the object into a dict
wt_public_vanity_page_merchant_dict = wt_public_vanity_page_merchant_instance.to_dict()
# create an instance of WTPublicVanityPageMerchant from a dict
wt_public_vanity_page_merchant_form_dict = wt_public_vanity_page_merchant.from_dict(wt_public_vanity_page_merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


