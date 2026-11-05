# WTMenuUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** |  | [optional] 
**description** | **object** |  | [optional] 
**order_number** | **object** |  | [optional] 
**time_zone** | **object** |  | [optional] 
**schedule** | **object** |  | [optional] 
**categories** | **object** |  | [optional] 
**venue_type** | [**WTMenuVenueType**](WTMenuVenueType.md) |  | [optional] 
**venue_id** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_menu_update_params import WTMenuUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTMenuUpdateParams from a JSON string
wt_menu_update_params_instance = WTMenuUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTMenuUpdateParams.to_json()

# convert the object into a dict
wt_menu_update_params_dict = wt_menu_update_params_instance.to_dict()
# create an instance of WTMenuUpdateParams from a dict
wt_menu_update_params_form_dict = wt_menu_update_params.from_dict(wt_menu_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


