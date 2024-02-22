# wallet.QuickLinksSectionApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_link_book_section**](QuickLinksSectionApi.md#archive_link_book_section) | **DELETE** /v2/linkBookSection/{id} | Archive link book section
[**create_link_book_section**](QuickLinksSectionApi.md#create_link_book_section) | **POST** /v2/linkBookSection | Create link book section
[**fetch_all_link_book_sections**](QuickLinksSectionApi.md#fetch_all_link_book_sections) | **GET** /v2/linkBookSection/all | Fetch all link book sections
[**restore_link_book_section**](QuickLinksSectionApi.md#restore_link_book_section) | **PATCH** /v2/linkBookSection/{id} | Restore link book section
[**update_link_book_section**](QuickLinksSectionApi.md#update_link_book_section) | **PUT** /v2/linkBookSection/{id} | Update link book section


# **archive_link_book_section**
> LinkBookSection archive_link_book_section(id)

Archive link book section

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
    id = None # object | 

    try:
        # Archive link book section
        api_response = api_instance.archive_link_book_section(id)
        print("The response of QuickLinksSectionApi->archive_link_book_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksSectionApi->archive_link_book_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
> LinkBookSection create_link_book_section(wt_link_book_section_create_params)

Create link book section

### Example


```python
import wallet
from wallet.models.link_book_section import LinkBookSection
from wallet.models.wt_link_book_section_create_params import WTLinkBookSectionCreateParams
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
    wt_link_book_section_create_params = wallet.WTLinkBookSectionCreateParams() # WTLinkBookSectionCreateParams | 

    try:
        # Create link book section
        api_response = api_instance.create_link_book_section(wt_link_book_section_create_params)
        print("The response of QuickLinksSectionApi->create_link_book_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksSectionApi->create_link_book_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_link_book_section_create_params** | [**WTLinkBookSectionCreateParams**](WTLinkBookSectionCreateParams.md)|  | 

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

Fetch all link book sections

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
        # Fetch all link book sections
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

Restore link book section

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
    id = None # object | 

    try:
        # Restore link book section
        api_response = api_instance.restore_link_book_section(id)
        print("The response of QuickLinksSectionApi->restore_link_book_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksSectionApi->restore_link_book_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
> LinkBookSection update_link_book_section(id, wt_link_book_section_update_params)

Update link book section

### Example


```python
import wallet
from wallet.models.link_book_section import LinkBookSection
from wallet.models.wt_link_book_section_update_params import WTLinkBookSectionUpdateParams
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
    id = None # object | 
    wt_link_book_section_update_params = wallet.WTLinkBookSectionUpdateParams() # WTLinkBookSectionUpdateParams | 

    try:
        # Update link book section
        api_response = api_instance.update_link_book_section(id, wt_link_book_section_update_params)
        print("The response of QuickLinksSectionApi->update_link_book_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuickLinksSectionApi->update_link_book_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **wt_link_book_section_update_params** | [**WTLinkBookSectionUpdateParams**](WTLinkBookSectionUpdateParams.md)|  | 

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

