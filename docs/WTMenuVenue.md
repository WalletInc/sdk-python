# WTMenuVenue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**venue_type** | [**WTMenuVenueType**](WTMenuVenueType.md) |  | 
**venue_id** | **object** |  | 
**venue_title** | **object** |  | 

## Example

```python
from wallet.models.wt_menu_venue import WTMenuVenue

# TODO update the JSON string below
json = "{}"
# create an instance of WTMenuVenue from a JSON string
wt_menu_venue_instance = WTMenuVenue.from_json(json)
# print the JSON string representation of the object
print WTMenuVenue.to_json()

# convert the object into a dict
wt_menu_venue_dict = wt_menu_venue_instance.to_dict()
# create an instance of WTMenuVenue from a dict
wt_menu_venue_form_dict = wt_menu_venue.from_dict(wt_menu_venue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


