# WTWalletItemRedemption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_amount** | **float** |  | 
**transaction_number** | **str** |  | 
**meta_value** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_wallet_item_redemption import WTWalletItemRedemption

# TODO update the JSON string below
json = "{}"
# create an instance of WTWalletItemRedemption from a JSON string
wt_wallet_item_redemption_instance = WTWalletItemRedemption.from_json(json)
# print the JSON string representation of the object
print WTWalletItemRedemption.to_json()

# convert the object into a dict
wt_wallet_item_redemption_dict = wt_wallet_item_redemption_instance.to_dict()
# create an instance of WTWalletItemRedemption from a dict
wt_wallet_item_redemption_form_dict = wt_wallet_item_redemption.from_dict(wt_wallet_item_redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


