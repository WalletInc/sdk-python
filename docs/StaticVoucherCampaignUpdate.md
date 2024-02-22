# StaticVoucherCampaignUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date_time** | **datetime** |  | 
**expiration_date_time** | **datetime** |  | 
**title** | **str** |  | 
**notes** | **str** |  | 
**value_type** | [**PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType**](PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType.md) |  | 
**display_value** | **str** |  | [optional] 
**merchants_reference_id** | **str** |  | [optional] 
**valid_only_at_pos_register_ids** | **List[str]** |  | [optional] 
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


