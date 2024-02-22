# wallet.AppleWalletSubscribersApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_apple_wallet_subscriber_activity**](AppleWalletSubscribersApi.md#fetch_apple_wallet_subscriber_activity) | **GET** /v2/apple/wallet/pass/subscriber/activity/{subscriptionID} | Fetch subscriber activity
[**fetch_apple_wallet_subscribers**](AppleWalletSubscribersApi.md#fetch_apple_wallet_subscribers) | **GET** /v2/apple/wallet/pass/subscribers/all | Fetch all subscribers


# **fetch_apple_wallet_subscriber_activity**
> List[object] fetch_apple_wallet_subscriber_activity(subscription_id)

Fetch subscriber activity

### Example


```python
import wallet
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.AppleWalletSubscribersApi(api_client)
    subscription_id = None # object | 

    try:
        # Fetch subscriber activity
        api_response = api_instance.fetch_apple_wallet_subscriber_activity(subscription_id)
        print("The response of AppleWalletSubscribersApi->fetch_apple_wallet_subscriber_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppleWalletSubscribersApi->fetch_apple_wallet_subscriber_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**object**](.md)|  | 

### Return type

**List[object]**

### Authorization

No authorization required

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

Fetch all subscribers

### Example


```python
import wallet
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.AppleWalletSubscribersApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Fetch all subscribers
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

No authorization required

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

