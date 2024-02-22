# PickWTMerchantCreditMemberIDOrCreditAmountOrMobileNumber

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | MerchantCredit ID as represented by the merchant | [optional] 
**mobile_number** | **str** |  | 
**credit_amount** | **int** | The amount that needs to be credited to the member | 

## Example

```python
from wallet.models.pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number import PickWTMerchantCreditMemberIDOrCreditAmountOrMobileNumber

# TODO update the JSON string below
json = "{}"
# create an instance of PickWTMerchantCreditMemberIDOrCreditAmountOrMobileNumber from a JSON string
pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number_instance = PickWTMerchantCreditMemberIDOrCreditAmountOrMobileNumber.from_json(json)
# print the JSON string representation of the object
print PickWTMerchantCreditMemberIDOrCreditAmountOrMobileNumber.to_json()

# convert the object into a dict
pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number_dict = pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number_instance.to_dict()
# create an instance of PickWTMerchantCreditMemberIDOrCreditAmountOrMobileNumber from a dict
pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number_form_dict = pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number.from_dict(pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


