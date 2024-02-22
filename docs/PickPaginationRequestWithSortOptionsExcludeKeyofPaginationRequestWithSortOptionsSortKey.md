# PickPaginationRequestWithSortOptionsExcludeKeyofPaginationRequestWithSortOptionsSortKey

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_archive_included** | **bool** | Denotes if archived records should be included in the response payload | [optional] 
**page_size** | **int** | Denotes the number of records per page | [optional] 
**page_num** | **int** | Denotes the page number | [optional] 
**sort_order** | [**PaginationRequestWithSortOptionsSortOrder**](PaginationRequestWithSortOptionsSortOrder.md) |  | [optional] 

## Example

```python
from wallet.models.pick_pagination_request_with_sort_options_exclude_keyof_pagination_request_with_sort_options_sort_key import PickPaginationRequestWithSortOptionsExcludeKeyofPaginationRequestWithSortOptionsSortKey

# TODO update the JSON string below
json = "{}"
# create an instance of PickPaginationRequestWithSortOptionsExcludeKeyofPaginationRequestWithSortOptionsSortKey from a JSON string
pick_pagination_request_with_sort_options_exclude_keyof_pagination_request_with_sort_options_sort_key_instance = PickPaginationRequestWithSortOptionsExcludeKeyofPaginationRequestWithSortOptionsSortKey.from_json(json)
# print the JSON string representation of the object
print PickPaginationRequestWithSortOptionsExcludeKeyofPaginationRequestWithSortOptionsSortKey.to_json()

# convert the object into a dict
pick_pagination_request_with_sort_options_exclude_keyof_pagination_request_with_sort_options_sort_key_dict = pick_pagination_request_with_sort_options_exclude_keyof_pagination_request_with_sort_options_sort_key_instance.to_dict()
# create an instance of PickPaginationRequestWithSortOptionsExcludeKeyofPaginationRequestWithSortOptionsSortKey from a dict
pick_pagination_request_with_sort_options_exclude_keyof_pagination_request_with_sort_options_sort_key_form_dict = pick_pagination_request_with_sort_options_exclude_keyof_pagination_request_with_sort_options_sort_key.from_dict(pick_pagination_request_with_sort_options_exclude_keyof_pagination_request_with_sort_options_sort_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


