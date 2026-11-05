# WTMemberUpdateRevertResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reverted** | **float** |  | 
**refused** | **object** |  | 

## Example

```python
from wallet.models.wt_member_update_revert_result import WTMemberUpdateRevertResult

# TODO update the JSON string below
json = "{}"
# create an instance of WTMemberUpdateRevertResult from a JSON string
wt_member_update_revert_result_instance = WTMemberUpdateRevertResult.from_json(json)
# print the JSON string representation of the object
print WTMemberUpdateRevertResult.to_json()

# convert the object into a dict
wt_member_update_revert_result_dict = wt_member_update_revert_result_instance.to_dict()
# create an instance of WTMemberUpdateRevertResult from a dict
wt_member_update_revert_result_form_dict = wt_member_update_revert_result.from_dict(wt_member_update_revert_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


