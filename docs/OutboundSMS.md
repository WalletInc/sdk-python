# OutboundSMS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**StaticVoucherId**](StaticVoucherId.md) |  | 
**employee_id** | **str** |  | 
**status** | [**OutboundSMSStatus**](OutboundSMSStatus.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**is_active** | **object** |  | 
**body** | **object** |  | 
**phone_number_id** | **str** |  | 
**media_urls** | **object** |  | 
**payment_object_broadcast_id** | [**OutboundSMSPaymentObjectBroadcastID**](OutboundSMSPaymentObjectBroadcastID.md) |  | [optional] 
**body_template** | **object** |  | 
**status_callback** | **object** |  | 
**is_sent** | **object** |  | 
**sent_at** | **object** |  | [optional] 
**delivered_at** | **object** |  | [optional] 
**message_sid** | **object** |  | 
**num_segments** | **object** |  | [optional] 
**num_media** | **object** |  | [optional] 
**error_code** | **object** |  | [optional] 
**error_message** | **object** |  | [optional] 
**to** | **object** |  | 

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


