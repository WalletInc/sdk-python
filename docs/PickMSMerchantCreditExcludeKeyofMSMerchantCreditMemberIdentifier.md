# PickMSMerchantCreditExcludeKeyofMSMerchantCreditMemberIdentifier

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** | The timestamp of when this resource was created | 
**updated_at** | **datetime** | The timestamp of when this resource was updated | 
**is_active** | **bool** | Denotes if this resource is active | 
**mobile_number** | **str** |  | 
**credit_amount** | **int** | The amount that needs to be credited to the member | 

## Example

```python
from wallet.models.pick_ms_merchant_credit_exclude_keyof_ms_merchant_credit_member_identifier import PickMSMerchantCreditExcludeKeyofMSMerchantCreditMemberIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PickMSMerchantCreditExcludeKeyofMSMerchantCreditMemberIdentifier from a JSON string
pick_ms_merchant_credit_exclude_keyof_ms_merchant_credit_member_identifier_instance = PickMSMerchantCreditExcludeKeyofMSMerchantCreditMemberIdentifier.from_json(json)
# print the JSON string representation of the object
print PickMSMerchantCreditExcludeKeyofMSMerchantCreditMemberIdentifier.to_json()

# convert the object into a dict
pick_ms_merchant_credit_exclude_keyof_ms_merchant_credit_member_identifier_dict = pick_ms_merchant_credit_exclude_keyof_ms_merchant_credit_member_identifier_instance.to_dict()
# create an instance of PickMSMerchantCreditExcludeKeyofMSMerchantCreditMemberIdentifier from a dict
pick_ms_merchant_credit_exclude_keyof_ms_merchant_credit_member_identifier_form_dict = pick_ms_merchant_credit_exclude_keyof_ms_merchant_credit_member_identifier.from_dict(pick_ms_merchant_credit_exclude_keyof_ms_merchant_credit_member_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


