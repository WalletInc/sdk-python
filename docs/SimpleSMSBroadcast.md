# SimpleSMSBroadcast


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

## Example

```python
from wallet.models.simple_sms_broadcast import SimpleSMSBroadcast

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleSMSBroadcast from a JSON string
simple_sms_broadcast_instance = SimpleSMSBroadcast.from_json(json)
# print the JSON string representation of the object
print SimpleSMSBroadcast.to_json()

# convert the object into a dict
simple_sms_broadcast_dict = simple_sms_broadcast_instance.to_dict()
# create an instance of SimpleSMSBroadcast from a dict
simple_sms_broadcast_form_dict = simple_sms_broadcast.from_dict(simple_sms_broadcast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


