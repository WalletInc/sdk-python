# Amenity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** |  | 
**description** | **object** |  | 
**displayed_price** | **object** |  | [optional] 
**order_number** | **object** |  | 
**media_url** | **object** |  | [optional] 
**additional_info_url** | **object** |  | [optional] 
**id** | [**AmenityId**](AmenityId.md) |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.amenity import Amenity

# TODO update the JSON string below
json = "{}"
# create an instance of Amenity from a JSON string
amenity_instance = Amenity.from_json(json)
# print the JSON string representation of the object
print Amenity.to_json()

# convert the object into a dict
amenity_dict = amenity_instance.to_dict()
# create an instance of Amenity from a dict
amenity_form_dict = amenity.from_dict(amenity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


