# ForbiddenRequest


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
from wallet.models.forbidden_request import ForbiddenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ForbiddenRequest from a JSON string
forbidden_request_instance = ForbiddenRequest.from_json(json)
# print the JSON string representation of the object
print ForbiddenRequest.to_json()

# convert the object into a dict
forbidden_request_dict = forbidden_request_instance.to_dict()
# create an instance of ForbiddenRequest from a dict
forbidden_request_form_dict = forbidden_request.from_dict(forbidden_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


