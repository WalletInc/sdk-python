# PickVSDynamicVoucherExcludeKeyofVSDynamicVoucherTemporalDecreaseFrequencyType

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** |  | 
**expiration_date** | **datetime** |  | 
**id** | **str** |  | 
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

## Example

```python
from wallet.models.pick_vs_dynamic_voucher_exclude_keyof_vs_dynamic_voucher_temporal_decrease_frequency_type import PickVSDynamicVoucherExcludeKeyofVSDynamicVoucherTemporalDecreaseFrequencyType

# TODO update the JSON string below
json = "{}"
# create an instance of PickVSDynamicVoucherExcludeKeyofVSDynamicVoucherTemporalDecreaseFrequencyType from a JSON string
pick_vs_dynamic_voucher_exclude_keyof_vs_dynamic_voucher_temporal_decrease_frequency_type_instance = PickVSDynamicVoucherExcludeKeyofVSDynamicVoucherTemporalDecreaseFrequencyType.from_json(json)
# print the JSON string representation of the object
print PickVSDynamicVoucherExcludeKeyofVSDynamicVoucherTemporalDecreaseFrequencyType.to_json()

# convert the object into a dict
pick_vs_dynamic_voucher_exclude_keyof_vs_dynamic_voucher_temporal_decrease_frequency_type_dict = pick_vs_dynamic_voucher_exclude_keyof_vs_dynamic_voucher_temporal_decrease_frequency_type_instance.to_dict()
# create an instance of PickVSDynamicVoucherExcludeKeyofVSDynamicVoucherTemporalDecreaseFrequencyType from a dict
pick_vs_dynamic_voucher_exclude_keyof_vs_dynamic_voucher_temporal_decrease_frequency_type_form_dict = pick_vs_dynamic_voucher_exclude_keyof_vs_dynamic_voucher_temporal_decrease_frequency_type.from_dict(pick_vs_dynamic_voucher_exclude_keyof_vs_dynamic_voucher_temporal_decrease_frequency_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


