# WTQuietHoursStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **object** |  | 
**applies_to** | **object** |  | 
**reference_zone** | **object** |  | 
**band_start_min** | **object** |  | 
**band_end_min** | **object** |  | 
**evaluated_at** | **object** |  | 
**within_band** | **object** |  | 
**would_reject** | **object** |  | 
**window_opens_at** | **object** |  | 
**window_closes_at** | **object** |  | 
**next_transition_at** | **object** |  | 

## Example

```python
from wallet.models.wt_quiet_hours_status import WTQuietHoursStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WTQuietHoursStatus from a JSON string
wt_quiet_hours_status_instance = WTQuietHoursStatus.from_json(json)
# print the JSON string representation of the object
print WTQuietHoursStatus.to_json()

# convert the object into a dict
wt_quiet_hours_status_dict = wt_quiet_hours_status_instance.to_dict()
# create an instance of WTQuietHoursStatus from a dict
wt_quiet_hours_status_form_dict = wt_quiet_hours_status.from_dict(wt_quiet_hours_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


