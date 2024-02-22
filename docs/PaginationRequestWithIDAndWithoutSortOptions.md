# PaginationRequestWithIDAndWithoutSortOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** | Denotes the number of records per page | [optional] 
**page_num** | **int** | Denotes the page number | [optional] 
**id** | **str** |  | 

## Example

```python
from wallet.models.pagination_request_with_id_and_without_sort_options import PaginationRequestWithIDAndWithoutSortOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationRequestWithIDAndWithoutSortOptions from a JSON string
pagination_request_with_id_and_without_sort_options_instance = PaginationRequestWithIDAndWithoutSortOptions.from_json(json)
# print the JSON string representation of the object
print PaginationRequestWithIDAndWithoutSortOptions.to_json()

# convert the object into a dict
pagination_request_with_id_and_without_sort_options_dict = pagination_request_with_id_and_without_sort_options_instance.to_dict()
# create an instance of PaginationRequestWithIDAndWithoutSortOptions from a dict
pagination_request_with_id_and_without_sort_options_form_dict = pagination_request_with_id_and_without_sort_options.from_dict(pagination_request_with_id_and_without_sort_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


