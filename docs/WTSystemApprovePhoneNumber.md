# WTSystemApprovePhoneNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | 
**phone_number_id** | **str** |  | 

## Example

```python
from wallet.models.wt_system_approve_phone_number import WTSystemApprovePhoneNumber

# TODO update the JSON string below
json = "{}"
# create an instance of WTSystemApprovePhoneNumber from a JSON string
wt_system_approve_phone_number_instance = WTSystemApprovePhoneNumber.from_json(json)
# print the JSON string representation of the object
print WTSystemApprovePhoneNumber.to_json()

# convert the object into a dict
wt_system_approve_phone_number_dict = wt_system_approve_phone_number_instance.to_dict()
# create an instance of WTSystemApprovePhoneNumber from a dict
wt_system_approve_phone_number_form_dict = wt_system_approve_phone_number.from_dict(wt_system_approve_phone_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


