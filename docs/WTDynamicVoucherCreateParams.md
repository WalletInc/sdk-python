# WTDynamicVoucherCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**notes** | **str** |  | 
**payment_design_id** | **str** |  | 
**date_time_start** | **datetime** |  | 
**date_time_expiration** | **datetime** |  | 
**starting_value** | **int** |  | 
**max_budget** | **int** |  | 
**decrease_amount** | **int** |  | 
**frequency** | **int** |  | 
**frequency_type** | [**DynamicVoucherTemporalDecreaseFrequencyType**](DynamicVoucherTemporalDecreaseFrequencyType.md) |  | 
**decrease_by** | **float** |  | [optional] 
**decrease_every** | **float** |  | [optional] 

## Example

```python
from wallet.models.wt_dynamic_voucher_create_params import WTDynamicVoucherCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTDynamicVoucherCreateParams from a JSON string
wt_dynamic_voucher_create_params_instance = WTDynamicVoucherCreateParams.from_json(json)
# print the JSON string representation of the object
print WTDynamicVoucherCreateParams.to_json()

# convert the object into a dict
wt_dynamic_voucher_create_params_dict = wt_dynamic_voucher_create_params_instance.to_dict()
# create an instance of WTDynamicVoucherCreateParams from a dict
wt_dynamic_voucher_create_params_form_dict = wt_dynamic_voucher_create_params.from_dict(wt_dynamic_voucher_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


