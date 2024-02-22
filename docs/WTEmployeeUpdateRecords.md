# WTEmployeeUpdateRecords


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**bucket** | **str** |  | 

## Example

```python
from wallet.models.wt_employee_update_records import WTEmployeeUpdateRecords

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeUpdateRecords from a JSON string
wt_employee_update_records_instance = WTEmployeeUpdateRecords.from_json(json)
# print the JSON string representation of the object
print WTEmployeeUpdateRecords.to_json()

# convert the object into a dict
wt_employee_update_records_dict = wt_employee_update_records_instance.to_dict()
# create an instance of WTEmployeeUpdateRecords from a dict
wt_employee_update_records_form_dict = wt_employee_update_records.from_dict(wt_employee_update_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


