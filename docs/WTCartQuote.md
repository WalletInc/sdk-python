# WTCartQuote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **object** |  | 
**currency** | **object** |  | 
**venue** | [**WTMenuVenue**](WTMenuVenue.md) |  | [optional] 
**lines** | **object** |  | 
**subtotal_cents** | **object** |  | 
**tax_cents** | **object** |  | 
**total_cents** | **object** |  | 
**ordering** | [**WTWalletOrdering**](WTWalletOrdering.md) |  | [optional] 
**age_requirement** | [**WTAgeRestriction**](WTAgeRestriction.md) |  | 
**id_check_required** | **object** |  | 
**is_valid** | **object** |  | 

## Example

```python
from wallet.models.wt_cart_quote import WTCartQuote

# TODO update the JSON string below
json = "{}"
# create an instance of WTCartQuote from a JSON string
wt_cart_quote_instance = WTCartQuote.from_json(json)
# print the JSON string representation of the object
print WTCartQuote.to_json()

# convert the object into a dict
wt_cart_quote_dict = wt_cart_quote_instance.to_dict()
# create an instance of WTCartQuote from a dict
wt_cart_quote_form_dict = wt_cart_quote.from_dict(wt_cart_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


