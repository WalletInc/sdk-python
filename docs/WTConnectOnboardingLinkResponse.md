# WTConnectOnboardingLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **object** |  | 
**expires_at** | **object** |  | 

## Example

```python
from wallet.models.wt_connect_onboarding_link_response import WTConnectOnboardingLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WTConnectOnboardingLinkResponse from a JSON string
wt_connect_onboarding_link_response_instance = WTConnectOnboardingLinkResponse.from_json(json)
# print the JSON string representation of the object
print WTConnectOnboardingLinkResponse.to_json()

# convert the object into a dict
wt_connect_onboarding_link_response_dict = wt_connect_onboarding_link_response_instance.to_dict()
# create an instance of WTConnectOnboardingLinkResponse from a dict
wt_connect_onboarding_link_response_form_dict = wt_connect_onboarding_link_response.from_dict(wt_connect_onboarding_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


