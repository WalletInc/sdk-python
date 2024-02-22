# WTMembershipTierUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier_number** | **str** | The tier number as defined by the merchant | 
**tier_name** | **str** | The tier name as defined by the merchant | 
**tier_discount** | **float** | The provided discount as percentage | 
**tier_design_id** | **str** |  | 
**points_design_id** | **str** |  | 

## Example

```python
from wallet.models.wt_membership_tier_update_params import WTMembershipTierUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTMembershipTierUpdateParams from a JSON string
wt_membership_tier_update_params_instance = WTMembershipTierUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTMembershipTierUpdateParams.to_json()

# convert the object into a dict
wt_membership_tier_update_params_dict = wt_membership_tier_update_params_instance.to_dict()
# create an instance of WTMembershipTierUpdateParams from a dict
wt_membership_tier_update_params_form_dict = wt_membership_tier_update_params.from_dict(wt_membership_tier_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


