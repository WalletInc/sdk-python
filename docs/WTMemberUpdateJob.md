# WTMemberUpdateJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**status** | [**WTMemberUpdateJobStatus**](WTMemberUpdateJobStatus.md) |  | 
**file_name** | **object** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**summary** | **object** |  | [optional] 
**diff_file_url** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**revert** | [**WTMemberUpdateRevertResult**](WTMemberUpdateRevertResult.md) |  | [optional] 

## Example

```python
from wallet.models.wt_member_update_job import WTMemberUpdateJob

# TODO update the JSON string below
json = "{}"
# create an instance of WTMemberUpdateJob from a JSON string
wt_member_update_job_instance = WTMemberUpdateJob.from_json(json)
# print the JSON string representation of the object
print WTMemberUpdateJob.to_json()

# convert the object into a dict
wt_member_update_job_dict = wt_member_update_job_instance.to_dict()
# create an instance of WTMemberUpdateJob from a dict
wt_member_update_job_form_dict = wt_member_update_job.from_dict(wt_member_update_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


