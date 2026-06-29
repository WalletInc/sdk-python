# Lounge


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
from wallet.models.lounge import Lounge

# TODO update the JSON string below
json = "{}"
# create an instance of Lounge from a JSON string
lounge_instance = Lounge.from_json(json)
# print the JSON string representation of the object
print Lounge.to_json()

# convert the object into a dict
lounge_dict = lounge_instance.to_dict()
# create an instance of Lounge from a dict
lounge_form_dict = lounge.from_dict(lounge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


