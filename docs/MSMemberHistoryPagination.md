# MSMemberHistoryPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[MSMemberHistory]**](MSMemberHistory.md) | Stores the results as an array | 
**length** | **int** | Denotes the length of the results array | 
**total** | **int** | Denotes the total number of records present in the database | 

## Example

```python
from wallet.models.ms_member_history_pagination import MSMemberHistoryPagination

# TODO update the JSON string below
json = "{}"
# create an instance of MSMemberHistoryPagination from a JSON string
ms_member_history_pagination_instance = MSMemberHistoryPagination.from_json(json)
# print the JSON string representation of the object
print MSMemberHistoryPagination.to_json()

# convert the object into a dict
ms_member_history_pagination_dict = ms_member_history_pagination_instance.to_dict()
# create an instance of MSMemberHistoryPagination from a dict
ms_member_history_pagination_form_dict = ms_member_history_pagination.from_dict(ms_member_history_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


