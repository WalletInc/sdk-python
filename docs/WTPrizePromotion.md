# WTPrizePromotion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_type** | [**WTPrizeGameType**](WTPrizeGameType.md) |  | 
**title** | **object** |  | 
**win_odds** | **object** |  | 
**prize_tiers** | **object** |  | 
**per_guest_play_limit** | **object** |  | 
**play_limit_period** | [**WTPrizeGamePlayLimitPeriod**](WTPrizeGamePlayLimitPeriod.md) |  | 
**start_date** | **object** |  | 
**end_date** | **object** |  | 
**trigger_type** | [**WTPrizeGameTrigger**](WTPrizeGameTrigger.md) |  | 
**minimum_age** | **object** |  | [optional] 
**registration_attested** | **object** |  | [optional] 
**id** | **object** |  | 
**merchant_id** | **object** |  | 
**is_active** | **object** |  | 
**total_prize_pool_value** | **object** |  | 
**odds_disclosure** | **object** |  | 

## Example

```python
from wallet.models.wt_prize_promotion import WTPrizePromotion

# TODO update the JSON string below
json = "{}"
# create an instance of WTPrizePromotion from a JSON string
wt_prize_promotion_instance = WTPrizePromotion.from_json(json)
# print the JSON string representation of the object
print WTPrizePromotion.to_json()

# convert the object into a dict
wt_prize_promotion_dict = wt_prize_promotion_instance.to_dict()
# create an instance of WTPrizePromotion from a dict
wt_prize_promotion_form_dict = wt_prize_promotion.from_dict(wt_prize_promotion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


