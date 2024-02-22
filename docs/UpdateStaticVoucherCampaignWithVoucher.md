# UpdateStaticVoucherCampaignWithVoucher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**notes** | **str** |  | 
**value_type** | [**PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType**](PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType.md) |  | 
**display_value** | **str** |  | [optional] 
**merchants_reference_id** | **str** |  | [optional] 
**valid_only_at_pos_register_ids** | **List[str]** |  | [optional] 
**payment_design_id** | **str** |  | 
**start_date_time** | **datetime** |  | 
**expiration_date_time** | **datetime** |  | 
**member_id** | **str** |  | [optional] 
**offer_amount_cents** | **int** |  | 
**cell_phone** | **str** |  | [optional] 
**voucher_id** | [**UpdateStaticVoucherCampaignWithVoucherVoucherID**](UpdateStaticVoucherCampaignWithVoucherVoucherID.md) |  | 

## Example

```python
from wallet.models.update_static_voucher_campaign_with_voucher import UpdateStaticVoucherCampaignWithVoucher

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStaticVoucherCampaignWithVoucher from a JSON string
update_static_voucher_campaign_with_voucher_instance = UpdateStaticVoucherCampaignWithVoucher.from_json(json)
# print the JSON string representation of the object
print UpdateStaticVoucherCampaignWithVoucher.to_json()

# convert the object into a dict
update_static_voucher_campaign_with_voucher_dict = update_static_voucher_campaign_with_voucher_instance.to_dict()
# create an instance of UpdateStaticVoucherCampaignWithVoucher from a dict
update_static_voucher_campaign_with_voucher_form_dict = update_static_voucher_campaign_with_voucher.from_dict(update_static_voucher_campaign_with_voucher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


