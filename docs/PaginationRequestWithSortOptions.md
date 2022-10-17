# PaginationRequestWithSortOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_archive_included** | **bool** | Denotes if archived records should be included in the response payload | [optional] 
**page_size** | **int** | Denotes the number of records per page | [optional] 
**page_num** | **int** | Denotes the page number | [optional] 
**sort_key** | **str** | Denotes the key using which the records need to be sorted | [optional]  if omitted the server will use the default value of "createdAt"
**sort_order** | **bool, date, datetime, dict, float, int, list, str, none_type** | Denotes the sort order | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


