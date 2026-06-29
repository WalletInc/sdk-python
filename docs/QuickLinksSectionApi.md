# wallet.QuickLinksSectionApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_link_book_section**](QuickLinksSectionApi.md#archive_link_book_section) | **DELETE** /v2/linkBookSection/{id} | Archive quick link section
[**create_link_book_section**](QuickLinksSectionApi.md#create_link_book_section) | **POST** /v2/linkBookSection | Create quick link section
[**fetch_all_link_book_sections**](QuickLinksSectionApi.md#fetch_all_link_book_sections) | **GET** /v2/linkBookSection/all | Get all quick link sections
[**restore_link_book_section**](QuickLinksSectionApi.md#restore_link_book_section) | **PATCH** /v2/linkBookSection/{id} | Restore quick link section
[**update_link_book_section**](QuickLinksSectionApi.md#update_link_book_section) | **PUT** /v2/linkBookSection/{id} | Update quick link section


# **archive_link_book_section**
> LinkBookSection archive_link_book_section(id)

Archive quick link section

### Example


```python
import wallet
from wallet.models.link_book_section import LinkBookSection
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
    api_instance = wallet.QuickLinksSectionApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive quick link section
        api_response = api_instance.archive_link_book_section(id)
        print("The response of QuickLinksSectionApi->archive_link_book_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksSectionApi->archive_link_book_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**LinkBookSection**](LinkBookSection.md)

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

# **create_link_book_section**
> LinkBookSection create_link_book_section(wt_quick_link_section_create_params)

Create quick link section

### Example


```python
import wallet
from wallet.models.link_book_section import LinkBookSection
from wallet.models.wt_quick_link_section_create_params import WTQuickLinkSectionCreateParams
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
    api_instance = wallet.QuickLinksSectionApi(api_client)
    wt_quick_link_section_create_params = wallet.WTQuickLinkSectionCreateParams() # WTQuickLinkSectionCreateParams | 

    try:
        # Create quick link section
        api_response = api_instance.create_link_book_section(wt_quick_link_section_create_params)
        print("The response of QuickLinksSectionApi->create_link_book_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksSectionApi->create_link_book_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_quick_link_section_create_params** | [**WTQuickLinkSectionCreateParams**](WTQuickLinkSectionCreateParams.md)|  | 

### Return type

[**LinkBookSection**](LinkBookSection.md)

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

# **fetch_all_link_book_sections**
> object fetch_all_link_book_sections(is_archive_included=is_archive_included)

Get all quick link sections

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
    api_instance = wallet.QuickLinksSectionApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all quick link sections
        api_response = api_instance.fetch_all_link_book_sections(is_archive_included=is_archive_included)
        print("The response of QuickLinksSectionApi->fetch_all_link_book_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksSectionApi->fetch_all_link_book_sections: %s\n" % e)
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

# **restore_link_book_section**
> LinkBookSection restore_link_book_section(id)

Restore quick link section

### Example


```python
import wallet
from wallet.models.link_book_section import LinkBookSection
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
    api_instance = wallet.QuickLinksSectionApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore quick link section
        api_response = api_instance.restore_link_book_section(id)
        print("The response of QuickLinksSectionApi->restore_link_book_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksSectionApi->restore_link_book_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**LinkBookSection**](LinkBookSection.md)

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

# **update_link_book_section**
> LinkBookSection update_link_book_section(id, wt_quick_link_section_update_params)

Update quick link section

### Example


```python
import wallet
from wallet.models.link_book_section import LinkBookSection
from wallet.models.wt_quick_link_section_update_params import WTQuickLinkSectionUpdateParams
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
    api_instance = wallet.QuickLinksSectionApi(api_client)
    id = 'id_example' # str | 
    wt_quick_link_section_update_params = wallet.WTQuickLinkSectionUpdateParams() # WTQuickLinkSectionUpdateParams | 

    try:
        # Update quick link section
        api_response = api_instance.update_link_book_section(id, wt_quick_link_section_update_params)
        print("The response of QuickLinksSectionApi->update_link_book_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksSectionApi->update_link_book_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wt_quick_link_section_update_params** | [**WTQuickLinkSectionUpdateParams**](WTQuickLinkSectionUpdateParams.md)|  | 

### Return type

[**LinkBookSection**](LinkBookSection.md)

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

