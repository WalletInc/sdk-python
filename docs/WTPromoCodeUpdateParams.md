# WTPromoCodeUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | 
**promo_code** | **str** |  | 
**display_value** | **str** |  | 
**order_number** | **int** |  | 
**media_url** | **str** |  | [optional] 
**start_date** | **datetime** |  | 
**expiration_date** | **datetime** |  | 

## Example

```python
from wallet.models.wt_promo_code_update_params import WTPromoCodeUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTPromoCodeUpdateParams from a JSON string
wt_promo_code_update_params_instance = WTPromoCodeUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTPromoCodeUpdateParams.to_json()

# convert the object into a dict
wt_promo_code_update_params_dict = wt_promo_code_update_params_instance.to_dict()
# create an instance of WTPromoCodeUpdateParams from a dict
wt_promo_code_update_params_form_dict = wt_promo_code_update_params.from_dict(wt_promo_code_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


