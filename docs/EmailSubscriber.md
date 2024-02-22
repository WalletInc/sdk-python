# EmailSubscriber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email_address** | **str** |  | 
**id** | [**SaveTicketSettingsRequestPaymentDesignID**](SaveTicketSettingsRequestPaymentDesignID.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.email_subscriber import EmailSubscriber

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSubscriber from a JSON string
email_subscriber_instance = EmailSubscriber.from_json(json)
# print the JSON string representation of the object
print EmailSubscriber.to_json()

# convert the object into a dict
email_subscriber_dict = email_subscriber_instance.to_dict()
# create an instance of EmailSubscriber from a dict
email_subscriber_form_dict = email_subscriber.from_dict(email_subscriber_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


