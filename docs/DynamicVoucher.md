# DynamicVoucher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **object** |  | 
**expiration_date** | **object** |  | 
**id** | [**StaticVoucherId**](StaticVoucherId.md) |  | 
**title** | **object** |  | 
**notes** | **object** |  | 
**merchants_reference_id** | **object** |  | [optional] 
**valid_only_at_pos_register_ids** | **object** |  | [optional] 
**payment_design_id** | **str** |  | 
**employee_id** | **str** |  | 
**merchant_id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**starting_value** | **object** |  | 
**max_budget** | **object** |  | 
**temporal_decrease_amount** | **object** |  | 
**temporal_decrease_frequency** | **object** |  | 
**numerical_decrease_amount** | **object** |  | [optional] 
**numerical_decrease_frequency** | **object** |  | [optional] 
**temporal_decrease_amount_decimal** | **object** |  | 
**temporal_decrease_amount_string** | **object** |  | 
**numerical_decrease_amount_decimal** | **object** |  | 
**numerical_decrease_amount_string** | **object** |  | 
**starting_value_decimal** | **object** |  | 
**starting_value_string** | **object** |  | 
**max_budget_decimal** | **object** |  | 
**max_budget_string** | **object** |  | 
**current_value** | **object** |  | 
**current_value_decimal** | **object** |  | 
**current_value_string** | **object** |  | 
**status** | [**WTDynamicVoucherSummaryStatus**](WTDynamicVoucherSummaryStatus.md) |  | 
**temporal_decrease_frequency_type** | [**DynamicVoucherTemporalDecreaseFrequencyType**](DynamicVoucherTemporalDecreaseFrequencyType.md) |  | 
**summary** | [**WTDynamicVoucherSummary**](WTDynamicVoucherSummary.md) |  | 

## Example

```python
from wallet.models.dynamic_voucher import DynamicVoucher

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicVoucher from a JSON string
dynamic_voucher_instance = DynamicVoucher.from_json(json)
# print the JSON string representation of the object
print DynamicVoucher.to_json()

# convert the object into a dict
dynamic_voucher_dict = dynamic_voucher_instance.to_dict()
# create an instance of DynamicVoucher from a dict
dynamic_voucher_form_dict = dynamic_voucher.from_dict(dynamic_voucher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


