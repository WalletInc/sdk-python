# WTGuestAmountBreakdown


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_amount_cents** | **object** |  | 
**credit_applied_cents** | **object** |  | 
**tip_cents** | **object** |  | 
**amount_due_cents** | **object** |  | 

## Example

```python
from wallet.models.wt_guest_amount_breakdown import WTGuestAmountBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of WTGuestAmountBreakdown from a JSON string
wt_guest_amount_breakdown_instance = WTGuestAmountBreakdown.from_json(json)
# print the JSON string representation of the object
print WTGuestAmountBreakdown.to_json()

# convert the object into a dict
wt_guest_amount_breakdown_dict = wt_guest_amount_breakdown_instance.to_dict()
# create an instance of WTGuestAmountBreakdown from a dict
wt_guest_amount_breakdown_form_dict = wt_guest_amount_breakdown.from_dict(wt_guest_amount_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


