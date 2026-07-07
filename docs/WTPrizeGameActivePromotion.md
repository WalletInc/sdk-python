# WTPrizeGameActivePromotion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **object** |  | 
**promotion_id** | **object** |  | [optional] 
**game_type** | [**WTPrizeGameType**](WTPrizeGameType.md) |  | [optional] 
**sponsor_name** | **object** |  | [optional] 
**title** | **object** |  | [optional] 
**odds_disclosure** | **object** |  | [optional] 
**minimum_age** | **object** |  | [optional] 
**start_date** | **object** |  | [optional] 
**end_date** | **object** |  | [optional] 
**per_guest_play_limit** | **object** |  | [optional] 
**play_limit_period** | [**WTPrizeGamePlayLimitPeriod**](WTPrizeGamePlayLimitPeriod.md) |  | [optional] 
**prizes** | **object** |  | [optional] 
**no_purchase_necessary** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_prize_game_active_promotion import WTPrizeGameActivePromotion

# TODO update the JSON string below
json = "{}"
# create an instance of WTPrizeGameActivePromotion from a JSON string
wt_prize_game_active_promotion_instance = WTPrizeGameActivePromotion.from_json(json)
# print the JSON string representation of the object
print WTPrizeGameActivePromotion.to_json()

# convert the object into a dict
wt_prize_game_active_promotion_dict = wt_prize_game_active_promotion_instance.to_dict()
# create an instance of WTPrizeGameActivePromotion from a dict
wt_prize_game_active_promotion_form_dict = wt_prize_game_active_promotion.from_dict(wt_prize_game_active_promotion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


