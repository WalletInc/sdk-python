# WTPrizeGamePlayResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome** | [**WTPrizeGamePlayResultOutcome**](WTPrizeGamePlayResultOutcome.md) |  | 
**plays_remaining** | **object** |  | 
**odds_disclosure** | **object** |  | 
**prize** | [**WTPrizeGamePlayResultPrize**](WTPrizeGamePlayResultPrize.md) |  | [optional] 

## Example

```python
from wallet.models.wt_prize_game_play_result import WTPrizeGamePlayResult

# TODO update the JSON string below
json = "{}"
# create an instance of WTPrizeGamePlayResult from a JSON string
wt_prize_game_play_result_instance = WTPrizeGamePlayResult.from_json(json)
# print the JSON string representation of the object
print WTPrizeGamePlayResult.to_json()

# convert the object into a dict
wt_prize_game_play_result_dict = wt_prize_game_play_result_instance.to_dict()
# create an instance of WTPrizeGamePlayResult from a dict
wt_prize_game_play_result_form_dict = wt_prize_game_play_result.from_dict(wt_prize_game_play_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


