# wallet.ServicesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_service**](ServicesApi.md#archive_service) | **DELETE** /v2/services/{id} | Archive Service
[**create_service**](ServicesApi.md#create_service) | **POST** /v2/services | Create Service
[**fetch_all_services**](ServicesApi.md#fetch_all_services) | **GET** /v2/services/all | Get all Services
[**restore_service**](ServicesApi.md#restore_service) | **PATCH** /v2/services/{id} | Restore Service
[**update_service**](ServicesApi.md#update_service) | **PUT** /v2/services/{id} | Update Service


# **archive_service**
> Service archive_service(id)

Archive Service

### Example


```python
import wallet
from wallet.models.service import Service
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
    api_instance = wallet.ServicesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive Service
        api_response = api_instance.archive_service(id)
        print("The response of ServicesApi->archive_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->archive_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Create Service

### Example


```python
import wallet
from wallet.models.service import Service
from wallet.models.wt_service_create_params import WTServiceCreateParams
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
    api_instance = wallet.ServicesApi(api_client)
    wt_service_create_params = wallet.WTServiceCreateParams() # WTServiceCreateParams | 

    try:
        # Create Service
        api_response = api_instance.create_service(wt_service_create_params)
        print("The response of ServicesApi->create_service:\n")
        pprint(api_response)
    except Exception as e:
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
> object fetch_all_services(is_archive_included=is_archive_included)

Get all Services

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
    api_instance = wallet.ServicesApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all Services
        api_response = api_instance.fetch_all_services(is_archive_included=is_archive_included)
        print("The response of ServicesApi->fetch_all_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->fetch_all_services: %s\n" % e)
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

# **restore_service**
> Service restore_service(id)

Restore Service

### Example


```python
import wallet
from wallet.models.service import Service
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
    api_instance = wallet.ServicesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore Service
        api_response = api_instance.restore_service(id)
        print("The response of ServicesApi->restore_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->restore_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Update Service

### Example


```python
import wallet
from wallet.models.service import Service
from wallet.models.wt_service_update_params import WTServiceUpdateParams
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
    api_instance = wallet.ServicesApi(api_client)
    id = 'id_example' # str | 
    wt_service_update_params = wallet.WTServiceUpdateParams() # WTServiceUpdateParams | 

    try:
        # Update Service
        api_response = api_instance.update_service(id, wt_service_update_params)
        print("The response of ServicesApi->update_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->update_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

