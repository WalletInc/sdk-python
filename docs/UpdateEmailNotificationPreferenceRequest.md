# UpdateEmailNotificationPreferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_email_notification_disabled** | **bool** |  | [optional] 

## Example

```python
from wallet.models.update_email_notification_preference_request import UpdateEmailNotificationPreferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEmailNotificationPreferenceRequest from a JSON string
update_email_notification_preference_request_instance = UpdateEmailNotificationPreferenceRequest.from_json(json)
# print the JSON string representation of the object
print UpdateEmailNotificationPreferenceRequest.to_json()

# convert the object into a dict
update_email_notification_preference_request_dict = update_email_notification_preference_request_instance.to_dict()
# create an instance of UpdateEmailNotificationPreferenceRequest from a dict
update_email_notification_preference_request_form_dict = update_email_notification_preference_request.from_dict(update_email_notification_preference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


