# wallet.LinkBookApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_link_book**](LinkBookApi.md#archive_link_book) | **DELETE** /v2/linkBook/{id} | Archive link
[**create_link_book**](LinkBookApi.md#create_link_book) | **POST** /v2/linkBook | Create link
[**fetch_all_link_book**](LinkBookApi.md#fetch_all_link_book) | **GET** /v2/linkBook/all | Fetch all links
[**fetch_link_book_by_id**](LinkBookApi.md#fetch_link_book_by_id) | **GET** /v2/linkBook/{id} | Fetch link book by id
[**restore_link_book**](LinkBookApi.md#restore_link_book) | **PATCH** /v2/linkBook/{id} | Restore link
[**update_link_book**](LinkBookApi.md#update_link_book) | **PUT** /v2/linkBook/{id} | Update link


# **archive_link_book**
> LinkBook archive_link_book(id)

Archive link

### Example


```python
import time
import wallet
from wallet.api import link_book_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.link_book import LinkBook
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
    api_instance = link_book_api.LinkBookApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive link
        api_response = api_instance.archive_link_book(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LinkBookApi->archive_link_book: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**LinkBook**](LinkBook.md)

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

# **create_link_book**
> LinkBook create_link_book(wt_link_book_create_params)

Create link

### Example


```python
import time
import wallet
from wallet.api import link_book_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_link_book_create_params import WTLinkBookCreateParams
from wallet.model.link_book import LinkBook
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
    api_instance = link_book_api.LinkBookApi(api_client)
    wt_link_book_create_params = WTLinkBookCreateParams(
        title="This is the title of the link",
        url="https://example.com",
        icon="fa-clock",
        order_number=1,
        link_book_section_id=None,
    ) # WTLinkBookCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create link
        api_response = api_instance.create_link_book(wt_link_book_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LinkBookApi->create_link_book: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_link_book_create_params** | [**WTLinkBookCreateParams**](WTLinkBookCreateParams.md)|  |

### Return type

[**LinkBook**](LinkBook.md)

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

# **fetch_all_link_book**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_link_book()

Fetch all links

### Example


```python
import time
import wallet
from wallet.api import link_book_api
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
    api_instance = link_book_api.LinkBookApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all links
        api_response = api_instance.fetch_all_link_book(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LinkBookApi->fetch_all_link_book: %s\n" % e)
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

# **fetch_link_book_by_id**
> WTLinkBook fetch_link_book_by_id(id)

Fetch link book by id

### Example


```python
import time
import wallet
from wallet.api import link_book_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_link_book import WTLinkBook
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
    api_instance = link_book_api.LinkBookApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch link book by id
        api_response = api_instance.fetch_link_book_by_id(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LinkBookApi->fetch_link_book_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**WTLinkBook**](WTLinkBook.md)

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

# **restore_link_book**
> LinkBook restore_link_book(id)

Restore link

### Example


```python
import time
import wallet
from wallet.api import link_book_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.link_book import LinkBook
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
    api_instance = link_book_api.LinkBookApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore link
        api_response = api_instance.restore_link_book(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LinkBookApi->restore_link_book: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**LinkBook**](LinkBook.md)

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

# **update_link_book**
> LinkBook update_link_book(id, wt_link_book_update_params)

Update link

### Example


```python
import time
import wallet
from wallet.api import link_book_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.link_book import LinkBook
from wallet.model.wt_link_book_update_params import WTLinkBookUpdateParams
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
    api_instance = link_book_api.LinkBookApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_link_book_update_params = WTLinkBookUpdateParams(
        title="This is the title of the link",
        url="https://example.com",
        icon="fa-clock",
        order_number=1,
        link_book_section_id=None,
    ) # WTLinkBookUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update link
        api_response = api_instance.update_link_book(id, wt_link_book_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LinkBookApi->update_link_book: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **wt_link_book_update_params** | [**WTLinkBookUpdateParams**](WTLinkBookUpdateParams.md)|  |

### Return type

[**LinkBook**](LinkBook.md)

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

