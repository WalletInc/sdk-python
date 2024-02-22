# WTAuthenticationRequestResetPassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** |  | 

## Example

```python
from wallet.models.wt_authentication_request_reset_password import WTAuthenticationRequestResetPassword

# TODO update the JSON string below
json = "{}"
# create an instance of WTAuthenticationRequestResetPassword from a JSON string
wt_authentication_request_reset_password_instance = WTAuthenticationRequestResetPassword.from_json(json)
# print the JSON string representation of the object
print WTAuthenticationRequestResetPassword.to_json()

# convert the object into a dict
wt_authentication_request_reset_password_dict = wt_authentication_request_reset_password_instance.to_dict()
# create an instance of WTAuthenticationRequestResetPassword from a dict
wt_authentication_request_reset_password_form_dict = wt_authentication_request_reset_password.from_dict(wt_authentication_request_reset_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


