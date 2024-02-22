# WTLoungeUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | 
**displayed_price** | **str** |  | [optional] 
**order_number** | **int** |  | 
**media_url** | **str** |  | [optional] 
**additional_info_url** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_lounge_update_params import WTLoungeUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTLoungeUpdateParams from a JSON string
wt_lounge_update_params_instance = WTLoungeUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTLoungeUpdateParams.to_json()

# convert the object into a dict
wt_lounge_update_params_dict = wt_lounge_update_params_instance.to_dict()
# create an instance of WTLoungeUpdateParams from a dict
wt_lounge_update_params_form_dict = wt_lounge_update_params.from_dict(wt_lounge_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


