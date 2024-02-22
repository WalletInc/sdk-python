# wallet.PerformancesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_performance**](PerformancesApi.md#archive_performance) | **DELETE** /v2/performances/{id} | Archive performance
[**count_claimed_comps**](PerformancesApi.md#count_claimed_comps) | **GET** /v2/performances/{id}/claimed/count | Count number claimed
[**count_redeemed_comps**](PerformancesApi.md#count_redeemed_comps) | **GET** /v2/performances/{id}/redeemed/count | Count number redeemed
[**create_performance**](PerformancesApi.md#create_performance) | **POST** /v2/performances | Create performance
[**export_tickets**](PerformancesApi.md#export_tickets) | **POST** /v2/performances/{id}/tickets/export | Update performance
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
import wallet
from wallet.models.performance import Performance
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
    api_instance = wallet.PerformancesApi(api_client)
    id = None # object | 

    try:
        # Archive performance
        api_response = api_instance.archive_performance(id)
        print("The response of PerformancesApi->archive_performance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformancesApi->archive_performance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
> CountClaimedComps200Response count_claimed_comps(id)

Count number claimed

### Example


```python
import wallet
from wallet.models.count_claimed_comps200_response import CountClaimedComps200Response
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
    api_instance = wallet.PerformancesApi(api_client)
    id = None # object | 

    try:
        # Count number claimed
        api_response = api_instance.count_claimed_comps(id)
        print("The response of PerformancesApi->count_claimed_comps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformancesApi->count_claimed_comps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**CountClaimedComps200Response**](CountClaimedComps200Response.md)

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
> CountClaimedComps200Response count_redeemed_comps(id)

Count number redeemed

### Example


```python
import wallet
from wallet.models.count_claimed_comps200_response import CountClaimedComps200Response
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
    api_instance = wallet.PerformancesApi(api_client)
    id = None # object | 

    try:
        # Count number redeemed
        api_response = api_instance.count_redeemed_comps(id)
        print("The response of PerformancesApi->count_redeemed_comps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformancesApi->count_redeemed_comps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**CountClaimedComps200Response**](CountClaimedComps200Response.md)

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
import wallet
from wallet.models.performance import Performance
from wallet.models.wt_performance_create_params import WTPerformanceCreateParams
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
    api_instance = wallet.PerformancesApi(api_client)
    wt_performance_create_params = wallet.WTPerformanceCreateParams() # WTPerformanceCreateParams | 

    try:
        # Create performance
        api_response = api_instance.create_performance(wt_performance_create_params)
        print("The response of PerformancesApi->create_performance:\n")
        pprint(api_response)
    except Exception as e:
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

# **export_tickets**
> List[Ticket] export_tickets(id)

Update performance

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
    api_instance = wallet.PerformancesApi(api_client)
    id = None # object | 

    try:
        # Update performance
        api_response = api_instance.export_tickets(id)
        print("The response of PerformancesApi->export_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformancesApi->export_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**List[Ticket]**](Ticket.md)

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

# **fetch_all_performance_tickets**
> List[Ticket] fetch_all_performance_tickets(id, is_archive_included=is_archive_included)

Fetch all tickets

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
    api_instance = wallet.PerformancesApi(api_client)
    id = None # object | 
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all tickets
        api_response = api_instance.fetch_all_performance_tickets(id, is_archive_included=is_archive_included)
        print("The response of PerformancesApi->fetch_all_performance_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformancesApi->fetch_all_performance_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[Ticket]**](Ticket.md)

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
> object fetch_all_performances(is_archive_included=is_archive_included)

Fetch all performances

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
    api_instance = wallet.PerformancesApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all performances
        api_response = api_instance.fetch_all_performances(is_archive_included=is_archive_included)
        print("The response of PerformancesApi->fetch_all_performances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformancesApi->fetch_all_performances: %s\n" % e)
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

# **fetch_performance**
> Performance fetch_performance(id)

Fetch a single performance

### Example


```python
import wallet
from wallet.models.performance import Performance
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
    api_instance = wallet.PerformancesApi(api_client)
    id = None # object | 

    try:
        # Fetch a single performance
        api_response = api_instance.fetch_performance(id)
        print("The response of PerformancesApi->fetch_performance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformancesApi->fetch_performance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
> FetchPerformanceTicketsPage200Response fetch_performance_tickets_page(performance_id, page_num, page_size, filter_comps=filter_comps, filter_claimed=filter_claimed, sort_by=sort_by, sort_direction=sort_direction, is_archive_included=is_archive_included)

Fetch tickets by page

### Example


```python
import wallet
from wallet.models.fetch_performance_tickets_page200_response import FetchPerformanceTicketsPage200Response
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
    api_instance = wallet.PerformancesApi(api_client)
    performance_id = None # object | 
    page_num = 3.4 # float | 
    page_size = 3.4 # float | 
    filter_comps = True # bool |  (optional)
    filter_claimed = True # bool |  (optional)
    sort_by = None # object |  (optional)
    sort_direction = None # object |  (optional)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch tickets by page
        api_response = api_instance.fetch_performance_tickets_page(performance_id, page_num, page_size, filter_comps=filter_comps, filter_claimed=filter_claimed, sort_by=sort_by, sort_direction=sort_direction, is_archive_included=is_archive_included)
        print("The response of PerformancesApi->fetch_performance_tickets_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformancesApi->fetch_performance_tickets_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performance_id** | [**object**](.md)|  | 
 **page_num** | **float**|  | 
 **page_size** | **float**|  | 
 **filter_comps** | **bool**|  | [optional] 
 **filter_claimed** | **bool**|  | [optional] 
 **sort_by** | [**object**](.md)|  | [optional] 
 **sort_direction** | [**object**](.md)|  | [optional] 
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**FetchPerformanceTicketsPage200Response**](FetchPerformanceTicketsPage200Response.md)

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
> str import_tickets(id, import_tickets_request)

Update performance

### Example


```python
import wallet
from wallet.models.import_tickets_request import ImportTicketsRequest
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
    api_instance = wallet.PerformancesApi(api_client)
    id = None # object | 
    import_tickets_request = wallet.ImportTicketsRequest() # ImportTicketsRequest | 

    try:
        # Update performance
        api_response = api_instance.import_tickets(id, import_tickets_request)
        print("The response of PerformancesApi->import_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformancesApi->import_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **import_tickets_request** | [**ImportTicketsRequest**](ImportTicketsRequest.md)|  | 

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
import wallet
from wallet.models.performance import Performance
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
    api_instance = wallet.PerformancesApi(api_client)
    id = None # object | 

    try:
        # Restore performance
        api_response = api_instance.restore_performance(id)
        print("The response of PerformancesApi->restore_performance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformancesApi->restore_performance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
> Performance save_ticket_settings(id, save_ticket_settings_request)

Update performance

### Example


```python
import wallet
from wallet.models.performance import Performance
from wallet.models.save_ticket_settings_request import SaveTicketSettingsRequest
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
    api_instance = wallet.PerformancesApi(api_client)
    id = None # object | 
    save_ticket_settings_request = wallet.SaveTicketSettingsRequest() # SaveTicketSettingsRequest | 

    try:
        # Update performance
        api_response = api_instance.save_ticket_settings(id, save_ticket_settings_request)
        print("The response of PerformancesApi->save_ticket_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformancesApi->save_ticket_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **save_ticket_settings_request** | [**SaveTicketSettingsRequest**](SaveTicketSettingsRequest.md)|  | 

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
import wallet
from wallet.models.performance import Performance
from wallet.models.wt_performance_update_params import WTPerformanceUpdateParams
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
    api_instance = wallet.PerformancesApi(api_client)
    id = None # object | 
    wt_performance_update_params = wallet.WTPerformanceUpdateParams() # WTPerformanceUpdateParams | 

    try:
        # Update performance
        api_response = api_instance.update_performance(id, wt_performance_update_params)
        print("The response of PerformancesApi->update_performance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformancesApi->update_performance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
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

