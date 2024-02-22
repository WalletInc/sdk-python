# RoleAuditLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**role_name** | **str** |  | 
**action** | **str** |  | 
**merchant_id** | **str** |  | 
**action_by_employee_id** | **str** |  | 
**action_by_employee_name** | **str** |  | 
**action_on_employee_id** | **str** |  | 
**action_on_employee_name** | **str** |  | 
**display_name** | **str** |  | 
**is_system** | **bool** |  | 

## Example

```python
from wallet.models.role_audit_log import RoleAuditLog

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAuditLog from a JSON string
role_audit_log_instance = RoleAuditLog.from_json(json)
# print the JSON string representation of the object
print RoleAuditLog.to_json()

# convert the object into a dict
role_audit_log_dict = role_audit_log_instance.to_dict()
# create an instance of RoleAuditLog from a dict
role_audit_log_form_dict = role_audit_log.from_dict(role_audit_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


