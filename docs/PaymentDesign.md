# PaymentDesign


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
**employee_id** | **str** |  | 
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 

## Example

```python
from wallet.models.payment_design import PaymentDesign

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDesign from a JSON string
payment_design_instance = PaymentDesign.from_json(json)
# print the JSON string representation of the object
print PaymentDesign.to_json()

# convert the object into a dict
payment_design_dict = payment_design_instance.to_dict()
# create an instance of PaymentDesign from a dict
payment_design_form_dict = payment_design.from_dict(payment_design_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


