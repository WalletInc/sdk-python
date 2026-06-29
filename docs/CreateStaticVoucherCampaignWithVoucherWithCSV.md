# CreateStaticVoucherCampaignWithVoucherWithCSV


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date_time** | **object** |  | 
**expiration_date_time** | **object** |  | 
**title** | **object** |  | 
**notes** | **object** |  | 
**value_type** | [**StaticVoucherCampaignValueType**](StaticVoucherCampaignValueType.md) |  | 
**display_value** | **object** |  | [optional] 
**merchants_reference_id** | **object** |  | [optional] 
**valid_only_at_pos_register_ids** | **object** |  | [optional] 
**payment_design_id** | **str** |  | 
**bucket** | **object** |  | 
**file_name** | **object** |  | 
**source_id** | **object** |  | 
**campaign_group_id** | **str** |  | [optional] 

## Example

```python
from wallet.models.create_static_voucher_campaign_with_voucher_with_csv import CreateStaticVoucherCampaignWithVoucherWithCSV

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStaticVoucherCampaignWithVoucherWithCSV from a JSON string
create_static_voucher_campaign_with_voucher_with_csv_instance = CreateStaticVoucherCampaignWithVoucherWithCSV.from_json(json)
# print the JSON string representation of the object
print CreateStaticVoucherCampaignWithVoucherWithCSV.to_json()

# convert the object into a dict
create_static_voucher_campaign_with_voucher_with_csv_dict = create_static_voucher_campaign_with_voucher_with_csv_instance.to_dict()
# create an instance of CreateStaticVoucherCampaignWithVoucherWithCSV from a dict
create_static_voucher_campaign_with_voucher_with_csv_form_dict = create_static_voucher_campaign_with_voucher_with_csv.from_dict(create_static_voucher_campaign_with_voucher_with_csv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


