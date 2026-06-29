# WTAuthenticationRegister


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **object** |  | 
**last_name** | **object** |  | 
**email** | **object** |  | 
**password** | **object** |  | 
**hear_about_us** | **object** |  | [optional] 
**hear_about_us_details** | **object** |  | [optional] 
**company_name** | **object** |  | 
**merchant_type** | **object** |  | 
**street_address1** | **object** |  | 
**street_address2** | **object** |  | 
**city** | **object** |  | 
**state** | **object** |  | 
**zip** | **object** |  | 
**country** | **object** |  | 
**phone_number** | **object** |  | 
**ein** | **object** |  | [optional] 
**ga_client_id** | **object** |  | [optional] 
**ga_measurement_id** | **object** |  | [optional] 
**recaptcha_token** | **object** |  | [optional] 
**affiliate_id** | **object** |  | [optional] 
**first_promoter_tracking_id** | **object** |  | [optional] 
**first_promoter_affiliate_id** | **object** |  | [optional] 

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


