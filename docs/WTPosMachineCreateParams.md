# WTPosMachineCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**register_id** | **str** |  | 
**register_name** | **str** |  | 
**outlet_name** | **str** |  | 
**outlet_number** | **int** | Stores the outlet number | 
**profit_center** | **str** |  | 

## Example

```python
from wallet.models.wt_pos_machine_create_params import WTPosMachineCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTPosMachineCreateParams from a JSON string
wt_pos_machine_create_params_instance = WTPosMachineCreateParams.from_json(json)
# print the JSON string representation of the object
print WTPosMachineCreateParams.to_json()

# convert the object into a dict
wt_pos_machine_create_params_dict = wt_pos_machine_create_params_instance.to_dict()
# create an instance of WTPosMachineCreateParams from a dict
wt_pos_machine_create_params_form_dict = wt_pos_machine_create_params.from_dict(wt_pos_machine_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


