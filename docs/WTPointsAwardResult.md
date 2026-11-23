# WTPointsAwardResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skipped** | [**WTPointsSkipReason**](WTPointsSkipReason.md) | Present only when nothing was awarded; the other fields are then absent. | [optional] 
**entry_id** | **str** |  | [optional] 
**points_awarded** | **float** |  | [optional] 
**balance** | **float** |  | [optional] 
**lifetime_earned** | **float** |  | [optional] 
**earned12_months** | **float** |  | [optional] 
**previous_tier_id** | **object** |  | [optional] 
**new_tier_id** | **object** |  | [optional] 
**tier_changed** | **bool** |  | [optional] 
**new_tier_name** | **object** | The new tier&#39;s name, set only when the award moved the member up a tier. | [optional] 
**replayed** | **object** | True when this answer repeats an earlier award with the same idempotency key. | [optional] 

## Example

```python
from wallet.models.wt_points_award_result import WTPointsAwardResult

# TODO update the JSON string below
json = "{}"
# create an instance of WTPointsAwardResult from a JSON string
wt_points_award_result_instance = WTPointsAwardResult.from_json(json)
# print the JSON string representation of the object
print WTPointsAwardResult.to_json()

# convert the object into a dict
wt_points_award_result_dict = wt_points_award_result_instance.to_dict()
# create an instance of WTPointsAwardResult from a dict
wt_points_award_result_form_dict = wt_points_award_result.from_dict(wt_points_award_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


