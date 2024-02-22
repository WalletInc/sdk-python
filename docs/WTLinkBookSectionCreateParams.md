# WTLinkBookSectionCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**order_number** | **int** |  | 

## Example

```python
from wallet.models.wt_link_book_section_create_params import WTLinkBookSectionCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTLinkBookSectionCreateParams from a JSON string
wt_link_book_section_create_params_instance = WTLinkBookSectionCreateParams.from_json(json)
# print the JSON string representation of the object
print WTLinkBookSectionCreateParams.to_json()

# convert the object into a dict
wt_link_book_section_create_params_dict = wt_link_book_section_create_params_instance.to_dict()
# create an instance of WTLinkBookSectionCreateParams from a dict
wt_link_book_section_create_params_form_dict = wt_link_book_section_create_params.from_dict(wt_link_book_section_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


