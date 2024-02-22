# PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherSourceID

From T, pick a set of properties whose keys are in the union K

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

## Example

```python
from wallet.models.pick_create_static_voucher_campaign_with_voucher_exclude_keyofcreate_static_voucher_campaign_with_voucher_source_id import PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherSourceID

# TODO update the JSON string below
json = "{}"
# create an instance of PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherSourceID from a JSON string
pick_create_static_voucher_campaign_with_voucher_exclude_keyofcreate_static_voucher_campaign_with_voucher_source_id_instance = PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherSourceID.from_json(json)
# print the JSON string representation of the object
print PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherSourceID.to_json()

# convert the object into a dict
pick_create_static_voucher_campaign_with_voucher_exclude_keyofcreate_static_voucher_campaign_with_voucher_source_id_dict = pick_create_static_voucher_campaign_with_voucher_exclude_keyofcreate_static_voucher_campaign_with_voucher_source_id_instance.to_dict()
# create an instance of PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherSourceID from a dict
pick_create_static_voucher_campaign_with_voucher_exclude_keyofcreate_static_voucher_campaign_with_voucher_source_id_form_dict = pick_create_static_voucher_campaign_with_voucher_exclude_keyofcreate_static_voucher_campaign_with_voucher_source_id.from_dict(pick_create_static_voucher_campaign_with_voucher_exclude_keyofcreate_static_voucher_campaign_with_voucher_source_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


