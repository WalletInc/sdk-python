# WTPointsAwardUndoResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points_reversed** | **float** |  | 
**balance** | **float** |  | 
**tier_reverted** | [**WTPointsAwardUndoResultTierReverted**](WTPointsAwardUndoResultTierReverted.md) |  | 
**replayed** | **bool** |  | 

## Example

```python
from wallet.models.wt_points_award_undo_result import WTPointsAwardUndoResult

# TODO update the JSON string below
json = "{}"
# create an instance of WTPointsAwardUndoResult from a JSON string
wt_points_award_undo_result_instance = WTPointsAwardUndoResult.from_json(json)
# print the JSON string representation of the object
print WTPointsAwardUndoResult.to_json()

# convert the object into a dict
wt_points_award_undo_result_dict = wt_points_award_undo_result_instance.to_dict()
# create an instance of WTPointsAwardUndoResult from a dict
wt_points_award_undo_result_form_dict = wt_points_award_undo_result.from_dict(wt_points_award_undo_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


