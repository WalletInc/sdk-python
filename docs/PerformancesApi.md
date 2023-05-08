# wallet.PerformancesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_performance**](PerformancesApi.md#archive_performance) | **DELETE** /v2/performances/{id} | Archive performance
[**create_performance**](PerformancesApi.md#create_performance) | **POST** /v2/performances | Create performance
[**fetch_all_performances**](PerformancesApi.md#fetch_all_performances) | **GET** /v2/performances/all | Fetch all performances
[**restore_performance**](PerformancesApi.md#restore_performance) | **PATCH** /v2/performances/{id} | Restore performance
[**update_performance**](PerformancesApi.md#update_performance) | **PUT** /v2/performances/{id} | Update performance


# **archive_performance**
> Performance archive_performance(id)

Archive performance

### Example


```python
import time
import wallet
from wallet.api import performances_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.performance import Performance
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
    api_instance = performances_api.PerformancesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive performance
        api_response = api_instance.archive_performance(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->archive_performance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Performance**](Performance.md)

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

# **create_performance**
> Performance create_performance(wt_performance_create_params)

Create performance

### Example


```python
import time
import wallet
from wallet.api import performances_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.performance import Performance
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_performance_create_params import WTPerformanceCreateParams
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = performances_api.PerformancesApi(api_client)
    wt_performance_create_params = WTPerformanceCreateParams(
        title="This is the title of the performance",
        body="This is the description of the performance",
        start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        price="43.29",
        url="https://example.com/performance.html",
        order_number=5,
        is_sold_out=True,
        media_url="https://wall.et/media/H847Sjudbw.png",
    ) # WTPerformanceCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create performance
        api_response = api_instance.create_performance(wt_performance_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->create_performance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_performance_create_params** | [**WTPerformanceCreateParams**](WTPerformanceCreateParams.md)|  |

### Return type

[**Performance**](Performance.md)

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

# **fetch_all_performances**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_performances()

Fetch all performances

### Example


```python
import time
import wallet
from wallet.api import performances_api
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
    api_instance = performances_api.PerformancesApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all performances
        api_response = api_instance.fetch_all_performances(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->fetch_all_performances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **restore_performance**
> Performance restore_performance(id)

Restore performance

### Example


```python
import time
import wallet
from wallet.api import performances_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.performance import Performance
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
    api_instance = performances_api.PerformancesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore performance
        api_response = api_instance.restore_performance(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->restore_performance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Performance**](Performance.md)

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

# **update_performance**
> Performance update_performance(id, wt_performance_update_params)

Update performance

### Example


```python
import time
import wallet
from wallet.api import performances_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.performance import Performance
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_performance_update_params import WTPerformanceUpdateParams
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = performances_api.PerformancesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_performance_update_params = WTPerformanceUpdateParams(
        title="This is the title of the performance",
        body="This is the description of the performance",
        start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        price="43.29",
        url="https://example.com/performance.html",
        order_number=5,
        is_sold_out=True,
        media_url="https://wall.et/media/H847Sjudbw.png",
    ) # WTPerformanceUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update performance
        api_response = api_instance.update_performance(id, wt_performance_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->update_performance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **wt_performance_update_params** | [**WTPerformanceUpdateParams**](WTPerformanceUpdateParams.md)|  |

### Return type

[**Performance**](Performance.md)

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

