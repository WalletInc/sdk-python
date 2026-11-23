# WTTierThresholdUndoResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moved_at_save** | **float** |  | 
**moved_by_purchases_since** | **float** |  | 
**moved_again_since_left_alone** | **float** |  | 
**discount_uses** | **object** | Discount uses at the higher tier, by the members being moved back, since the threshold was saved. They are kept, never charged back. | 
**reverted** | **float** |  | 
**threshold_restored_to** | **object** |  | 
**new_version_id** | **object** |  | 

## Example

```python
from wallet.models.wt_tier_threshold_undo_result import WTTierThresholdUndoResult

# TODO update the JSON string below
json = "{}"
# create an instance of WTTierThresholdUndoResult from a JSON string
wt_tier_threshold_undo_result_instance = WTTierThresholdUndoResult.from_json(json)
# print the JSON string representation of the object
print WTTierThresholdUndoResult.to_json()

# convert the object into a dict
wt_tier_threshold_undo_result_dict = wt_tier_threshold_undo_result_instance.to_dict()
# create an instance of WTTierThresholdUndoResult from a dict
wt_tier_threshold_undo_result_form_dict = wt_tier_threshold_undo_result.from_dict(wt_tier_threshold_undo_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


