# Tcpa


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_phone** | **str** |  | 
**phone_number_id** | **str** |  | 
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 

## Example

```python
from wallet.models.tcpa import Tcpa

# TODO update the JSON string below
json = "{}"
# create an instance of Tcpa from a JSON string
tcpa_instance = Tcpa.from_json(json)
# print the JSON string representation of the object
print Tcpa.to_json()

# convert the object into a dict
tcpa_dict = tcpa_instance.to_dict()
# create an instance of Tcpa from a dict
tcpa_form_dict = tcpa.from_dict(tcpa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


