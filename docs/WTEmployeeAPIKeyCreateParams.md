# WTEmployeeAPIKeyCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from wallet.models.wt_employee_api_key_create_params import WTEmployeeAPIKeyCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeAPIKeyCreateParams from a JSON string
wt_employee_api_key_create_params_instance = WTEmployeeAPIKeyCreateParams.from_json(json)
# print the JSON string representation of the object
print WTEmployeeAPIKeyCreateParams.to_json()

# convert the object into a dict
wt_employee_api_key_create_params_dict = wt_employee_api_key_create_params_instance.to_dict()
# create an instance of WTEmployeeAPIKeyCreateParams from a dict
wt_employee_api_key_create_params_form_dict = wt_employee_api_key_create_params.from_dict(wt_employee_api_key_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


