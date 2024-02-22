# WTEmployeeNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WTEmployeeNotificationType**](WTEmployeeNotificationType.md) |  | 
**title** | **str** |  | 
**content** | **str** |  | 
**payload** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_employee_notification import WTEmployeeNotification

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeNotification from a JSON string
wt_employee_notification_instance = WTEmployeeNotification.from_json(json)
# print the JSON string representation of the object
print WTEmployeeNotification.to_json()

# convert the object into a dict
wt_employee_notification_dict = wt_employee_notification_instance.to_dict()
# create an instance of WTEmployeeNotification from a dict
wt_employee_notification_form_dict = wt_employee_notification.from_dict(wt_employee_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


