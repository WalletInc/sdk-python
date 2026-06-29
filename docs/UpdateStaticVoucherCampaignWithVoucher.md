# UpdateStaticVoucherCampaignWithVoucher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** |  | 
**notes** | **object** |  | 
**value_type** | [**StaticVoucherCampaignValueType**](StaticVoucherCampaignValueType.md) |  | 
**display_value** | **object** |  | [optional] 
**merchants_reference_id** | **object** |  | [optional] 
**valid_only_at_pos_register_ids** | **object** |  | [optional] 
**payment_design_id** | **str** |  | 
**start_date_time** | **object** |  | 
**expiration_date_time** | **object** |  | 
**member_id** | **object** |  | [optional] 
**offer_amount_cents** | **object** |  | 
**cell_phone** | **object** |  | [optional] 
**voucher_id** | **str** |  | 

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


