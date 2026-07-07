# WTConnectOnboardingLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_url** | **object** |  | 
**refresh_url** | **object** |  | 

## Example

```python
from wallet.models.wt_connect_onboarding_link_request import WTConnectOnboardingLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTConnectOnboardingLinkRequest from a JSON string
wt_connect_onboarding_link_request_instance = WTConnectOnboardingLinkRequest.from_json(json)
# print the JSON string representation of the object
print WTConnectOnboardingLinkRequest.to_json()

# convert the object into a dict
wt_connect_onboarding_link_request_dict = wt_connect_onboarding_link_request_instance.to_dict()
# create an instance of WTConnectOnboardingLinkRequest from a dict
wt_connect_onboarding_link_request_form_dict = wt_connect_onboarding_link_request.from_dict(wt_connect_onboarding_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


