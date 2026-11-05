# WTMenu


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**merchant_id** | **str** |  | 
**title** | **object** |  | 
**description** | **object** |  | 
**order_number** | **object** |  | 
**time_zone** | **object** |  | 
**schedule** | **object** |  | 
**categories** | **object** |  | 
**venue_type** | [**WTMenuVenueType**](WTMenuVenueType.md) |  | [optional] 
**venue_id** | **object** |  | [optional] 
**is_active** | **object** |  | 

## Example

```python
from wallet.models.wt_menu import WTMenu

# TODO update the JSON string below
json = "{}"
# create an instance of WTMenu from a JSON string
wt_menu_instance = WTMenu.from_json(json)
# print the JSON string representation of the object
print WTMenu.to_json()

# convert the object into a dict
wt_menu_dict = wt_menu_instance.to_dict()
# create an instance of WTMenu from a dict
wt_menu_form_dict = wt_menu.from_dict(wt_menu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


