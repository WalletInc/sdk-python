# WTDynamicVoucherSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calc_error** | **object** |  | 
**calc_error_details** | **object** |  | 
**current_value** | **object** |  | 
**current_value_decimal** | **object** |  | 
**current_value_string** | **object** |  | 
**time_value_zero** | **object** |  | 
**time_value_zero_subtracted_amount** | **object** |  | 
**total_number_redeemed** | **object** |  | 
**total_value_redeemed** | **object** |  | 
**total_budget_remaining** | **object** |  | 
**maximum_budget_exhausted** | **object** |  | 
**maximum_budget_exhausted_by** | **object** |  | 
**maximum_budget_exhausted_by_decimal** | **object** |  | 
**maximum_budget_exhausted_by_string** | **object** |  | 
**maximum_budget_exhausted_total_value_redeemed** | **object** |  | 
**maximum_budget_exhausted_total_value_redeemed_decimal** | **object** |  | 
**maximum_budget_exhausted_total_value_redeemed_string** | **object** |  | 
**total_amount_subtracted** | **object** |  | 
**total_amount_subtracted_decimal** | **object** |  | 
**total_amount_subtracted_string** | **object** |  | 
**total_decremented_multiple** | **object** |  | 
**redeemed_keys** | **object** |  | 
**status** | [**WTDynamicVoucherSummaryStatus**](WTDynamicVoucherSummaryStatus.md) |  | 
**expired** | **object** |  | 

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


