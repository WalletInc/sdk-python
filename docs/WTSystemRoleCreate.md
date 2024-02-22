# WTSystemRoleCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**webpages_to_add** | **List[str]** |  | 

## Example

```python
from wallet.models.wt_system_role_create import WTSystemRoleCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WTSystemRoleCreate from a JSON string
wt_system_role_create_instance = WTSystemRoleCreate.from_json(json)
# print the JSON string representation of the object
print WTSystemRoleCreate.to_json()

# convert the object into a dict
wt_system_role_create_dict = wt_system_role_create_instance.to_dict()
# create an instance of WTSystemRoleCreate from a dict
wt_system_role_create_form_dict = wt_system_role_create.from_dict(wt_system_role_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


