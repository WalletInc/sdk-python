# EntityTooLarge


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
from wallet.models.entity_too_large import EntityTooLarge

# TODO update the JSON string below
json = "{}"
# create an instance of EntityTooLarge from a JSON string
entity_too_large_instance = EntityTooLarge.from_json(json)
# print the JSON string representation of the object
print EntityTooLarge.to_json()

# convert the object into a dict
entity_too_large_dict = entity_too_large_instance.to_dict()
# create an instance of EntityTooLarge from a dict
entity_too_large_form_dict = entity_too_large.from_dict(entity_too_large_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


