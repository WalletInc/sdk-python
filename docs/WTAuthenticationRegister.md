# WTAuthenticationRegister


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**password** | **str** |  | 
**hear_about_us** | **str** |  | [optional] 
**hear_about_us_details** | **str** |  | [optional] 
**company_name** | **str** |  | 
**merchant_type** | **str** |  | 
**street_address1** | **str** |  | 
**street_address2** | **str** |  | 
**city** | **str** |  | 
**state** | **str** |  | 
**zip** | **str** |  | 
**country** | **str** |  | 
**phone_number** | **str** |  | 
**ein** | **str** |  | [optional] 
**ga_client_id** | **str** |  | [optional] 
**ga_measurement_id** | **str** |  | [optional] 
**recaptcha_token** | **str** |  | [optional] 
**affiliate_id** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_authentication_register import WTAuthenticationRegister

# TODO update the JSON string below
json = "{}"
# create an instance of WTAuthenticationRegister from a JSON string
wt_authentication_register_instance = WTAuthenticationRegister.from_json(json)
# print the JSON string representation of the object
print WTAuthenticationRegister.to_json()

# convert the object into a dict
wt_authentication_register_dict = wt_authentication_register_instance.to_dict()
# create an instance of WTAuthenticationRegister from a dict
wt_authentication_register_form_dict = wt_authentication_register.from_dict(wt_authentication_register_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


