# PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDate

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**notes** | **str** |  | 
**value_type** | [**PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType**](PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType.md) |  | 
**is_loaded** | **bool** |  | 
**display_value** | **str** |  | [optional] 
**merchants_reference_id** | **str** |  | [optional] 
**valid_only_at_pos_register_ids** | **List[str]** |  | [optional] 
**payment_design_id** | **str** |  | 
**employee_id** | **str** |  | 
**reinvestment_sum** | **int** |  | 
**number_of_vouchers_in_file** | **int** |  | 

## Example

```python
from wallet.models.pick_vs_campaign_update_params_exclude_keyof_vs_campaign_update_params_start_date_or_expiration_date import PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDate

# TODO update the JSON string below
json = "{}"
# create an instance of PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDate from a JSON string
pick_vs_campaign_update_params_exclude_keyof_vs_campaign_update_params_start_date_or_expiration_date_instance = PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDate.from_json(json)
# print the JSON string representation of the object
print PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDate.to_json()

# convert the object into a dict
pick_vs_campaign_update_params_exclude_keyof_vs_campaign_update_params_start_date_or_expiration_date_dict = pick_vs_campaign_update_params_exclude_keyof_vs_campaign_update_params_start_date_or_expiration_date_instance.to_dict()
# create an instance of PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDate from a dict
pick_vs_campaign_update_params_exclude_keyof_vs_campaign_update_params_start_date_or_expiration_date_form_dict = pick_vs_campaign_update_params_exclude_keyof_vs_campaign_update_params_start_date_or_expiration_date.from_dict(pick_vs_campaign_update_params_exclude_keyof_vs_campaign_update_params_start_date_or_expiration_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


