# WTTCPAPrivacyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_phone** | **object** |  | 
**received_via** | [**WTPrivacyRequestChannel**](WTPrivacyRequestChannel.md) |  | 
**reference** | **object** |  | 

## Example

```python
from wallet.models.wttcpa_privacy_request import WTTCPAPrivacyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTTCPAPrivacyRequest from a JSON string
wttcpa_privacy_request_instance = WTTCPAPrivacyRequest.from_json(json)
# print the JSON string representation of the object
print WTTCPAPrivacyRequest.to_json()

# convert the object into a dict
wttcpa_privacy_request_dict = wttcpa_privacy_request_instance.to_dict()
# create an instance of WTTCPAPrivacyRequest from a dict
wttcpa_privacy_request_form_dict = wttcpa_privacy_request.from_dict(wttcpa_privacy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


