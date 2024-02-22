# WTSettingsSetPassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 

## Example

```python
from wallet.models.wt_settings_set_password import WTSettingsSetPassword

# TODO update the JSON string below
json = "{}"
# create an instance of WTSettingsSetPassword from a JSON string
wt_settings_set_password_instance = WTSettingsSetPassword.from_json(json)
# print the JSON string representation of the object
print WTSettingsSetPassword.to_json()

# convert the object into a dict
wt_settings_set_password_dict = wt_settings_set_password_instance.to_dict()
# create an instance of WTSettingsSetPassword from a dict
wt_settings_set_password_form_dict = wt_settings_set_password.from_dict(wt_settings_set_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


