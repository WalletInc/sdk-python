# OptInListSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**StaticVoucherId**](StaticVoucherId.md) |  | 
**list_id** | **str** |  | 
**source_name** | **object** |  | 
**employee_id** | **str** |  | 
**merchant_id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 

## Example

```python
from wallet.models.opt_in_list_source import OptInListSource

# TODO update the JSON string below
json = "{}"
# create an instance of OptInListSource from a JSON string
opt_in_list_source_instance = OptInListSource.from_json(json)
# print the JSON string representation of the object
print OptInListSource.to_json()

# convert the object into a dict
opt_in_list_source_dict = opt_in_list_source_instance.to_dict()
# create an instance of OptInListSource from a dict
opt_in_list_source_form_dict = opt_in_list_source.from_dict(opt_in_list_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


