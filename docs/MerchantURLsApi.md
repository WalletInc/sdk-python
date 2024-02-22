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
import wallet
from wallet.models.merchant_url import MerchantURL
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
    api_instance = wallet.MerchantURLsApi(api_client)
    id = None # object | 

    try:
        # Archive merchant url
        api_response = api_instance.archive_merchant_url(id)
        print("The response of MerchantURLsApi->archive_merchant_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantURLsApi->archive_merchant_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
import wallet
from wallet.models.merchant_url import MerchantURL
from wallet.models.wt_merchant_url_create import WTMerchantURLCreate
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
    api_instance = wallet.MerchantURLsApi(api_client)
    wt_merchant_url_create = wallet.WTMerchantURLCreate() # WTMerchantURLCreate | 

    try:
        # Create merchant url
        api_response = api_instance.create_merchant_url(wt_merchant_url_create)
        print("The response of MerchantURLsApi->create_merchant_url:\n")
        pprint(api_response)
    except Exception as e:
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
> object fetch_all_merchant_urls(is_archive_included=is_archive_included)

Fetch all merchant urls

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
    api_instance = wallet.MerchantURLsApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all merchant urls
        api_response = api_instance.fetch_all_merchant_urls(is_archive_included=is_archive_included)
        print("The response of MerchantURLsApi->fetch_all_merchant_urls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantURLsApi->fetch_all_merchant_urls: %s\n" % e)
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

# **fetch_merchant_url**
> MerchantURL fetch_merchant_url(id)

Fetch merchant url

### Example


```python
import wallet
from wallet.models.merchant_url import MerchantURL
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
    api_instance = wallet.MerchantURLsApi(api_client)
    id = None # object | 

    try:
        # Fetch merchant url
        api_response = api_instance.fetch_merchant_url(id)
        print("The response of MerchantURLsApi->fetch_merchant_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantURLsApi->fetch_merchant_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
> List[WalletPageView] fetch_merchant_url_requests(id)

Fetch requests

### Example


```python
import wallet
from wallet.models.wallet_page_view import WalletPageView
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
    api_instance = wallet.MerchantURLsApi(api_client)
    id = None # object | 

    try:
        # Fetch requests
        api_response = api_instance.fetch_merchant_url_requests(id)
        print("The response of MerchantURLsApi->fetch_merchant_url_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantURLsApi->fetch_merchant_url_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**List[WalletPageView]**](WalletPageView.md)

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
import wallet
from wallet.models.merchant_url import MerchantURL
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
    api_instance = wallet.MerchantURLsApi(api_client)
    id = None # object | 

    try:
        # Restore merchant url
        api_response = api_instance.restore_merchant_url(id)
        print("The response of MerchantURLsApi->restore_merchant_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantURLsApi->restore_merchant_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
import wallet
from wallet.models.merchant_url import MerchantURL
from wallet.models.wt_merchant_url_update import WTMerchantURLUpdate
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
    api_instance = wallet.MerchantURLsApi(api_client)
    id = None # object | 
    wt_merchant_url_update = wallet.WTMerchantURLUpdate() # WTMerchantURLUpdate | 

    try:
        # Update merchant url
        api_response = api_instance.update_merchant_url(id, wt_merchant_url_update)
        print("The response of MerchantURLsApi->update_merchant_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantURLsApi->update_merchant_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
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

