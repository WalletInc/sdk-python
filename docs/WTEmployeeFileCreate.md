# WTEmployeeFileCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**file_data** | **str** |  | 

## Example

```python
from wallet.models.wt_employee_file_create import WTEmployeeFileCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeFileCreate from a JSON string
wt_employee_file_create_instance = WTEmployeeFileCreate.from_json(json)
# print the JSON string representation of the object
print WTEmployeeFileCreate.to_json()

# convert the object into a dict
wt_employee_file_create_dict = wt_employee_file_create_instance.to_dict()
# create an instance of WTEmployeeFileCreate from a dict
wt_employee_file_create_form_dict = wt_employee_file_create.from_dict(wt_employee_file_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


