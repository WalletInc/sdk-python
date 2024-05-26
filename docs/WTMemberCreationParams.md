# WTMemberCreationParams


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
**member_id** | **str** | Member ID as represented by the merchant | 

## Example

```python
from wallet.models.wt_member_creation_params import WTMemberCreationParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTMemberCreationParams from a JSON string
wt_member_creation_params_instance = WTMemberCreationParams.from_json(json)
# print the JSON string representation of the object
print WTMemberCreationParams.to_json()

# convert the object into a dict
wt_member_creation_params_dict = wt_member_creation_params_instance.to_dict()
# create an instance of WTMemberCreationParams from a dict
wt_member_creation_params_form_dict = wt_member_creation_params.from_dict(wt_member_creation_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


