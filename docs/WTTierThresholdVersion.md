# WTTierThresholdVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_id** | **str** |  | 
**previous_qualify_points** | **object** |  | 
**qualify_points** | **object** |  | 
**kind** | [**WTTierThresholdVersionKind**](WTTierThresholdVersionKind.md) |  | 
**upgraded_at_save** | **float** |  | 
**employee_name** | **object** |  | 
**created_at** | **datetime** |  | 
**undone_at** | **object** |  | 
**can_undo** | **object** | True only for the tier&#39;s current version, if it has not been undone. | 

## Example

```python
from wallet.models.wt_tier_threshold_version import WTTierThresholdVersion

# TODO update the JSON string below
json = "{}"
# create an instance of WTTierThresholdVersion from a JSON string
wt_tier_threshold_version_instance = WTTierThresholdVersion.from_json(json)
# print the JSON string representation of the object
print WTTierThresholdVersion.to_json()

# convert the object into a dict
wt_tier_threshold_version_dict = wt_tier_threshold_version_instance.to_dict()
# create an instance of WTTierThresholdVersion from a dict
wt_tier_threshold_version_form_dict = wt_tier_threshold_version.from_dict(wt_tier_threshold_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


