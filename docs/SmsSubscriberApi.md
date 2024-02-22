# wallet.SmsSubscriberApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_sms_subscriber**](SmsSubscriberApi.md#archive_sms_subscriber) | **DELETE** /v2/SmsSubscriber/{id} | Archive email subscriber
[**create_sms_subscriber**](SmsSubscriberApi.md#create_sms_subscriber) | **POST** /v2/SmsSubscriber | Create email subscriber
[**fetch_all_sms_subscribers**](SmsSubscriberApi.md#fetch_all_sms_subscribers) | **GET** /v2/SmsSubscriber/all | Fetch all email subscribers
[**restore_sms_subscriber**](SmsSubscriberApi.md#restore_sms_subscriber) | **PATCH** /v2/SmsSubscriber/{id} | Restore email subscriber
[**update_sms_subscriber**](SmsSubscriberApi.md#update_sms_subscriber) | **PUT** /v2/SmsSubscriber/{id} | Update email subscriber


# **archive_sms_subscriber**
> SmsSubscriber archive_sms_subscriber(id)

Archive email subscriber

### Example


```python
import wallet
from wallet.models.sms_subscriber import SmsSubscriber
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
    api_instance = wallet.SmsSubscriberApi(api_client)
    id = None # object | 

    try:
        # Archive email subscriber
        api_response = api_instance.archive_sms_subscriber(id)
        print("The response of SmsSubscriberApi->archive_sms_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmsSubscriberApi->archive_sms_subscriber: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**SmsSubscriber**](SmsSubscriber.md)

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

# **create_sms_subscriber**
> SmsSubscriber create_sms_subscriber(wt_sms_subscriber_create_params)

Create email subscriber

### Example


```python
import wallet
from wallet.models.sms_subscriber import SmsSubscriber
from wallet.models.wt_sms_subscriber_create_params import WTSmsSubscriberCreateParams
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
    api_instance = wallet.SmsSubscriberApi(api_client)
    wt_sms_subscriber_create_params = wallet.WTSmsSubscriberCreateParams() # WTSmsSubscriberCreateParams | 

    try:
        # Create email subscriber
        api_response = api_instance.create_sms_subscriber(wt_sms_subscriber_create_params)
        print("The response of SmsSubscriberApi->create_sms_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmsSubscriberApi->create_sms_subscriber: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_sms_subscriber_create_params** | [**WTSmsSubscriberCreateParams**](WTSmsSubscriberCreateParams.md)|  | 

### Return type

[**SmsSubscriber**](SmsSubscriber.md)

### Authorization

No authorization required

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

# **fetch_all_sms_subscribers**
> object fetch_all_sms_subscribers(start_date_time=start_date_time, end_date_time=end_date_time, is_archive_included=is_archive_included)

Fetch all email subscribers

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
    api_instance = wallet.SmsSubscriberApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all email subscribers
        api_response = api_instance.fetch_all_sms_subscribers(start_date_time=start_date_time, end_date_time=end_date_time, is_archive_included=is_archive_included)
        print("The response of SmsSubscriberApi->fetch_all_sms_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmsSubscriberApi->fetch_all_sms_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | [optional] 
 **end_date_time** | **datetime**|  | [optional] 
 **is_archive_included** | **bool**|  | [optional] 

### Return type

**object**

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

# **restore_sms_subscriber**
> SmsSubscriber restore_sms_subscriber(id)

Restore email subscriber

### Example


```python
import wallet
from wallet.models.sms_subscriber import SmsSubscriber
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
    api_instance = wallet.SmsSubscriberApi(api_client)
    id = None # object | 

    try:
        # Restore email subscriber
        api_response = api_instance.restore_sms_subscriber(id)
        print("The response of SmsSubscriberApi->restore_sms_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmsSubscriberApi->restore_sms_subscriber: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**SmsSubscriber**](SmsSubscriber.md)

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

# **update_sms_subscriber**
> SmsSubscriber update_sms_subscriber(id, wt_sms_subscriber_update_params)

Update email subscriber

### Example


```python
import wallet
from wallet.models.sms_subscriber import SmsSubscriber
from wallet.models.wt_sms_subscriber_update_params import WTSmsSubscriberUpdateParams
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
    api_instance = wallet.SmsSubscriberApi(api_client)
    id = None # object | 
    wt_sms_subscriber_update_params = wallet.WTSmsSubscriberUpdateParams() # WTSmsSubscriberUpdateParams | 

    try:
        # Update email subscriber
        api_response = api_instance.update_sms_subscriber(id, wt_sms_subscriber_update_params)
        print("The response of SmsSubscriberApi->update_sms_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmsSubscriberApi->update_sms_subscriber: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **wt_sms_subscriber_update_params** | [**WTSmsSubscriberUpdateParams**](WTSmsSubscriberUpdateParams.md)|  | 

### Return type

[**SmsSubscriber**](SmsSubscriber.md)

### Authorization

No authorization required

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

