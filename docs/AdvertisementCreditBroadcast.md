# AdvertisementCreditBroadcast


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
**advertisement_credit** | [**AdvertisementCredit**](AdvertisementCredit.md) |  | 

## Example

```python
from wallet.models.advertisement_credit_broadcast import AdvertisementCreditBroadcast

# TODO update the JSON string below
json = "{}"
# create an instance of AdvertisementCreditBroadcast from a JSON string
advertisement_credit_broadcast_instance = AdvertisementCreditBroadcast.from_json(json)
# print the JSON string representation of the object
print AdvertisementCreditBroadcast.to_json()

# convert the object into a dict
advertisement_credit_broadcast_dict = advertisement_credit_broadcast_instance.to_dict()
# create an instance of AdvertisementCreditBroadcast from a dict
advertisement_credit_broadcast_form_dict = advertisement_credit_broadcast.from_dict(advertisement_credit_broadcast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


