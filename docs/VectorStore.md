# VectorStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**AmenityId**](AmenityId.md) |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**merchant_id** | **str** |  | 
**vector_store_id** | **object** |  | 

## Example

```python
from wallet.models.vector_store import VectorStore

# TODO update the JSON string below
json = "{}"
# create an instance of VectorStore from a JSON string
vector_store_instance = VectorStore.from_json(json)
# print the JSON string representation of the object
print VectorStore.to_json()

# convert the object into a dict
vector_store_dict = vector_store_instance.to_dict()
# create an instance of VectorStore from a dict
vector_store_form_dict = vector_store.from_dict(vector_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


