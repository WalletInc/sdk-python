# wallet.SystemApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](SystemApi.md#create_role) | **POST** /v2/system/roles | Create role
[**delete_role**](SystemApi.md#delete_role) | **DELETE** /v2/system/roles/{roleID} | Delete role
[**fetch_audit_log_of_roles**](SystemApi.md#fetch_audit_log_of_roles) | **GET** /v2/system/roles/auditLog | Fetch role&#39;s audit log
[**fetch_employees_with_role**](SystemApi.md#fetch_employees_with_role) | **GET** /v2/system/roles/employees/{roleID} | Fetch employees with role
[**fetch_webpages_for_role**](SystemApi.md#fetch_webpages_for_role) | **GET** /v2/system/roles/webpages/{roleID} | Fetch webpages for role
[**get_payment_prefixes**](SystemApi.md#get_payment_prefixes) | **GET** /v2/system/prefixes | Get payment prefixes
[**load_role**](SystemApi.md#load_role) | **GET** /v2/system/roles/{roleID} | Fetch role
[**save_role**](SystemApi.md#save_role) | **PUT** /v2/system/roles/{roleID} | Update role


# **create_role**
> Role create_role(wt_system_role_create)

Create role

### Example


```python
import time
import wallet
from wallet.api import system_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.role import Role
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_system_role_create import WTSystemRoleCreate
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
    api_instance = system_api.SystemApi(api_client)
    wt_system_role_create = WTSystemRoleCreate(
        display_name="Marketing Associate",
        webpages_to_add=[
            "webpages_to_add_example",
        ],
    ) # WTSystemRoleCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create role
        api_response = api_instance.create_role(wt_system_role_create)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SystemApi->create_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_system_role_create** | [**WTSystemRoleCreate**](WTSystemRoleCreate.md)|  |

### Return type

[**Role**](Role.md)

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

# **delete_role**
> bool delete_role(role_id)

Delete role

### Example


```python
import time
import wallet
from wallet.api import system_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
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
    api_instance = system_api.SystemApi(api_client)
    role_id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Delete role
        api_response = api_instance.delete_role(role_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SystemApi->delete_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **NanoID**|  |

### Return type

**bool**

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

# **fetch_audit_log_of_roles**
> [RoleAuditLog] fetch_audit_log_of_roles(start_date_time, end_date_time)

Fetch role's audit log

### Example


```python
import time
import wallet
from wallet.api import system_api
from wallet.model.role_audit_log import RoleAuditLog
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
    api_instance = system_api.SystemApi(api_client)
    start_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | 
    end_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch role's audit log
        api_response = api_instance.fetch_audit_log_of_roles(start_date_time, end_date_time)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SystemApi->fetch_audit_log_of_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  |
 **end_date_time** | **datetime**|  |

### Return type

[**[RoleAuditLog]**](RoleAuditLog.md)

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

# **fetch_employees_with_role**
> [Employee] fetch_employees_with_role(role_id)

Fetch employees with role

### Example


```python
import time
import wallet
from wallet.api import system_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.employee import Employee
from wallet.model.nano_id import NanoID
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
    api_instance = system_api.SystemApi(api_client)
    role_id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch employees with role
        api_response = api_instance.fetch_employees_with_role(role_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SystemApi->fetch_employees_with_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **NanoID**|  |

### Return type

[**[Employee]**](Employee.md)

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

# **fetch_webpages_for_role**
> [Webpage] fetch_webpages_for_role(role_id)

Fetch webpages for role

### Example


```python
import time
import wallet
from wallet.api import system_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.webpage import Webpage
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
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
    api_instance = system_api.SystemApi(api_client)
    role_id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch webpages for role
        api_response = api_instance.fetch_webpages_for_role(role_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SystemApi->fetch_webpages_for_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **NanoID**|  |

### Return type

[**[Webpage]**](Webpage.md)

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

# **get_payment_prefixes**
> [bool, date, datetime, dict, float, int, list, str, none_type] get_payment_prefixes()

Get payment prefixes

### Example


```python
import time
import wallet
from wallet.api import system_api
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
    api_instance = system_api.SystemApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get payment prefixes
        api_response = api_instance.get_payment_prefixes()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SystemApi->get_payment_prefixes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[bool, date, datetime, dict, float, int, list, str, none_type]**

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

# **load_role**
> WTRole load_role(role_id)

Fetch role

### Example


```python
import time
import wallet
from wallet.api import system_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
from wallet.model.auth_error import AuthError
from wallet.model.wt_role import WTRole
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_api.SystemApi(api_client)
    role_id = NanoID("C") # NanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch role
        api_response = api_instance.load_role(role_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SystemApi->load_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **NanoID**|  |

### Return type

[**WTRole**](WTRole.md)

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

# **save_role**
> Role save_role(role_id, wt_system_role_create)

Update role

### Example


```python
import time
import wallet
from wallet.api import system_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.role import Role
from wallet.model.falsum_error import FalsumError
from wallet.model.nano_id import NanoID
from wallet.model.wt_system_role_create import WTSystemRoleCreate
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
    api_instance = system_api.SystemApi(api_client)
    role_id = NanoID("C") # NanoID | 
    wt_system_role_create = WTSystemRoleCreate(
        display_name="Marketing Associate",
        webpages_to_add=[
            "webpages_to_add_example",
        ],
    ) # WTSystemRoleCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Update role
        api_response = api_instance.save_role(role_id, wt_system_role_create)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling SystemApi->save_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **NanoID**|  |
 **wt_system_role_create** | [**WTSystemRoleCreate**](WTSystemRoleCreate.md)|  |

### Return type

[**Role**](Role.md)

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

