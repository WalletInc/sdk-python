# WTQuickLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** |  | 
**url** | **str** |  | 
**icon** | **object** |  | 
**order_number** | **int** |  | 
**link_book_section_id** | [**WTQuickLinkLinkBookSectionID**](WTQuickLinkLinkBookSectionID.md) |  | [optional] 
**id** | [**AmenityId**](AmenityId.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.wt_quick_link import WTQuickLink

# TODO update the JSON string below
json = "{}"
# create an instance of WTQuickLink from a JSON string
wt_quick_link_instance = WTQuickLink.from_json(json)
# print the JSON string representation of the object
print WTQuickLink.to_json()

# convert the object into a dict
wt_quick_link_dict = wt_quick_link_instance.to_dict()
# create an instance of WTQuickLink from a dict
wt_quick_link_form_dict = wt_quick_link.from_dict(wt_quick_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


