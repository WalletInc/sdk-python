# WTSmsCreditSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** |  | 
**is_on_ledger** | **object** | False until the merchant&#39;s first grant: until then sends use the legacy MaxSMSCount ceiling. | 
**credits_granted** | **object** | Total segments ever granted (purchases, bonuses and adjustments). | 
**credit_overdraft** | **float** |  | 
**ledger_epoch** | **object** | The first grant&#39;s time; usage before it never counts against the ledger. | [optional] 
**grants** | **object** |  | 

## Example

```python
from wallet.models.wt_sms_credit_summary import WTSmsCreditSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WTSmsCreditSummary from a JSON string
wt_sms_credit_summary_instance = WTSmsCreditSummary.from_json(json)
# print the JSON string representation of the object
print WTSmsCreditSummary.to_json()

# convert the object into a dict
wt_sms_credit_summary_dict = wt_sms_credit_summary_instance.to_dict()
# create an instance of WTSmsCreditSummary from a dict
wt_sms_credit_summary_form_dict = wt_sms_credit_summary.from_dict(wt_sms_credit_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


