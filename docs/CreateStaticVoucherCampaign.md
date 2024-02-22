# CreateStaticVoucherCampaign


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
**bucket** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**source_id** | **int** |  | 
**campaign_group_id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | [optional] 

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


