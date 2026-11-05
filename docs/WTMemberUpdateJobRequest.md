# WTMemberUpdateJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **object** |  | 

## Example

```python
from wallet.models.wt_member_update_job_request import WTMemberUpdateJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTMemberUpdateJobRequest from a JSON string
wt_member_update_job_request_instance = WTMemberUpdateJobRequest.from_json(json)
# print the JSON string representation of the object
print WTMemberUpdateJobRequest.to_json()

# convert the object into a dict
wt_member_update_job_request_dict = wt_member_update_job_request_instance.to_dict()
# create an instance of WTMemberUpdateJobRequest from a dict
wt_member_update_job_request_form_dict = wt_member_update_job_request.from_dict(wt_member_update_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


