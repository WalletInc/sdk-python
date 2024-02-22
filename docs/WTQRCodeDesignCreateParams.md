# WTQRCodeDesignCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**size** | **int** |  | 
**margin** | **int** |  | 
**is_margin_white** | **bool** |  | 
**corner_radius** | **int** |  | 
**color_dark_hex** | **str** |  | 
**color_light_hex** | **str** |  | 
**background_dimming_hex** | **str** |  | 
**logo_image_url** | **str** |  | [optional] 
**background_image_url** | **str** |  | [optional] 
**animated_gif_background_url** | **str** |  | [optional] 

## Example

```python
from wallet.models.wtqr_code_design_create_params import WTQRCodeDesignCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTQRCodeDesignCreateParams from a JSON string
wtqr_code_design_create_params_instance = WTQRCodeDesignCreateParams.from_json(json)
# print the JSON string representation of the object
print WTQRCodeDesignCreateParams.to_json()

# convert the object into a dict
wtqr_code_design_create_params_dict = wtqr_code_design_create_params_instance.to_dict()
# create an instance of WTQRCodeDesignCreateParams from a dict
wtqr_code_design_create_params_form_dict = wtqr_code_design_create_params.from_dict(wtqr_code_design_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


