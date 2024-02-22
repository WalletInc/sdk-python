# MSAnalyticsMemberPointsRefundedPartitionedByDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Represents the date when the points were refunded | 
**points** | **int** | Represents the sum of points refunded on that particular date | 

## Example

```python
from wallet.models.ms_analytics_member_points_refunded_partitioned_by_date import MSAnalyticsMemberPointsRefundedPartitionedByDate

# TODO update the JSON string below
json = "{}"
# create an instance of MSAnalyticsMemberPointsRefundedPartitionedByDate from a JSON string
ms_analytics_member_points_refunded_partitioned_by_date_instance = MSAnalyticsMemberPointsRefundedPartitionedByDate.from_json(json)
# print the JSON string representation of the object
print MSAnalyticsMemberPointsRefundedPartitionedByDate.to_json()

# convert the object into a dict
ms_analytics_member_points_refunded_partitioned_by_date_dict = ms_analytics_member_points_refunded_partitioned_by_date_instance.to_dict()
# create an instance of MSAnalyticsMemberPointsRefundedPartitionedByDate from a dict
ms_analytics_member_points_refunded_partitioned_by_date_form_dict = ms_analytics_member_points_refunded_partitioned_by_date.from_dict(ms_analytics_member_points_refunded_partitioned_by_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


