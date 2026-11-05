# WTTCPAPrivacyRequestForMerchant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_phone** | **object** |  | 
**received_via** | [**WTPrivacyRequestChannel**](WTPrivacyRequestChannel.md) |  | 
**reference** | **object** |  | 
**merchant_id** | [**WTTCPAPrivacyRequestForMerchantMerchantID**](WTTCPAPrivacyRequestForMerchantMerchantID.md) |  | 

## Example

```python
from wallet.models.wttcpa_privacy_request_for_merchant import WTTCPAPrivacyRequestForMerchant

# TODO update the JSON string below
json = "{}"
# create an instance of WTTCPAPrivacyRequestForMerchant from a JSON string
wttcpa_privacy_request_for_merchant_instance = WTTCPAPrivacyRequestForMerchant.from_json(json)
# print the JSON string representation of the object
print WTTCPAPrivacyRequestForMerchant.to_json()

# convert the object into a dict
wttcpa_privacy_request_for_merchant_dict = wttcpa_privacy_request_for_merchant_instance.to_dict()
# create an instance of WTTCPAPrivacyRequestForMerchant from a dict
wttcpa_privacy_request_for_merchant_form_dict = wttcpa_privacy_request_for_merchant.from_dict(wttcpa_privacy_request_for_merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


