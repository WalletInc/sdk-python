# InternalServerError500


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
from wallet.models.internal_server_error500 import InternalServerError500

# TODO update the JSON string below
json = "{}"
# create an instance of InternalServerError500 from a JSON string
internal_server_error500_instance = InternalServerError500.from_json(json)
# print the JSON string representation of the object
print InternalServerError500.to_json()

# convert the object into a dict
internal_server_error500_dict = internal_server_error500_instance.to_dict()
# create an instance of InternalServerError500 from a dict
internal_server_error500_form_dict = internal_server_error500.from_dict(internal_server_error500_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


