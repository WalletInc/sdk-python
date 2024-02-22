# WTDynamicVoucher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** |  | 
**expiration_date** | **datetime** |  | 
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
**title** | **str** |  | 
**notes** | **str** |  | 
**merchants_reference_id** | **str** |  | [optional] 
**valid_only_at_pos_register_ids** | **List[str]** |  | [optional] 
**payment_design_id** | **str** |  | 
**employee_id** | **str** |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**starting_value** | **int** |  | 
**max_budget** | **int** |  | 
**temporal_decrease_amount** | **int** |  | 
**temporal_decrease_frequency** | **int** |  | 
**numerical_decrease_amount** | **int** |  | [optional] 
**numerical_decrease_frequency** | **int** |  | [optional] 
**temporal_decrease_amount_decimal** | **str** |  | 
**temporal_decrease_amount_string** | **str** |  | 
**numerical_decrease_amount_decimal** | **str** |  | 
**numerical_decrease_amount_string** | **str** |  | 
**starting_value_decimal** | **str** |  | 
**starting_value_string** | **str** |  | 
**max_budget_decimal** | **str** |  | 
**max_budget_string** | **str** |  | 
**current_value** | **float** |  | 
**current_value_decimal** | **str** |  | 
**current_value_string** | **str** |  | 
**status** | [**WTDynamicVoucherSummaryStatus**](WTDynamicVoucherSummaryStatus.md) |  | 
**temporal_decrease_frequency_type** | [**DynamicVoucherTemporalDecreaseFrequencyType**](DynamicVoucherTemporalDecreaseFrequencyType.md) |  | 
**summary** | [**WTDynamicVoucherSummary**](WTDynamicVoucherSummary.md) |  | 

## Example

```python
from wallet.models.wt_dynamic_voucher import WTDynamicVoucher

# TODO update the JSON string below
json = "{}"
# create an instance of WTDynamicVoucher from a JSON string
wt_dynamic_voucher_instance = WTDynamicVoucher.from_json(json)
# print the JSON string representation of the object
print WTDynamicVoucher.to_json()

# convert the object into a dict
wt_dynamic_voucher_dict = wt_dynamic_voucher_instance.to_dict()
# create an instance of WTDynamicVoucher from a dict
wt_dynamic_voucher_form_dict = wt_dynamic_voucher.from_dict(wt_dynamic_voucher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


