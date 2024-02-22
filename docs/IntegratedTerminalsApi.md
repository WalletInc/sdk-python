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
import wallet
from wallet.models.wt_pos_machine import WTPosMachine
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
    api_instance = wallet.IntegratedTerminalsApi(api_client)
    id = None # object | 

    try:
        # Archive POS machine
        api_response = api_instance.archive_pos_machine(id)
        print("The response of IntegratedTerminalsApi->archive_pos_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedTerminalsApi->archive_pos_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
import wallet
from wallet.models.wt_pos_machine import WTPosMachine
from wallet.models.wt_pos_machine_create_params import WTPosMachineCreateParams
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
    api_instance = wallet.IntegratedTerminalsApi(api_client)
    wt_pos_machine_create_params = wallet.WTPosMachineCreateParams() # WTPosMachineCreateParams | 

    try:
        # Create POS machine
        api_response = api_instance.create_pos_machine(wt_pos_machine_create_params)
        print("The response of IntegratedTerminalsApi->create_pos_machine:\n")
        pprint(api_response)
    except Exception as e:
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
> List[object] fetch_all_pos_machines(is_archive_included=is_archive_included)

Fetch all POS machines

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
    api_instance = wallet.IntegratedTerminalsApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all POS machines
        api_response = api_instance.fetch_all_pos_machines(is_archive_included=is_archive_included)
        print("The response of IntegratedTerminalsApi->fetch_all_pos_machines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedTerminalsApi->fetch_all_pos_machines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

**List[object]**

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
import wallet
from wallet.models.wt_pos_machine import WTPosMachine
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
    api_instance = wallet.IntegratedTerminalsApi(api_client)
    id = None # object | 

    try:
        # Restore POS machine
        api_response = api_instance.restore_pos_machine(id)
        print("The response of IntegratedTerminalsApi->restore_pos_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedTerminalsApi->restore_pos_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
import wallet
from wallet.models.wt_pos_machine import WTPosMachine
from wallet.models.wt_pos_machine_update_params import WTPosMachineUpdateParams
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
    api_instance = wallet.IntegratedTerminalsApi(api_client)
    id = None # object | 
    wt_pos_machine_update_params = wallet.WTPosMachineUpdateParams() # WTPosMachineUpdateParams | 

    try:
        # Update POS machine
        api_response = api_instance.update_pos_machine(id, wt_pos_machine_update_params)
        print("The response of IntegratedTerminalsApi->update_pos_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratedTerminalsApi->update_pos_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
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

