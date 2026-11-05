# WTRelatedItemSearchResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **object** |  | 
**has_more** | **object** |  | 

## Example

```python
from wallet.models.wt_related_item_search_results import WTRelatedItemSearchResults

# TODO update the JSON string below
json = "{}"
# create an instance of WTRelatedItemSearchResults from a JSON string
wt_related_item_search_results_instance = WTRelatedItemSearchResults.from_json(json)
# print the JSON string representation of the object
print WTRelatedItemSearchResults.to_json()

# convert the object into a dict
wt_related_item_search_results_dict = wt_related_item_search_results_instance.to_dict()
# create an instance of WTRelatedItemSearchResults from a dict
wt_related_item_search_results_form_dict = wt_related_item_search_results.from_dict(wt_related_item_search_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


