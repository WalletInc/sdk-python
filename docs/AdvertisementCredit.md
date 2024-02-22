# AdvertisementCredit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**value_type** | [**PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType**](PickVSCampaignUpdateParamsExcludeKeyofVSCampaignUpdateParamsStartDateOrExpirationDateValueType.md) |  | 
**payment_design_id** | **str** |  | 
**max_uses** | **int** |  | 
**discount_value** | **int** |  | 
**employee_id** | **str** |  | 
**id** | [**WTWalletPageViewId**](WTWalletPageViewId.md) |  | 
**merchant_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**discount_value_decimal** | **str** |  | 
**discount_value_string** | **str** |  | 

## Example

```python
from wallet.models.advertisement_credit import AdvertisementCredit

# TODO update the JSON string below
json = "{}"
# create an instance of AdvertisementCredit from a JSON string
advertisement_credit_instance = AdvertisementCredit.from_json(json)
# print the JSON string representation of the object
print AdvertisementCredit.to_json()

# convert the object into a dict
advertisement_credit_dict = advertisement_credit_instance.to_dict()
# create an instance of AdvertisementCredit from a dict
advertisement_credit_form_dict = advertisement_credit.from_dict(advertisement_credit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


