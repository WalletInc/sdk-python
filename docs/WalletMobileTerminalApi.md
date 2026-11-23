# wallet.WalletMobileTerminalApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_wallet_item_from_mobile_terminal**](WalletMobileTerminalApi.md#fetch_wallet_item_from_mobile_terminal) | **GET** /v2/pos/mobile/item/{itemID} | Get item
[**find_member_by_id**](WalletMobileTerminalApi.md#find_member_by_id) | **GET** /v2/pos/mobile/member/{memberID} | Search for Member&#39;s rewards
[**redeem_wallet_item_from_mobile_terminal**](WalletMobileTerminalApi.md#redeem_wallet_item_from_mobile_terminal) | **POST** /v2/pos/mobile/item/redeem/{itemID} | Redeem item


# **fetch_wallet_item_from_mobile_terminal**
> object fetch_wallet_item_from_mobile_terminal(item_id)

Get item

### Example

* Api Key Authentication (api_token):

```python
import wallet
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.WalletMobileTerminalApi(api_client)
    item_id = 'item_id_example' # str | 

    try:
        # Get item
        api_response = api_instance.fetch_wallet_item_from_mobile_terminal(item_id)
        print("The response of WalletMobileTerminalApi->fetch_wallet_item_from_mobile_terminal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletMobileTerminalApi->fetch_wallet_item_from_mobile_terminal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_member_by_id**
> Member find_member_by_id(member_id)

Search for Member's rewards

### Example

* Api Key Authentication (api_token):

```python
import wallet
from wallet.models.member import Member
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.WalletMobileTerminalApi(api_client)
    member_id = 'member_id_example' # str | 

    try:
        # Search for Member's rewards
        api_response = api_instance.find_member_by_id(member_id)
        print("The response of WalletMobileTerminalApi->find_member_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletMobileTerminalApi->find_member_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | 

### Return type

[**Member**](Member.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_wallet_item_from_mobile_terminal**
> object redeem_wallet_item_from_mobile_terminal(item_id, wt_wallet_item_redemption)

Redeem item

### Example

* Api Key Authentication (api_token):

```python
import wallet
from wallet.models.wt_wallet_item_redemption import WTWalletItemRedemption
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.WalletMobileTerminalApi(api_client)
    item_id = 'item_id_example' # str | 
    wt_wallet_item_redemption = wallet.WTWalletItemRedemption() # WTWalletItemRedemption | 

    try:
        # Redeem item
        api_response = api_instance.redeem_wallet_item_from_mobile_terminal(item_id, wt_wallet_item_redemption)
        print("The response of WalletMobileTerminalApi->redeem_wallet_item_from_mobile_terminal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletMobileTerminalApi->redeem_wallet_item_from_mobile_terminal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **wt_wallet_item_redemption** | [**WTWalletItemRedemption**](WTWalletItemRedemption.md)|  | 

### Return type

**object**

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

