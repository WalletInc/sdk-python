# Employee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **object** |  | 
**last_name** | **object** |  | 
**email** | **object** |  | 
**phone_number** | **object** |  | 
**is_public_representative** | **object** |  | 
**wallet_sequence_number** | **object** |  | 
**employee_id** | **object** |  | 
**job_title** | **object** |  | 
**department** | **object** |  | 
**schedule_start_day** | [**EmployeeScheduleStartDay**](EmployeeScheduleStartDay.md) |  | [optional] 
**schedule_start_hour** | [**EmployeeScheduleStartHour**](EmployeeScheduleStartHour.md) |  | [optional] 
**schedule_start_minute** | [**EmployeeScheduleStartMinute**](EmployeeScheduleStartMinute.md) |  | [optional] 
**schedule_start_meridiem** | [**EmployeeScheduleStartMeridiem**](EmployeeScheduleStartMeridiem.md) |  | [optional] 
**schedule_end_day** | [**EmployeeScheduleStartDay**](EmployeeScheduleStartDay.md) |  | [optional] 
**schedule_end_hour** | [**EmployeeScheduleStartHour**](EmployeeScheduleStartHour.md) |  | [optional] 
**schedule_end_minute** | [**EmployeeScheduleStartMinute**](EmployeeScheduleStartMinute.md) |  | [optional] 
**schedule_end_meridiem** | [**EmployeeScheduleStartMeridiem**](EmployeeScheduleStartMeridiem.md) |  | [optional] 
**id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**username** | **object** |  | 
**email_verified** | **object** |  | 
**profile_picture_url** | **object** |  | 
**merchant_id** | **str** |  | 
**session_token** | **object** |  | 
**failed_login_attempts** | **object** |  | [optional] 
**last_login_date** | **object** |  | [optional] 
**cfuvid** | **object** |  | [optional] 
**schedule** | **object** | Construct a type with a set of properties K of type T | [optional] 
**is_email_notification_disabled** | **object** |  | [optional] 

## Example

```python
from wallet.models.employee import Employee

# TODO update the JSON string below
json = "{}"
# create an instance of Employee from a JSON string
employee_instance = Employee.from_json(json)
# print the JSON string representation of the object
print Employee.to_json()

# convert the object into a dict
employee_dict = employee_instance.to_dict()
# create an instance of Employee from a dict
employee_form_dict = employee.from_dict(employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


