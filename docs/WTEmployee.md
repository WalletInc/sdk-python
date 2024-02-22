# WTEmployee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**phone_number** | **str** |  | 
**is_public_representative** | **bool** |  | 
**wallet_sequence_number** | **int** |  | 
**employee_id** | **str** |  | 
**job_title** | **str** |  | 
**department** | **str** |  | 
**schedule_start_day** | [**EmployeeScheduleStartDay**](EmployeeScheduleStartDay.md) |  | [optional] 
**schedule_start_hour** | [**EmployeeScheduleStartHour**](EmployeeScheduleStartHour.md) |  | [optional] 
**schedule_start_minute** | [**EmployeeScheduleStartMinute**](EmployeeScheduleStartMinute.md) |  | [optional] 
**schedule_start_meridiem** | [**EmployeeScheduleStartMeridiem**](EmployeeScheduleStartMeridiem.md) |  | [optional] 
**schedule_end_day** | [**EmployeeScheduleStartDay**](EmployeeScheduleStartDay.md) |  | [optional] 
**schedule_end_hour** | [**EmployeeScheduleStartHour**](EmployeeScheduleStartHour.md) |  | [optional] 
**schedule_end_minute** | [**EmployeeScheduleStartMinute**](EmployeeScheduleStartMinute.md) |  | [optional] 
**schedule_end_meridiem** | [**EmployeeScheduleStartMeridiem**](EmployeeScheduleStartMeridiem.md) |  | [optional] 
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**username** | **str** |  | 
**email_verified** | **str** |  | 
**profile_picture_url** | **str** |  | 
**merchant_id** | **str** |  | 
**session_token** | **str** |  | 
**failed_login_attempts** | **float** |  | [optional] 
**last_login_date** | **datetime** |  | [optional] 
**cfuvid** | **str** |  | [optional] 
**schedule** | **object** |  | [optional] 
**is_email_notification_disabled** | **bool** |  | [optional] 

## Example

```python
from wallet.models.wt_employee import WTEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployee from a JSON string
wt_employee_instance = WTEmployee.from_json(json)
# print the JSON string representation of the object
print WTEmployee.to_json()

# convert the object into a dict
wt_employee_dict = wt_employee_instance.to_dict()
# create an instance of WTEmployee from a dict
wt_employee_form_dict = wt_employee.from_dict(wt_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


