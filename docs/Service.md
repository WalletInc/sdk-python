# Service


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
from wallet.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print Service.to_json()

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_form_dict = service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


