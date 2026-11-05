# WTMenuOptionGroupCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** |  | 
**min_choices** | **object** |  | [optional] 
**max_choices** | **object** |  | [optional] 
**options** | **object** |  | 

## Example

```python
from wallet.models.wt_menu_option_group_create_params import WTMenuOptionGroupCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTMenuOptionGroupCreateParams from a JSON string
wt_menu_option_group_create_params_instance = WTMenuOptionGroupCreateParams.from_json(json)
# print the JSON string representation of the object
print WTMenuOptionGroupCreateParams.to_json()

# convert the object into a dict
wt_menu_option_group_create_params_dict = wt_menu_option_group_create_params_instance.to_dict()
# create an instance of WTMenuOptionGroupCreateParams from a dict
wt_menu_option_group_create_params_form_dict = wt_menu_option_group_create_params.from_dict(wt_menu_option_group_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


