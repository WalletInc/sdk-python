# MSMerchantCreditRedemption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **object** | The transaction ID at the POS | 
**transaction_type** | [**MSMemberRedemptionTransactionType**](MSMemberRedemptionTransactionType.md) |  | 
**amount** | **object** | The number of amount involved in this transaction | 
**register_id** | [**MSMemberRedemptionRegisterID**](MSMemberRedemptionRegisterID.md) |  | [optional] 
**terminal_type** | **object** | The type of the terminal | 
**id** | **object** | The UUID of this record | 
**merchant_credit_id** | **str** |  | 
**merchant_id** | **str** |  | 
**created_at** | **object** | The timestamp of when this resource was created | 
**is_active** | **object** | Denotes if this resource is active | 

## Example

```python
from wallet.models.ms_merchant_credit_redemption import MSMerchantCreditRedemption

# TODO update the JSON string below
json = "{}"
# create an instance of MSMerchantCreditRedemption from a JSON string
ms_merchant_credit_redemption_instance = MSMerchantCreditRedemption.from_json(json)
# print the JSON string representation of the object
print MSMerchantCreditRedemption.to_json()

# convert the object into a dict
ms_merchant_credit_redemption_dict = ms_merchant_credit_redemption_instance.to_dict()
# create an instance of MSMerchantCreditRedemption from a dict
ms_merchant_credit_redemption_form_dict = ms_merchant_credit_redemption.from_dict(ms_merchant_credit_redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


