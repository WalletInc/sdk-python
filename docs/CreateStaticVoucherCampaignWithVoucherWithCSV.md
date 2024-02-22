# CreateStaticVoucherCampaignWithVoucherWithCSV


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
**bucket** | **str** |  | 
**file_name** | **str** |  | 
**source_id** | **int** |  | 
**campaign_group_id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | [optional] 

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


