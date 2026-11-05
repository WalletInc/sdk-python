# WTRelatedItemUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**WTRelatedItemSourceType**](WTRelatedItemSourceType.md) |  | 
**source_id** | **object** |  | 
**title** | **object** |  | 

## Example

```python
from wallet.models.wt_related_item_usage import WTRelatedItemUsage

# TODO update the JSON string below
json = "{}"
# create an instance of WTRelatedItemUsage from a JSON string
wt_related_item_usage_instance = WTRelatedItemUsage.from_json(json)
# print the JSON string representation of the object
print WTRelatedItemUsage.to_json()

# convert the object into a dict
wt_related_item_usage_dict = wt_related_item_usage_instance.to_dict()
# create an instance of WTRelatedItemUsage from a dict
wt_related_item_usage_form_dict = wt_related_item_usage.from_dict(wt_related_item_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


