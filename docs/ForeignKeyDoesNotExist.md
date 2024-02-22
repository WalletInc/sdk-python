# ForeignKeyDoesNotExist


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
from wallet.models.foreign_key_does_not_exist import ForeignKeyDoesNotExist

# TODO update the JSON string below
json = "{}"
# create an instance of ForeignKeyDoesNotExist from a JSON string
foreign_key_does_not_exist_instance = ForeignKeyDoesNotExist.from_json(json)
# print the JSON string representation of the object
print ForeignKeyDoesNotExist.to_json()

# convert the object into a dict
foreign_key_does_not_exist_dict = foreign_key_does_not_exist_instance.to_dict()
# create an instance of ForeignKeyDoesNotExist from a dict
foreign_key_does_not_exist_form_dict = foreign_key_does_not_exist.from_dict(foreign_key_does_not_exist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


