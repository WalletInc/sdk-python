# WTPaymentDesignUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**border_color** | **str** |  | 
**border_style_type** | [**PickVSPaymentDesignUpdateParamsExcludeKeyofVSPaymentDesignUpdateParamsIdBorderStyleType**](PickVSPaymentDesignUpdateParamsExcludeKeyofVSPaymentDesignUpdateParamsIdBorderStyleType.md) |  | 
**border_size** | **str** |  | 
**border_radius** | **int** |  | 
**font_color** | **str** |  | 
**font_type** | **str** |  | 
**abbreviation** | **str** |  | 
**acronym** | **str** |  | 
**icon** | **str** |  | 
**design_name** | **str** |  | 
**display_name** | **str** |  | 
**background_image_url** | **str** |  | [optional] 
**company_logo_url** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_payment_design_update_params import WTPaymentDesignUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTPaymentDesignUpdateParams from a JSON string
wt_payment_design_update_params_instance = WTPaymentDesignUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTPaymentDesignUpdateParams.to_json()

# convert the object into a dict
wt_payment_design_update_params_dict = wt_payment_design_update_params_instance.to_dict()
# create an instance of WTPaymentDesignUpdateParams from a dict
wt_payment_design_update_params_form_dict = wt_payment_design_update_params.from_dict(wt_payment_design_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


