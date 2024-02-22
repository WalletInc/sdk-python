# WTAuthenticationForgotPassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from wallet.models.wt_authentication_forgot_password import WTAuthenticationForgotPassword

# TODO update the JSON string below
json = "{}"
# create an instance of WTAuthenticationForgotPassword from a JSON string
wt_authentication_forgot_password_instance = WTAuthenticationForgotPassword.from_json(json)
# print the JSON string representation of the object
print WTAuthenticationForgotPassword.to_json()

# convert the object into a dict
wt_authentication_forgot_password_dict = wt_authentication_forgot_password_instance.to_dict()
# create an instance of WTAuthenticationForgotPassword from a dict
wt_authentication_forgot_password_form_dict = wt_authentication_forgot_password.from_dict(wt_authentication_forgot_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


