# WTPublicItemBranding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** |  | [optional] 
**header_background_color** | **str** |  | [optional] 
**mobile_app_icon_url** | **str** |  | [optional] 
**header_image_url** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_public_item_branding import WTPublicItemBranding

# TODO update the JSON string below
json = "{}"
# create an instance of WTPublicItemBranding from a JSON string
wt_public_item_branding_instance = WTPublicItemBranding.from_json(json)
# print the JSON string representation of the object
print WTPublicItemBranding.to_json()

# convert the object into a dict
wt_public_item_branding_dict = wt_public_item_branding_instance.to_dict()
# create an instance of WTPublicItemBranding from a dict
wt_public_item_branding_form_dict = wt_public_item_branding.from_dict(wt_public_item_branding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


