# FalsumField

Interface that lists the properties of a field that has failed validation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the field | 
**message** | **str** | Error message | 
**value** | **str** | The provided value | 

## Example

```python
from wallet.models.falsum_field import FalsumField

# TODO update the JSON string below
json = "{}"
# create an instance of FalsumField from a JSON string
falsum_field_instance = FalsumField.from_json(json)
# print the JSON string representation of the object
print FalsumField.to_json()

# convert the object into a dict
falsum_field_dict = falsum_field_instance.to_dict()
# create an instance of FalsumField from a dict
falsum_field_form_dict = falsum_field.from_dict(falsum_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


