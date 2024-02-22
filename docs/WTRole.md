# WTRole


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
from wallet.models.wt_role import WTRole

# TODO update the JSON string below
json = "{}"
# create an instance of WTRole from a JSON string
wt_role_instance = WTRole.from_json(json)
# print the JSON string representation of the object
print WTRole.to_json()

# convert the object into a dict
wt_role_dict = wt_role_instance.to_dict()
# create an instance of WTRole from a dict
wt_role_form_dict = wt_role.from_dict(wt_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


