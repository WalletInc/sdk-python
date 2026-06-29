# Gaming


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
from wallet.models.gaming import Gaming

# TODO update the JSON string below
json = "{}"
# create an instance of Gaming from a JSON string
gaming_instance = Gaming.from_json(json)
# print the JSON string representation of the object
print Gaming.to_json()

# convert the object into a dict
gaming_dict = gaming_instance.to_dict()
# create an instance of Gaming from a dict
gaming_form_dict = gaming.from_dict(gaming_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


