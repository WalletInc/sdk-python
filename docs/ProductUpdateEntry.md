# ProductUpdateEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**ProductKey**](ProductKey.md) |  | 
**version** | **str** |  | 
**type** | [**ProductUpdateType**](ProductUpdateType.md) |  | 
**title** | **str** |  | 
**items** | **object** |  | 
**published_at** | **str** |  | 

## Example

```python
from wallet.models.product_update_entry import ProductUpdateEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ProductUpdateEntry from a JSON string
product_update_entry_instance = ProductUpdateEntry.from_json(json)
# print the JSON string representation of the object
print ProductUpdateEntry.to_json()

# convert the object into a dict
product_update_entry_dict = product_update_entry_instance.to_dict()
# create an instance of ProductUpdateEntry from a dict
product_update_entry_form_dict = product_update_entry.from_dict(product_update_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


