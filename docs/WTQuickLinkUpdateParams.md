# WTQuickLinkUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** |  | 
**url** | **str** |  | 
**icon** | **object** |  | 
**order_number** | **int** |  | 
**link_book_section_id** | [**WTQuickLinkLinkBookSectionID**](WTQuickLinkLinkBookSectionID.md) |  | [optional] 

## Example

```python
from wallet.models.wt_quick_link_update_params import WTQuickLinkUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTQuickLinkUpdateParams from a JSON string
wt_quick_link_update_params_instance = WTQuickLinkUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTQuickLinkUpdateParams.to_json()

# convert the object into a dict
wt_quick_link_update_params_dict = wt_quick_link_update_params_instance.to_dict()
# create an instance of WTQuickLinkUpdateParams from a dict
wt_quick_link_update_params_form_dict = wt_quick_link_update_params.from_dict(wt_quick_link_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


