# WTRelatedItemSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WTRelatedItemType**](WTRelatedItemType.md) |  | 
**id** | **object** |  | 
**title** | **object** |  | 
**thumbnail_url** | **object** |  | [optional] 
**is_active** | **object** |  | 

## Example

```python
from wallet.models.wt_related_item_search_result import WTRelatedItemSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of WTRelatedItemSearchResult from a JSON string
wt_related_item_search_result_instance = WTRelatedItemSearchResult.from_json(json)
# print the JSON string representation of the object
print WTRelatedItemSearchResult.to_json()

# convert the object into a dict
wt_related_item_search_result_dict = wt_related_item_search_result_instance.to_dict()
# create an instance of WTRelatedItemSearchResult from a dict
wt_related_item_search_result_form_dict = wt_related_item_search_result.from_dict(wt_related_item_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


