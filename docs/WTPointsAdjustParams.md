# WTPointsAdjustParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta** | **object** | Points to add (positive) or remove (negative). Never zero. | 
**reason** | **object** | Why the balance is being changed. Shown in the member&#39;s points history. | 
**idempotency_key** | **object** |  | 

## Example

```python
from wallet.models.wt_points_adjust_params import WTPointsAdjustParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTPointsAdjustParams from a JSON string
wt_points_adjust_params_instance = WTPointsAdjustParams.from_json(json)
# print the JSON string representation of the object
print WTPointsAdjustParams.to_json()

# convert the object into a dict
wt_points_adjust_params_dict = wt_points_adjust_params_instance.to_dict()
# create an instance of WTPointsAdjustParams from a dict
wt_points_adjust_params_form_dict = wt_points_adjust_params.from_dict(wt_points_adjust_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


