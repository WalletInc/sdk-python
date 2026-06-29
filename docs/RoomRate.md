# RoomRate


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
from wallet.models.room_rate import RoomRate

# TODO update the JSON string below
json = "{}"
# create an instance of RoomRate from a JSON string
room_rate_instance = RoomRate.from_json(json)
# print the JSON string representation of the object
print RoomRate.to_json()

# convert the object into a dict
room_rate_dict = room_rate_instance.to_dict()
# create an instance of RoomRate from a dict
room_rate_form_dict = room_rate.from_dict(room_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


