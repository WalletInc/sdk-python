# MSMembershipTierRedemptionPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[MSMembershipTierRedemption]**](MSMembershipTierRedemption.md) | Stores the results as an array | 
**length** | **int** | Denotes the length of the results array | 
**total** | **int** | Denotes the total number of records present in the database | 

## Example

```python
from wallet.models.ms_membership_tier_redemption_pagination import MSMembershipTierRedemptionPagination

# TODO update the JSON string below
json = "{}"
# create an instance of MSMembershipTierRedemptionPagination from a JSON string
ms_membership_tier_redemption_pagination_instance = MSMembershipTierRedemptionPagination.from_json(json)
# print the JSON string representation of the object
print MSMembershipTierRedemptionPagination.to_json()

# convert the object into a dict
ms_membership_tier_redemption_pagination_dict = ms_membership_tier_redemption_pagination_instance.to_dict()
# create an instance of MSMembershipTierRedemptionPagination from a dict
ms_membership_tier_redemption_pagination_form_dict = ms_membership_tier_redemption_pagination.from_dict(ms_membership_tier_redemption_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


