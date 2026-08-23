# UpdateChromeThemePreferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chrome_theme** | [**UpdateChromeThemePreferenceRequestChromeTheme**](UpdateChromeThemePreferenceRequestChromeTheme.md) |  | [optional] 

## Example

```python
from wallet.models.update_chrome_theme_preference_request import UpdateChromeThemePreferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChromeThemePreferenceRequest from a JSON string
update_chrome_theme_preference_request_instance = UpdateChromeThemePreferenceRequest.from_json(json)
# print the JSON string representation of the object
print UpdateChromeThemePreferenceRequest.to_json()

# convert the object into a dict
update_chrome_theme_preference_request_dict = update_chrome_theme_preference_request_instance.to_dict()
# create an instance of UpdateChromeThemePreferenceRequest from a dict
update_chrome_theme_preference_request_form_dict = update_chrome_theme_preference_request.from_dict(update_chrome_theme_preference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


