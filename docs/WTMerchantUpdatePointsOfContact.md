# WTMerchantUpdatePointsOfContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_employee_id** | **str** |  | 
**marketing_employee_id** | **str** |  | [optional] 
**technical_employee_id** | **str** |  | [optional] 
**customer_service_employee_id** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_merchant_update_points_of_contact import WTMerchantUpdatePointsOfContact

# TODO update the JSON string below
json = "{}"
# create an instance of WTMerchantUpdatePointsOfContact from a JSON string
wt_merchant_update_points_of_contact_instance = WTMerchantUpdatePointsOfContact.from_json(json)
# print the JSON string representation of the object
print WTMerchantUpdatePointsOfContact.to_json()

# convert the object into a dict
wt_merchant_update_points_of_contact_dict = wt_merchant_update_points_of_contact_instance.to_dict()
# create an instance of WTMerchantUpdatePointsOfContact from a dict
wt_merchant_update_points_of_contact_form_dict = wt_merchant_update_points_of_contact.from_dict(wt_merchant_update_points_of_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


