# NotFound

Returned when the requested object does not exist (KAN-990). Silent: a mistyped, expired or crawled link is the caller's error, so it is not posted to the error sink.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**message** | **object** |  | 
**stack** | **object** |  | [optional] 
**http_error_code** | **object** |  | 
**tracking_code** | **object** |  | 

## Example

```python
from wallet.models.not_found import NotFound

# TODO update the JSON string below
json = "{}"
# create an instance of NotFound from a JSON string
not_found_instance = NotFound.from_json(json)
# print the JSON string representation of the object
print NotFound.to_json()

# convert the object into a dict
not_found_dict = not_found_instance.to_dict()
# create an instance of NotFound from a dict
not_found_form_dict = not_found.from_dict(not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


