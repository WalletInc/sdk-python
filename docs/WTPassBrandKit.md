# WTPassBrandKit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_color** | **object** |  | [optional] 
**text_color** | **object** |  | [optional] 
**accent_color** | **object** |  | [optional] 
**logo_url** | **object** |  | [optional] 
**mark_url** | **object** |  | [optional] 
**banner_image_url** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_pass_brand_kit import WTPassBrandKit

# TODO update the JSON string below
json = "{}"
# create an instance of WTPassBrandKit from a JSON string
wt_pass_brand_kit_instance = WTPassBrandKit.from_json(json)
# print the JSON string representation of the object
print WTPassBrandKit.to_json()

# convert the object into a dict
wt_pass_brand_kit_dict = wt_pass_brand_kit_instance.to_dict()
# create an instance of WTPassBrandKit from a dict
wt_pass_brand_kit_form_dict = wt_pass_brand_kit.from_dict(wt_pass_brand_kit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


