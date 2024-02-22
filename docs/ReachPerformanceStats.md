# ReachPerformanceStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent_count** | **int** | Denotes the number of SMSes sent | 
**delivered_count** | **int** | Denotes the number of SMSes delivered | 
**failed_count** | **int** | Denotes the number of SMSes that have failed to deliver | 
**undelivered_count** | **int** | Denotes the number of SMSes that were undelivered | 
**viewed_count** | **int** | Denotes the count of SMSes viewed (by clicking on the link sent as part of the SMS) | 
**redemptions_count** | **int** | Denotes the count of redemptions | 
**value_claimed** | **int** | Denotes the total value claimed as discounts (in cents) | 
**revenue_generated** | **int** | Denotes the total revenue generated for the business by using various payment objects (in cents) | 
**refunds_count** | **int** | Denotes the count of refunds | 
**value_refunded** | **int** | Denotes the total value refunded (in the form of discounts, in cents) | 
**revenue_lost** | **int** | Denotes the total revenue lost for the business on account of refunds (in cents) | 

## Example

```python
from wallet.models.reach_performance_stats import ReachPerformanceStats

# TODO update the JSON string below
json = "{}"
# create an instance of ReachPerformanceStats from a JSON string
reach_performance_stats_instance = ReachPerformanceStats.from_json(json)
# print the JSON string representation of the object
print ReachPerformanceStats.to_json()

# convert the object into a dict
reach_performance_stats_dict = reach_performance_stats_instance.to_dict()
# create an instance of ReachPerformanceStats from a dict
reach_performance_stats_form_dict = reach_performance_stats.from_dict(reach_performance_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


