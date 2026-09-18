# WTGooglePassStyle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_color** | **object** |  | [optional] 
**logo_url** | **object** |  | [optional] 
**hero_image_url** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_google_pass_style import WTGooglePassStyle

# TODO update the JSON string below
json = "{}"
# create an instance of WTGooglePassStyle from a JSON string
wt_google_pass_style_instance = WTGooglePassStyle.from_json(json)
# print the JSON string representation of the object
print WTGooglePassStyle.to_json()

# convert the object into a dict
wt_google_pass_style_dict = wt_google_pass_style_instance.to_dict()
# create an instance of WTGooglePassStyle from a dict
wt_google_pass_style_form_dict = wt_google_pass_style.from_dict(wt_google_pass_style_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


