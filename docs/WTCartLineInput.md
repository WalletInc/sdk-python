# WTCartLineInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **object** |  | 
**quantity** | **object** |  | 
**note** | **object** |  | [optional] 
**option_ids** | **object** |  | [optional] 
**menu_id** | **object** |  | [optional] 
**expected_unit_amount_cents** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_cart_line_input import WTCartLineInput

# TODO update the JSON string below
json = "{}"
# create an instance of WTCartLineInput from a JSON string
wt_cart_line_input_instance = WTCartLineInput.from_json(json)
# print the JSON string representation of the object
print WTCartLineInput.to_json()

# convert the object into a dict
wt_cart_line_input_dict = wt_cart_line_input_instance.to_dict()
# create an instance of WTCartLineInput from a dict
wt_cart_line_input_form_dict = wt_cart_line_input.from_dict(wt_cart_line_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


