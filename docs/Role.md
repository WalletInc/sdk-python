# Role


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**employees** | [**List[WTEmployee]**](WTEmployee.md) |  | 
**roles** | [**List[WTRole]**](WTRole.md) |  | 
**employee_id** | **str** |  | 
**merchant_id** | **str** |  | 
**name** | **str** |  | 
**display_name** | **str** |  | 
**is_public** | **bool** |  | 
**order_number** | **float** |  | 
**is_system** | **bool** |  | 
**icons** | **List[str]** |  | 
**category** | **str** |  | 
**admin_page** | **str** |  | 

## Example

```python
from wallet.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print Role.to_json()

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_form_dict = role.from_dict(role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


