# WTTCPAPrivacyRequestResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**WTTCPAFilter**](WTTCPAFilter.md) |  | 
**already_suppressed** | **object** |  | 

## Example

```python
from wallet.models.wttcpa_privacy_request_result import WTTCPAPrivacyRequestResult

# TODO update the JSON string below
json = "{}"
# create an instance of WTTCPAPrivacyRequestResult from a JSON string
wttcpa_privacy_request_result_instance = WTTCPAPrivacyRequestResult.from_json(json)
# print the JSON string representation of the object
print WTTCPAPrivacyRequestResult.to_json()

# convert the object into a dict
wttcpa_privacy_request_result_dict = wttcpa_privacy_request_result_instance.to_dict()
# create an instance of WTTCPAPrivacyRequestResult from a dict
wttcpa_privacy_request_result_form_dict = wttcpa_privacy_request_result.from_dict(wttcpa_privacy_request_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


