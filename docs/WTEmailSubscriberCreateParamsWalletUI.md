# WTEmailSubscriberCreateParamsWalletUI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email_address** | **str** |  | 
**merchant_id** | **str** |  | 

## Example

```python
from wallet.models.wt_email_subscriber_create_params_wallet_ui import WTEmailSubscriberCreateParamsWalletUI

# TODO update the JSON string below
json = "{}"
# create an instance of WTEmailSubscriberCreateParamsWalletUI from a JSON string
wt_email_subscriber_create_params_wallet_ui_instance = WTEmailSubscriberCreateParamsWalletUI.from_json(json)
# print the JSON string representation of the object
print WTEmailSubscriberCreateParamsWalletUI.to_json()

# convert the object into a dict
wt_email_subscriber_create_params_wallet_ui_dict = wt_email_subscriber_create_params_wallet_ui_instance.to_dict()
# create an instance of WTEmailSubscriberCreateParamsWalletUI from a dict
wt_email_subscriber_create_params_wallet_ui_form_dict = wt_email_subscriber_create_params_wallet_ui.from_dict(wt_email_subscriber_create_params_wallet_ui_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


