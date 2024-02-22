# WTEmployeeImportRecords


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**bucket** | **str** |  | 

## Example

```python
from wallet.models.wt_employee_import_records import WTEmployeeImportRecords

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeImportRecords from a JSON string
wt_employee_import_records_instance = WTEmployeeImportRecords.from_json(json)
# print the JSON string representation of the object
print WTEmployeeImportRecords.to_json()

# convert the object into a dict
wt_employee_import_records_dict = wt_employee_import_records_instance.to_dict()
# create an instance of WTEmployeeImportRecords from a dict
wt_employee_import_records_form_dict = wt_employee_import_records.from_dict(wt_employee_import_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


