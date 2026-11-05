# WTOrderingSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | 
**tax_rate_percent** | **object** |  | 
**alcohol_tax_rate_percent** | **object** |  | [optional] 
**default_prep_minutes** | **object** |  | 
**busy_extra_minutes** | **object** |  | 
**is_paused** | **object** |  | 
**paused_reason** | **object** |  | [optional] 
**auto_accept** | **object** |  | 
**scheduled_pickup** | **object** |  | 
**time_zone** | **object** |  | 
**hours** | **object** |  | 

## Example

```python
from wallet.models.wt_ordering_settings import WTOrderingSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WTOrderingSettings from a JSON string
wt_ordering_settings_instance = WTOrderingSettings.from_json(json)
# print the JSON string representation of the object
print WTOrderingSettings.to_json()

# convert the object into a dict
wt_ordering_settings_dict = wt_ordering_settings_instance.to_dict()
# create an instance of WTOrderingSettings from a dict
wt_ordering_settings_form_dict = wt_ordering_settings.from_dict(wt_ordering_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


