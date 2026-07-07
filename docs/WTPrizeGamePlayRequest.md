# WTPrizeGamePlayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promotion_id** | **object** |  | 
**phone_verification_token** | **object** |  | 

## Example

```python
from wallet.models.wt_prize_game_play_request import WTPrizeGamePlayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTPrizeGamePlayRequest from a JSON string
wt_prize_game_play_request_instance = WTPrizeGamePlayRequest.from_json(json)
# print the JSON string representation of the object
print WTPrizeGamePlayRequest.to_json()

# convert the object into a dict
wt_prize_game_play_request_dict = wt_prize_game_play_request_instance.to_dict()
# create an instance of WTPrizeGamePlayRequest from a dict
wt_prize_game_play_request_form_dict = wt_prize_game_play_request.from_dict(wt_prize_game_play_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


