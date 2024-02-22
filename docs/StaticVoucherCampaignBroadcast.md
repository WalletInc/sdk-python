# StaticVoucherCampaignBroadcast


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
**employee_id** | **str** |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**phone_number_id** | **str** |  | 
**media_urls** | **List[str]** |  | 
**opt_in_list** | [**WTOptInList**](WTOptInList.md) |  | [optional] 
**imported_list** | [**WTImportedList**](WTImportedList.md) |  | [optional] 
**broadcast_status** | [**PickWTPaymentObjectBroadcastExcludeKeyofWTPaymentObjectBroadcastListTypeOrListIDBroadcastStatus**](PickWTPaymentObjectBroadcastExcludeKeyofWTPaymentObjectBroadcastListTypeOrListIDBroadcastStatus.md) |  | 
**broadcast_queued_at** | **datetime** |  | 
**broadcast_started_at** | **datetime** |  | 
**broadcast_completed_at** | **datetime** |  | 
**payment_object_prefix** | [**PickWTPaymentObjectBroadcastExcludeKeyofWTPaymentObjectBroadcastListTypeOrListIDPaymentObjectPrefix**](PickWTPaymentObjectBroadcastExcludeKeyofWTPaymentObjectBroadcastListTypeOrListIDPaymentObjectPrefix.md) |  | 
**payment_object_id** | **str** |  | 
**message_template** | **str** |  | 
**broadcast_scheduled_at** | **datetime** |  | 
**static_voucher_campaign** | [**StaticVoucherCampaign**](StaticVoucherCampaign.md) |  | 

## Example

```python
from wallet.models.static_voucher_campaign_broadcast import StaticVoucherCampaignBroadcast

# TODO update the JSON string below
json = "{}"
# create an instance of StaticVoucherCampaignBroadcast from a JSON string
static_voucher_campaign_broadcast_instance = StaticVoucherCampaignBroadcast.from_json(json)
# print the JSON string representation of the object
print StaticVoucherCampaignBroadcast.to_json()

# convert the object into a dict
static_voucher_campaign_broadcast_dict = static_voucher_campaign_broadcast_instance.to_dict()
# create an instance of StaticVoucherCampaignBroadcast from a dict
static_voucher_campaign_broadcast_form_dict = static_voucher_campaign_broadcast.from_dict(static_voucher_campaign_broadcast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


