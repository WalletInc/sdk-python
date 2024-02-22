# Merchant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** |  | 
**address1** | **str** |  | 
**address2** | **str** |  | 
**city** | **str** |  | 
**state** | **str** |  | 
**country** | **str** |  | 
**phone_number** | **str** |  | 
**zip** | **str** |  | 
**currency_abbreviation** | **str** |  | [optional] 
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**industry** | **str** |  | 
**industry_name** | **str** |  | 
**info_genesis_property_id** | **str** |  | 
**is_frozen** | **bool** |  | 
**billing_contact_employee_id** | **str** |  | 
**marketing_contact_employee_id** | **str** |  | 
**technical_contact_employee_id** | **str** |  | 
**customer_service_contact_employee_id** | **str** |  | 
**stripe_customer_id** | **str** |  | 
**is_payment_method_provided** | **bool** |  | 
**plan_nickname** | **str** |  | 
**max_sms_count** | **float** |  | 
**is_sms_agreement** | **bool** |  | [optional] 
**is_white_labeled** | **bool** |  | [optional] 
**is_featured** | **bool** |  | [optional] 

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


