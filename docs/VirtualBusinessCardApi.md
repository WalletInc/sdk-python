# wallet.VirtualBusinessCardApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_virtual_business_card**](VirtualBusinessCardApi.md#archive_virtual_business_card) | **DELETE** /v2/virtualBusinessCard/{id} | Archive VirtualBusinessCard
[**create_virtual_business_card**](VirtualBusinessCardApi.md#create_virtual_business_card) | **POST** /v2/virtualBusinessCard | Create VirtualBusinessCard
[**fetch_all_virtual_business_cards**](VirtualBusinessCardApi.md#fetch_all_virtual_business_cards) | **GET** /v2/virtualBusinessCard/all | Fetch all VirtualBusinessCards
[**fetch_virtual_business_card**](VirtualBusinessCardApi.md#fetch_virtual_business_card) | **GET** /v2/virtualBusinessCard/{id} | Fetch virtual business card
[**fetch_virtual_business_card_requests**](VirtualBusinessCardApi.md#fetch_virtual_business_card_requests) | **GET** /v2/virtualBusinessCard/requests/{id} | Fetch requests
[**restore_virtual_business_card**](VirtualBusinessCardApi.md#restore_virtual_business_card) | **PATCH** /v2/virtualBusinessCard/{id} | Restore VirtualBusinessCard
[**update_virtual_business_card**](VirtualBusinessCardApi.md#update_virtual_business_card) | **PUT** /v2/virtualBusinessCard/{id} | Update VirtualBusinessCard


# **archive_virtual_business_card**
> VirtualBusinessCard archive_virtual_business_card(id)

Archive VirtualBusinessCard

### Example


```python
import wallet
from wallet.models.virtual_business_card import VirtualBusinessCard
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
    api_instance = wallet.VirtualBusinessCardApi(api_client)
    id = None # object | 

    try:
        # Archive VirtualBusinessCard
        api_response = api_instance.archive_virtual_business_card(id)
        print("The response of VirtualBusinessCardApi->archive_virtual_business_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualBusinessCardApi->archive_virtual_business_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**VirtualBusinessCard**](VirtualBusinessCard.md)

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

# **create_virtual_business_card**
> VirtualBusinessCard create_virtual_business_card(wt_virtual_business_card_create_params)

Create VirtualBusinessCard

### Example


```python
import wallet
from wallet.models.virtual_business_card import VirtualBusinessCard
from wallet.models.wt_virtual_business_card_create_params import WTVirtualBusinessCardCreateParams
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
    api_instance = wallet.VirtualBusinessCardApi(api_client)
    wt_virtual_business_card_create_params = wallet.WTVirtualBusinessCardCreateParams() # WTVirtualBusinessCardCreateParams | 

    try:
        # Create VirtualBusinessCard
        api_response = api_instance.create_virtual_business_card(wt_virtual_business_card_create_params)
        print("The response of VirtualBusinessCardApi->create_virtual_business_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualBusinessCardApi->create_virtual_business_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_virtual_business_card_create_params** | [**WTVirtualBusinessCardCreateParams**](WTVirtualBusinessCardCreateParams.md)|  | 

### Return type

[**VirtualBusinessCard**](VirtualBusinessCard.md)

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

# **fetch_all_virtual_business_cards**
> object fetch_all_virtual_business_cards(is_archive_included=is_archive_included)

Fetch all VirtualBusinessCards

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
    api_instance = wallet.VirtualBusinessCardApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all VirtualBusinessCards
        api_response = api_instance.fetch_all_virtual_business_cards(is_archive_included=is_archive_included)
        print("The response of VirtualBusinessCardApi->fetch_all_virtual_business_cards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualBusinessCardApi->fetch_all_virtual_business_cards: %s\n" % e)
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

# **fetch_virtual_business_card**
> VirtualBusinessCard fetch_virtual_business_card(id)

Fetch virtual business card

### Example


```python
import wallet
from wallet.models.virtual_business_card import VirtualBusinessCard
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
    api_instance = wallet.VirtualBusinessCardApi(api_client)
    id = None # object | 

    try:
        # Fetch virtual business card
        api_response = api_instance.fetch_virtual_business_card(id)
        print("The response of VirtualBusinessCardApi->fetch_virtual_business_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualBusinessCardApi->fetch_virtual_business_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**VirtualBusinessCard**](VirtualBusinessCard.md)

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

# **fetch_virtual_business_card_requests**
> List[WalletPageView] fetch_virtual_business_card_requests(id)

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
    api_instance = wallet.VirtualBusinessCardApi(api_client)
    id = None # object | 

    try:
        # Fetch requests
        api_response = api_instance.fetch_virtual_business_card_requests(id)
        print("The response of VirtualBusinessCardApi->fetch_virtual_business_card_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualBusinessCardApi->fetch_virtual_business_card_requests: %s\n" % e)
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

# **restore_virtual_business_card**
> VirtualBusinessCard restore_virtual_business_card(id)

Restore VirtualBusinessCard

### Example


```python
import wallet
from wallet.models.virtual_business_card import VirtualBusinessCard
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
    api_instance = wallet.VirtualBusinessCardApi(api_client)
    id = None # object | 

    try:
        # Restore VirtualBusinessCard
        api_response = api_instance.restore_virtual_business_card(id)
        print("The response of VirtualBusinessCardApi->restore_virtual_business_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualBusinessCardApi->restore_virtual_business_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**VirtualBusinessCard**](VirtualBusinessCard.md)

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

# **update_virtual_business_card**
> VirtualBusinessCard update_virtual_business_card(id, wt_virtual_business_card_update_params)

Update VirtualBusinessCard

### Example


```python
import wallet
from wallet.models.virtual_business_card import VirtualBusinessCard
from wallet.models.wt_virtual_business_card_update_params import WTVirtualBusinessCardUpdateParams
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
    api_instance = wallet.VirtualBusinessCardApi(api_client)
    id = None # object | 
    wt_virtual_business_card_update_params = wallet.WTVirtualBusinessCardUpdateParams() # WTVirtualBusinessCardUpdateParams | 

    try:
        # Update VirtualBusinessCard
        api_response = api_instance.update_virtual_business_card(id, wt_virtual_business_card_update_params)
        print("The response of VirtualBusinessCardApi->update_virtual_business_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualBusinessCardApi->update_virtual_business_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **wt_virtual_business_card_update_params** | [**WTVirtualBusinessCardUpdateParams**](WTVirtualBusinessCardUpdateParams.md)|  | 

### Return type

[**VirtualBusinessCard**](VirtualBusinessCard.md)

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

