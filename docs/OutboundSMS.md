# OutboundSMS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
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
**to** | **str** |  | 

## Example

```python
from wallet.models.outbound_sms import OutboundSMS

# TODO update the JSON string below
json = "{}"
# create an instance of OutboundSMS from a JSON string
outbound_sms_instance = OutboundSMS.from_json(json)
# print the JSON string representation of the object
print OutboundSMS.to_json()

# convert the object into a dict
outbound_sms_dict = outbound_sms_instance.to_dict()
# create an instance of OutboundSMS from a dict
outbound_sms_form_dict = outbound_sms.from_dict(outbound_sms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


