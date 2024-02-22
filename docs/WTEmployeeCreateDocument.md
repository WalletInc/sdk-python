# WTEmployeeCreateDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**file_data** | **object** |  | 
**folder** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_employee_create_document import WTEmployeeCreateDocument

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeCreateDocument from a JSON string
wt_employee_create_document_instance = WTEmployeeCreateDocument.from_json(json)
# print the JSON string representation of the object
print WTEmployeeCreateDocument.to_json()

# convert the object into a dict
wt_employee_create_document_dict = wt_employee_create_document_instance.to_dict()
# create an instance of WTEmployeeCreateDocument from a dict
wt_employee_create_document_form_dict = wt_employee_create_document.from_dict(wt_employee_create_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


