# InternalServerError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**message** | **str** |  | 
**stack** | **str** |  | [optional] 
**http_error_code** | **float** |  | 
**tracking_code** | **str** |  | 

## Example

```python
from wallet.models.internal_server_error import InternalServerError

# TODO update the JSON string below
json = "{}"
# create an instance of InternalServerError from a JSON string
internal_server_error_instance = InternalServerError.from_json(json)
# print the JSON string representation of the object
print InternalServerError.to_json()

# convert the object into a dict
internal_server_error_dict = internal_server_error_instance.to_dict()
# create an instance of InternalServerError from a dict
internal_server_error_form_dict = internal_server_error.from_dict(internal_server_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


