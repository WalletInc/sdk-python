# FalsumError

The error interface that consists of detailed info about why the validation has failed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**fields** | [**List[FalsumField]**](FalsumField.md) |  | 

## Example

```python
from wallet.models.falsum_error import FalsumError

# TODO update the JSON string below
json = "{}"
# create an instance of FalsumError from a JSON string
falsum_error_instance = FalsumError.from_json(json)
# print the JSON string representation of the object
print FalsumError.to_json()

# convert the object into a dict
falsum_error_dict = falsum_error_instance.to_dict()
# create an instance of FalsumError from a dict
falsum_error_form_dict = falsum_error.from_dict(falsum_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


