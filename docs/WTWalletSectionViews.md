# WTWalletSectionViews


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**section_prefix** | **object** |  | 
**list_views** | **float** |  | 
**item_views** | **float** |  | 
**views** | **float** |  | 
**item_prefix** | **object** |  | [optional] 
**top_items** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_wallet_section_views import WTWalletSectionViews

# TODO update the JSON string below
json = "{}"
# create an instance of WTWalletSectionViews from a JSON string
wt_wallet_section_views_instance = WTWalletSectionViews.from_json(json)
# print the JSON string representation of the object
print WTWalletSectionViews.to_json()

# convert the object into a dict
wt_wallet_section_views_dict = wt_wallet_section_views_instance.to_dict()
# create an instance of WTWalletSectionViews from a dict
wt_wallet_section_views_form_dict = wt_wallet_section_views.from_dict(wt_wallet_section_views_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


