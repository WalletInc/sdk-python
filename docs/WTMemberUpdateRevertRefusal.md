# WTMemberUpdateRevertRefusal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** |  | 
**member_identifier** | **str** |  | [optional] 
**reason** | [**WTMemberUpdateRevertRefusalReason**](WTMemberUpdateRevertRefusalReason.md) |  | 

## Example

```python
from wallet.models.wt_member_update_revert_refusal import WTMemberUpdateRevertRefusal

# TODO update the JSON string below
json = "{}"
# create an instance of WTMemberUpdateRevertRefusal from a JSON string
wt_member_update_revert_refusal_instance = WTMemberUpdateRevertRefusal.from_json(json)
# print the JSON string representation of the object
print WTMemberUpdateRevertRefusal.to_json()

# convert the object into a dict
wt_member_update_revert_refusal_dict = wt_member_update_revert_refusal_instance.to_dict()
# create an instance of WTMemberUpdateRevertRefusal from a dict
wt_member_update_revert_refusal_form_dict = wt_member_update_revert_refusal.from_dict(wt_member_update_revert_refusal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


