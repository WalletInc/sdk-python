# WTTierThresholdParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qualify_points** | **object** | Points earned in the last 12 months that move a member up to this tier, or null to turn automatic upgrades to this tier off. | 

## Example

```python
from wallet.models.wt_tier_threshold_params import WTTierThresholdParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTTierThresholdParams from a JSON string
wt_tier_threshold_params_instance = WTTierThresholdParams.from_json(json)
# print the JSON string representation of the object
print WTTierThresholdParams.to_json()

# convert the object into a dict
wt_tier_threshold_params_dict = wt_tier_threshold_params_instance.to_dict()
# create an instance of WTTierThresholdParams from a dict
wt_tier_threshold_params_form_dict = wt_tier_threshold_params.from_dict(wt_tier_threshold_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


