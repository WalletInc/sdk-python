# wallet.OptInListsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_opt_in_list_subscribers**](OptInListsApi.md#count_opt_in_list_subscribers) | **GET** /v2/sms/optInList/subscribers/count/{listID} | Count opt in list subscribers
[**count_opt_in_source_subscribers**](OptInListsApi.md#count_opt_in_source_subscribers) | **GET** /v2/sms/optInSource/subscribers/count/{sourceID} | Count opt in source subscribers
[**create_opt_in_list**](OptInListsApi.md#create_opt_in_list) | **POST** /v2/sms/optInList | Create opt in list
[**create_opt_in_list_source**](OptInListsApi.md#create_opt_in_list_source) | **POST** /v2/sms/optInListSource | Send SMS to opt in list
[**export_opt_in_list_subscribers**](OptInListsApi.md#export_opt_in_list_subscribers) | **POST** /v2/sms/optInList/subscribers/export/{listID} | Export opt in list subscribers
[**fetch_opt_in_list**](OptInListsApi.md#fetch_opt_in_list) | **GET** /v2/merchant/lists/optIn/{listID} | Get opt in list
[**fetch_opt_in_list_source**](OptInListsApi.md#fetch_opt_in_list_source) | **GET** /v2/employee/optInListSource/{sourceID} | Get opt in list source
[**fetch_opt_in_list_sources**](OptInListsApi.md#fetch_opt_in_list_sources) | **GET** /v2/sms/optInListSources/all | Get all opt in list sources
[**fetch_opt_in_list_sources_created_by_employee**](OptInListsApi.md#fetch_opt_in_list_sources_created_by_employee) | **GET** /v2/employee/optInListSources/all | Get all opt in list sources
[**fetch_opt_in_list_subscribers**](OptInListsApi.md#fetch_opt_in_list_subscribers) | **GET** /v2/sms/optInList/subscribers/{listID} | Get opt in list subscribers
[**fetch_opt_in_list_subscribers_by_page**](OptInListsApi.md#fetch_opt_in_list_subscribers_by_page) | **GET** /v2/sms/optInList/subscribers/page/{listID} | Get opt in list subscribers by page
[**fetch_opt_in_lists**](OptInListsApi.md#fetch_opt_in_lists) | **GET** /v2/merchant/lists/optIn/all | Get all opt in lists
[**fetch_opt_in_lists_associated_with_phone_number**](OptInListsApi.md#fetch_opt_in_lists_associated_with_phone_number) | **GET** /v2/sms/phoneNumber/lists/{phoneNumberID} | Get opt in lists
[**fetch_opt_in_source_subscribers**](OptInListsApi.md#fetch_opt_in_source_subscribers) | **GET** /v2/sms/optInSource/subscribers/{sourceID} | Get opt in source subscribers
[**fetch_opt_in_sources_associated_with_phone_number**](OptInListsApi.md#fetch_opt_in_sources_associated_with_phone_number) | **GET** /v2/sms/phoneNumber/sources/{phoneNumberID} | Get opt in sources
[**import_opt_in_list_subscribers**](OptInListsApi.md#import_opt_in_list_subscribers) | **POST** /v2/sms/optInList/subscribers/import/{listID} | Import opt in list subscribers
[**save_opt_in_list**](OptInListsApi.md#save_opt_in_list) | **PUT** /v2/sms/optInList/{listID} | Save opt in list
[**save_opt_in_list_source**](OptInListsApi.md#save_opt_in_list_source) | **PUT** /v2/sms/optInListSource/{sourceID} | Save opt in list source


# **count_opt_in_list_subscribers**
> WTCountResult count_opt_in_list_subscribers(list_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)

Count opt in list subscribers

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.OptInListsApi(api_client)
    list_id = 'list_id_example' # str | 
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count opt in list subscribers
        api_response = api_instance.count_opt_in_list_subscribers(list_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)
        print("The response of OptInListsApi->count_opt_in_list_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->count_opt_in_list_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **is_subscribed** | **bool**|  | [optional] 
 **is_pending_age21_verification** | **bool**|  | [optional] 
 **is_archive_included** | **bool**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **count_opt_in_source_subscribers**
> WTCountResult count_opt_in_source_subscribers(source_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)

Count opt in source subscribers

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.OptInListsApi(api_client)
    source_id = 'source_id_example' # str | 
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Count opt in source subscribers
        api_response = api_instance.count_opt_in_source_subscribers(source_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included, start_date=start_date, end_date=end_date)
        print("The response of OptInListsApi->count_opt_in_source_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->count_opt_in_source_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **is_subscribed** | **bool**|  | [optional] 
 **is_pending_age21_verification** | **bool**|  | [optional] 
 **is_archive_included** | **bool**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **create_opt_in_list**
> OptInList create_opt_in_list(wt_opt_in_list_creation_params)

Create opt in list

### Example


```python
import wallet
from wallet.models.opt_in_list import OptInList
from wallet.models.wt_opt_in_list_creation_params import WTOptInListCreationParams
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
    api_instance = wallet.OptInListsApi(api_client)
    wt_opt_in_list_creation_params = wallet.WTOptInListCreationParams() # WTOptInListCreationParams | 

    try:
        # Create opt in list
        api_response = api_instance.create_opt_in_list(wt_opt_in_list_creation_params)
        print("The response of OptInListsApi->create_opt_in_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->create_opt_in_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_opt_in_list_creation_params** | [**WTOptInListCreationParams**](WTOptInListCreationParams.md)|  | 

### Return type

[**OptInList**](OptInList.md)

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

# **create_opt_in_list_source**
> OptInListSource create_opt_in_list_source(wtsms_opt_in_list_source_create)

Send SMS to opt in list

### Example


```python
import wallet
from wallet.models.opt_in_list_source import OptInListSource
from wallet.models.wtsms_opt_in_list_source_create import WTSMSOptInListSourceCreate
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
    api_instance = wallet.OptInListsApi(api_client)
    wtsms_opt_in_list_source_create = wallet.WTSMSOptInListSourceCreate() # WTSMSOptInListSourceCreate | 

    try:
        # Send SMS to opt in list
        api_response = api_instance.create_opt_in_list_source(wtsms_opt_in_list_source_create)
        print("The response of OptInListsApi->create_opt_in_list_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->create_opt_in_list_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wtsms_opt_in_list_source_create** | [**WTSMSOptInListSourceCreate**](WTSMSOptInListSourceCreate.md)|  | 

### Return type

[**OptInListSource**](OptInListSource.md)

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

# **export_opt_in_list_subscribers**
> str export_opt_in_list_subscribers(list_id)

Export opt in list subscribers

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
    api_instance = wallet.OptInListsApi(api_client)
    list_id = 'list_id_example' # str | 

    try:
        # Export opt in list subscribers
        api_response = api_instance.export_opt_in_list_subscribers(list_id)
        print("The response of OptInListsApi->export_opt_in_list_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->export_opt_in_list_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 

### Return type

**str**

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

# **fetch_opt_in_list**
> OptInList fetch_opt_in_list(list_id)

Get opt in list

### Example


```python
import wallet
from wallet.models.opt_in_list import OptInList
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
    api_instance = wallet.OptInListsApi(api_client)
    list_id = 'list_id_example' # str | 

    try:
        # Get opt in list
        api_response = api_instance.fetch_opt_in_list(list_id)
        print("The response of OptInListsApi->fetch_opt_in_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->fetch_opt_in_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 

### Return type

[**OptInList**](OptInList.md)

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

# **fetch_opt_in_list_source**
> OptInListSource fetch_opt_in_list_source(source_id)

Get opt in list source

### Example


```python
import wallet
from wallet.models.opt_in_list_source import OptInListSource
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
    api_instance = wallet.OptInListsApi(api_client)
    source_id = 'source_id_example' # str | 

    try:
        # Get opt in list source
        api_response = api_instance.fetch_opt_in_list_source(source_id)
        print("The response of OptInListsApi->fetch_opt_in_list_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->fetch_opt_in_list_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 

### Return type

[**OptInListSource**](OptInListSource.md)

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

# **fetch_opt_in_list_sources**
> object fetch_opt_in_list_sources(is_archive_included=is_archive_included)

Get all opt in list sources

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
    api_instance = wallet.OptInListsApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all opt in list sources
        api_response = api_instance.fetch_opt_in_list_sources(is_archive_included=is_archive_included)
        print("The response of OptInListsApi->fetch_opt_in_list_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->fetch_opt_in_list_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **fetch_opt_in_list_sources_created_by_employee**
> List[OptInListSource] fetch_opt_in_list_sources_created_by_employee()

Get all opt in list sources

### Example


```python
import wallet
from wallet.models.opt_in_list_source import OptInListSource
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
    api_instance = wallet.OptInListsApi(api_client)

    try:
        # Get all opt in list sources
        api_response = api_instance.fetch_opt_in_list_sources_created_by_employee()
        print("The response of OptInListsApi->fetch_opt_in_list_sources_created_by_employee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->fetch_opt_in_list_sources_created_by_employee: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OptInListSource]**](OptInListSource.md)

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

# **fetch_opt_in_list_subscribers**
> List[OptInListSubscriber] fetch_opt_in_list_subscribers(list_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)

Get opt in list subscribers

### Example


```python
import wallet
from wallet.models.opt_in_list_subscriber import OptInListSubscriber
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
    api_instance = wallet.OptInListsApi(api_client)
    list_id = 'list_id_example' # str | 
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)

    try:
        # Get opt in list subscribers
        api_response = api_instance.fetch_opt_in_list_subscribers(list_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)
        print("The response of OptInListsApi->fetch_opt_in_list_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->fetch_opt_in_list_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **is_subscribed** | **bool**|  | [optional] 
 **is_pending_age21_verification** | **bool**|  | [optional] 
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[OptInListSubscriber]**](OptInListSubscriber.md)

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

# **fetch_opt_in_list_subscribers_by_page**
> FetchOptInListSubscribersByPage200Response fetch_opt_in_list_subscribers_by_page(list_id, page_size=page_size, page_num=page_num, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)

Get opt in list subscribers by page

### Example


```python
import wallet
from wallet.models.fetch_opt_in_list_subscribers_by_page200_response import FetchOptInListSubscribersByPage200Response
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
    api_instance = wallet.OptInListsApi(api_client)
    list_id = 'list_id_example' # str | 
    page_size = 3.4 # float |  (optional)
    page_num = 3.4 # float |  (optional)
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)

    try:
        # Get opt in list subscribers by page
        api_response = api_instance.fetch_opt_in_list_subscribers_by_page(list_id, page_size=page_size, page_num=page_num, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)
        print("The response of OptInListsApi->fetch_opt_in_list_subscribers_by_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->fetch_opt_in_list_subscribers_by_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **page_size** | **float**|  | [optional] 
 **page_num** | **float**|  | [optional] 
 **is_subscribed** | **bool**|  | [optional] 
 **is_pending_age21_verification** | **bool**|  | [optional] 
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**FetchOptInListSubscribersByPage200Response**](FetchOptInListSubscribersByPage200Response.md)

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

# **fetch_opt_in_lists**
> object fetch_opt_in_lists(is_archive_included=is_archive_included)

Get all opt in lists

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
    api_instance = wallet.OptInListsApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all opt in lists
        api_response = api_instance.fetch_opt_in_lists(is_archive_included=is_archive_included)
        print("The response of OptInListsApi->fetch_opt_in_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->fetch_opt_in_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **fetch_opt_in_lists_associated_with_phone_number**
> List[OptInList] fetch_opt_in_lists_associated_with_phone_number(phone_number_id)

Get opt in lists

### Example


```python
import wallet
from wallet.models.opt_in_list import OptInList
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
    api_instance = wallet.OptInListsApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 

    try:
        # Get opt in lists
        api_response = api_instance.fetch_opt_in_lists_associated_with_phone_number(phone_number_id)
        print("The response of OptInListsApi->fetch_opt_in_lists_associated_with_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->fetch_opt_in_lists_associated_with_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 

### Return type

[**List[OptInList]**](OptInList.md)

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

# **fetch_opt_in_source_subscribers**
> List[OptInListSubscriber] fetch_opt_in_source_subscribers(source_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)

Get opt in source subscribers

### Example


```python
import wallet
from wallet.models.opt_in_list_subscriber import OptInListSubscriber
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
    api_instance = wallet.OptInListsApi(api_client)
    source_id = 'source_id_example' # str | 
    is_subscribed = True # bool |  (optional)
    is_pending_age21_verification = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)

    try:
        # Get opt in source subscribers
        api_response = api_instance.fetch_opt_in_source_subscribers(source_id, is_subscribed=is_subscribed, is_pending_age21_verification=is_pending_age21_verification, is_archive_included=is_archive_included)
        print("The response of OptInListsApi->fetch_opt_in_source_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->fetch_opt_in_source_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **is_subscribed** | **bool**|  | [optional] 
 **is_pending_age21_verification** | **bool**|  | [optional] 
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[OptInListSubscriber]**](OptInListSubscriber.md)

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

# **fetch_opt_in_sources_associated_with_phone_number**
> List[OptInListSource] fetch_opt_in_sources_associated_with_phone_number(phone_number_id)

Get opt in sources

### Example


```python
import wallet
from wallet.models.opt_in_list_source import OptInListSource
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
    api_instance = wallet.OptInListsApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | 

    try:
        # Get opt in sources
        api_response = api_instance.fetch_opt_in_sources_associated_with_phone_number(phone_number_id)
        print("The response of OptInListsApi->fetch_opt_in_sources_associated_with_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->fetch_opt_in_sources_associated_with_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**|  | 

### Return type

[**List[OptInListSource]**](OptInListSource.md)

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

# **import_opt_in_list_subscribers**
> str import_opt_in_list_subscribers(list_id, wtsms_import_opt_in_list_subscribers)

Import opt in list subscribers

### Example


```python
import wallet
from wallet.models.wtsms_import_opt_in_list_subscribers import WTSMSImportOptInListSubscribers
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
    api_instance = wallet.OptInListsApi(api_client)
    list_id = 'list_id_example' # str | 
    wtsms_import_opt_in_list_subscribers = wallet.WTSMSImportOptInListSubscribers() # WTSMSImportOptInListSubscribers | 

    try:
        # Import opt in list subscribers
        api_response = api_instance.import_opt_in_list_subscribers(list_id, wtsms_import_opt_in_list_subscribers)
        print("The response of OptInListsApi->import_opt_in_list_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->import_opt_in_list_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **wtsms_import_opt_in_list_subscribers** | [**WTSMSImportOptInListSubscribers**](WTSMSImportOptInListSubscribers.md)|  | 

### Return type

**str**

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

# **save_opt_in_list**
> OptInList save_opt_in_list(list_id, wt_opt_in_list_creation_params)

Save opt in list

### Example


```python
import wallet
from wallet.models.opt_in_list import OptInList
from wallet.models.wt_opt_in_list_creation_params import WTOptInListCreationParams
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
    api_instance = wallet.OptInListsApi(api_client)
    list_id = 'list_id_example' # str | 
    wt_opt_in_list_creation_params = wallet.WTOptInListCreationParams() # WTOptInListCreationParams | 

    try:
        # Save opt in list
        api_response = api_instance.save_opt_in_list(list_id, wt_opt_in_list_creation_params)
        print("The response of OptInListsApi->save_opt_in_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->save_opt_in_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 
 **wt_opt_in_list_creation_params** | [**WTOptInListCreationParams**](WTOptInListCreationParams.md)|  | 

### Return type

[**OptInList**](OptInList.md)

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

# **save_opt_in_list_source**
> OptInListSource save_opt_in_list_source(source_id, wtsms_opt_in_list_source_create)

Save opt in list source

### Example


```python
import wallet
from wallet.models.opt_in_list_source import OptInListSource
from wallet.models.wtsms_opt_in_list_source_create import WTSMSOptInListSourceCreate
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
    api_instance = wallet.OptInListsApi(api_client)
    source_id = 'source_id_example' # str | 
    wtsms_opt_in_list_source_create = wallet.WTSMSOptInListSourceCreate() # WTSMSOptInListSourceCreate | 

    try:
        # Save opt in list source
        api_response = api_instance.save_opt_in_list_source(source_id, wtsms_opt_in_list_source_create)
        print("The response of OptInListsApi->save_opt_in_list_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OptInListsApi->save_opt_in_list_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **wtsms_opt_in_list_source_create** | [**WTSMSOptInListSourceCreate**](WTSMSOptInListSourceCreate.md)|  | 

### Return type

[**OptInListSource**](OptInListSource.md)

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

