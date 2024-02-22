# PickWTPaymentObjectBroadcastExcludeKeyofWTPaymentObjectBroadcastListTypeOrListID

From T, pick a set of properties whose keys are in the union K

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

## Example

```python
from wallet.models.pick_wt_payment_object_broadcast_exclude_keyof_wt_payment_object_broadcast_list_type_or_list_id import PickWTPaymentObjectBroadcastExcludeKeyofWTPaymentObjectBroadcastListTypeOrListID

# TODO update the JSON string below
json = "{}"
# create an instance of PickWTPaymentObjectBroadcastExcludeKeyofWTPaymentObjectBroadcastListTypeOrListID from a JSON string
pick_wt_payment_object_broadcast_exclude_keyof_wt_payment_object_broadcast_list_type_or_list_id_instance = PickWTPaymentObjectBroadcastExcludeKeyofWTPaymentObjectBroadcastListTypeOrListID.from_json(json)
# print the JSON string representation of the object
print PickWTPaymentObjectBroadcastExcludeKeyofWTPaymentObjectBroadcastListTypeOrListID.to_json()

# convert the object into a dict
pick_wt_payment_object_broadcast_exclude_keyof_wt_payment_object_broadcast_list_type_or_list_id_dict = pick_wt_payment_object_broadcast_exclude_keyof_wt_payment_object_broadcast_list_type_or_list_id_instance.to_dict()
# create an instance of PickWTPaymentObjectBroadcastExcludeKeyofWTPaymentObjectBroadcastListTypeOrListID from a dict
pick_wt_payment_object_broadcast_exclude_keyof_wt_payment_object_broadcast_list_type_or_list_id_form_dict = pick_wt_payment_object_broadcast_exclude_keyof_wt_payment_object_broadcast_list_type_or_list_id.from_dict(pick_wt_payment_object_broadcast_exclude_keyof_wt_payment_object_broadcast_list_type_or_list_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


