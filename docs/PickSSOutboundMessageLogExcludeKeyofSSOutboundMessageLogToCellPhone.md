# PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhone

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**employee_id** | **str** |  | 
**status** | [**PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhoneStatus**](PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhoneStatus.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**body** | **str** |  | 
**phone_number_id** | **str** |  | 
**media_urls** | **List[str]** |  | 
**payment_object_broadcast_id** | [**PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhonePaymentObjectBroadcastID**](PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhonePaymentObjectBroadcastID.md) |  | [optional] 
**body_template** | **str** |  | 
**status_callback** | **str** |  | 
**is_sent** | **bool** |  | 
**sent_at** | **datetime** |  | [optional] 
**delivered_at** | **datetime** |  | [optional] 
**message_sid** | **str** |  | 
**num_segments** | **int** |  | [optional] 
**num_media** | **int** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from wallet.models.pick_ss_outbound_message_log_exclude_keyof_ss_outbound_message_log_to_cell_phone import PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhone

# TODO update the JSON string below
json = "{}"
# create an instance of PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhone from a JSON string
pick_ss_outbound_message_log_exclude_keyof_ss_outbound_message_log_to_cell_phone_instance = PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhone.from_json(json)
# print the JSON string representation of the object
print PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhone.to_json()

# convert the object into a dict
pick_ss_outbound_message_log_exclude_keyof_ss_outbound_message_log_to_cell_phone_dict = pick_ss_outbound_message_log_exclude_keyof_ss_outbound_message_log_to_cell_phone_instance.to_dict()
# create an instance of PickSSOutboundMessageLogExcludeKeyofSSOutboundMessageLogToCellPhone from a dict
pick_ss_outbound_message_log_exclude_keyof_ss_outbound_message_log_to_cell_phone_form_dict = pick_ss_outbound_message_log_exclude_keyof_ss_outbound_message_log_to_cell_phone.from_dict(pick_ss_outbound_message_log_exclude_keyof_ss_outbound_message_log_to_cell_phone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


