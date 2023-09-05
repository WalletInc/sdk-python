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
import time
import wallet
from wallet.api import ticket_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.ticket import Ticket
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
    api_instance = ticket_api.TicketApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive ticket
        api_response = api_instance.archive_ticket(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling TicketApi->archive_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import ticket_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_ticket_create_params import WTTicketCreateParams
from wallet.model.ticket import Ticket
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
    api_instance = ticket_api.TicketApi(api_client)
    wt_ticket_create_params = WTTicketCreateParams(
        recipient_phone_number="recipient_phone_number_example",
        recipient_email_address="recipient_email_address_example",
        recipient_member_id="recipient_member_id_example",
        is_comp=True,
        quantity=1,
        performance_id="performance_id_example",
    ) # WTTicketCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create ticket
        api_response = api_instance.create_ticket(wt_ticket_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import ticket_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.foreign_key_does_not_exist import ForeignKeyDoesNotExist
from wallet.model.wt_ticket import WTTicket
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
    api_instance = ticket_api.TicketApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch ticket
        api_response = api_instance.fetch_ticket(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling TicketApi->fetch_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import ticket_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.ticket import Ticket
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
    api_instance = ticket_api.TicketApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore ticket
        api_response = api_instance.restore_ticket(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling TicketApi->restore_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import ticket_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_ticket_update_params import WTTicketUpdateParams
from wallet.model.ticket import Ticket
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
    api_instance = ticket_api.TicketApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_ticket_update_params = WTTicketUpdateParams(
        recipient_phone_number="recipient_phone_number_example",
        recipient_email_address="recipient_email_address_example",
        recipient_member_id="recipient_member_id_example",
        is_comp=True,
        quantity=1,
    ) # WTTicketUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update ticket
        api_response = api_instance.update_ticket(id, wt_ticket_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling TicketApi->update_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

