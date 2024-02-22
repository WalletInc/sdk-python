# WTImageGridUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**url** | **str** |  | 
**media_url** | **str** |  | 
**sequence_number** | **int** |  | 
**is_pinned** | **bool** |  | [optional] 

## Example

```python
from wallet.models.wt_image_grid_update_params import WTImageGridUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTImageGridUpdateParams from a JSON string
wt_image_grid_update_params_instance = WTImageGridUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTImageGridUpdateParams.to_json()

# convert the object into a dict
wt_image_grid_update_params_dict = wt_image_grid_update_params_instance.to_dict()
# create an instance of WTImageGridUpdateParams from a dict
wt_image_grid_update_params_form_dict = wt_image_grid_update_params.from_dict(wt_image_grid_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


