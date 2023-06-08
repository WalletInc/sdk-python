# wallet.ServicesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_service**](ServicesApi.md#archive_service) | **DELETE** /v2/services/{id} | Archive service
[**create_service**](ServicesApi.md#create_service) | **POST** /v2/services | Create service
[**fetch_all_services**](ServicesApi.md#fetch_all_services) | **GET** /v2/services/all | Fetch all services
[**restore_service**](ServicesApi.md#restore_service) | **PATCH** /v2/services/{id} | Restore service
[**update_service**](ServicesApi.md#update_service) | **PUT** /v2/services/{id} | Update service


# **archive_service**
> Service archive_service(id)

Archive service

### Example


```python
import time
import wallet
from wallet.api import services_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.service import Service
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
    api_instance = services_api.ServicesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive service
        api_response = api_instance.archive_service(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ServicesApi->archive_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Service**](Service.md)

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

# **create_service**
> Service create_service(wt_service_create_params)

Create service

### Example


```python
import time
import wallet
from wallet.api import services_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.service import Service
from wallet.model.auth_error import AuthError
from wallet.model.wt_service_create_params import WTServiceCreateParams
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = services_api.ServicesApi(api_client)
    wt_service_create_params = WTServiceCreateParams(
        title="This is the title of the service",
        description="This is the description of the service",
        displayed_price="$200-$350",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.png",
        additional_info_url="https://your-website.com/service-1/reserve-now",
    ) # WTServiceCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create service
        api_response = api_instance.create_service(wt_service_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ServicesApi->create_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_service_create_params** | [**WTServiceCreateParams**](WTServiceCreateParams.md)|  |

### Return type

[**Service**](Service.md)

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

# **fetch_all_services**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_services()

Fetch all services

### Example


```python
import time
import wallet
from wallet.api import services_api
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
    api_instance = services_api.ServicesApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all services
        api_response = api_instance.fetch_all_services(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ServicesApi->fetch_all_services: %s\n" % e)
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

# **restore_service**
> Service restore_service(id)

Restore service

### Example


```python
import time
import wallet
from wallet.api import services_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.service import Service
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
    api_instance = services_api.ServicesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore service
        api_response = api_instance.restore_service(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ServicesApi->restore_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Service**](Service.md)

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

# **update_service**
> Service update_service(id, wt_service_update_params)

Update service

### Example


```python
import time
import wallet
from wallet.api import services_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_service_update_params import WTServiceUpdateParams
from wallet.model.service import Service
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
    api_instance = services_api.ServicesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_service_update_params = WTServiceUpdateParams(
        title="This is the title of the service",
        description="This is the description of the service",
        displayed_price="$200-$350",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.png",
        additional_info_url="https://your-website.com/service-1/reserve-now",
    ) # WTServiceUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update service
        api_response = api_instance.update_service(id, wt_service_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ServicesApi->update_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **wt_service_update_params** | [**WTServiceUpdateParams**](WTServiceUpdateParams.md)|  |

### Return type

[**Service**](Service.md)

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

