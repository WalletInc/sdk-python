# DuplicateRowFound


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
from wallet.models.duplicate_row_found import DuplicateRowFound

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateRowFound from a JSON string
duplicate_row_found_instance = DuplicateRowFound.from_json(json)
# print the JSON string representation of the object
print DuplicateRowFound.to_json()

# convert the object into a dict
duplicate_row_found_dict = duplicate_row_found_instance.to_dict()
# create an instance of DuplicateRowFound from a dict
duplicate_row_found_form_dict = duplicate_row_found.from_dict(duplicate_row_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


