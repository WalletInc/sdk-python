# WTMemberUpdatePreviewReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**summary** | **object** |  | [optional] 
**diff_file_key** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_member_update_preview_report import WTMemberUpdatePreviewReport

# TODO update the JSON string below
json = "{}"
# create an instance of WTMemberUpdatePreviewReport from a JSON string
wt_member_update_preview_report_instance = WTMemberUpdatePreviewReport.from_json(json)
# print the JSON string representation of the object
print WTMemberUpdatePreviewReport.to_json()

# convert the object into a dict
wt_member_update_preview_report_dict = wt_member_update_preview_report_instance.to_dict()
# create an instance of WTMemberUpdatePreviewReport from a dict
wt_member_update_preview_report_form_dict = wt_member_update_preview_report.from_dict(wt_member_update_preview_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


