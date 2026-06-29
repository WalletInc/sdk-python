# WTQuickLinkSectionCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**order_number** | **int** |  | 

## Example

```python
from wallet.models.wt_quick_link_section_create_params import WTQuickLinkSectionCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTQuickLinkSectionCreateParams from a JSON string
wt_quick_link_section_create_params_instance = WTQuickLinkSectionCreateParams.from_json(json)
# print the JSON string representation of the object
print WTQuickLinkSectionCreateParams.to_json()

# convert the object into a dict
wt_quick_link_section_create_params_dict = wt_quick_link_section_create_params_instance.to_dict()
# create an instance of WTQuickLinkSectionCreateParams from a dict
wt_quick_link_section_create_params_form_dict = wt_quick_link_section_create_params.from_dict(wt_quick_link_section_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


