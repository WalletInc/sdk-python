# MSAnalyticsMemberPointsRedeemedPartitionedByDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Represents the date of points redemption | 
**points** | **int** | Represents the sum of points redeemed on that particular date | 

## Example

```python
from wallet.models.ms_analytics_member_points_redeemed_partitioned_by_date import MSAnalyticsMemberPointsRedeemedPartitionedByDate

# TODO update the JSON string below
json = "{}"
# create an instance of MSAnalyticsMemberPointsRedeemedPartitionedByDate from a JSON string
ms_analytics_member_points_redeemed_partitioned_by_date_instance = MSAnalyticsMemberPointsRedeemedPartitionedByDate.from_json(json)
# print the JSON string representation of the object
print MSAnalyticsMemberPointsRedeemedPartitionedByDate.to_json()

# convert the object into a dict
ms_analytics_member_points_redeemed_partitioned_by_date_dict = ms_analytics_member_points_redeemed_partitioned_by_date_instance.to_dict()
# create an instance of MSAnalyticsMemberPointsRedeemedPartitionedByDate from a dict
ms_analytics_member_points_redeemed_partitioned_by_date_form_dict = ms_analytics_member_points_redeemed_partitioned_by_date.from_dict(ms_analytics_member_points_redeemed_partitioned_by_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


