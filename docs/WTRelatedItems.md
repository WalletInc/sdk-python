# WTRelatedItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**WTRelatedItemSourceType**](WTRelatedItemSourceType.md) |  | 
**source_id** | **object** |  | 
**items** | **object** |  | 

## Example

```python
from wallet.models.wt_related_items import WTRelatedItems

# TODO update the JSON string below
json = "{}"
# create an instance of WTRelatedItems from a JSON string
wt_related_items_instance = WTRelatedItems.from_json(json)
# print the JSON string representation of the object
print WTRelatedItems.to_json()

# convert the object into a dict
wt_related_items_dict = wt_related_items_instance.to_dict()
# create an instance of WTRelatedItems from a dict
wt_related_items_form_dict = wt_related_items.from_dict(wt_related_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


