# wallet.GoogleWalletSubscribersApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_google_wallet_subscriber_activity**](GoogleWalletSubscribersApi.md#fetch_google_wallet_subscriber_activity) | **GET** /google/wallet/pass/subscriber/activity/{subscriptionID} | Get subscriber activity Scoped to the caller&#39;s merchant: the subscription must belong to them (tightening the Apple sibling, which does not re-check ownership on this route).
[**fetch_google_wallet_subscribers**](GoogleWalletSubscribersApi.md#fetch_google_wallet_subscribers) | **GET** /google/wallet/pass/subscribers/all | Get all subscribers


# **fetch_google_wallet_subscriber_activity**
> List[object] fetch_google_wallet_subscriber_activity(subscription_id)

Get subscriber activity Scoped to the caller's merchant: the subscription must belong to them (tightening the Apple sibling, which does not re-check ownership on this route).

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
    api_instance = wallet.GoogleWalletSubscribersApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Get subscriber activity Scoped to the caller's merchant: the subscription must belong to them (tightening the Apple sibling, which does not re-check ownership on this route).
        api_response = api_instance.fetch_google_wallet_subscriber_activity(subscription_id)
        print("The response of GoogleWalletSubscribersApi->fetch_google_wallet_subscriber_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleWalletSubscribersApi->fetch_google_wallet_subscriber_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

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

# **fetch_google_wallet_subscribers**
> List[object] fetch_google_wallet_subscribers(start_date_time=start_date_time, end_date_time=end_date_time)

Get all subscribers

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
    api_instance = wallet.GoogleWalletSubscribersApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get all subscribers
        api_response = api_instance.fetch_google_wallet_subscribers(start_date_time=start_date_time, end_date_time=end_date_time)
        print("The response of GoogleWalletSubscribersApi->fetch_google_wallet_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleWalletSubscribersApi->fetch_google_wallet_subscribers: %s\n" % e)
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

