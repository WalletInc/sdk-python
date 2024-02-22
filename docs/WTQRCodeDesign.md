# WTQRCodeDesign


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
**id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.wtqr_code_design import WTQRCodeDesign

# TODO update the JSON string below
json = "{}"
# create an instance of WTQRCodeDesign from a JSON string
wtqr_code_design_instance = WTQRCodeDesign.from_json(json)
# print the JSON string representation of the object
print WTQRCodeDesign.to_json()

# convert the object into a dict
wtqr_code_design_dict = wtqr_code_design_instance.to_dict()
# create an instance of WTQRCodeDesign from a dict
wtqr_code_design_form_dict = wtqr_code_design.from_dict(wtqr_code_design_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


