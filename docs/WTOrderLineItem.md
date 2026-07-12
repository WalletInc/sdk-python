# WTOrderLineItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**AmenityId**](AmenityId.md) |  | 
**product_id** | [**AmenityId**](AmenityId.md) |  | [optional] 
**service_id** | [**AmenityId**](AmenityId.md) |  | [optional] 
**title_snapshot** | **object** |  | 
**unit_amount** | **object** |  | 
**quantity** | **object** |  | 

## Example

```python
from wallet.models.wt_order_line_item import WTOrderLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of WTOrderLineItem from a JSON string
wt_order_line_item_instance = WTOrderLineItem.from_json(json)
# print the JSON string representation of the object
print WTOrderLineItem.to_json()

# convert the object into a dict
wt_order_line_item_dict = wt_order_line_item_instance.to_dict()
# create an instance of WTOrderLineItem from a dict
wt_order_line_item_form_dict = wt_order_line_item.from_dict(wt_order_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


