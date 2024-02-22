# WTAuthenticationResetPassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from wallet.models.wt_authentication_reset_password import WTAuthenticationResetPassword

# TODO update the JSON string below
json = "{}"
# create an instance of WTAuthenticationResetPassword from a JSON string
wt_authentication_reset_password_instance = WTAuthenticationResetPassword.from_json(json)
# print the JSON string representation of the object
print WTAuthenticationResetPassword.to_json()

# convert the object into a dict
wt_authentication_reset_password_dict = wt_authentication_reset_password_instance.to_dict()
# create an instance of WTAuthenticationResetPassword from a dict
wt_authentication_reset_password_form_dict = wt_authentication_reset_password.from_dict(wt_authentication_reset_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


