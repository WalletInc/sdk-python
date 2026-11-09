# WTSmsCreditGrant

KAN-463: the SMS credit ledger. Grants are in SEGMENTS, the unit Twilio bills.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | The grant&#39;s id. | 
**merchant_id** | **str** |  | 
**segments** | **object** | Segments added (negative only for an adjustment). | 
**source** | **object** | \&quot;purchase\&quot;, \&quot;bonus\&quot; or \&quot;adjustment\&quot;. | 
**note** | **object** | Why it was granted (required for a bonus or an adjustment). | [optional] 
**reference** | **object** | The purchase it came from, e.g. a Stripe payment id, when there is one. | [optional] 
**granted_by** | **object** | The Wallet staff user, or \&quot;system\&quot;, that made the grant. | 
**created_at** | **datetime** |  | 

## Example

```python
from wallet.models.wt_sms_credit_grant import WTSmsCreditGrant

# TODO update the JSON string below
json = "{}"
# create an instance of WTSmsCreditGrant from a JSON string
wt_sms_credit_grant_instance = WTSmsCreditGrant.from_json(json)
# print the JSON string representation of the object
print WTSmsCreditGrant.to_json()

# convert the object into a dict
wt_sms_credit_grant_dict = wt_sms_credit_grant_instance.to_dict()
# create an instance of WTSmsCreditGrant from a dict
wt_sms_credit_grant_form_dict = wt_sms_credit_grant.from_dict(wt_sms_credit_grant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


