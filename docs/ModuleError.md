# ModuleError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**message** | **str** |  | 
**stack** | **str** |  | [optional] 
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**module** | **str** |  | 
**module_name** | **str** |  | 
**module_id** | **str** |  | 
**code** | **str** |  | 
**method_type** | **str** |  | 
**stack_trace** | **object** |  | 
**exception** | **object** |  | 
**severity** | **float** |  | 
**microservice_url** | **str** |  | 
**microservice_data** | **object** |  | 
**microservice_method** | **str** |  | 
**microservice_options** | **object** |  | 
**microservice_response_code** | **str** |  | 
**microservice_response_message** | **str** |  | 
**microservice_response_http_status** | **str** |  | 
**microservice_response_fields** | **object** |  | 

## Example

```python
from wallet.models.module_error import ModuleError

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleError from a JSON string
module_error_instance = ModuleError.from_json(json)
# print the JSON string representation of the object
print ModuleError.to_json()

# convert the object into a dict
module_error_dict = module_error_instance.to_dict()
# create an instance of ModuleError from a dict
module_error_form_dict = module_error.from_dict(module_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


