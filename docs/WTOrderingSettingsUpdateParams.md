# WTOrderingSettingsUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_rate_percent** | **object** |  | [optional] 
**alcohol_tax_rate_percent** | **object** |  | [optional] 
**default_prep_minutes** | **object** |  | [optional] 
**busy_extra_minutes** | **object** |  | [optional] 
**is_paused** | **bool** |  | [optional] 
**paused_reason** | **object** |  | [optional] 
**auto_accept** | **bool** |  | [optional] 
**scheduled_pickup** | **bool** |  | [optional] 
**time_zone** | **object** |  | [optional] 
**hours** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_ordering_settings_update_params import WTOrderingSettingsUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTOrderingSettingsUpdateParams from a JSON string
wt_ordering_settings_update_params_instance = WTOrderingSettingsUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTOrderingSettingsUpdateParams.to_json()

# convert the object into a dict
wt_ordering_settings_update_params_dict = wt_ordering_settings_update_params_instance.to_dict()
# create an instance of WTOrderingSettingsUpdateParams from a dict
wt_ordering_settings_update_params_form_dict = wt_ordering_settings_update_params.from_dict(wt_ordering_settings_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


