# WTImageGridCreateParams


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
from wallet.models.wt_image_grid_create_params import WTImageGridCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTImageGridCreateParams from a JSON string
wt_image_grid_create_params_instance = WTImageGridCreateParams.from_json(json)
# print the JSON string representation of the object
print WTImageGridCreateParams.to_json()

# convert the object into a dict
wt_image_grid_create_params_dict = wt_image_grid_create_params_instance.to_dict()
# create an instance of WTImageGridCreateParams from a dict
wt_image_grid_create_params_form_dict = wt_image_grid_create_params.from_dict(wt_image_grid_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


