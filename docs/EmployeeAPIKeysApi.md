# wallet.EmployeeAPIKeysApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_employee_api_keys**](EmployeeAPIKeysApi.md#archive_employee_api_keys) | **DELETE** /v2/employee/apiKeys/{id} | Archive employee API Key
[**create_employee_api_keys**](EmployeeAPIKeysApi.md#create_employee_api_keys) | **POST** /v2/employee/apiKeys | Create employee API Key
[**fetch_all_employee_api_keys**](EmployeeAPIKeysApi.md#fetch_all_employee_api_keys) | **GET** /v2/employee/apiKeys/all | Fetch all employee API Keys
[**fetch_employee_api_key_by_id**](EmployeeAPIKeysApi.md#fetch_employee_api_key_by_id) | **GET** /v2/employee/apiKeys/{id} | Fetch API Key
[**update_employee_api_keys**](EmployeeAPIKeysApi.md#update_employee_api_keys) | **PUT** /v2/employee/apiKeys/{id} | Update employee API Key


# **archive_employee_api_keys**
> EmployeeAPIKey archive_employee_api_keys(id)

Archive employee API Key

### Example


```python
import time
import wallet
from wallet.api import employee_api_keys_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.employee_api_key import EmployeeAPIKey
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
    api_instance = employee_api_keys_api.EmployeeAPIKeysApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive employee API Key
        api_response = api_instance.archive_employee_api_keys(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeeAPIKeysApi->archive_employee_api_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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

Create employee API Key

### Example


```python
import time
import wallet
from wallet.api import employee_api_keys_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.employee_api_key import EmployeeAPIKey
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_employee_api_key_create_params import WTEmployeeAPIKeyCreateParams
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
    api_instance = employee_api_keys_api.EmployeeAPIKeysApi(api_client)
    wt_employee_api_key_create_params = WTEmployeeAPIKeyCreateParams(
        title="This is the title of the API Key",
        description="This is the description of the API Key",
    ) # WTEmployeeAPIKeyCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create employee API Key
        api_response = api_instance.create_employee_api_keys(wt_employee_api_key_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeeAPIKeysApi->create_employee_api_keys: %s\n" % e)
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
> [EmployeeAPIKey] fetch_all_employee_api_keys()

Fetch all employee API Keys

### Example


```python
import time
import wallet
from wallet.api import employee_api_keys_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.employee_api_key import EmployeeAPIKey
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
    api_instance = employee_api_keys_api.EmployeeAPIKeysApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all employee API Keys
        api_response = api_instance.fetch_all_employee_api_keys(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeeAPIKeysApi->fetch_all_employee_api_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**[EmployeeAPIKey]**](EmployeeAPIKey.md)

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

Fetch API Key

### Example


```python
import time
import wallet
from wallet.api import employee_api_keys_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_employee_api_key import WTEmployeeAPIKey
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
    api_instance = employee_api_keys_api.EmployeeAPIKeysApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch API Key
        api_response = api_instance.fetch_employee_api_key_by_id(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeeAPIKeysApi->fetch_employee_api_key_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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

Update employee API Key

### Example


```python
import time
import wallet
from wallet.api import employee_api_keys_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.employee_api_key import EmployeeAPIKey
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_employee_api_key_update_params import WTEmployeeAPIKeyUpdateParams
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = employee_api_keys_api.EmployeeAPIKeysApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_employee_api_key_update_params = WTEmployeeAPIKeyUpdateParams(
        title="This is the title of the API Key",
        description="This is the description of the API Key",
    ) # WTEmployeeAPIKeyUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update employee API Key
        api_response = api_instance.update_employee_api_keys(id, wt_employee_api_key_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling EmployeeAPIKeysApi->update_employee_api_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

