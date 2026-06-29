# wallet.SMSSubscribersApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_sms_subscriber**](SMSSubscribersApi.md#archive_sms_subscriber) | **DELETE** /v2/SmsSubscriber/{id} | Archive SMS Subscriber
[**create_sms_subscriber**](SMSSubscribersApi.md#create_sms_subscriber) | **POST** /v2/SmsSubscriber | Create SMS Subscriber
[**fetch_all_sms_subscribers**](SMSSubscribersApi.md#fetch_all_sms_subscribers) | **GET** /v2/SmsSubscriber/all | Get all SMS Subscribers
[**restore_sms_subscriber**](SMSSubscribersApi.md#restore_sms_subscriber) | **PATCH** /v2/SmsSubscriber/{id} | Restore SMS Subscriber
[**update_sms_subscriber**](SMSSubscribersApi.md#update_sms_subscriber) | **PUT** /v2/SmsSubscriber/{id} | Update SMS Subscriber


# **archive_sms_subscriber**
> SmsSubscriber archive_sms_subscriber(id)

Archive SMS Subscriber

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
    api_instance = wallet.SMSSubscribersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive SMS Subscriber
        api_response = api_instance.archive_sms_subscriber(id)
        print("The response of SMSSubscribersApi->archive_sms_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSSubscribersApi->archive_sms_subscriber: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Create SMS Subscriber

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
    api_instance = wallet.SMSSubscribersApi(api_client)
    wt_sms_subscriber_create_params = wallet.WTSmsSubscriberCreateParams() # WTSmsSubscriberCreateParams | 

    try:
        # Create SMS Subscriber
        api_response = api_instance.create_sms_subscriber(wt_sms_subscriber_create_params)
        print("The response of SMSSubscribersApi->create_sms_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSSubscribersApi->create_sms_subscriber: %s\n" % e)
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

Get all SMS Subscribers

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
    api_instance = wallet.SMSSubscribersApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all SMS Subscribers
        api_response = api_instance.fetch_all_sms_subscribers(start_date_time=start_date_time, end_date_time=end_date_time, is_archive_included=is_archive_included)
        print("The response of SMSSubscribersApi->fetch_all_sms_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSSubscribersApi->fetch_all_sms_subscribers: %s\n" % e)
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

Restore SMS Subscriber

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
    api_instance = wallet.SMSSubscribersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore SMS Subscriber
        api_response = api_instance.restore_sms_subscriber(id)
        print("The response of SMSSubscribersApi->restore_sms_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSSubscribersApi->restore_sms_subscriber: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Update SMS Subscriber

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
    api_instance = wallet.SMSSubscribersApi(api_client)
    id = 'id_example' # str | 
    wt_sms_subscriber_update_params = wallet.WTSmsSubscriberUpdateParams() # WTSmsSubscriberUpdateParams | 

    try:
        # Update SMS Subscriber
        api_response = api_instance.update_sms_subscriber(id, wt_sms_subscriber_update_params)
        print("The response of SMSSubscribersApi->update_sms_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SMSSubscribersApi->update_sms_subscriber: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

