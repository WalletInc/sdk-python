# WTAuthenticationLoginResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**first_name** | **object** |  | 
**last_name** | **object** |  | 
**username** | **object** |  | 
**email** | **object** |  | 
**merchant_id** | **object** |  | 
**employee_id** | **object** |  | 
**profile_picture_url** | **object** |  | 
**job_title** | **object** |  | 
**department** | **object** |  | 
**merchant_name** | **object** |  | 
**merchant_currency_abbreviation** | **object** |  | [optional] 
**merchant_industry** | **object** |  | 
**custom_domain** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_authentication_login_response import WTAuthenticationLoginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WTAuthenticationLoginResponse from a JSON string
wt_authentication_login_response_instance = WTAuthenticationLoginResponse.from_json(json)
# print the JSON string representation of the object
print WTAuthenticationLoginResponse.to_json()

# convert the object into a dict
wt_authentication_login_response_dict = wt_authentication_login_response_instance.to_dict()
# create an instance of WTAuthenticationLoginResponse from a dict
wt_authentication_login_response_form_dict = wt_authentication_login_response.from_dict(wt_authentication_login_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


