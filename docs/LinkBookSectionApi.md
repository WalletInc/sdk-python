# wallet.LinkBookSectionApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_link_book_section**](LinkBookSectionApi.md#archive_link_book_section) | **DELETE** /v2/linkBookSection/{id} | Archive link book section
[**create_link_book_section**](LinkBookSectionApi.md#create_link_book_section) | **POST** /v2/linkBookSection | Create link book section
[**fetch_all_link_book_sections**](LinkBookSectionApi.md#fetch_all_link_book_sections) | **GET** /v2/linkBookSection/all | Fetch all link book sections
[**restore_link_book_section**](LinkBookSectionApi.md#restore_link_book_section) | **PATCH** /v2/linkBookSection/{id} | Restore link book section
[**update_link_book_section**](LinkBookSectionApi.md#update_link_book_section) | **PUT** /v2/linkBookSection/{id} | Update link book section


# **archive_link_book_section**
> LinkBookSection archive_link_book_section(id)

Archive link book section

### Example


```python
import time
import wallet
from wallet.api import link_book_section_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.link_book_section import LinkBookSection
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
    api_instance = link_book_section_api.LinkBookSectionApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive link book section
        api_response = api_instance.archive_link_book_section(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LinkBookSectionApi->archive_link_book_section: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import link_book_section_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.link_book_section import LinkBookSection
from wallet.model.wt_link_book_section_create_params import WTLinkBookSectionCreateParams
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
    api_instance = link_book_section_api.LinkBookSectionApi(api_client)
    wt_link_book_section_create_params = WTLinkBookSectionCreateParams(
        name="This is the name of the link book section",
        order_number=1,
    ) # WTLinkBookSectionCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create link book section
        api_response = api_instance.create_link_book_section(wt_link_book_section_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LinkBookSectionApi->create_link_book_section: %s\n" % e)
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
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_link_book_sections()

Fetch all link book sections

### Example


```python
import time
import wallet
from wallet.api import link_book_section_api
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
    api_instance = link_book_section_api.LinkBookSectionApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all link book sections
        api_response = api_instance.fetch_all_link_book_sections(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LinkBookSectionApi->fetch_all_link_book_sections: %s\n" % e)
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

# **restore_link_book_section**
> LinkBookSection restore_link_book_section(id)

Restore link book section

### Example


```python
import time
import wallet
from wallet.api import link_book_section_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.link_book_section import LinkBookSection
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
    api_instance = link_book_section_api.LinkBookSectionApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore link book section
        api_response = api_instance.restore_link_book_section(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LinkBookSectionApi->restore_link_book_section: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import link_book_section_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.link_book_section import LinkBookSection
from wallet.model.wt_link_book_section_update_params import WTLinkBookSectionUpdateParams
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
    api_instance = link_book_section_api.LinkBookSectionApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_link_book_section_update_params = WTLinkBookSectionUpdateParams(
        name="This is the name of the link book section",
        order_number=1,
    ) # WTLinkBookSectionUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update link book section
        api_response = api_instance.update_link_book_section(id, wt_link_book_section_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LinkBookSectionApi->update_link_book_section: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

