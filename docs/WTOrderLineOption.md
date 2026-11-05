# WTOrderLineOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_title** | **object** |  | 
**title** | **object** |  | 
**price_delta_cents** | **object** |  | 

## Example

```python
from wallet.models.wt_order_line_option import WTOrderLineOption

# TODO update the JSON string below
json = "{}"
# create an instance of WTOrderLineOption from a JSON string
wt_order_line_option_instance = WTOrderLineOption.from_json(json)
# print the JSON string representation of the object
print WTOrderLineOption.to_json()

# convert the object into a dict
wt_order_line_option_dict = wt_order_line_option_instance.to_dict()
# create an instance of WTOrderLineOption from a dict
wt_order_line_option_form_dict = wt_order_line_option.from_dict(wt_order_line_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


