# WTEmployeeCreate


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

## Example

```python
from wallet.models.wt_employee_create import WTEmployeeCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeCreate from a JSON string
wt_employee_create_instance = WTEmployeeCreate.from_json(json)
# print the JSON string representation of the object
print WTEmployeeCreate.to_json()

# convert the object into a dict
wt_employee_create_dict = wt_employee_create_instance.to_dict()
# create an instance of WTEmployeeCreate from a dict
wt_employee_create_form_dict = wt_employee_create.from_dict(wt_employee_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


