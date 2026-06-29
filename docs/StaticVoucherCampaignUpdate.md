# StaticVoucherCampaignUpdate


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

## Example

```python
from wallet.models.static_voucher_campaign_update import StaticVoucherCampaignUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of StaticVoucherCampaignUpdate from a JSON string
static_voucher_campaign_update_instance = StaticVoucherCampaignUpdate.from_json(json)
# print the JSON string representation of the object
print StaticVoucherCampaignUpdate.to_json()

# convert the object into a dict
static_voucher_campaign_update_dict = static_voucher_campaign_update_instance.to_dict()
# create an instance of StaticVoucherCampaignUpdate from a dict
static_voucher_campaign_update_form_dict = static_voucher_campaign_update.from_dict(static_voucher_campaign_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


