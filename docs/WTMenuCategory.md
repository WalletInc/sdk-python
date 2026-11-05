# WTMenuCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**title** | **object** |  | 
**item_ids** | **object** |  | 

## Example

```python
from wallet.models.wt_menu_category import WTMenuCategory

# TODO update the JSON string below
json = "{}"
# create an instance of WTMenuCategory from a JSON string
wt_menu_category_instance = WTMenuCategory.from_json(json)
# print the JSON string representation of the object
print WTMenuCategory.to_json()

# convert the object into a dict
wt_menu_category_dict = wt_menu_category_instance.to_dict()
# create an instance of WTMenuCategory from a dict
wt_menu_category_form_dict = wt_menu_category.from_dict(wt_menu_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


