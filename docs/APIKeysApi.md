# wallet.APIKeysApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_employee_api_keys**](APIKeysApi.md#archive_employee_api_keys) | **DELETE** /v2/employee/apiKeys/{id} | Archive API Key
[**create_employee_api_keys**](APIKeysApi.md#create_employee_api_keys) | **POST** /v2/employee/apiKeys | Create API Key
[**fetch_all_employee_api_keys**](APIKeysApi.md#fetch_all_employee_api_keys) | **GET** /v2/employee/apiKeys/all | Get API Keys
[**fetch_employee_api_key_by_id**](APIKeysApi.md#fetch_employee_api_key_by_id) | **GET** /v2/employee/apiKeys/{id} | Get API Key
[**update_employee_api_keys**](APIKeysApi.md#update_employee_api_keys) | **PUT** /v2/employee/apiKeys/{id} | Update API Key


# **archive_employee_api_keys**
> EmployeeAPIKey archive_employee_api_keys(id)

Archive API Key

### Example


```python
import wallet
from wallet.models.employee_api_key import EmployeeAPIKey
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
    api_instance = wallet.APIKeysApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive API Key
        api_response = api_instance.archive_employee_api_keys(id)
        print("The response of APIKeysApi->archive_employee_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->archive_employee_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**EmployeeAPIKey**](EmployeeAPIKey.md)

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

# **create_employee_api_keys**
> EmployeeAPIKey create_employee_api_keys(wt_employee_api_key_create_params)

Create API Key

### Example


```python
import wallet
from wallet.models.employee_api_key import EmployeeAPIKey
from wallet.models.wt_employee_api_key_create_params import WTEmployeeAPIKeyCreateParams
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
    api_instance = wallet.APIKeysApi(api_client)
    wt_employee_api_key_create_params = wallet.WTEmployeeAPIKeyCreateParams() # WTEmployeeAPIKeyCreateParams | 

    try:
        # Create API Key
        api_response = api_instance.create_employee_api_keys(wt_employee_api_key_create_params)
        print("The response of APIKeysApi->create_employee_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->create_employee_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_employee_api_key_create_params** | [**WTEmployeeAPIKeyCreateParams**](WTEmployeeAPIKeyCreateParams.md)|  | 

### Return type

[**EmployeeAPIKey**](EmployeeAPIKey.md)

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

# **fetch_all_employee_api_keys**
> List[EmployeeAPIKey] fetch_all_employee_api_keys(is_archive_included=is_archive_included)

Get API Keys

### Example


```python
import wallet
from wallet.models.employee_api_key import EmployeeAPIKey
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
    api_instance = wallet.APIKeysApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get API Keys
        api_response = api_instance.fetch_all_employee_api_keys(is_archive_included=is_archive_included)
        print("The response of APIKeysApi->fetch_all_employee_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->fetch_all_employee_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[EmployeeAPIKey]**](EmployeeAPIKey.md)

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

# **fetch_employee_api_key_by_id**
> WTEmployeeAPIKey fetch_employee_api_key_by_id(id)

Get API Key

### Example


```python
import wallet
from wallet.models.wt_employee_api_key import WTEmployeeAPIKey
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
    api_instance = wallet.APIKeysApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get API Key
        api_response = api_instance.fetch_employee_api_key_by_id(id)
        print("The response of APIKeysApi->fetch_employee_api_key_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->fetch_employee_api_key_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTEmployeeAPIKey**](WTEmployeeAPIKey.md)

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

# **update_employee_api_keys**
> EmployeeAPIKey update_employee_api_keys(id, wt_employee_api_key_update_params)

Update API Key

### Example


```python
import wallet
from wallet.models.employee_api_key import EmployeeAPIKey
from wallet.models.wt_employee_api_key_update_params import WTEmployeeAPIKeyUpdateParams
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
    api_instance = wallet.APIKeysApi(api_client)
    id = 'id_example' # str | 
    wt_employee_api_key_update_params = wallet.WTEmployeeAPIKeyUpdateParams() # WTEmployeeAPIKeyUpdateParams | 

    try:
        # Update API Key
        api_response = api_instance.update_employee_api_keys(id, wt_employee_api_key_update_params)
        print("The response of APIKeysApi->update_employee_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->update_employee_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wt_employee_api_key_update_params** | [**WTEmployeeAPIKeyUpdateParams**](WTEmployeeAPIKeyUpdateParams.md)|  | 

### Return type

[**EmployeeAPIKey**](EmployeeAPIKey.md)

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

