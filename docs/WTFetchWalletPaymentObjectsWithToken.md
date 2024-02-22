# WTFetchWalletPaymentObjectsWithToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_verification_token** | **str** |  | 
**merchant_id** | **str** |  | 
**page_type** | **str** |  | 
**is_refresh** | **bool** |  | [optional] 
**referrer** | **str** |  | [optional] 

## Example

```python
from wallet.models.wt_fetch_wallet_payment_objects_with_token import WTFetchWalletPaymentObjectsWithToken

# TODO update the JSON string below
json = "{}"
# create an instance of WTFetchWalletPaymentObjectsWithToken from a JSON string
wt_fetch_wallet_payment_objects_with_token_instance = WTFetchWalletPaymentObjectsWithToken.from_json(json)
# print the JSON string representation of the object
print WTFetchWalletPaymentObjectsWithToken.to_json()

# convert the object into a dict
wt_fetch_wallet_payment_objects_with_token_dict = wt_fetch_wallet_payment_objects_with_token_instance.to_dict()
# create an instance of WTFetchWalletPaymentObjectsWithToken from a dict
wt_fetch_wallet_payment_objects_with_token_form_dict = wt_fetch_wallet_payment_objects_with_token.from_dict(wt_fetch_wallet_payment_objects_with_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


