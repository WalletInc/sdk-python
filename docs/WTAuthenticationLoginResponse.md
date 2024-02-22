# WTAuthenticationLoginResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**username** | **str** |  | 
**email** | **str** |  | 
**merchant_id** | **str** |  | 
**employee_id** | **str** |  | 
**profile_picture_url** | **str** |  | 
**job_title** | **str** |  | 
**department** | **str** |  | 
**merchant_name** | **str** |  | 
**merchant_currency_abbreviation** | **str** |  | [optional] 
**merchant_industry** | **str** |  | 
**custom_domain** | **str** |  | [optional] 

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


