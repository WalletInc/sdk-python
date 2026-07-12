# Merchant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **object** |  | 
**address1** | **object** |  | 
**address2** | **object** |  | 
**city** | **object** |  | 
**state** | **object** |  | 
**country** | **object** |  | 
**phone_number** | **object** |  | 
**zip** | **object** |  | 
**currency_abbreviation** | **object** |  | [optional] 
**id** | **str** |  | 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 
**industry** | **object** |  | 
**industry_name** | **object** |  | 
**info_genesis_property_id** | **object** |  | 
**is_frozen** | **object** |  | 
**billing_contact_employee_id** | **object** |  | 
**marketing_contact_employee_id** | **object** |  | 
**technical_contact_employee_id** | **object** |  | 
**customer_service_contact_employee_id** | **object** |  | 
**stripe_customer_id** | **object** |  | 
**stripe_connect_account_id** | **object** |  | [optional] 
**stripe_connect_charges_enabled** | **object** |  | [optional] 
**stripe_connect_payouts_enabled** | **object** |  | [optional] 
**stripe_connect_details_submitted** | **object** |  | [optional] 
**stripe_connect_onboarding_status** | **object** |  | [optional] 
**is_payment_method_provided** | **object** |  | 
**plan_nickname** | **object** |  | 
**billing_cadence** | [**WTBillingVerifyPaymentMethodResponseBillingCadence**](WTBillingVerifyPaymentMethodResponseBillingCadence.md) |  | [optional] 
**max_sms_count** | **object** |  | 
**is_sms_agreement** | **object** |  | [optional] 
**is_white_labeled** | **object** |  | [optional] 
**is_featured** | **object** |  | [optional] 

## Example

```python
from wallet.models.merchant import Merchant

# TODO update the JSON string below
json = "{}"
# create an instance of Merchant from a JSON string
merchant_instance = Merchant.from_json(json)
# print the JSON string representation of the object
print Merchant.to_json()

# convert the object into a dict
merchant_dict = merchant_instance.to_dict()
# create an instance of Merchant from a dict
merchant_form_dict = merchant.from_dict(merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


