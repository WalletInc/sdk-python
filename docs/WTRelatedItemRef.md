# WTRelatedItemRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WTRelatedItemType**](WTRelatedItemType.md) |  | 
**id** | **object** |  | 

## Example

```python
from wallet.models.wt_related_item_ref import WTRelatedItemRef

# TODO update the JSON string below
json = "{}"
# create an instance of WTRelatedItemRef from a JSON string
wt_related_item_ref_instance = WTRelatedItemRef.from_json(json)
# print the JSON string representation of the object
print WTRelatedItemRef.to_json()

# convert the object into a dict
wt_related_item_ref_dict = wt_related_item_ref_instance.to_dict()
# create an instance of WTRelatedItemRef from a dict
wt_related_item_ref_form_dict = wt_related_item_ref.from_dict(wt_related_item_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


