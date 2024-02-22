# WTAuthenticationSSOLoginForDiscourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 
**sso_payload** | **str** |  | 
**sig_payload** | **str** |  | 

## Example

```python
from wallet.models.wt_authentication_sso_login_for_discourse import WTAuthenticationSSOLoginForDiscourse

# TODO update the JSON string below
json = "{}"
# create an instance of WTAuthenticationSSOLoginForDiscourse from a JSON string
wt_authentication_sso_login_for_discourse_instance = WTAuthenticationSSOLoginForDiscourse.from_json(json)
# print the JSON string representation of the object
print WTAuthenticationSSOLoginForDiscourse.to_json()

# convert the object into a dict
wt_authentication_sso_login_for_discourse_dict = wt_authentication_sso_login_for_discourse_instance.to_dict()
# create an instance of WTAuthenticationSSOLoginForDiscourse from a dict
wt_authentication_sso_login_for_discourse_form_dict = wt_authentication_sso_login_for_discourse.from_dict(wt_authentication_sso_login_for_discourse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


