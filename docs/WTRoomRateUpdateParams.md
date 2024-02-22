# WTRoomRateUpdateParams


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
from wallet.models.wt_room_rate_update_params import WTRoomRateUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTRoomRateUpdateParams from a JSON string
wt_room_rate_update_params_instance = WTRoomRateUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTRoomRateUpdateParams.to_json()

# convert the object into a dict
wt_room_rate_update_params_dict = wt_room_rate_update_params_instance.to_dict()
# create an instance of WTRoomRateUpdateParams from a dict
wt_room_rate_update_params_form_dict = wt_room_rate_update_params.from_dict(wt_room_rate_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


