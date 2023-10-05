# wallet.PerformancesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_performance**](PerformancesApi.md#archive_performance) | **DELETE** /v2/performances/{id} | Archive performance
[**count_claimed_comps**](PerformancesApi.md#count_claimed_comps) | **GET** /v2/performances/{id}/claimed/count | Count number claimed
[**count_redeemed_comps**](PerformancesApi.md#count_redeemed_comps) | **GET** /v2/performances/{id}/redeemed/count | Count number redeemed
[**create_performance**](PerformancesApi.md#create_performance) | **POST** /v2/performances | Create performance
[**fetch_all_performance_tickets**](PerformancesApi.md#fetch_all_performance_tickets) | **GET** /v2/performances/tickets/all/{id} | Fetch all tickets
[**fetch_all_performances**](PerformancesApi.md#fetch_all_performances) | **GET** /v2/performances/all | Fetch all performances
[**fetch_performance**](PerformancesApi.md#fetch_performance) | **GET** /v2/performances/{id} | Fetch a single performance
[**fetch_performance_tickets_page**](PerformancesApi.md#fetch_performance_tickets_page) | **GET** /v2/performances/tickets/page/{performanceID} | Fetch tickets by page
[**import_tickets**](PerformancesApi.md#import_tickets) | **POST** /v2/performances/{id}/tickets/import | Update performance
[**restore_performance**](PerformancesApi.md#restore_performance) | **PATCH** /v2/performances/{id} | Restore performance
[**save_ticket_settings**](PerformancesApi.md#save_ticket_settings) | **POST** /v2/performances/{id} | Update performance
[**update_performance**](PerformancesApi.md#update_performance) | **PUT** /v2/performances/{id} | Update performance


# **archive_performance**
> Performance archive_performance(id)

Archive performance

### Example


```python
import time
import wallet
from wallet.api import performances_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.performance import Performance
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
    api_instance = performances_api.PerformancesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive performance
        api_response = api_instance.archive_performance(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->archive_performance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Performance**](Performance.md)

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

# **count_claimed_comps**
> InlineResponse2003 count_claimed_comps(id)

Count number claimed

### Example


```python
import time
import wallet
from wallet.api import performances_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.inline_response2003 import InlineResponse2003
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = performances_api.PerformancesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Count number claimed
        api_response = api_instance.count_claimed_comps(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->count_claimed_comps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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

# **count_redeemed_comps**
> InlineResponse2003 count_redeemed_comps(id)

Count number redeemed

### Example


```python
import time
import wallet
from wallet.api import performances_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.inline_response2003 import InlineResponse2003
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = performances_api.PerformancesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Count number redeemed
        api_response = api_instance.count_redeemed_comps(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->count_redeemed_comps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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

# **create_performance**
> Performance create_performance(wt_performance_create_params)

Create performance

### Example


```python
import time
import wallet
from wallet.api import performances_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.performance import Performance
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_performance_create_params import WTPerformanceCreateParams
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = performances_api.PerformancesApi(api_client)
    wt_performance_create_params = WTPerformanceCreateParams(
        title="This is the title of the performance",
        body="This is the description of the performance",
        start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        price="43.29",
        url="https://example.com/performance.html",
        order_number=5,
        is_sold_out=True,
        media_url="https://wall.et/media/H847Sjudbw.png",
        payment_design_id=NanoID("C"),
        max_comp_tickets=3.14,
        ticket_expiration_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        redemption_instructions="redemption_instructions_example",
    ) # WTPerformanceCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create performance
        api_response = api_instance.create_performance(wt_performance_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->create_performance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_performance_create_params** | [**WTPerformanceCreateParams**](WTPerformanceCreateParams.md)|  |

### Return type

[**Performance**](Performance.md)

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

# **fetch_all_performance_tickets**
> [Ticket] fetch_all_performance_tickets(id)

Fetch all tickets

### Example


```python
import time
import wallet
from wallet.api import performances_api
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
    api_instance = performances_api.PerformancesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch all tickets
        api_response = api_instance.fetch_all_performance_tickets(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->fetch_all_performance_tickets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all tickets
        api_response = api_instance.fetch_all_performance_tickets(id, is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->fetch_all_performance_tickets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**[Ticket]**](Ticket.md)

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

# **fetch_all_performances**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_performances()

Fetch all performances

### Example


```python
import time
import wallet
from wallet.api import performances_api
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
    api_instance = performances_api.PerformancesApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all performances
        api_response = api_instance.fetch_all_performances(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->fetch_all_performances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **fetch_performance**
> Performance fetch_performance(id)

Fetch a single performance

### Example


```python
import time
import wallet
from wallet.api import performances_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.performance import Performance
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
    api_instance = performances_api.PerformancesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch a single performance
        api_response = api_instance.fetch_performance(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->fetch_performance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Performance**](Performance.md)

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

# **fetch_performance_tickets_page**
> InlineResponse2004 fetch_performance_tickets_page(performance_id, page_num, page_size)

Fetch tickets by page

### Example


```python
import time
import wallet
from wallet.api import performances_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.inline_response2004 import InlineResponse2004
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
    api_instance = performances_api.PerformancesApi(api_client)
    performance_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    page_num = 3.14 # float | 
    page_size = 3.14 # float | 
    filter_comps = True # bool |  (optional)
    filter_claimed = True # bool |  (optional)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch tickets by page
        api_response = api_instance.fetch_performance_tickets_page(performance_id, page_num, page_size)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->fetch_performance_tickets_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch tickets by page
        api_response = api_instance.fetch_performance_tickets_page(performance_id, page_num, page_size, filter_comps=filter_comps, filter_claimed=filter_claimed, is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->fetch_performance_tickets_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performance_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **page_num** | **float**|  |
 **page_size** | **float**|  |
 **filter_comps** | **bool**|  | [optional]
 **filter_claimed** | **bool**|  | [optional]
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **import_tickets**
> str import_tickets(id, inline_object2)

Update performance

### Example


```python
import time
import wallet
from wallet.api import performances_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.inline_object2 import InlineObject2
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = performances_api.PerformancesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    inline_object2 = InlineObject2(
        tickets=[
            WTTicketUpdateParams(
                recipient_phone_number="recipient_phone_number_example",
                recipient_email_address="recipient_email_address_example",
                recipient_member_id="recipient_member_id_example",
                is_comp=True,
                quantity=1,
            ),
        ],
    ) # InlineObject2 | 

    # example passing only required values which don't have defaults set
    try:
        # Update performance
        api_response = api_instance.import_tickets(id, inline_object2)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->import_tickets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  |

### Return type

**str**

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

# **restore_performance**
> Performance restore_performance(id)

Restore performance

### Example


```python
import time
import wallet
from wallet.api import performances_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.performance import Performance
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
    api_instance = performances_api.PerformancesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore performance
        api_response = api_instance.restore_performance(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->restore_performance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Performance**](Performance.md)

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

# **save_ticket_settings**
> Performance save_ticket_settings(id, inline_object1)

Update performance

### Example


```python
import time
import wallet
from wallet.api import performances_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.performance import Performance
from wallet.model.falsum_error import FalsumError
from wallet.model.inline_object1 import InlineObject1
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
    api_instance = performances_api.PerformancesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    inline_object1 = InlineObject1(
        redemption_instructions="redemption_instructions_example",
        ticket_expiration_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        max_comp_tickets=3.14,
        payment_design_id=None,
    ) # InlineObject1 | 

    # example passing only required values which don't have defaults set
    try:
        # Update performance
        api_response = api_instance.save_ticket_settings(id, inline_object1)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->save_ticket_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  |

### Return type

[**Performance**](Performance.md)

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

# **update_performance**
> Performance update_performance(id, wt_performance_update_params)

Update performance

### Example


```python
import time
import wallet
from wallet.api import performances_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.performance import Performance
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_performance_update_params import WTPerformanceUpdateParams
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = performances_api.PerformancesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_performance_update_params = WTPerformanceUpdateParams(
        title="This is the title of the performance",
        body="This is the description of the performance",
        start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        price="43.29",
        url="https://example.com/performance.html",
        order_number=5,
        is_sold_out=True,
        media_url="https://wall.et/media/H847Sjudbw.png",
        payment_design_id=NanoID("C"),
        max_comp_tickets=3.14,
        ticket_expiration_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        redemption_instructions="redemption_instructions_example",
    ) # WTPerformanceUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update performance
        api_response = api_instance.update_performance(id, wt_performance_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PerformancesApi->update_performance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **wt_performance_update_params** | [**WTPerformanceUpdateParams**](WTPerformanceUpdateParams.md)|  |

### Return type

[**Performance**](Performance.md)

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

