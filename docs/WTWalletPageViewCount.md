# WTWalletPageViewCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_object_id** | **str** |  | 
**count** | **float** |  | 
**date_occurred** | **datetime** |  | 
**wallet_object_name** | **str** |  | 

## Example

```python
from wallet.models.wt_wallet_page_view_count import WTWalletPageViewCount

# TODO update the JSON string below
json = "{}"
# create an instance of WTWalletPageViewCount from a JSON string
wt_wallet_page_view_count_instance = WTWalletPageViewCount.from_json(json)
# print the JSON string representation of the object
print WTWalletPageViewCount.to_json()

# convert the object into a dict
wt_wallet_page_view_count_dict = wt_wallet_page_view_count_instance.to_dict()
# create an instance of WTWalletPageViewCount from a dict
wt_wallet_page_view_count_form_dict = wt_wallet_page_view_count.from_dict(wt_wallet_page_view_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


