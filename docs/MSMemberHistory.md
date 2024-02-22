# MSMemberHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_identifier** | **str** | Member ID as represented by the merchant | 
**first_name** | **str** | An optional first name of the member | [optional] 
**last_name** | **str** | An optional last name of the member | [optional] 
**membership_tier_id** | **str** |  | 
**mobile_number** | **str** |  | 
**email** | **str** |  | 
**birthday** | **str** | Represents the date of birth of the member. Defaults to 0000-00-00, which represents that the date of birth has not been configured | 
**points_accrued** | **int** | The number of points that the member has accrued | 
**id** | **str** | The UUID of this record | 
**member_id** | **str** |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** | The timestamp of when this resource was created | 
**is_active** | **bool** | Denotes if this resource is active | 

## Example

```python
from wallet.models.ms_member_history import MSMemberHistory

# TODO update the JSON string below
json = "{}"
# create an instance of MSMemberHistory from a JSON string
ms_member_history_instance = MSMemberHistory.from_json(json)
# print the JSON string representation of the object
print MSMemberHistory.to_json()

# convert the object into a dict
ms_member_history_dict = ms_member_history_instance.to_dict()
# create an instance of MSMemberHistory from a dict
ms_member_history_form_dict = ms_member_history.from_dict(ms_member_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


