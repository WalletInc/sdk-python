# WTSmsCreditOverdraftUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overdraft** | **object** | Segments a contracted account may go below zero, settled on its invoice. 0 for everyone else. | 

## Example

```python
from wallet.models.wt_sms_credit_overdraft_update import WTSmsCreditOverdraftUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WTSmsCreditOverdraftUpdate from a JSON string
wt_sms_credit_overdraft_update_instance = WTSmsCreditOverdraftUpdate.from_json(json)
# print the JSON string representation of the object
print WTSmsCreditOverdraftUpdate.to_json()

# convert the object into a dict
wt_sms_credit_overdraft_update_dict = wt_sms_credit_overdraft_update_instance.to_dict()
# create an instance of WTSmsCreditOverdraftUpdate from a dict
wt_sms_credit_overdraft_update_form_dict = wt_sms_credit_overdraft_update.from_dict(wt_sms_credit_overdraft_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


