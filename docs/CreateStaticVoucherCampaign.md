# CreateStaticVoucherCampaign


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
**bucket** | **object** |  | [optional] 
**file_name** | **object** |  | [optional] 
**source_id** | **object** |  | 
**campaign_group_id** | **str** |  | [optional] 

## Example

```python
from wallet.models.create_static_voucher_campaign import CreateStaticVoucherCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStaticVoucherCampaign from a JSON string
create_static_voucher_campaign_instance = CreateStaticVoucherCampaign.from_json(json)
# print the JSON string representation of the object
print CreateStaticVoucherCampaign.to_json()

# convert the object into a dict
create_static_voucher_campaign_dict = create_static_voucher_campaign_instance.to_dict()
# create an instance of CreateStaticVoucherCampaign from a dict
create_static_voucher_campaign_form_dict = create_static_voucher_campaign.from_dict(create_static_voucher_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


