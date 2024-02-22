# MSMembershipTierRedemption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | A 10 character alphanumeric unique value that represents each member | 
**transaction_id** | **str** | The transaction ID at the POS | 
**transaction_type** | [**MSMemberRedemptionTransactionType**](MSMemberRedemptionTransactionType.md) |  | 
**amount** | **int** | The amount that has been redeemed, in cents | 
**register_id** | [**PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID**](PickVSStaticVoucherExcludeKeyofVSStaticVoucherRedeemedAtOrRefundedAtOrLastViewedAtRegisterID.md) |  | [optional] 
**terminal_type** | **str** | The type of the terminal | 
**id** | **str** | The UUID of this record | 
**tier_id** | **str** | A 10 character alphanumeric unique value that represents each membership tier | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** | The timestamp of when this resource was created | 
**is_active** | **bool** | Denotes if this resource is active | 

## Example

```python
from wallet.models.ms_membership_tier_redemption import MSMembershipTierRedemption

# TODO update the JSON string below
json = "{}"
# create an instance of MSMembershipTierRedemption from a JSON string
ms_membership_tier_redemption_instance = MSMembershipTierRedemption.from_json(json)
# print the JSON string representation of the object
print MSMembershipTierRedemption.to_json()

# convert the object into a dict
ms_membership_tier_redemption_dict = ms_membership_tier_redemption_instance.to_dict()
# create an instance of MSMembershipTierRedemption from a dict
ms_membership_tier_redemption_form_dict = ms_membership_tier_redemption.from_dict(ms_membership_tier_redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


