# WTGuestOrderReceipt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**WTOrder**](WTOrder.md) |  | 
**amount_breakdown** | [**WTGuestAmountBreakdown**](WTGuestAmountBreakdown.md) |  | 

## Example

```python
from wallet.models.wt_guest_order_receipt import WTGuestOrderReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of WTGuestOrderReceipt from a JSON string
wt_guest_order_receipt_instance = WTGuestOrderReceipt.from_json(json)
# print the JSON string representation of the object
print WTGuestOrderReceipt.to_json()

# convert the object into a dict
wt_guest_order_receipt_dict = wt_guest_order_receipt_instance.to_dict()
# create an instance of WTGuestOrderReceipt from a dict
wt_guest_order_receipt_form_dict = wt_guest_order_receipt.from_dict(wt_guest_order_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


