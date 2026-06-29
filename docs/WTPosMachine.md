# WTPosMachine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**register_id** | **object** |  | 
**register_name** | **object** |  | 
**outlet_name** | **object** |  | 
**outlet_number** | **object** | Stores the outlet number | 
**profit_center** | **object** |  | 
**id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**merchant_id** | **str** |  | 
**is_active** | **object** |  | 

## Example

```python
from wallet.models.wt_pos_machine import WTPosMachine

# TODO update the JSON string below
json = "{}"
# create an instance of WTPosMachine from a JSON string
wt_pos_machine_instance = WTPosMachine.from_json(json)
# print the JSON string representation of the object
print WTPosMachine.to_json()

# convert the object into a dict
wt_pos_machine_dict = wt_pos_machine_instance.to_dict()
# create an instance of WTPosMachine from a dict
wt_pos_machine_form_dict = wt_pos_machine.from_dict(wt_pos_machine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


