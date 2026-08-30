# WTPrizePromotionCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_type** | [**WTPrizeGameType**](WTPrizeGameType.md) |  | 
**title** | **object** |  | 
**win_odds** | **object** |  | 
**prize_tiers** | **object** |  | 
**per_guest_play_limit** | **int** |  | 
**play_limit_period** | [**WTPrizeGamePlayLimitPeriod**](WTPrizeGamePlayLimitPeriod.md) |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**trigger_type** | [**WTPrizeGameTrigger**](WTPrizeGameTrigger.md) |  | 
**minimum_age** | **object** |  | [optional] 
**registration_attested** | **bool** |  | [optional] 

## Example

```python
from wallet.models.wt_prize_promotion_create_params import WTPrizePromotionCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTPrizePromotionCreateParams from a JSON string
wt_prize_promotion_create_params_instance = WTPrizePromotionCreateParams.from_json(json)
# print the JSON string representation of the object
print WTPrizePromotionCreateParams.to_json()

# convert the object into a dict
wt_prize_promotion_create_params_dict = wt_prize_promotion_create_params_instance.to_dict()
# create an instance of WTPrizePromotionCreateParams from a dict
wt_prize_promotion_create_params_form_dict = wt_prize_promotion_create_params.from_dict(wt_prize_promotion_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


