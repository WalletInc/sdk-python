# PaginationRequestWithSortOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_archive_included** | **bool** | Denotes if archived records should be included in the response payload | [optional] 
**page_size** | **int** | Denotes the number of records per page | [optional] 
**page_num** | **int** | Denotes the page number | [optional] 
**sort_key** | **str** | Denotes the key using which the records need to be sorted | [optional] 
**sort_order** | [**PaginationRequestWithSortOptionsSortOrder**](PaginationRequestWithSortOptionsSortOrder.md) |  | [optional] 

## Example

```python
from wallet.models.pagination_request_with_sort_options import PaginationRequestWithSortOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationRequestWithSortOptions from a JSON string
pagination_request_with_sort_options_instance = PaginationRequestWithSortOptions.from_json(json)
# print the JSON string representation of the object
print PaginationRequestWithSortOptions.to_json()

# convert the object into a dict
pagination_request_with_sort_options_dict = pagination_request_with_sort_options_instance.to_dict()
# create an instance of PaginationRequestWithSortOptions from a dict
pagination_request_with_sort_options_form_dict = pagination_request_with_sort_options.from_dict(pagination_request_with_sort_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


