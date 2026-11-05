# WTMenuCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** |  | 
**description** | **object** |  | [optional] 
**order_number** | **object** |  | [optional] 
**time_zone** | **object** |  | [optional] 
**schedule** | **object** |  | [optional] 
**categories** | **object** |  | [optional] 
**venue_type** | [**WTMenuVenueType**](WTMenuVenueType.md) |  | [optional] 
**venue_id** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_menu_create_params import WTMenuCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTMenuCreateParams from a JSON string
wt_menu_create_params_instance = WTMenuCreateParams.from_json(json)
# print the JSON string representation of the object
print WTMenuCreateParams.to_json()

# convert the object into a dict
wt_menu_create_params_dict = wt_menu_create_params_instance.to_dict()
# create an instance of WTMenuCreateParams from a dict
wt_menu_create_params_form_dict = wt_menu_create_params.from_dict(wt_menu_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


