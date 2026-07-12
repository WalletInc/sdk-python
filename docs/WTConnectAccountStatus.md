# WTConnectAccountStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **object** |  | 
**onboarding_status** | [**WTConnectOnboardingStatus**](WTConnectOnboardingStatus.md) |  | 
**details_submitted** | **object** |  | 
**charges_enabled** | **object** |  | 
**payouts_enabled** | **object** |  | 
**ecommerce_eligible** | **object** |  | 
**requirements** | [**WTConnectRequirements**](WTConnectRequirements.md) |  | 

## Example

```python
from wallet.models.wt_connect_account_status import WTConnectAccountStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WTConnectAccountStatus from a JSON string
wt_connect_account_status_instance = WTConnectAccountStatus.from_json(json)
# print the JSON string representation of the object
print WTConnectAccountStatus.to_json()

# convert the object into a dict
wt_connect_account_status_dict = wt_connect_account_status_instance.to_dict()
# create an instance of WTConnectAccountStatus from a dict
wt_connect_account_status_form_dict = wt_connect_account_status.from_dict(wt_connect_account_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


