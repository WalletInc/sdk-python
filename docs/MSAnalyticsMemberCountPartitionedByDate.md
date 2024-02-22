# MSAnalyticsMemberCountPartitionedByDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Represents the date of creation (or addition) of members into the platform | 
**count** | **int** | Represents the number of members that were added on that particular date | 

## Example

```python
from wallet.models.ms_analytics_member_count_partitioned_by_date import MSAnalyticsMemberCountPartitionedByDate

# TODO update the JSON string below
json = "{}"
# create an instance of MSAnalyticsMemberCountPartitionedByDate from a JSON string
ms_analytics_member_count_partitioned_by_date_instance = MSAnalyticsMemberCountPartitionedByDate.from_json(json)
# print the JSON string representation of the object
print MSAnalyticsMemberCountPartitionedByDate.to_json()

# convert the object into a dict
ms_analytics_member_count_partitioned_by_date_dict = ms_analytics_member_count_partitioned_by_date_instance.to_dict()
# create an instance of MSAnalyticsMemberCountPartitionedByDate from a dict
ms_analytics_member_count_partitioned_by_date_form_dict = ms_analytics_member_count_partitioned_by_date.from_dict(ms_analytics_member_count_partitioned_by_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


