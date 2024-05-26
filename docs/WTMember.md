# WTMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** | The timestamp of when this resource was created | 
**updated_at** | **datetime** | The timestamp of when this resource was updated | 
**is_active** | **bool** | Denotes if this resource is active | 
**first_name** | **str** | An optional first name of the member | [optional] 
**last_name** | **str** | An optional last name of the member | [optional] 
**membership_tier_id** | **str** |  | 
**mobile_number** | **str** |  | 
**email** | **str** |  | 
**birthday** | **str** | Represents the date of birth of the member. Defaults to 0000-00-00, which represents that the date of birth has not been configured | 
**points_accrued** | **int** | The number of points that the member has accrued | 
**member_id** | **str** | Member ID as represented by the merchant | 
**membership_tier_redeemable_id** | **str** |  | 

## Example

```python
from wallet.models.wt_member import WTMember

# TODO update the JSON string below
json = "{}"
# create an instance of WTMember from a JSON string
wt_member_instance = WTMember.from_json(json)
# print the JSON string representation of the object
print WTMember.to_json()

# convert the object into a dict
wt_member_dict = wt_member_instance.to_dict()
# create an instance of WTMember from a dict
wt_member_form_dict = wt_member.from_dict(wt_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


