# wallet.OpenAIApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_assistant**](OpenAIApi.md#archive_assistant) | **DELETE** /v2/interop/openai/assistant/{id} | Archive Assistant
[**archive_thread**](OpenAIApi.md#archive_thread) | **DELETE** /v2/interop/openai/thread/{id} | Archive Thread
[**archive_vector_store**](OpenAIApi.md#archive_vector_store) | **DELETE** /v2/interop/openai/vectorStore/{id} | Archive VectorStore
[**create_assistant**](OpenAIApi.md#create_assistant) | **POST** /v2/interop/openai/assistant | Create Assistant
[**create_run_on_thread**](OpenAIApi.md#create_run_on_thread) | **POST** /v2/interop/openai/thread/{id}/run/create | Create Run on Thread
[**create_thread**](OpenAIApi.md#create_thread) | **POST** /v2/interop/openai/thread | Create Thread
[**create_thread_message**](OpenAIApi.md#create_thread_message) | **POST** /v2/interop/openai/thread/{id}/message/create | Add Message to Thread
[**create_vector_store**](OpenAIApi.md#create_vector_store) | **POST** /v2/interop/openai/vectorStore | Create VectorStore
[**fetch_all_assistants**](OpenAIApi.md#fetch_all_assistants) | **GET** /v2/interop/openai/assistant/all | Get all Assistants
[**fetch_all_threads**](OpenAIApi.md#fetch_all_threads) | **GET** /v2/interop/openai/thread/all | Get all Threads
[**fetch_all_vector_stores**](OpenAIApi.md#fetch_all_vector_stores) | **GET** /v2/interop/openai/vectorStore/all | Get all VectorStores
[**fetch_assistant**](OpenAIApi.md#fetch_assistant) | **GET** /v2/interop/openai/assistant/{id} | Get Assistant
[**fetch_thread_messages**](OpenAIApi.md#fetch_thread_messages) | **GET** /v2/interop/openai/thread/{id}/messages | Get Thread&#39;s Messages
[**restore_assistant**](OpenAIApi.md#restore_assistant) | **PATCH** /v2/interop/openai/assistant/{id} | Restore Assistant
[**restore_thread**](OpenAIApi.md#restore_thread) | **PATCH** /v2/interop/openai/thread/{id} | Restore Thread
[**restore_vector_store**](OpenAIApi.md#restore_vector_store) | **PATCH** /v2/interop/openai/vectorStore/{id} | Restore VectorStore
[**update_assistant**](OpenAIApi.md#update_assistant) | **PUT** /v2/interop/openai/assistant/{id} | Update Assistant
[**update_thread**](OpenAIApi.md#update_thread) | **PUT** /v2/interop/openai/thread/{id} | Update Thread
[**update_vector_store**](OpenAIApi.md#update_vector_store) | **PUT** /v2/interop/openai/vectorStore/{id} | Update VectorStore


# **archive_assistant**
> Assistant archive_assistant(id)

Archive Assistant

### Example


```python
import wallet
from wallet.models.assistant import Assistant
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
    api_instance = wallet.OpenAIApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive Assistant
        api_response = api_instance.archive_assistant(id)
        print("The response of OpenAIApi->archive_assistant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->archive_assistant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Assistant**](Assistant.md)

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

# **archive_thread**
> Thread archive_thread(id)

Archive Thread

### Example


```python
import wallet
from wallet.models.thread import Thread
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
    api_instance = wallet.OpenAIApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive Thread
        api_response = api_instance.archive_thread(id)
        print("The response of OpenAIApi->archive_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->archive_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Thread**](Thread.md)

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

# **archive_vector_store**
> VectorStore archive_vector_store(id)

Archive VectorStore

### Example


```python
import wallet
from wallet.models.vector_store import VectorStore
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
    api_instance = wallet.OpenAIApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive VectorStore
        api_response = api_instance.archive_vector_store(id)
        print("The response of OpenAIApi->archive_vector_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->archive_vector_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VectorStore**](VectorStore.md)

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

# **create_assistant**
> Assistant create_assistant(oai_assistant_update_params_create_params)

Create Assistant

### Example


```python
import wallet
from wallet.models.assistant import Assistant
from wallet.models.oai_assistant_update_params_create_params import OAIAssistantUpdateParamsCreateParams
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
    api_instance = wallet.OpenAIApi(api_client)
    oai_assistant_update_params_create_params = wallet.OAIAssistantUpdateParamsCreateParams() # OAIAssistantUpdateParamsCreateParams | 

    try:
        # Create Assistant
        api_response = api_instance.create_assistant(oai_assistant_update_params_create_params)
        print("The response of OpenAIApi->create_assistant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->create_assistant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oai_assistant_update_params_create_params** | [**OAIAssistantUpdateParamsCreateParams**](OAIAssistantUpdateParamsCreateParams.md)|  | 

### Return type

[**Assistant**](Assistant.md)

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

# **create_run_on_thread**
> create_run_on_thread(id, create_run_on_thread_request)

Create Run on Thread

### Example


```python
import wallet
from wallet.models.create_run_on_thread_request import CreateRunOnThreadRequest
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
    api_instance = wallet.OpenAIApi(api_client)
    id = 'id_example' # str | 
    create_run_on_thread_request = wallet.CreateRunOnThreadRequest() # CreateRunOnThreadRequest | 

    try:
        # Create Run on Thread
        api_instance.create_run_on_thread(id, create_run_on_thread_request)
    except Exception as e:
        print("Exception when calling OpenAIApi->create_run_on_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_run_on_thread_request** | [**CreateRunOnThreadRequest**](CreateRunOnThreadRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thread**
> Thread create_thread(request_body)

Create Thread

### Example


```python
import wallet
from wallet.models.thread import Thread
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
    api_instance = wallet.OpenAIApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Create Thread
        api_response = api_instance.create_thread(request_body)
        print("The response of OpenAIApi->create_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->create_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**Thread**](Thread.md)

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

# **create_thread_message**
> create_thread_message(id, create_run_on_thread_request)

Add Message to Thread

### Example


```python
import wallet
from wallet.models.create_run_on_thread_request import CreateRunOnThreadRequest
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
    api_instance = wallet.OpenAIApi(api_client)
    id = 'id_example' # str | 
    create_run_on_thread_request = wallet.CreateRunOnThreadRequest() # CreateRunOnThreadRequest | 

    try:
        # Add Message to Thread
        api_instance.create_thread_message(id, create_run_on_thread_request)
    except Exception as e:
        print("Exception when calling OpenAIApi->create_thread_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_run_on_thread_request** | [**CreateRunOnThreadRequest**](CreateRunOnThreadRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vector_store**
> VectorStore create_vector_store(request_body)

Create VectorStore

### Example


```python
import wallet
from wallet.models.vector_store import VectorStore
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
    api_instance = wallet.OpenAIApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Create VectorStore
        api_response = api_instance.create_vector_store(request_body)
        print("The response of OpenAIApi->create_vector_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->create_vector_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**VectorStore**](VectorStore.md)

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

# **fetch_all_assistants**
> object fetch_all_assistants(is_archive_included=is_archive_included)

Get all Assistants

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
    api_instance = wallet.OpenAIApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all Assistants
        api_response = api_instance.fetch_all_assistants(is_archive_included=is_archive_included)
        print("The response of OpenAIApi->fetch_all_assistants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->fetch_all_assistants: %s\n" % e)
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

# **fetch_all_threads**
> object fetch_all_threads(is_archive_included=is_archive_included)

Get all Threads

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
    api_instance = wallet.OpenAIApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all Threads
        api_response = api_instance.fetch_all_threads(is_archive_included=is_archive_included)
        print("The response of OpenAIApi->fetch_all_threads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->fetch_all_threads: %s\n" % e)
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

# **fetch_all_vector_stores**
> object fetch_all_vector_stores(is_archive_included=is_archive_included)

Get all VectorStores

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
    api_instance = wallet.OpenAIApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all VectorStores
        api_response = api_instance.fetch_all_vector_stores(is_archive_included=is_archive_included)
        print("The response of OpenAIApi->fetch_all_vector_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->fetch_all_vector_stores: %s\n" % e)
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

# **fetch_assistant**
> Assistant fetch_assistant(id)

Get Assistant

### Example


```python
import wallet
from wallet.models.assistant import Assistant
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
    api_instance = wallet.OpenAIApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Assistant
        api_response = api_instance.fetch_assistant(id)
        print("The response of OpenAIApi->fetch_assistant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->fetch_assistant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Assistant**](Assistant.md)

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

# **fetch_thread_messages**
> List[Message] fetch_thread_messages(id)

Get Thread's Messages

### Example


```python
import wallet
from wallet.models.message import Message
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
    api_instance = wallet.OpenAIApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Thread's Messages
        api_response = api_instance.fetch_thread_messages(id)
        print("The response of OpenAIApi->fetch_thread_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->fetch_thread_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[Message]**](Message.md)

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

# **restore_assistant**
> Assistant restore_assistant(id)

Restore Assistant

### Example


```python
import wallet
from wallet.models.assistant import Assistant
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
    api_instance = wallet.OpenAIApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore Assistant
        api_response = api_instance.restore_assistant(id)
        print("The response of OpenAIApi->restore_assistant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->restore_assistant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Assistant**](Assistant.md)

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

# **restore_thread**
> Thread restore_thread(id)

Restore Thread

### Example


```python
import wallet
from wallet.models.thread import Thread
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
    api_instance = wallet.OpenAIApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore Thread
        api_response = api_instance.restore_thread(id)
        print("The response of OpenAIApi->restore_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->restore_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Thread**](Thread.md)

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

# **restore_vector_store**
> VectorStore restore_vector_store(id)

Restore VectorStore

### Example


```python
import wallet
from wallet.models.vector_store import VectorStore
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
    api_instance = wallet.OpenAIApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore VectorStore
        api_response = api_instance.restore_vector_store(id)
        print("The response of OpenAIApi->restore_vector_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->restore_vector_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VectorStore**](VectorStore.md)

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

# **update_assistant**
> Assistant update_assistant(id, oai_assistant_update_params)

Update Assistant

### Example


```python
import wallet
from wallet.models.assistant import Assistant
from wallet.models.oai_assistant_update_params import OAIAssistantUpdateParams
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
    api_instance = wallet.OpenAIApi(api_client)
    id = 'id_example' # str | 
    oai_assistant_update_params = wallet.OAIAssistantUpdateParams() # OAIAssistantUpdateParams | 

    try:
        # Update Assistant
        api_response = api_instance.update_assistant(id, oai_assistant_update_params)
        print("The response of OpenAIApi->update_assistant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->update_assistant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **oai_assistant_update_params** | [**OAIAssistantUpdateParams**](OAIAssistantUpdateParams.md)|  | 

### Return type

[**Assistant**](Assistant.md)

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

# **update_thread**
> Thread update_thread(id, request_body)

Update Thread

### Example


```python
import wallet
from wallet.models.thread import Thread
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
    api_instance = wallet.OpenAIApi(api_client)
    id = 'id_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Update Thread
        api_response = api_instance.update_thread(id, request_body)
        print("The response of OpenAIApi->update_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->update_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**Thread**](Thread.md)

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

# **update_vector_store**
> VectorStore update_vector_store(id, request_body)

Update VectorStore

### Example


```python
import wallet
from wallet.models.vector_store import VectorStore
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
    api_instance = wallet.OpenAIApi(api_client)
    id = 'id_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Update VectorStore
        api_response = api_instance.update_vector_store(id, request_body)
        print("The response of OpenAIApi->update_vector_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->update_vector_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**VectorStore**](VectorStore.md)

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

