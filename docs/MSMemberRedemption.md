# MSMemberRedemption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The transaction ID at the POS | 
**transaction_type** | [**MSMemberRedemptionTransactionType**](MSMemberRedemptionTransactionType.md) |  | 
**points** | **int** | The number of points involved in this transaction | 
**register_id** | [**PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID**](PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID.md) |  | [optional] 
**terminal_type** | **str** | The type of the terminal | 
**id** | **str** | The UUID of this record | 
**member_id** | **str** |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** | The timestamp of when this resource was created | 
**is_active** | **bool** | Denotes if this resource is active | 

## Example

```python
from wallet.models.ms_member_redemption import MSMemberRedemption

# TODO update the JSON string below
json = "{}"
# create an instance of MSMemberRedemption from a JSON string
ms_member_redemption_instance = MSMemberRedemption.from_json(json)
# print the JSON string representation of the object
print MSMemberRedemption.to_json()

# convert the object into a dict
ms_member_redemption_dict = ms_member_redemption_instance.to_dict()
# create an instance of MSMemberRedemption from a dict
ms_member_redemption_form_dict = ms_member_redemption.from_dict(ms_member_redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


