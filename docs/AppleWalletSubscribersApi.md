# wallet.AppleWalletSubscribersApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_apple_wallet_subscriber_activity**](AppleWalletSubscribersApi.md#fetch_apple_wallet_subscriber_activity) | **GET** /v2/apple/wallet/pass/subscriber/activity/{subscriptionID} | Fetch subscriber activity
[**fetch_apple_wallet_subscribers**](AppleWalletSubscribersApi.md#fetch_apple_wallet_subscribers) | **GET** /v2/apple/wallet/pass/subscribers/all | Fetch all subscribers


# **fetch_apple_wallet_subscriber_activity**
> [bool, date, datetime, dict, float, int, list, str, none_type] fetch_apple_wallet_subscriber_activity(subscription_id)

Fetch subscriber activity

### Example


```python
import time
import wallet
from wallet.api import apple_wallet_subscribers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = apple_wallet_subscribers_api.AppleWalletSubscribersApi(api_client)
    subscription_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch subscriber activity
        api_response = api_instance.fetch_apple_wallet_subscriber_activity(subscription_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling AppleWalletSubscribersApi->fetch_apple_wallet_subscriber_activity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

**[bool, date, datetime, dict, float, int, list, str, none_type]**

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
> [bool, date, datetime, dict, float, int, list, str, none_type] fetch_apple_wallet_subscribers()

Fetch all subscribers

### Example


```python
import time
import wallet
from wallet.api import apple_wallet_subscribers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = apple_wallet_subscribers_api.AppleWalletSubscribersApi(api_client)
    start_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    end_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all subscribers
        api_response = api_instance.fetch_apple_wallet_subscribers(start_date_time=start_date_time, end_date_time=end_date_time)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling AppleWalletSubscribersApi->fetch_apple_wallet_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | [optional]
 **end_date_time** | **datetime**|  | [optional]

### Return type

**[bool, date, datetime, dict, float, int, list, str, none_type]**

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

