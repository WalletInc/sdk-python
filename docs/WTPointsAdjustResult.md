# WTPointsAdjustResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_id** | **str** |  | 
**balance** | **float** |  | 
**replayed** | **bool** |  | 

## Example

```python
from wallet.models.wt_points_adjust_result import WTPointsAdjustResult

# TODO update the JSON string below
json = "{}"
# create an instance of WTPointsAdjustResult from a JSON string
wt_points_adjust_result_instance = WTPointsAdjustResult.from_json(json)
# print the JSON string representation of the object
print WTPointsAdjustResult.to_json()

# convert the object into a dict
wt_points_adjust_result_dict = wt_points_adjust_result_instance.to_dict()
# create an instance of WTPointsAdjustResult from a dict
wt_points_adjust_result_form_dict = wt_points_adjust_result.from_dict(wt_points_adjust_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


