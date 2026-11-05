# WTMenuOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**title** | **object** |  | 
**price_delta_cents** | **object** |  | 
**is_sold_out** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_menu_option import WTMenuOption

# TODO update the JSON string below
json = "{}"
# create an instance of WTMenuOption from a JSON string
wt_menu_option_instance = WTMenuOption.from_json(json)
# print the JSON string representation of the object
print WTMenuOption.to_json()

# convert the object into a dict
wt_menu_option_dict = wt_menu_option_instance.to_dict()
# create an instance of WTMenuOption from a dict
wt_menu_option_form_dict = wt_menu_option.from_dict(wt_menu_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


