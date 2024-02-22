# MemberSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_archive_included** | **bool** | Denotes if archived records should be included in the response payload | [optional] 
**page_size** | **int** | Denotes the number of records per page | [optional] 
**page_num** | **int** | Denotes the page number | [optional] 
**sort_order** | [**PaginationRequestWithSortOptionsSortOrder**](PaginationRequestWithSortOptionsSortOrder.md) |  | [optional] 
**sort_key** | [**MemberSearchSortKey**](MemberSearchSortKey.md) |  | [optional] 
**search_key** | [**MemberSearchSearchKey**](MemberSearchSearchKey.md) |  | 
**search_value** | **str** | The search value to be queried | 

## Example

```python
from wallet.models.member_search import MemberSearch

# TODO update the JSON string below
json = "{}"
# create an instance of MemberSearch from a JSON string
member_search_instance = MemberSearch.from_json(json)
# print the JSON string representation of the object
print MemberSearch.to_json()

# convert the object into a dict
member_search_dict = member_search_instance.to_dict()
# create an instance of MemberSearch from a dict
member_search_form_dict = member_search.from_dict(member_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


