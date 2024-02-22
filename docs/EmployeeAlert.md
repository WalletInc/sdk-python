# EmployeeAlert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** |  | 
**title** | **str** |  | 
**message** | **str** |  | 
**s3_bucket** | **str** |  | 
**s3_key** | **str** |  | 
**file_size_bytes** | **float** |  | 
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_read** | **bool** |  | 

## Example

```python
from wallet.models.employee_alert import EmployeeAlert

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeAlert from a JSON string
employee_alert_instance = EmployeeAlert.from_json(json)
# print the JSON string representation of the object
print EmployeeAlert.to_json()

# convert the object into a dict
employee_alert_dict = employee_alert_instance.to_dict()
# create an instance of EmployeeAlert from a dict
employee_alert_form_dict = employee_alert.from_dict(employee_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


