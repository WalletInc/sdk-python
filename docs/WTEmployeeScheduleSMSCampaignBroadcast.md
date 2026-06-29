# WTEmployeeScheduleSMSCampaignBroadcast


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number_id** | **str** |  | 
**message_template** | **object** |  | 
**send_qr_code** | **object** |  | 
**media_urls** | **object** |  | [optional] 
**broadcast_scheduled_at** | **object** |  | 
**locale** | **object** |  | 
**timezone** | **object** |  | 

## Example

```python
from wallet.models.wt_employee_schedule_sms_campaign_broadcast import WTEmployeeScheduleSMSCampaignBroadcast

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmployeeScheduleSMSCampaignBroadcast from a JSON string
wt_employee_schedule_sms_campaign_broadcast_instance = WTEmployeeScheduleSMSCampaignBroadcast.from_json(json)
# print the JSON string representation of the object
print WTEmployeeScheduleSMSCampaignBroadcast.to_json()

# convert the object into a dict
wt_employee_schedule_sms_campaign_broadcast_dict = wt_employee_schedule_sms_campaign_broadcast_instance.to_dict()
# create an instance of WTEmployeeScheduleSMSCampaignBroadcast from a dict
wt_employee_schedule_sms_campaign_broadcast_form_dict = wt_employee_schedule_sms_campaign_broadcast.from_dict(wt_employee_schedule_sms_campaign_broadcast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


