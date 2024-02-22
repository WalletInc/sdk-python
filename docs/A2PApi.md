# wallet.A2PApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**begin_a2_p_application**](A2PApi.md#begin_a2_p_application) | **POST** /v2/a2p/application | Create A2P Application
[**fetch_a2_p_application**](A2PApi.md#fetch_a2_p_application) | **GET** /v2/a2p/application | Fetch A2P Application
[**fetch_a2_p_registration**](A2PApi.md#fetch_a2_p_registration) | **GET** /v2/a2p/registration | Fetch A2P Registration
[**update_a2_p_application**](A2PApi.md#update_a2_p_application) | **PUT** /v2/a2p/application/{applicationID} | Update A2P Application


# **begin_a2_p_application**
> bool begin_a2_p_application(a2_p_application_submission)

Create A2P Application

### Example


```python
import wallet
from wallet.models.a2_p_application_submission import A2PApplicationSubmission
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
    api_instance = wallet.A2PApi(api_client)
    a2_p_application_submission = wallet.A2PApplicationSubmission() # A2PApplicationSubmission | 

    try:
        # Create A2P Application
        api_response = api_instance.begin_a2_p_application(a2_p_application_submission)
        print("The response of A2PApi->begin_a2_p_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling A2PApi->begin_a2_p_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **a2_p_application_submission** | [**A2PApplicationSubmission**](A2PApplicationSubmission.md)|  | 

### Return type

**bool**

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

# **fetch_a2_p_application**
> object fetch_a2_p_application()

Fetch A2P Application

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
    api_instance = wallet.A2PApi(api_client)

    try:
        # Fetch A2P Application
        api_response = api_instance.fetch_a2_p_application()
        print("The response of A2PApi->fetch_a2_p_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling A2PApi->fetch_a2_p_application: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **fetch_a2_p_registration**
> object fetch_a2_p_registration()

Fetch A2P Registration

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
    api_instance = wallet.A2PApi(api_client)

    try:
        # Fetch A2P Registration
        api_response = api_instance.fetch_a2_p_registration()
        print("The response of A2PApi->fetch_a2_p_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling A2PApi->fetch_a2_p_registration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **update_a2_p_application**
> bool update_a2_p_application(application_id, wta2_p_application_update_params)

Update A2P Application

### Example


```python
import wallet
from wallet.models.wta2_p_application_update_params import WTA2PApplicationUpdateParams
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
    api_instance = wallet.A2PApi(api_client)
    application_id = 'application_id_example' # str | 
    wta2_p_application_update_params = wallet.WTA2PApplicationUpdateParams() # WTA2PApplicationUpdateParams | 

    try:
        # Update A2P Application
        api_response = api_instance.update_a2_p_application(application_id, wta2_p_application_update_params)
        print("The response of A2PApi->update_a2_p_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling A2PApi->update_a2_p_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **wta2_p_application_update_params** | [**WTA2PApplicationUpdateParams**](WTA2PApplicationUpdateParams.md)|  | 

### Return type

**bool**

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

