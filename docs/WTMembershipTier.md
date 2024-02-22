# WTMembershipTier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier_number** | **str** | The tier number as defined by the merchant | 
**tier_name** | **str** | The tier name as defined by the merchant | 
**tier_discount** | **float** | The provided discount as percentage | 
**tier_design_id** | **str** |  | 
**points_design_id** | **str** |  | 
**id** | [**WTMembershipTierId**](WTMembershipTierId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** | The timestamp of when this resource was created | 
**updated_at** | **datetime** | The timestamp of when this resource was updated | 
**is_active** | **bool** | Denotes if this resource is active | 

## Example

```python
from wallet.models.wt_membership_tier import WTMembershipTier

# TODO update the JSON string below
json = "{}"
# create an instance of WTMembershipTier from a JSON string
wt_membership_tier_instance = WTMembershipTier.from_json(json)
# print the JSON string representation of the object
print WTMembershipTier.to_json()

# convert the object into a dict
wt_membership_tier_dict = wt_membership_tier_instance.to_dict()
# create an instance of WTMembershipTier from a dict
wt_membership_tier_form_dict = wt_membership_tier.from_dict(wt_membership_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


