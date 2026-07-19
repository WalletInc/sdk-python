# WTSegmentEstimateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **object** |  | 
**has_media** | **object** |  | [optional] 
**recipient_count** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_segment_estimate_request import WTSegmentEstimateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTSegmentEstimateRequest from a JSON string
wt_segment_estimate_request_instance = WTSegmentEstimateRequest.from_json(json)
# print the JSON string representation of the object
print WTSegmentEstimateRequest.to_json()

# convert the object into a dict
wt_segment_estimate_request_dict = wt_segment_estimate_request_instance.to_dict()
# create an instance of WTSegmentEstimateRequest from a dict
wt_segment_estimate_request_form_dict = wt_segment_estimate_request.from_dict(wt_segment_estimate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


