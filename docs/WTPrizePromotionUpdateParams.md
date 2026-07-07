# WTPrizePromotionUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **object** |  | [optional] 
**end_date** | **object** |  | [optional] 

## Example

```python
from wallet.models.wt_prize_promotion_update_params import WTPrizePromotionUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTPrizePromotionUpdateParams from a JSON string
wt_prize_promotion_update_params_instance = WTPrizePromotionUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTPrizePromotionUpdateParams.to_json()

# convert the object into a dict
wt_prize_promotion_update_params_dict = wt_prize_promotion_update_params_instance.to_dict()
# create an instance of WTPrizePromotionUpdateParams from a dict
wt_prize_promotion_update_params_form_dict = wt_prize_promotion_update_params.from_dict(wt_prize_promotion_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


