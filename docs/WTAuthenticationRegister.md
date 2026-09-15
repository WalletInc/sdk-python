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
**merchant_type** | **object** |  | [optional] 
**street_address1** | **object** |  | [optional] 
**street_address2** | **object** |  | [optional] 
**city** | **object** |  | [optional] 
**state** | **object** |  | [optional] 
**zip** | **object** |  | [optional] 
**country** | **object** |  | [optional] 
**phone_number** | **object** |  | [optional] 
**ein** | **object** |  | [optional] 
**accepted_terms_version** | **object** |  | [optional] 
**accepted_privacy_version** | **object** |  | [optional] 
**utm_source** | **object** |  | [optional] 
**utm_medium** | **object** |  | [optional] 
**utm_term** | **object** |  | [optional] 
**utm_content** | **object** |  | [optional] 
**utm_campaign** | **object** |  | [optional] 
**utm_source_platform** | **object** |  | [optional] 
**utm_creative_format** | **object** |  | [optional] 
**utm_marketing_tactic** | **object** |  | [optional] 
**http_referrer** | **object** |  | [optional] 
**landing_page** | **object** |  | [optional] 
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


