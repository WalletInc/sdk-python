# PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumberOrEmailOrBirthday

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | Member ID as represented by the merchant | 
**first_name** | **str** | An optional first name of the member | [optional] 
**last_name** | **str** | An optional last name of the member | [optional] 
**membership_tier_id** | **str** |  | 
**mobile_number** | **str** |  | 
**email** | **str** |  | 
**birthday** | **str** | Represents the date of birth of the member. Defaults to 0000-00-00, which represents that the date of birth has not been configured | 
**points_accrued** | **int** | The number of points that the member has accrued | 

## Example

```python
from wallet.models.pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number_or_email_or_birthday import PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumberOrEmailOrBirthday

# TODO update the JSON string below
json = "{}"
# create an instance of PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumberOrEmailOrBirthday from a JSON string
pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number_or_email_or_birthday_instance = PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumberOrEmailOrBirthday.from_json(json)
# print the JSON string representation of the object
print PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumberOrEmailOrBirthday.to_json()

# convert the object into a dict
pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number_or_email_or_birthday_dict = pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number_or_email_or_birthday_instance.to_dict()
# create an instance of PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumberOrEmailOrBirthday from a dict
pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number_or_email_or_birthday_form_dict = pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number_or_email_or_birthday.from_dict(pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number_or_email_or_birthday_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


