# WTPublicBranding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** |  | [optional] 
**header_background_color** | **str** |  | [optional] 
**mobile_app_icon_url** | **str** |  | [optional] 
**login_logo_url** | **str** |  | [optional] 
**login_panel_image_url** | **str** |  | [optional] 
**login_headline** | **str** |  | [optional] 
**login_subcopy** | **str** |  | [optional] 
**login_background_color** | **str** |  | [optional] 
**login_background_image_url** | **str** |  | [optional] 
**register_url** | **str** |  | [optional] 
**login_footer_links** | **object** |  | [optional] 
**desktop_frame_logo_url** | **str** |  | [optional] 
**desktop_frame_background_color** | **str** |  | [optional] 
**desktop_frame_background_image_url** | **str** |  | [optional] 
**desktop_frame_byline** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_public_branding import WTPublicBranding

# TODO update the JSON string below
json = "{}"
# create an instance of WTPublicBranding from a JSON string
wt_public_branding_instance = WTPublicBranding.from_json(json)
# print the JSON string representation of the object
print WTPublicBranding.to_json()

# convert the object into a dict
wt_public_branding_dict = wt_public_branding_instance.to_dict()
# create an instance of WTPublicBranding from a dict
wt_public_branding_form_dict = wt_public_branding.from_dict(wt_public_branding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


