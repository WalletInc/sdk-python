# WTEmployeeAPIKeyUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from wallet.models.wt_employee_api_key_update_params import WTEmployeeAPIKeyUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeAPIKeyUpdateParams from a JSON string
wt_employee_api_key_update_params_instance = WTEmployeeAPIKeyUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTEmployeeAPIKeyUpdateParams.to_json()

# convert the object into a dict
wt_employee_api_key_update_params_dict = wt_employee_api_key_update_params_instance.to_dict()
# create an instance of WTEmployeeAPIKeyUpdateParams from a dict
wt_employee_api_key_update_params_form_dict = wt_employee_api_key_update_params.from_dict(wt_employee_api_key_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


