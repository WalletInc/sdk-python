# wallet.QuickLinksApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_link_book**](QuickLinksApi.md#archive_link_book) | **DELETE** /v2/linkBook/{id} | Archive link
[**create_link_book**](QuickLinksApi.md#create_link_book) | **POST** /v2/linkBook | Create link
[**fetch_all_link_book**](QuickLinksApi.md#fetch_all_link_book) | **GET** /v2/linkBook/all | Fetch all links
[**fetch_link_book_by_id**](QuickLinksApi.md#fetch_link_book_by_id) | **GET** /v2/linkBook/{id} | Fetch link book by id
[**restore_link_book**](QuickLinksApi.md#restore_link_book) | **PATCH** /v2/linkBook/{id} | Restore link
[**update_link_book**](QuickLinksApi.md#update_link_book) | **PUT** /v2/linkBook/{id} | Update link


# **archive_link_book**
> LinkBook archive_link_book(id)

Archive link

### Example


```python
import wallet
from wallet.models.link_book import LinkBook
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
    api_instance = wallet.QuickLinksApi(api_client)
    id = None # object | 

    try:
        # Archive link
        api_response = api_instance.archive_link_book(id)
        print("The response of QuickLinksApi->archive_link_book:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksApi->archive_link_book: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
import wallet
from wallet.models.link_book import LinkBook
from wallet.models.wt_link_book_create_params import WTLinkBookCreateParams
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
    api_instance = wallet.QuickLinksApi(api_client)
    wt_link_book_create_params = wallet.WTLinkBookCreateParams() # WTLinkBookCreateParams | 

    try:
        # Create link
        api_response = api_instance.create_link_book(wt_link_book_create_params)
        print("The response of QuickLinksApi->create_link_book:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksApi->create_link_book: %s\n" % e)
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
> object fetch_all_link_book(is_archive_included=is_archive_included)

Fetch all links

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
    api_instance = wallet.QuickLinksApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all links
        api_response = api_instance.fetch_all_link_book(is_archive_included=is_archive_included)
        print("The response of QuickLinksApi->fetch_all_link_book:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksApi->fetch_all_link_book: %s\n" % e)
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

# **fetch_link_book_by_id**
> WTLinkBook fetch_link_book_by_id(id)

Fetch link book by id

### Example


```python
import wallet
from wallet.models.wt_link_book import WTLinkBook
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
    api_instance = wallet.QuickLinksApi(api_client)
    id = None # object | 

    try:
        # Fetch link book by id
        api_response = api_instance.fetch_link_book_by_id(id)
        print("The response of QuickLinksApi->fetch_link_book_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksApi->fetch_link_book_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
import wallet
from wallet.models.link_book import LinkBook
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
    api_instance = wallet.QuickLinksApi(api_client)
    id = None # object | 

    try:
        # Restore link
        api_response = api_instance.restore_link_book(id)
        print("The response of QuickLinksApi->restore_link_book:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksApi->restore_link_book: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
import wallet
from wallet.models.link_book import LinkBook
from wallet.models.wt_link_book_update_params import WTLinkBookUpdateParams
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
    api_instance = wallet.QuickLinksApi(api_client)
    id = None # object | 
    wt_link_book_update_params = wallet.WTLinkBookUpdateParams() # WTLinkBookUpdateParams | 

    try:
        # Update link
        api_response = api_instance.update_link_book(id, wt_link_book_update_params)
        print("The response of QuickLinksApi->update_link_book:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksApi->update_link_book: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
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

