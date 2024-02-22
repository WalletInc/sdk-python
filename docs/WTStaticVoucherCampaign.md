# WTStaticVoucherCampaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
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
**campaign_group_id** | **str** |  | [optional] 
**bucket** | **str** |  | [optional] 
**created_by_source_id** | **int** |  | 
**original_file_name** | **str** |  | [optional] 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**voucher_type** | **float** |  | 
**reinvestment_sum_decimal** | **str** |  | 
**reinvestment_sum_string** | **str** |  | 
**start_date** | **datetime** |  | 
**expiration_date** | **datetime** |  | 

## Example

```python
from wallet.models.wt_static_voucher_campaign import WTStaticVoucherCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of WTStaticVoucherCampaign from a JSON string
wt_static_voucher_campaign_instance = WTStaticVoucherCampaign.from_json(json)
# print the JSON string representation of the object
print WTStaticVoucherCampaign.to_json()

# convert the object into a dict
wt_static_voucher_campaign_dict = wt_static_voucher_campaign_instance.to_dict()
# create an instance of WTStaticVoucherCampaign from a dict
wt_static_voucher_campaign_form_dict = wt_static_voucher_campaign.from_dict(wt_static_voucher_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


