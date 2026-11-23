# WTPointsSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earning_enabled** | **object** | Off until the merchant switches it on. A merchant that never saved settings earns nothing. | 
**points_per_dollar** | **object** | Points awarded per whole dollar the guest actually paid (after Wallet discounts, excluding tax and tip). | 
**award_cap_cents** | **object** | The largest check, in cents, a staff member can award points on from a terminal. | 
**updated_at** | **object** | When the settings were last saved, or null if they never were. | 

## Example

```python
from wallet.models.wt_points_settings import WTPointsSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WTPointsSettings from a JSON string
wt_points_settings_instance = WTPointsSettings.from_json(json)
# print the JSON string representation of the object
print WTPointsSettings.to_json()

# convert the object into a dict
wt_points_settings_dict = wt_points_settings_instance.to_dict()
# create an instance of WTPointsSettings from a dict
wt_points_settings_form_dict = wt_points_settings.from_dict(wt_points_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


