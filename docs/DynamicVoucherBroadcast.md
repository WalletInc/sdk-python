# DynamicVoucherBroadcast


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number_id** | **str** |  | 
**payment_object_prefix** | [**StaticVoucherCampaignBroadcastPaymentObjectPrefix**](StaticVoucherCampaignBroadcastPaymentObjectPrefix.md) |  | 
**payment_object_id** | **str** |  | 
**message_template** | **object** |  | 
**media_urls** | **object** |  | 
**employee_id** | **str** |  | 
**broadcast_scheduled_at** | **object** |  | 
**id** | [**StaticVoucherId**](StaticVoucherId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**broadcast_status** | [**StaticVoucherCampaignBroadcastBroadcastStatus**](StaticVoucherCampaignBroadcastBroadcastStatus.md) |  | 
**broadcast_queued_at** | **object** |  | 
**broadcast_started_at** | **object** |  | 
**broadcast_completed_at** | **object** |  | 
**list_type** | [**DynamicVoucherBroadcastListType**](DynamicVoucherBroadcastListType.md) |  | 
**list_id** | **str** |  | 
**opt_in_list** | [**WTOptInList**](WTOptInList.md) |  | [optional] 
**imported_list** | [**WTImportedList**](WTImportedList.md) |  | [optional] 
**dynamic_voucher** | [**DynamicVoucher**](DynamicVoucher.md) |  | 

## Example

```python
from wallet.models.dynamic_voucher_broadcast import DynamicVoucherBroadcast

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicVoucherBroadcast from a JSON string
dynamic_voucher_broadcast_instance = DynamicVoucherBroadcast.from_json(json)
# print the JSON string representation of the object
print DynamicVoucherBroadcast.to_json()

# convert the object into a dict
dynamic_voucher_broadcast_dict = dynamic_voucher_broadcast_instance.to_dict()
# create an instance of DynamicVoucherBroadcast from a dict
dynamic_voucher_broadcast_form_dict = dynamic_voucher_broadcast.from_dict(dynamic_voucher_broadcast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


