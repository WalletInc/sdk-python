# PaginatedWTMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[WTMember]**](WTMember.md) | Stores the results as an array | 
**length** | **int** | Denotes the length of the results array | 
**total** | **int** | Denotes the total number of records present in the database | 

## Example

```python
from wallet.models.paginated_wt_members import PaginatedWTMembers

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedWTMembers from a JSON string
paginated_wt_members_instance = PaginatedWTMembers.from_json(json)
# print the JSON string representation of the object
print PaginatedWTMembers.to_json()

# convert the object into a dict
paginated_wt_members_dict = paginated_wt_members_instance.to_dict()
# create an instance of PaginatedWTMembers from a dict
paginated_wt_members_form_dict = paginated_wt_members.from_dict(paginated_wt_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


