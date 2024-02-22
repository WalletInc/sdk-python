# wallet.EmailSubscriberApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_email_subscriber**](EmailSubscriberApi.md#archive_email_subscriber) | **DELETE** /v2/emailSubscriber/{id} | Archive email subscriber
[**create_email_subscriber**](EmailSubscriberApi.md#create_email_subscriber) | **POST** /v2/emailSubscriber | Create email subscriber
[**fetch_all_email_subscribers**](EmailSubscriberApi.md#fetch_all_email_subscribers) | **GET** /v2/emailSubscriber/all | Fetch all email subscribers
[**restore_email_subscriber**](EmailSubscriberApi.md#restore_email_subscriber) | **PATCH** /v2/emailSubscriber/{id} | Restore email subscriber
[**update_email_subscriber**](EmailSubscriberApi.md#update_email_subscriber) | **PUT** /v2/emailSubscriber/{id} | Update email subscriber


# **archive_email_subscriber**
> EmailSubscriber archive_email_subscriber(id)

Archive email subscriber

### Example


```python
import wallet
from wallet.models.email_subscriber import EmailSubscriber
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
    api_instance = wallet.EmailSubscriberApi(api_client)
    id = None # object | 

    try:
        # Archive email subscriber
        api_response = api_instance.archive_email_subscriber(id)
        print("The response of EmailSubscriberApi->archive_email_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSubscriberApi->archive_email_subscriber: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**EmailSubscriber**](EmailSubscriber.md)

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

# **create_email_subscriber**
> EmailSubscriber create_email_subscriber(wt_email_subscriber_create_params)

Create email subscriber

### Example


```python
import wallet
from wallet.models.email_subscriber import EmailSubscriber
from wallet.models.wt_email_subscriber_create_params import WTEmailSubscriberCreateParams
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
    api_instance = wallet.EmailSubscriberApi(api_client)
    wt_email_subscriber_create_params = wallet.WTEmailSubscriberCreateParams() # WTEmailSubscriberCreateParams | 

    try:
        # Create email subscriber
        api_response = api_instance.create_email_subscriber(wt_email_subscriber_create_params)
        print("The response of EmailSubscriberApi->create_email_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSubscriberApi->create_email_subscriber: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_email_subscriber_create_params** | [**WTEmailSubscriberCreateParams**](WTEmailSubscriberCreateParams.md)|  | 

### Return type

[**EmailSubscriber**](EmailSubscriber.md)

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

# **fetch_all_email_subscribers**
> object fetch_all_email_subscribers(start_date_time=start_date_time, end_date_time=end_date_time, is_archive_included=is_archive_included)

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
    api_instance = wallet.EmailSubscriberApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all email subscribers
        api_response = api_instance.fetch_all_email_subscribers(start_date_time=start_date_time, end_date_time=end_date_time, is_archive_included=is_archive_included)
        print("The response of EmailSubscriberApi->fetch_all_email_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSubscriberApi->fetch_all_email_subscribers: %s\n" % e)
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

# **restore_email_subscriber**
> EmailSubscriber restore_email_subscriber(id)

Restore email subscriber

### Example


```python
import wallet
from wallet.models.email_subscriber import EmailSubscriber
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
    api_instance = wallet.EmailSubscriberApi(api_client)
    id = None # object | 

    try:
        # Restore email subscriber
        api_response = api_instance.restore_email_subscriber(id)
        print("The response of EmailSubscriberApi->restore_email_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSubscriberApi->restore_email_subscriber: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**EmailSubscriber**](EmailSubscriber.md)

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

# **update_email_subscriber**
> EmailSubscriber update_email_subscriber(id, wt_email_subscriber_update_params)

Update email subscriber

### Example


```python
import wallet
from wallet.models.email_subscriber import EmailSubscriber
from wallet.models.wt_email_subscriber_update_params import WTEmailSubscriberUpdateParams
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
    api_instance = wallet.EmailSubscriberApi(api_client)
    id = None # object | 
    wt_email_subscriber_update_params = wallet.WTEmailSubscriberUpdateParams() # WTEmailSubscriberUpdateParams | 

    try:
        # Update email subscriber
        api_response = api_instance.update_email_subscriber(id, wt_email_subscriber_update_params)
        print("The response of EmailSubscriberApi->update_email_subscriber:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSubscriberApi->update_email_subscriber: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **wt_email_subscriber_update_params** | [**WTEmailSubscriberUpdateParams**](WTEmailSubscriberUpdateParams.md)|  | 

### Return type

[**EmailSubscriber**](EmailSubscriber.md)

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

