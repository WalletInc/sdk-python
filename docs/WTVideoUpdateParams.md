# WTVideoUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | 
**order_number** | **int** |  | 
**media_url** | **str** |  | 
**additional_info_url** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_video_update_params import WTVideoUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTVideoUpdateParams from a JSON string
wt_video_update_params_instance = WTVideoUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTVideoUpdateParams.to_json()

# convert the object into a dict
wt_video_update_params_dict = wt_video_update_params_instance.to_dict()
# create an instance of WTVideoUpdateParams from a dict
wt_video_update_params_form_dict = wt_video_update_params.from_dict(wt_video_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


