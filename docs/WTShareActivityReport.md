# WTShareActivityReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | 
**window_days** | **object** |  | 
**rows** | **object** |  | 
**totals** | [**WTShareActivityRow**](WTShareActivityRow.md) |  | 

## Example

```python
from wallet.models.wt_share_activity_report import WTShareActivityReport

# TODO update the JSON string below
json = "{}"
# create an instance of WTShareActivityReport from a JSON string
wt_share_activity_report_instance = WTShareActivityReport.from_json(json)
# print the JSON string representation of the object
print WTShareActivityReport.to_json()

# convert the object into a dict
wt_share_activity_report_dict = wt_share_activity_report_instance.to_dict()
# create an instance of WTShareActivityReport from a dict
wt_share_activity_report_form_dict = wt_share_activity_report.from_dict(wt_share_activity_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


