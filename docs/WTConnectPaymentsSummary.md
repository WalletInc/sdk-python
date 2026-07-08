# WTConnectPaymentsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**WTConnectPaymentsSummaryBalance**](WTConnectPaymentsSummaryBalance.md) |  | 
**recent_payouts** | **object** |  | 
**recent_charges** | **object** |  | 

## Example

```python
from wallet.models.wt_connect_payments_summary import WTConnectPaymentsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WTConnectPaymentsSummary from a JSON string
wt_connect_payments_summary_instance = WTConnectPaymentsSummary.from_json(json)
# print the JSON string representation of the object
print WTConnectPaymentsSummary.to_json()

# convert the object into a dict
wt_connect_payments_summary_dict = wt_connect_payments_summary_instance.to_dict()
# create an instance of WTConnectPaymentsSummary from a dict
wt_connect_payments_summary_form_dict = wt_connect_payments_summary.from_dict(wt_connect_payments_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


