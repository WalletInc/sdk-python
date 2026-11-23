# wallet.TicketsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_ticket**](TicketsApi.md#archive_ticket) | **DELETE** /v2/ticket/{id} | Archive Ticket
[**create_ticket**](TicketsApi.md#create_ticket) | **POST** /v2/ticket | Create Ticket
[**fetch_ticket**](TicketsApi.md#fetch_ticket) | **GET** /v2/ticket/{id} | Get Ticket
[**restore_ticket**](TicketsApi.md#restore_ticket) | **PATCH** /v2/ticket/{id} | Restore Ticket
[**update_ticket**](TicketsApi.md#update_ticket) | **PUT** /v2/ticket/{id} | Update Ticket


# **archive_ticket**
> Ticket archive_ticket(id)

Archive Ticket

### Example

* Api Key Authentication (api_token):

```python
import wallet
from wallet.models.ticket import Ticket
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.TicketsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive Ticket
        api_response = api_instance.archive_ticket(id)
        print("The response of TicketsApi->archive_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketsApi->archive_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[api_token](../README.md#api_token)

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

# **create_ticket**
> Ticket create_ticket(wt_ticket_create_params)

Create Ticket

### Example

* Api Key Authentication (api_token):

```python
import wallet
from wallet.models.ticket import Ticket
from wallet.models.wt_ticket_create_params import WTTicketCreateParams
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.TicketsApi(api_client)
    wt_ticket_create_params = wallet.WTTicketCreateParams() # WTTicketCreateParams | 

    try:
        # Create Ticket
        api_response = api_instance.create_ticket(wt_ticket_create_params)
        print("The response of TicketsApi->create_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketsApi->create_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_ticket_create_params** | [**WTTicketCreateParams**](WTTicketCreateParams.md)|  | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[api_token](../README.md#api_token)

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

# **fetch_ticket**
> WTTicket fetch_ticket(id)

Get Ticket

### Example

* Api Key Authentication (api_token):

```python
import wallet
from wallet.models.wt_ticket import WTTicket
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.TicketsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Ticket
        api_response = api_instance.fetch_ticket(id)
        print("The response of TicketsApi->fetch_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketsApi->fetch_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTTicket**](WTTicket.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**424** | Foreign Key does not exist |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_ticket**
> Ticket restore_ticket(id)

Restore Ticket

### Example

* Api Key Authentication (api_token):

```python
import wallet
from wallet.models.ticket import Ticket
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.TicketsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore Ticket
        api_response = api_instance.restore_ticket(id)
        print("The response of TicketsApi->restore_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketsApi->restore_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[api_token](../README.md#api_token)

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

# **update_ticket**
> Ticket update_ticket(id, wt_ticket_update_params)

Update Ticket

### Example

* Api Key Authentication (api_token):

```python
import wallet
from wallet.models.ticket import Ticket
from wallet.models.wt_ticket_update_params import WTTicketUpdateParams
from wallet.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.TicketsApi(api_client)
    id = 'id_example' # str | 
    wt_ticket_update_params = wallet.WTTicketUpdateParams() # WTTicketUpdateParams | 

    try:
        # Update Ticket
        api_response = api_instance.update_ticket(id, wt_ticket_update_params)
        print("The response of TicketsApi->update_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketsApi->update_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wt_ticket_update_params** | [**WTTicketUpdateParams**](WTTicketUpdateParams.md)|  | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[api_token](../README.md#api_token)

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

