# WTMenuOptionGroupUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** |  | [optional] 
**min_choices** | **object** |  | [optional] 
**max_choices** | **object** |  | [optional] 
**options** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_menu_option_group_update_params import WTMenuOptionGroupUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTMenuOptionGroupUpdateParams from a JSON string
wt_menu_option_group_update_params_instance = WTMenuOptionGroupUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTMenuOptionGroupUpdateParams.to_json()

# convert the object into a dict
wt_menu_option_group_update_params_dict = wt_menu_option_group_update_params_instance.to_dict()
# create an instance of WTMenuOptionGroupUpdateParams from a dict
wt_menu_option_group_update_params_form_dict = wt_menu_option_group_update_params.from_dict(wt_menu_option_group_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


