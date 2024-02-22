# WTEmployeeScheduleSimpleSMSToRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number_id** | **str** |  | 
**message_template** | **str** |  | 
**media_urls** | **List[str]** |  | [optional] 
**broadcast_scheduled_at** | **datetime** |  | 
**to_cell_phone** | **str** |  | 

## Example

```python
from wallet.models.wt_employee_schedule_simple_smsto_recipient import WTEmployeeScheduleSimpleSMSToRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeScheduleSimpleSMSToRecipient from a JSON string
wt_employee_schedule_simple_smsto_recipient_instance = WTEmployeeScheduleSimpleSMSToRecipient.from_json(json)
# print the JSON string representation of the object
print WTEmployeeScheduleSimpleSMSToRecipient.to_json()

# convert the object into a dict
wt_employee_schedule_simple_smsto_recipient_dict = wt_employee_schedule_simple_smsto_recipient_instance.to_dict()
# create an instance of WTEmployeeScheduleSimpleSMSToRecipient from a dict
wt_employee_schedule_simple_smsto_recipient_form_dict = wt_employee_schedule_simple_smsto_recipient.from_dict(wt_employee_schedule_simple_smsto_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


