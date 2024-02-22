# PickWTEmployeeCreateExcludeKeyofWTEmployeeCreateEmail

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**phone_number** | **str** |  | 
**is_public_representative** | **bool** |  | 
**wallet_sequence_number** | **int** |  | 
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

## Example

```python
from wallet.models.pick_wt_employee_create_exclude_keyof_wt_employee_create_email import PickWTEmployeeCreateExcludeKeyofWTEmployeeCreateEmail

# TODO update the JSON string below
json = "{}"
# create an instance of PickWTEmployeeCreateExcludeKeyofWTEmployeeCreateEmail from a JSON string
pick_wt_employee_create_exclude_keyof_wt_employee_create_email_instance = PickWTEmployeeCreateExcludeKeyofWTEmployeeCreateEmail.from_json(json)
# print the JSON string representation of the object
print PickWTEmployeeCreateExcludeKeyofWTEmployeeCreateEmail.to_json()

# convert the object into a dict
pick_wt_employee_create_exclude_keyof_wt_employee_create_email_dict = pick_wt_employee_create_exclude_keyof_wt_employee_create_email_instance.to_dict()
# create an instance of PickWTEmployeeCreateExcludeKeyofWTEmployeeCreateEmail from a dict
pick_wt_employee_create_exclude_keyof_wt_employee_create_email_form_dict = pick_wt_employee_create_exclude_keyof_wt_employee_create_email.from_dict(pick_wt_employee_create_exclude_keyof_wt_employee_create_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


