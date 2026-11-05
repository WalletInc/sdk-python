# WTWalletSectionTopItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_id** | **str** |  | 
**title** | **str** |  | 
**views** | **float** |  | 

## Example

```python
from wallet.models.wt_wallet_section_top_item import WTWalletSectionTopItem

# TODO update the JSON string below
json = "{}"
# create an instance of WTWalletSectionTopItem from a JSON string
wt_wallet_section_top_item_instance = WTWalletSectionTopItem.from_json(json)
# print the JSON string representation of the object
print WTWalletSectionTopItem.to_json()

# convert the object into a dict
wt_wallet_section_top_item_dict = wt_wallet_section_top_item_instance.to_dict()
# create an instance of WTWalletSectionTopItem from a dict
wt_wallet_section_top_item_form_dict = wt_wallet_section_top_item.from_dict(wt_wallet_section_top_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


