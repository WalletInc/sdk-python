# WTStaticVoucherCampaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**StaticVoucherId**](StaticVoucherId.md) |  | 
**title** | **object** |  | 
**notes** | **object** |  | 
**value_type** | [**StaticVoucherCampaignValueType**](StaticVoucherCampaignValueType.md) |  | 
**is_loaded** | **object** |  | 
**display_value** | **object** |  | [optional] 
**merchants_reference_id** | **object** |  | [optional] 
**valid_only_at_pos_register_ids** | **object** |  | [optional] 
**payment_design_id** | **str** |  | 
**employee_id** | **str** |  | 
**reinvestment_sum** | **object** |  | 
**number_of_vouchers_in_file** | **object** |  | 
**campaign_group_id** | **str** |  | [optional] 
**bucket** | **object** |  | [optional] 
**created_by_source_id** | **object** |  | 
**original_file_name** | **object** |  | [optional] 
**merchant_id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**voucher_type** | **object** |  | 
**reinvestment_sum_decimal** | **object** |  | 
**reinvestment_sum_string** | **object** |  | 
**start_date** | **object** |  | 
**expiration_date** | **object** |  | 

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


