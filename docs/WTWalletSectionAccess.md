# WTWalletSectionAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section** | **object** |  | 
**included** | **bool** |  | 
**lowest_tier** | [**WTPlanTier**](WTPlanTier.md) |  | [optional] 

## Example

```python
from wallet.models.wt_wallet_section_access import WTWalletSectionAccess

# TODO update the JSON string below
json = "{}"
# create an instance of WTWalletSectionAccess from a JSON string
wt_wallet_section_access_instance = WTWalletSectionAccess.from_json(json)
# print the JSON string representation of the object
print WTWalletSectionAccess.to_json()

# convert the object into a dict
wt_wallet_section_access_dict = wt_wallet_section_access_instance.to_dict()
# create an instance of WTWalletSectionAccess from a dict
wt_wallet_section_access_form_dict = wt_wallet_section_access.from_dict(wt_wallet_section_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


