# WTEmployeeScheduleSimpleSMS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number_id** | **str** |  | 
**message_template** | **str** |  | 
**media_urls** | **List[str]** |  | [optional] 
**broadcast_scheduled_at** | **datetime** |  | 
**list_type** | [**WTEmployeeScheduleSimpleSMSListType**](WTEmployeeScheduleSimpleSMSListType.md) |  | 
**list_id** | **str** |  | 

## Example

```python
from wallet.models.wt_employee_schedule_simple_sms import WTEmployeeScheduleSimpleSMS

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeScheduleSimpleSMS from a JSON string
wt_employee_schedule_simple_sms_instance = WTEmployeeScheduleSimpleSMS.from_json(json)
# print the JSON string representation of the object
print WTEmployeeScheduleSimpleSMS.to_json()

# convert the object into a dict
wt_employee_schedule_simple_sms_dict = wt_employee_schedule_simple_sms_instance.to_dict()
# create an instance of WTEmployeeScheduleSimpleSMS from a dict
wt_employee_schedule_simple_sms_form_dict = wt_employee_schedule_simple_sms.from_dict(wt_employee_schedule_simple_sms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


