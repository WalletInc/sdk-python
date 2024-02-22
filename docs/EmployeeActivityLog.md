# EmployeeActivityLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**employee_id** | **str** |  | 
**action** | **str** |  | 
**route** | **str** |  | 
**page_name** | **str** |  | 

## Example

```python
from wallet.models.employee_activity_log import EmployeeActivityLog

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeActivityLog from a JSON string
employee_activity_log_instance = EmployeeActivityLog.from_json(json)
# print the JSON string representation of the object
print EmployeeActivityLog.to_json()

# convert the object into a dict
employee_activity_log_dict = employee_activity_log_instance.to_dict()
# create an instance of EmployeeActivityLog from a dict
employee_activity_log_form_dict = employee_activity_log.from_dict(employee_activity_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


