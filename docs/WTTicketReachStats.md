# WTTicketReachStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issued_count** | **object** |  | 
**issued_seats** | **object** |  | 
**viewed_count** | **object** |  | [optional] 
**viewed_seats** | **object** |  | [optional] 
**claimed_count** | **object** |  | 
**claimed_seats** | **object** |  | 
**redeemed_count** | **object** |  | 
**redeemed_seats** | **object** |  | 
**comp_count** | **object** |  | 
**comp_seats** | **object** |  | 
**paid_count** | **object** |  | 
**paid_seats** | **object** |  | 
**redeemed_value** | **object** |  | 

## Example

```python
from wallet.models.wt_ticket_reach_stats import WTTicketReachStats

# TODO update the JSON string below
json = "{}"
# create an instance of WTTicketReachStats from a JSON string
wt_ticket_reach_stats_instance = WTTicketReachStats.from_json(json)
# print the JSON string representation of the object
print WTTicketReachStats.to_json()

# convert the object into a dict
wt_ticket_reach_stats_dict = wt_ticket_reach_stats_instance.to_dict()
# create an instance of WTTicketReachStats from a dict
wt_ticket_reach_stats_form_dict = wt_ticket_reach_stats.from_dict(wt_ticket_reach_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


