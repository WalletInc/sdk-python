# wallet.GamingApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_gaming**](GamingApi.md#archive_gaming) | **DELETE** /v2/gaming/{id} | Archive gaming
[**create_gaming**](GamingApi.md#create_gaming) | **POST** /v2/gaming | Create gaming
[**fetch_all_gaming**](GamingApi.md#fetch_all_gaming) | **GET** /v2/gaming/all | Fetch all gaming
[**restore_gaming**](GamingApi.md#restore_gaming) | **PATCH** /v2/gaming/{id} | Restore gaming
[**update_gaming**](GamingApi.md#update_gaming) | **PUT** /v2/gaming/{id} | Update gaming


# **archive_gaming**
> Gaming archive_gaming(id)

Archive gaming

### Example


```python
import wallet
from wallet.models.gaming import Gaming
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
    api_instance = wallet.GamingApi(api_client)
    id = None # object | 

    try:
        # Archive gaming
        api_response = api_instance.archive_gaming(id)
        print("The response of GamingApi->archive_gaming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamingApi->archive_gaming: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**Gaming**](Gaming.md)

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

# **create_gaming**
> Gaming create_gaming(wt_gaming_create_params)

Create gaming

### Example


```python
import wallet
from wallet.models.gaming import Gaming
from wallet.models.wt_gaming_create_params import WTGamingCreateParams
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
    api_instance = wallet.GamingApi(api_client)
    wt_gaming_create_params = wallet.WTGamingCreateParams() # WTGamingCreateParams | 

    try:
        # Create gaming
        api_response = api_instance.create_gaming(wt_gaming_create_params)
        print("The response of GamingApi->create_gaming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamingApi->create_gaming: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_gaming_create_params** | [**WTGamingCreateParams**](WTGamingCreateParams.md)|  | 

### Return type

[**Gaming**](Gaming.md)

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

# **fetch_all_gaming**
> object fetch_all_gaming(is_archive_included=is_archive_included)

Fetch all gaming

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
    api_instance = wallet.GamingApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all gaming
        api_response = api_instance.fetch_all_gaming(is_archive_included=is_archive_included)
        print("The response of GamingApi->fetch_all_gaming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamingApi->fetch_all_gaming: %s\n" % e)
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

# **restore_gaming**
> Gaming restore_gaming(id)

Restore gaming

### Example


```python
import wallet
from wallet.models.gaming import Gaming
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
    api_instance = wallet.GamingApi(api_client)
    id = None # object | 

    try:
        # Restore gaming
        api_response = api_instance.restore_gaming(id)
        print("The response of GamingApi->restore_gaming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamingApi->restore_gaming: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**Gaming**](Gaming.md)

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

# **update_gaming**
> Gaming update_gaming(id, wt_gaming_update_params)

Update gaming

### Example


```python
import wallet
from wallet.models.gaming import Gaming
from wallet.models.wt_gaming_update_params import WTGamingUpdateParams
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
    api_instance = wallet.GamingApi(api_client)
    id = None # object | 
    wt_gaming_update_params = wallet.WTGamingUpdateParams() # WTGamingUpdateParams | 

    try:
        # Update gaming
        api_response = api_instance.update_gaming(id, wt_gaming_update_params)
        print("The response of GamingApi->update_gaming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamingApi->update_gaming: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **wt_gaming_update_params** | [**WTGamingUpdateParams**](WTGamingUpdateParams.md)|  | 

### Return type

[**Gaming**](Gaming.md)

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

