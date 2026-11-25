# WTMerchantURLPathRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | 
**phone_verification_token** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**navigator_agent** | **str** |  | [optional] 
**referrer** | **str** |  | [optional] 
**merchant_id** | **object** |  | 
**path** | **object** |  | 

## Example

```python
from wallet.models.wt_merchant_url_path_request import WTMerchantURLPathRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WTMerchantURLPathRequest from a JSON string
wt_merchant_url_path_request_instance = WTMerchantURLPathRequest.from_json(json)
# print the JSON string representation of the object
print WTMerchantURLPathRequest.to_json()

# convert the object into a dict
wt_merchant_url_path_request_dict = wt_merchant_url_path_request_instance.to_dict()
# create an instance of WTMerchantURLPathRequest from a dict
wt_merchant_url_path_request_form_dict = wt_merchant_url_path_request.from_dict(wt_merchant_url_path_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


