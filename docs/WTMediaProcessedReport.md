# WTMediaProcessedReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_key** | **str** |  | 
**status** | [**WTMediaProcessedReportStatus**](WTMediaProcessedReportStatus.md) |  | 
**file_url** | **str** |  | [optional] 
**file_type** | **str** |  | [optional] 
**file_size** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_media_processed_report import WTMediaProcessedReport

# TODO update the JSON string below
json = "{}"
# create an instance of WTMediaProcessedReport from a JSON string
wt_media_processed_report_instance = WTMediaProcessedReport.from_json(json)
# print the JSON string representation of the object
print WTMediaProcessedReport.to_json()

# convert the object into a dict
wt_media_processed_report_dict = wt_media_processed_report_instance.to_dict()
# create an instance of WTMediaProcessedReport from a dict
wt_media_processed_report_form_dict = wt_media_processed_report.from_dict(wt_media_processed_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


