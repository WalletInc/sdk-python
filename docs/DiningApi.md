# wallet.DiningApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_dining**](DiningApi.md#archive_dining) | **DELETE** /v2/dining/{id} | Archive dining
[**create_dining**](DiningApi.md#create_dining) | **POST** /v2/dining | Create dining
[**fetch_all_dining**](DiningApi.md#fetch_all_dining) | **GET** /v2/dining/all | Fetch all dining
[**restore_dining**](DiningApi.md#restore_dining) | **PATCH** /v2/dining/{id} | Restore dining
[**update_dining**](DiningApi.md#update_dining) | **PUT** /v2/dining/{id} | Update dining


# **archive_dining**
> Dining archive_dining(id)

Archive dining

### Example


```python
import wallet
from wallet.models.dining import Dining
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
    api_instance = wallet.DiningApi(api_client)
    id = None # object | 

    try:
        # Archive dining
        api_response = api_instance.archive_dining(id)
        print("The response of DiningApi->archive_dining:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiningApi->archive_dining: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**Dining**](Dining.md)

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

# **create_dining**
> Dining create_dining(wt_dining_create_params)

Create dining

### Example


```python
import wallet
from wallet.models.dining import Dining
from wallet.models.wt_dining_create_params import WTDiningCreateParams
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
    api_instance = wallet.DiningApi(api_client)
    wt_dining_create_params = wallet.WTDiningCreateParams() # WTDiningCreateParams | 

    try:
        # Create dining
        api_response = api_instance.create_dining(wt_dining_create_params)
        print("The response of DiningApi->create_dining:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiningApi->create_dining: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_dining_create_params** | [**WTDiningCreateParams**](WTDiningCreateParams.md)|  | 

### Return type

[**Dining**](Dining.md)

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

# **fetch_all_dining**
> object fetch_all_dining(is_archive_included=is_archive_included)

Fetch all dining

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
    api_instance = wallet.DiningApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all dining
        api_response = api_instance.fetch_all_dining(is_archive_included=is_archive_included)
        print("The response of DiningApi->fetch_all_dining:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiningApi->fetch_all_dining: %s\n" % e)
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

# **restore_dining**
> Dining restore_dining(id)

Restore dining

### Example


```python
import wallet
from wallet.models.dining import Dining
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
    api_instance = wallet.DiningApi(api_client)
    id = None # object | 

    try:
        # Restore dining
        api_response = api_instance.restore_dining(id)
        print("The response of DiningApi->restore_dining:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiningApi->restore_dining: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**Dining**](Dining.md)

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

# **update_dining**
> Dining update_dining(id, wt_dining_update_params)

Update dining

### Example


```python
import wallet
from wallet.models.dining import Dining
from wallet.models.wt_dining_update_params import WTDiningUpdateParams
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
    api_instance = wallet.DiningApi(api_client)
    id = None # object | 
    wt_dining_update_params = wallet.WTDiningUpdateParams() # WTDiningUpdateParams | 

    try:
        # Update dining
        api_response = api_instance.update_dining(id, wt_dining_update_params)
        print("The response of DiningApi->update_dining:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiningApi->update_dining: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **wt_dining_update_params** | [**WTDiningUpdateParams**](WTDiningUpdateParams.md)|  | 

### Return type

[**Dining**](Dining.md)

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

