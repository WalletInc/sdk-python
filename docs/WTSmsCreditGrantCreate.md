# WTSmsCreditGrantCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segments** | **object** | Whole segments to add; negative only with source \&quot;adjustment\&quot;. | 
**source** | **object** | \&quot;bonus\&quot; (free credits from Wallet) or \&quot;adjustment\&quot; (a correction). Purchases are recorded by the purchase path. | 
**note** | **object** | Why. Required. | 

## Example

```python
from wallet.models.wt_sms_credit_grant_create import WTSmsCreditGrantCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WTSmsCreditGrantCreate from a JSON string
wt_sms_credit_grant_create_instance = WTSmsCreditGrantCreate.from_json(json)
# print the JSON string representation of the object
print WTSmsCreditGrantCreate.to_json()

# convert the object into a dict
wt_sms_credit_grant_create_dict = wt_sms_credit_grant_create_instance.to_dict()
# create an instance of WTSmsCreditGrantCreate from a dict
wt_sms_credit_grant_create_form_dict = wt_sms_credit_grant_create.from_dict(wt_sms_credit_grant_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


