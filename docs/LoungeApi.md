# wallet.LoungeApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_lounge**](LoungeApi.md#archive_lounge) | **DELETE** /v2/lounge/{id} | Archive Lounge
[**create_lounge**](LoungeApi.md#create_lounge) | **POST** /v2/lounge | Create Lounge
[**fetch_all_lounge**](LoungeApi.md#fetch_all_lounge) | **GET** /v2/lounge/all | Get all Lounges
[**restore_lounge**](LoungeApi.md#restore_lounge) | **PATCH** /v2/lounge/{id} | Restore Lounge
[**update_lounge**](LoungeApi.md#update_lounge) | **PUT** /v2/lounge/{id} | Update Lounge


# **archive_lounge**
> Lounge archive_lounge(id)

Archive Lounge

### Example


```python
import wallet
from wallet.models.lounge import Lounge
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
    api_instance = wallet.LoungeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive Lounge
        api_response = api_instance.archive_lounge(id)
        print("The response of LoungeApi->archive_lounge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoungeApi->archive_lounge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Lounge**](Lounge.md)

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

# **create_lounge**
> Lounge create_lounge(wt_lounge_create_params)

Create Lounge

### Example


```python
import wallet
from wallet.models.lounge import Lounge
from wallet.models.wt_lounge_create_params import WTLoungeCreateParams
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
    api_instance = wallet.LoungeApi(api_client)
    wt_lounge_create_params = wallet.WTLoungeCreateParams() # WTLoungeCreateParams | 

    try:
        # Create Lounge
        api_response = api_instance.create_lounge(wt_lounge_create_params)
        print("The response of LoungeApi->create_lounge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoungeApi->create_lounge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_lounge_create_params** | [**WTLoungeCreateParams**](WTLoungeCreateParams.md)|  | 

### Return type

[**Lounge**](Lounge.md)

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

# **fetch_all_lounge**
> object fetch_all_lounge(is_archive_included=is_archive_included)

Get all Lounges

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
    api_instance = wallet.LoungeApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all Lounges
        api_response = api_instance.fetch_all_lounge(is_archive_included=is_archive_included)
        print("The response of LoungeApi->fetch_all_lounge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoungeApi->fetch_all_lounge: %s\n" % e)
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

# **restore_lounge**
> Lounge restore_lounge(id)

Restore Lounge

### Example


```python
import wallet
from wallet.models.lounge import Lounge
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
    api_instance = wallet.LoungeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore Lounge
        api_response = api_instance.restore_lounge(id)
        print("The response of LoungeApi->restore_lounge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoungeApi->restore_lounge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Lounge**](Lounge.md)

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

# **update_lounge**
> Lounge update_lounge(id, wt_lounge_update_params)

Update Lounge

### Example


```python
import wallet
from wallet.models.lounge import Lounge
from wallet.models.wt_lounge_update_params import WTLoungeUpdateParams
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
    api_instance = wallet.LoungeApi(api_client)
    id = 'id_example' # str | 
    wt_lounge_update_params = wallet.WTLoungeUpdateParams() # WTLoungeUpdateParams | 

    try:
        # Update Lounge
        api_response = api_instance.update_lounge(id, wt_lounge_update_params)
        print("The response of LoungeApi->update_lounge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoungeApi->update_lounge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wt_lounge_update_params** | [**WTLoungeUpdateParams**](WTLoungeUpdateParams.md)|  | 

### Return type

[**Lounge**](Lounge.md)

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

