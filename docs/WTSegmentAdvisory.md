# WTSegmentAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommend** | [**WTSegmentAdvisoryRecommend**](WTSegmentAdvisoryRecommend.md) |  | 
**per_recipient_saving** | **object** |  | 
**campaign_saving** | **object** |  | 
**cost_neutral** | **object** |  | 

## Example

```python
from wallet.models.wt_segment_advisory import WTSegmentAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of WTSegmentAdvisory from a JSON string
wt_segment_advisory_instance = WTSegmentAdvisory.from_json(json)
# print the JSON string representation of the object
print WTSegmentAdvisory.to_json()

# convert the object into a dict
wt_segment_advisory_dict = wt_segment_advisory_instance.to_dict()
# create an instance of WTSegmentAdvisory from a dict
wt_segment_advisory_form_dict = wt_segment_advisory.from_dict(wt_segment_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


