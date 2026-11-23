# WTPointsSettingsSaveParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earning_enabled** | **bool** |  | 
**points_per_dollar** | **object** |  | 
**award_cap_cents** | **object** |  | 

## Example

```python
from wallet.models.wt_points_settings_save_params import WTPointsSettingsSaveParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTPointsSettingsSaveParams from a JSON string
wt_points_settings_save_params_instance = WTPointsSettingsSaveParams.from_json(json)
# print the JSON string representation of the object
print WTPointsSettingsSaveParams.to_json()

# convert the object into a dict
wt_points_settings_save_params_dict = wt_points_settings_save_params_instance.to_dict()
# create an instance of WTPointsSettingsSaveParams from a dict
wt_points_settings_save_params_form_dict = wt_points_settings_save_params.from_dict(wt_points_settings_save_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


