# WTMenuOptionGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**merchant_id** | **str** |  | 
**title** | **object** |  | 
**min_choices** | **object** |  | 
**max_choices** | **object** |  | 
**options** | **object** |  | 
**is_active** | **object** |  | 

## Example

```python
from wallet.models.wt_menu_option_group import WTMenuOptionGroup

# TODO update the JSON string below
json = "{}"
# create an instance of WTMenuOptionGroup from a JSON string
wt_menu_option_group_instance = WTMenuOptionGroup.from_json(json)
# print the JSON string representation of the object
print WTMenuOptionGroup.to_json()

# convert the object into a dict
wt_menu_option_group_dict = wt_menu_option_group_instance.to_dict()
# create an instance of WTMenuOptionGroup from a dict
wt_menu_option_group_form_dict = wt_menu_option_group.from_dict(wt_menu_option_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


