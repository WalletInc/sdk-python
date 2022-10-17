# wallet.IntegratedTerminalsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_pos_machine**](IntegratedTerminalsApi.md#archive_pos_machine) | **DELETE** /v2/pos/machine/{id} | Archive POS machine
[**create_pos_machine**](IntegratedTerminalsApi.md#create_pos_machine) | **POST** /v2/pos/machine | Create POS machine
[**fetch_all_pos_machines**](IntegratedTerminalsApi.md#fetch_all_pos_machines) | **GET** /v2/pos/machine/all | Fetch all POS machines
[**restore_pos_machine**](IntegratedTerminalsApi.md#restore_pos_machine) | **PATCH** /v2/pos/machine/{id} | Restore POS machine
[**update_pos_machine**](IntegratedTerminalsApi.md#update_pos_machine) | **PUT** /v2/pos/machine/{id} | Update POS machine


# **archive_pos_machine**
> WTPosMachine archive_pos_machine(id)

Archive POS machine

### Example


```python
import time
import wallet
from wallet.api import integrated_terminals_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_pos_machine import WTPosMachine
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
    api_instance = integrated_terminals_api.IntegratedTerminalsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive POS machine
        api_response = api_instance.archive_pos_machine(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling IntegratedTerminalsApi->archive_pos_machine: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**WTPosMachine**](WTPosMachine.md)

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

# **create_pos_machine**
> WTPosMachine create_pos_machine(wt_pos_machine_create_params)

Create POS machine

### Example


```python
import time
import wallet
from wallet.api import integrated_terminals_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_pos_machine import WTPosMachine
from wallet.model.wt_pos_machine_create_params import WTPosMachineCreateParams
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
    api_instance = integrated_terminals_api.IntegratedTerminalsApi(api_client)
    wt_pos_machine_create_params = WTPosMachineCreateParams(
        register_id="1",
        register_name="Register 1",
        outlet_name="California",
        outlet_number=5,
        profit_center="profit_center_example",
    ) # WTPosMachineCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create POS machine
        api_response = api_instance.create_pos_machine(wt_pos_machine_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling IntegratedTerminalsApi->create_pos_machine: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_pos_machine_create_params** | [**WTPosMachineCreateParams**](WTPosMachineCreateParams.md)|  |

### Return type

[**WTPosMachine**](WTPosMachine.md)

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

# **fetch_all_pos_machines**
> [bool, date, datetime, dict, float, int, list, str, none_type] fetch_all_pos_machines()

Fetch all POS machines

### Example


```python
import time
import wallet
from wallet.api import integrated_terminals_api
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
    api_instance = integrated_terminals_api.IntegratedTerminalsApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all POS machines
        api_response = api_instance.fetch_all_pos_machines(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling IntegratedTerminalsApi->fetch_all_pos_machines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

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

# **restore_pos_machine**
> WTPosMachine restore_pos_machine(id)

Restore POS machine

### Example


```python
import time
import wallet
from wallet.api import integrated_terminals_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_pos_machine import WTPosMachine
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
    api_instance = integrated_terminals_api.IntegratedTerminalsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore POS machine
        api_response = api_instance.restore_pos_machine(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling IntegratedTerminalsApi->restore_pos_machine: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**WTPosMachine**](WTPosMachine.md)

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

# **update_pos_machine**
> WTPosMachine update_pos_machine(id, wt_pos_machine_update_params)

Update POS machine

### Example


```python
import time
import wallet
from wallet.api import integrated_terminals_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_pos_machine import WTPosMachine
from wallet.model.wt_pos_machine_update_params import WTPosMachineUpdateParams
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
    api_instance = integrated_terminals_api.IntegratedTerminalsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_pos_machine_update_params = WTPosMachineUpdateParams(
        register_id="1",
        register_name="Register 1",
        outlet_name="California",
        outlet_number=5,
        profit_center="profit_center_example",
    ) # WTPosMachineUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update POS machine
        api_response = api_instance.update_pos_machine(id, wt_pos_machine_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling IntegratedTerminalsApi->update_pos_machine: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **wt_pos_machine_update_params** | [**WTPosMachineUpdateParams**](WTPosMachineUpdateParams.md)|  |

### Return type

[**WTPosMachine**](WTPosMachine.md)

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

