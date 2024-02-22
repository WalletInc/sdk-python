# WTEmployeeUpdate


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
from wallet.models.wt_employee_update import WTEmployeeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeUpdate from a JSON string
wt_employee_update_instance = WTEmployeeUpdate.from_json(json)
# print the JSON string representation of the object
print WTEmployeeUpdate.to_json()

# convert the object into a dict
wt_employee_update_dict = wt_employee_update_instance.to_dict()
# create an instance of WTEmployeeUpdate from a dict
wt_employee_update_form_dict = wt_employee_update.from_dict(wt_employee_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


