# WTWalletOrdering


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_online_checkout** | **object** |  | 
**is_accepting_orders** | **object** |  | 
**paused_reason** | **object** |  | [optional] 
**opens_at** | **object** |  | [optional] 
**opens_day** | **object** |  | [optional] 
**time_zone** | **object** |  | 
**prep_minutes** | **object** |  | 
**scheduled_pickup** | **object** |  | 

## Example

```python
from wallet.models.wt_wallet_ordering import WTWalletOrdering

# TODO update the JSON string below
json = "{}"
# create an instance of WTWalletOrdering from a JSON string
wt_wallet_ordering_instance = WTWalletOrdering.from_json(json)
# print the JSON string representation of the object
print WTWalletOrdering.to_json()

# convert the object into a dict
wt_wallet_ordering_dict = wt_wallet_ordering_instance.to_dict()
# create an instance of WTWalletOrdering from a dict
wt_wallet_ordering_form_dict = wt_wallet_ordering.from_dict(wt_wallet_ordering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


