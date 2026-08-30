# FetchMerchantURLRequestsPaged200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**length** | **float** |  | 
**results** | [**List[WalletPageView]**](WalletPageView.md) |  | 

## Example

```python
from wallet.models.fetch_merchant_url_requests_paged200_response import FetchMerchantURLRequestsPaged200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FetchMerchantURLRequestsPaged200Response from a JSON string
fetch_merchant_url_requests_paged200_response_instance = FetchMerchantURLRequestsPaged200Response.from_json(json)
# print the JSON string representation of the object
print FetchMerchantURLRequestsPaged200Response.to_json()

# convert the object into a dict
fetch_merchant_url_requests_paged200_response_dict = fetch_merchant_url_requests_paged200_response_instance.to_dict()
# create an instance of FetchMerchantURLRequestsPaged200Response from a dict
fetch_merchant_url_requests_paged200_response_form_dict = fetch_merchant_url_requests_paged200_response.from_dict(fetch_merchant_url_requests_paged200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


