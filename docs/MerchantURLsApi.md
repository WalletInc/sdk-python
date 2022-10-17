# wallet.MerchantURLsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_merchant_url**](MerchantURLsApi.md#archive_merchant_url) | **DELETE** /v2/business/merchantUrl/{id} | Archive merchant url
[**create_merchant_url**](MerchantURLsApi.md#create_merchant_url) | **POST** /v2/business/merchantUrl | Create merchant url
[**fetch_all_merchant_urls**](MerchantURLsApi.md#fetch_all_merchant_urls) | **GET** /v2/business/merchantUrl/all | Fetch all merchant urls
[**fetch_merchant_url**](MerchantURLsApi.md#fetch_merchant_url) | **GET** /v2/business/merchantUrl/{id} | Fetch merchant url
[**fetch_merchant_url_requests**](MerchantURLsApi.md#fetch_merchant_url_requests) | **GET** /v2/business/merchantUrl/requests/{id} | Fetch requests
[**restore_merchant_url**](MerchantURLsApi.md#restore_merchant_url) | **PATCH** /v2/business/merchantUrl/{id} | Restore merchant url
[**update_merchant_url**](MerchantURLsApi.md#update_merchant_url) | **PUT** /v2/business/merchantUrl/{id} | Update merchant url


# **archive_merchant_url**
> MerchantURL archive_merchant_url(id)

Archive merchant url

### Example


```python
import time
import wallet
from wallet.api import merchant_urls_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.merchant_url import MerchantURL
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
    api_instance = merchant_urls_api.MerchantURLsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive merchant url
        api_response = api_instance.archive_merchant_url(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantURLsApi->archive_merchant_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**MerchantURL**](MerchantURL.md)

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

# **create_merchant_url**
> MerchantURL create_merchant_url(wt_merchant_url_create)

Create merchant url

### Example


```python
import time
import wallet
from wallet.api import merchant_urls_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.merchant_url import MerchantURL
from wallet.model.auth_error import AuthError
from wallet.model.wt_merchant_url_create import WTMerchantURLCreate
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = merchant_urls_api.MerchantURLsApi(api_client)
    wt_merchant_url_create = WTMerchantURLCreate(
        nickname="Title",
        destination_url="https://example.com",
    ) # WTMerchantURLCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create merchant url
        api_response = api_instance.create_merchant_url(wt_merchant_url_create)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantURLsApi->create_merchant_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_merchant_url_create** | [**WTMerchantURLCreate**](WTMerchantURLCreate.md)|  |

### Return type

[**MerchantURL**](MerchantURL.md)

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

# **fetch_all_merchant_urls**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_merchant_urls()

Fetch all merchant urls

### Example


```python
import time
import wallet
from wallet.api import merchant_urls_api
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
    api_instance = merchant_urls_api.MerchantURLsApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all merchant urls
        api_response = api_instance.fetch_all_merchant_urls(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantURLsApi->fetch_all_merchant_urls: %s\n" % e)
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

# **fetch_merchant_url**
> MerchantURL fetch_merchant_url(id)

Fetch merchant url

### Example


```python
import time
import wallet
from wallet.api import merchant_urls_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.merchant_url import MerchantURL
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
    api_instance = merchant_urls_api.MerchantURLsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch merchant url
        api_response = api_instance.fetch_merchant_url(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantURLsApi->fetch_merchant_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**MerchantURL**](MerchantURL.md)

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

# **fetch_merchant_url_requests**
> [WalletPageView] fetch_merchant_url_requests(id)

Fetch requests

### Example


```python
import time
import wallet
from wallet.api import merchant_urls_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wallet_page_view import WalletPageView
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
    api_instance = merchant_urls_api.MerchantURLsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch requests
        api_response = api_instance.fetch_merchant_url_requests(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantURLsApi->fetch_merchant_url_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**[WalletPageView]**](WalletPageView.md)

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

# **restore_merchant_url**
> MerchantURL restore_merchant_url(id)

Restore merchant url

### Example


```python
import time
import wallet
from wallet.api import merchant_urls_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.merchant_url import MerchantURL
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
    api_instance = merchant_urls_api.MerchantURLsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore merchant url
        api_response = api_instance.restore_merchant_url(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantURLsApi->restore_merchant_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**MerchantURL**](MerchantURL.md)

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

# **update_merchant_url**
> MerchantURL update_merchant_url(id, wt_merchant_url_update)

Update merchant url

### Example


```python
import time
import wallet
from wallet.api import merchant_urls_api
from wallet.model.wt_merchant_url_update import WTMerchantURLUpdate
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.merchant_url import MerchantURL
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
    api_instance = merchant_urls_api.MerchantURLsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_merchant_url_update = WTMerchantURLUpdate(
        nickname="Title",
        destination_url="https://example.com",
    ) # WTMerchantURLUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update merchant url
        api_response = api_instance.update_merchant_url(id, wt_merchant_url_update)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantURLsApi->update_merchant_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **wt_merchant_url_update** | [**WTMerchantURLUpdate**](WTMerchantURLUpdate.md)|  |

### Return type

[**MerchantURL**](MerchantURL.md)

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

