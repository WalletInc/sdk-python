# WTAdvertisementCreditUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**value_type** | [**PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType**](PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType.md) |  | 
**payment_design_id** | **str** |  | 
**max_uses** | **int** |  | 
**discount_value** | **int** |  | 

## Example

```python
from wallet.models.wt_advertisement_credit_update_params import WTAdvertisementCreditUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WTAdvertisementCreditUpdateParams from a JSON string
wt_advertisement_credit_update_params_instance = WTAdvertisementCreditUpdateParams.from_json(json)
# print the JSON string representation of the object
print WTAdvertisementCreditUpdateParams.to_json()

# convert the object into a dict
wt_advertisement_credit_update_params_dict = wt_advertisement_credit_update_params_instance.to_dict()
# create an instance of WTAdvertisementCreditUpdateParams from a dict
wt_advertisement_credit_update_params_form_dict = wt_advertisement_credit_update_params.from_dict(wt_advertisement_credit_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


