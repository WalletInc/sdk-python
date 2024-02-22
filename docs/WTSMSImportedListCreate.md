# WTSMSImportedListCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number_id** | **str** |  | 
**is_active** | **bool** |  | 
**list_name** | **str** |  | 

## Example

```python
from wallet.models.wtsms_imported_list_create import WTSMSImportedListCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WTSMSImportedListCreate from a JSON string
wtsms_imported_list_create_instance = WTSMSImportedListCreate.from_json(json)
# print the JSON string representation of the object
print WTSMSImportedListCreate.to_json()

# convert the object into a dict
wtsms_imported_list_create_dict = wtsms_imported_list_create_instance.to_dict()
# create an instance of WTSMSImportedListCreate from a dict
wtsms_imported_list_create_form_dict = wtsms_imported_list_create.from_dict(wtsms_imported_list_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


