# WTSegmentEstimate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoding** | [**WTSegmentEstimateEncoding**](WTSegmentEstimateEncoding.md) |  | 
**characters** | **object** |  | 
**text_segments** | **object** |  | 
**units** | **object** |  | 
**is_mms** | **object** |  | 
**non_gsm_characters** | **object** |  | 
**segments_if_cleaned** | **object** |  | 
**advisory** | [**WTSegmentAdvisory**](WTSegmentAdvisory.md) |  | 

## Example

```python
from wallet.models.wt_segment_estimate import WTSegmentEstimate

# TODO update the JSON string below
json = "{}"
# create an instance of WTSegmentEstimate from a JSON string
wt_segment_estimate_instance = WTSegmentEstimate.from_json(json)
# print the JSON string representation of the object
print WTSegmentEstimate.to_json()

# convert the object into a dict
wt_segment_estimate_dict = wt_segment_estimate_instance.to_dict()
# create an instance of WTSegmentEstimate from a dict
wt_segment_estimate_form_dict = wt_segment_estimate.from_dict(wt_segment_estimate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


