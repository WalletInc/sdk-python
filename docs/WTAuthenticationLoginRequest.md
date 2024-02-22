# WTAuthenticationLoginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from wallet.models.wt_authentication_login_request import WTAuthenticationLoginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTAuthenticationLoginRequest from a JSON string
wt_authentication_login_request_instance = WTAuthenticationLoginRequest.from_json(json)
# print the JSON string representation of the object
print WTAuthenticationLoginRequest.to_json()

# convert the object into a dict
wt_authentication_login_request_dict = wt_authentication_login_request_instance.to_dict()
# create an instance of WTAuthenticationLoginRequest from a dict
wt_authentication_login_request_form_dict = wt_authentication_login_request.from_dict(wt_authentication_login_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


