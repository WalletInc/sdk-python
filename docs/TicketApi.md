# wallet.TicketApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_ticket**](TicketApi.md#archive_ticket) | **DELETE** /v2/ticket/{id} | Archive ticket
[**create_ticket**](TicketApi.md#create_ticket) | **POST** /v2/ticket | Create ticket
[**fetch_ticket**](TicketApi.md#fetch_ticket) | **GET** /v2/ticket/{id} | Fetch ticket
[**restore_ticket**](TicketApi.md#restore_ticket) | **PATCH** /v2/ticket/{id} | Restore ticket
[**update_ticket**](TicketApi.md#update_ticket) | **PUT** /v2/ticket/{id} | Update ticket


# **archive_ticket**
> Ticket archive_ticket(id)

Archive ticket

### Example


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


# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.TicketApi(api_client)
    id = None # object | 

    try:
        # Archive ticket
        api_response = api_instance.archive_ticket(id)
        print("The response of TicketApi->archive_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->archive_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**Ticket**](Ticket.md)

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

# **create_ticket**
> Ticket create_ticket(wt_ticket_create_params)

Create ticket

### Example


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


# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.TicketApi(api_client)
    wt_ticket_create_params = wallet.WTTicketCreateParams() # WTTicketCreateParams | 

    try:
        # Create ticket
        api_response = api_instance.create_ticket(wt_ticket_create_params)
        print("The response of TicketApi->create_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->create_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_ticket_create_params** | [**WTTicketCreateParams**](WTTicketCreateParams.md)|  | 

### Return type

[**Ticket**](Ticket.md)

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

# **fetch_ticket**
> WTTicket fetch_ticket(id)

Fetch ticket

### Example


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


# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.TicketApi(api_client)
    id = None # object | 

    try:
        # Fetch ticket
        api_response = api_instance.fetch_ticket(id)
        print("The response of TicketApi->fetch_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->fetch_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**WTTicket**](WTTicket.md)

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
**424** | Foreign Key does not exist |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_ticket**
> Ticket restore_ticket(id)

Restore ticket

### Example


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


# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.TicketApi(api_client)
    id = None # object | 

    try:
        # Restore ticket
        api_response = api_instance.restore_ticket(id)
        print("The response of TicketApi->restore_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->restore_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**Ticket**](Ticket.md)

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

# **update_ticket**
> Ticket update_ticket(id, wt_ticket_update_params)

Update ticket

### Example


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


# Enter a context with an instance of the API client
with wallet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wallet.TicketApi(api_client)
    id = None # object | 
    wt_ticket_update_params = wallet.WTTicketUpdateParams() # WTTicketUpdateParams | 

    try:
        # Update ticket
        api_response = api_instance.update_ticket(id, wt_ticket_update_params)
        print("The response of TicketApi->update_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->update_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **wt_ticket_update_params** | [**WTTicketUpdateParams**](WTTicketUpdateParams.md)|  | 

### Return type

[**Ticket**](Ticket.md)

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

