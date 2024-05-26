# PickMSMemberCreationParamsExcludeKeyofMSMemberCreationParamsMemberIdentifier

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile_number** | **str** |  | 
**first_name** | **str** | An optional first name of the member | [optional] 
**last_name** | **str** | An optional last name of the member | [optional] 
**membership_tier_id** | **str** |  | 
**email** | **str** |  | 
**birthday** | **str** | Represents the date of birth of the member. Defaults to 0000-00-00, which represents that the date of birth has not been configured | 
**points_accrued** | **int** | The number of points that the member has accrued | 

## Example

```python
from wallet.models.pick_ms_member_creation_params_exclude_keyof_ms_member_creation_params_member_identifier import PickMSMemberCreationParamsExcludeKeyofMSMemberCreationParamsMemberIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PickMSMemberCreationParamsExcludeKeyofMSMemberCreationParamsMemberIdentifier from a JSON string
pick_ms_member_creation_params_exclude_keyof_ms_member_creation_params_member_identifier_instance = PickMSMemberCreationParamsExcludeKeyofMSMemberCreationParamsMemberIdentifier.from_json(json)
# print the JSON string representation of the object
print PickMSMemberCreationParamsExcludeKeyofMSMemberCreationParamsMemberIdentifier.to_json()

# convert the object into a dict
pick_ms_member_creation_params_exclude_keyof_ms_member_creation_params_member_identifier_dict = pick_ms_member_creation_params_exclude_keyof_ms_member_creation_params_member_identifier_instance.to_dict()
# create an instance of PickMSMemberCreationParamsExcludeKeyofMSMemberCreationParamsMemberIdentifier from a dict
pick_ms_member_creation_params_exclude_keyof_ms_member_creation_params_member_identifier_form_dict = pick_ms_member_creation_params_exclude_keyof_ms_member_creation_params_member_identifier.from_dict(pick_ms_member_creation_params_exclude_keyof_ms_member_creation_params_member_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


