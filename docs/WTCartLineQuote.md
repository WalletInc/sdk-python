# WTCartLineQuote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **object** |  | 
**title** | **object** |  | 
**quantity** | **object** |  | 
**unit_amount_cents** | **object** |  | 
**options** | **object** |  | [optional] 
**price_changed** | **object** |  | [optional] 
**line_total_cents** | **object** |  | 
**tax_cents** | **object** |  | [optional] 
**note** | **object** |  | [optional] 
**age_restriction** | [**WTAgeRestriction**](WTAgeRestriction.md) |  | 
**id_check_on_handoff** | **object** |  | 
**venue** | [**WTMenuVenue**](WTMenuVenue.md) |  | [optional] 
**problem** | [**WTCartLineProblem**](WTCartLineProblem.md) |  | [optional] 

## Example

```python
from wallet.models.wt_cart_line_quote import WTCartLineQuote

# TODO update the JSON string below
json = "{}"
# create an instance of WTCartLineQuote from a JSON string
wt_cart_line_quote_instance = WTCartLineQuote.from_json(json)
# print the JSON string representation of the object
print WTCartLineQuote.to_json()

# convert the object into a dict
wt_cart_line_quote_dict = wt_cart_line_quote_instance.to_dict()
# create an instance of WTCartLineQuote from a dict
wt_cart_line_quote_form_dict = wt_cart_line_quote.from_dict(wt_cart_line_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


