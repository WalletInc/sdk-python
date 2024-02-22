# SmsSubscriber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile_number** | **str** |  | 
**id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.sms_subscriber import SmsSubscriber

# TODO update the JSON string below
json = "{}"
# create an instance of SmsSubscriber from a JSON string
sms_subscriber_instance = SmsSubscriber.from_json(json)
# print the JSON string representation of the object
print SmsSubscriber.to_json()

# convert the object into a dict
sms_subscriber_dict = sms_subscriber_instance.to_dict()
# create an instance of SmsSubscriber from a dict
sms_subscriber_form_dict = sms_subscriber.from_dict(sms_subscriber_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


