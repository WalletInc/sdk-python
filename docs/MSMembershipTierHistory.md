# MSMembershipTierHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier_number** | **object** | The tier number as defined by the merchant | 
**tier_name** | **object** | The tier name as defined by the merchant | 
**tier_discount** | **object** | The provided discount as percentage | 
**tier_design_id** | **str** |  | 
**points_design_id** | **str** |  | 
**id** | **object** | The UUID of this record | 
**merchant_id** | **str** |  | 
**tier_id** | **object** | The id of the membership tier - autopopulated by the service | 
**created_at** | **object** | The timestamp of when this resource was created | 
**is_active** | **object** | Denotes if this resource is active | 

## Example

```python
from wallet.models.ms_membership_tier_history import MSMembershipTierHistory

# TODO update the JSON string below
json = "{}"
# create an instance of MSMembershipTierHistory from a JSON string
ms_membership_tier_history_instance = MSMembershipTierHistory.from_json(json)
# print the JSON string representation of the object
print MSMembershipTierHistory.to_json()

# convert the object into a dict
ms_membership_tier_history_dict = ms_membership_tier_history_instance.to_dict()
# create an instance of MSMembershipTierHistory from a dict
ms_membership_tier_history_form_dict = ms_membership_tier_history.from_dict(ms_membership_tier_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


