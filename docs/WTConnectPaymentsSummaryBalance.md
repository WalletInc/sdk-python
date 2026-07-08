# WTConnectPaymentsSummaryBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending** | **object** |  | 
**available** | **object** |  | 

## Example

```python
from wallet.models.wt_connect_payments_summary_balance import WTConnectPaymentsSummaryBalance

# TODO update the JSON string below
json = "{}"
# create an instance of WTConnectPaymentsSummaryBalance from a JSON string
wt_connect_payments_summary_balance_instance = WTConnectPaymentsSummaryBalance.from_json(json)
# print the JSON string representation of the object
print WTConnectPaymentsSummaryBalance.to_json()

# convert the object into a dict
wt_connect_payments_summary_balance_dict = wt_connect_payments_summary_balance_instance.to_dict()
# create an instance of WTConnectPaymentsSummaryBalance from a dict
wt_connect_payments_summary_balance_form_dict = wt_connect_payments_summary_balance.from_dict(wt_connect_payments_summary_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


