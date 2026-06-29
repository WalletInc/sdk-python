# wallet.QuickLinksApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_link_book**](QuickLinksApi.md#archive_link_book) | **DELETE** /v2/linkBook/{id} | Archive Quick Link
[**create_link_book**](QuickLinksApi.md#create_link_book) | **POST** /v2/linkBook | Create Quick Link
[**fetch_all_link_book**](QuickLinksApi.md#fetch_all_link_book) | **GET** /v2/linkBook/all | Get all Quick Links
[**fetch_link_book_by_id**](QuickLinksApi.md#fetch_link_book_by_id) | **GET** /v2/linkBook/{id} | Get Quick Link
[**restore_link_book**](QuickLinksApi.md#restore_link_book) | **PATCH** /v2/linkBook/{id} | Restore Quick Link
[**update_link_book**](QuickLinksApi.md#update_link_book) | **PUT** /v2/linkBook/{id} | Update Quick Link


# **archive_link_book**
> LinkBook archive_link_book(id)

Archive Quick Link

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
    id = 'id_example' # str | 

    try:
        # Archive Quick Link
        api_response = api_instance.archive_link_book(id)
        print("The response of QuickLinksApi->archive_link_book:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksApi->archive_link_book: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
> LinkBook create_link_book(wt_quick_link_create_params)

Create Quick Link

### Example


```python
import wallet
from wallet.models.link_book import LinkBook
from wallet.models.wt_quick_link_create_params import WTQuickLinkCreateParams
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
    wt_quick_link_create_params = wallet.WTQuickLinkCreateParams() # WTQuickLinkCreateParams | 

    try:
        # Create Quick Link
        api_response = api_instance.create_link_book(wt_quick_link_create_params)
        print("The response of QuickLinksApi->create_link_book:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksApi->create_link_book: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_quick_link_create_params** | [**WTQuickLinkCreateParams**](WTQuickLinkCreateParams.md)|  | 

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

Get all Quick Links

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
        # Get all Quick Links
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
> WTQuickLink fetch_link_book_by_id(id)

Get Quick Link

### Example


```python
import wallet
from wallet.models.wt_quick_link import WTQuickLink
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
    id = 'id_example' # str | 

    try:
        # Get Quick Link
        api_response = api_instance.fetch_link_book_by_id(id)
        print("The response of QuickLinksApi->fetch_link_book_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksApi->fetch_link_book_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTQuickLink**](WTQuickLink.md)

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

Restore Quick Link

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
    id = 'id_example' # str | 

    try:
        # Restore Quick Link
        api_response = api_instance.restore_link_book(id)
        print("The response of QuickLinksApi->restore_link_book:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksApi->restore_link_book: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
> LinkBook update_link_book(id, wt_quick_link_update_params)

Update Quick Link

### Example


```python
import wallet
from wallet.models.link_book import LinkBook
from wallet.models.wt_quick_link_update_params import WTQuickLinkUpdateParams
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
    id = 'id_example' # str | 
    wt_quick_link_update_params = wallet.WTQuickLinkUpdateParams() # WTQuickLinkUpdateParams | 

    try:
        # Update Quick Link
        api_response = api_instance.update_link_book(id, wt_quick_link_update_params)
        print("The response of QuickLinksApi->update_link_book:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksApi->update_link_book: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wt_quick_link_update_params** | [**WTQuickLinkUpdateParams**](WTQuickLinkUpdateParams.md)|  | 

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

