# wallet.AppleWalletSubscribersApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_apple_wallet_subscriber_activity**](AppleWalletSubscribersApi.md#fetch_apple_wallet_subscriber_activity) | **GET** /v2/apple/wallet/pass/subscriber/activity/{subscriptionID} | Get subscriber activity Scoped to the caller&#39;s merchant: the subscription must belong to them.
[**fetch_apple_wallet_subscribers**](AppleWalletSubscribersApi.md#fetch_apple_wallet_subscribers) | **GET** /v2/apple/wallet/pass/subscribers/all | Get all subscribers


# **fetch_apple_wallet_subscriber_activity**
> List[object] fetch_apple_wallet_subscriber_activity(subscription_id)

Get subscriber activity Scoped to the caller's merchant: the subscription must belong to them.

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
    api_instance = wallet.AppleWalletSubscribersApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Get subscriber activity Scoped to the caller's merchant: the subscription must belong to them.
        api_response = api_instance.fetch_apple_wallet_subscriber_activity(subscription_id)
        print("The response of AppleWalletSubscribersApi->fetch_apple_wallet_subscriber_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppleWalletSubscribersApi->fetch_apple_wallet_subscriber_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

**List[object]**

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

# **fetch_apple_wallet_subscribers**
> List[object] fetch_apple_wallet_subscribers(start_date_time=start_date_time, end_date_time=end_date_time)

Get all subscribers

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
    api_instance = wallet.AppleWalletSubscribersApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get all subscribers
        api_response = api_instance.fetch_apple_wallet_subscribers(start_date_time=start_date_time, end_date_time=end_date_time)
        print("The response of AppleWalletSubscribersApi->fetch_apple_wallet_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppleWalletSubscribersApi->fetch_apple_wallet_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | [optional] 
 **end_date_time** | **datetime**|  | [optional] 

### Return type

**List[object]**

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

