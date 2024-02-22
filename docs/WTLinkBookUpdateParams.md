# WTLinkBookUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**url** | **str** |  | 
**icon** | **str** |  | 
**order_number** | **int** |  | 
**link_book_section_id** | [**WTLinkBookLinkBookSectionID**](WTLinkBookLinkBookSectionID.md) |  | [optional] 

## Example

```python
from wallet.models.wt_link_book_update_params import WTLinkBookUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTLinkBookUpdateParams from a JSON string
wt_link_book_update_params_instance = WTLinkBookUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTLinkBookUpdateParams.to_json()

# convert the object into a dict
wt_link_book_update_params_dict = wt_link_book_update_params_instance.to_dict()
# create an instance of WTLinkBookUpdateParams from a dict
wt_link_book_update_params_form_dict = wt_link_book_update_params.from_dict(wt_link_book_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


