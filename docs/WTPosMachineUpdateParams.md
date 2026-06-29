# WTPosMachineUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**register_id** | **object** |  | 
**register_name** | **object** |  | 
**outlet_name** | **object** |  | 
**outlet_number** | **object** | Stores the outlet number | 
**profit_center** | **object** |  | 

## Example

```python
from wallet.models.wt_pos_machine_update_params import WTPosMachineUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTPosMachineUpdateParams from a JSON string
wt_pos_machine_update_params_instance = WTPosMachineUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTPosMachineUpdateParams.to_json()

# convert the object into a dict
wt_pos_machine_update_params_dict = wt_pos_machine_update_params_instance.to_dict()
# create an instance of WTPosMachineUpdateParams from a dict
wt_pos_machine_update_params_form_dict = wt_pos_machine_update_params.from_dict(wt_pos_machine_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


