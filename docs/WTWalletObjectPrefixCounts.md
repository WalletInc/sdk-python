# WTWalletObjectPrefixCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_object_prefix** | **str** |  | 
**wallet_object_name** | **str** |  | 
**list** | [**List[WTWalletPageViewCount]**](WTWalletPageViewCount.md) |  | 

## Example

```python
from wallet.models.wt_wallet_object_prefix_counts import WTWalletObjectPrefixCounts

# TODO update the JSON string below
json = "{}"
# create an instance of WTWalletObjectPrefixCounts from a JSON string
wt_wallet_object_prefix_counts_instance = WTWalletObjectPrefixCounts.from_json(json)
# print the JSON string representation of the object
print WTWalletObjectPrefixCounts.to_json()

# convert the object into a dict
wt_wallet_object_prefix_counts_dict = wt_wallet_object_prefix_counts_instance.to_dict()
# create an instance of WTWalletObjectPrefixCounts from a dict
wt_wallet_object_prefix_counts_form_dict = wt_wallet_object_prefix_counts.from_dict(wt_wallet_object_prefix_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


