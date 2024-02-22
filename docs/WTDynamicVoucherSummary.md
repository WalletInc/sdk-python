# WTDynamicVoucherSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calc_error** | **bool** |  | 
**calc_error_details** | **str** |  | 
**current_value** | **float** |  | 
**current_value_decimal** | **str** |  | 
**current_value_string** | **str** |  | 
**time_value_zero** | **bool** |  | 
**time_value_zero_subtracted_amount** | **float** |  | 
**total_number_redeemed** | **float** |  | 
**total_value_redeemed** | **float** |  | 
**total_budget_remaining** | **float** |  | 
**maximum_budget_exhausted** | **bool** |  | 
**maximum_budget_exhausted_by** | **float** |  | 
**maximum_budget_exhausted_by_decimal** | **str** |  | 
**maximum_budget_exhausted_by_string** | **str** |  | 
**maximum_budget_exhausted_total_value_redeemed** | **float** |  | 
**maximum_budget_exhausted_total_value_redeemed_decimal** | **str** |  | 
**maximum_budget_exhausted_total_value_redeemed_string** | **str** |  | 
**total_amount_subtracted** | **float** |  | 
**total_amount_subtracted_decimal** | **str** |  | 
**total_amount_subtracted_string** | **str** |  | 
**total_decremented_multiple** | **float** |  | 
**redeemed_keys** | **List[str]** |  | 
**status** | [**WTDynamicVoucherSummaryStatus**](WTDynamicVoucherSummaryStatus.md) |  | 
**expired** | **bool** |  | 

## Example

```python
from wallet.models.wt_dynamic_voucher_summary import WTDynamicVoucherSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WTDynamicVoucherSummary from a JSON string
wt_dynamic_voucher_summary_instance = WTDynamicVoucherSummary.from_json(json)
# print the JSON string representation of the object
print WTDynamicVoucherSummary.to_json()

# convert the object into a dict
wt_dynamic_voucher_summary_dict = wt_dynamic_voucher_summary_instance.to_dict()
# create an instance of WTDynamicVoucherSummary from a dict
wt_dynamic_voucher_summary_form_dict = wt_dynamic_voucher_summary.from_dict(wt_dynamic_voucher_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


