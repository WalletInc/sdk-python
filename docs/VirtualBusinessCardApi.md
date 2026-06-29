# wallet.VirtualBusinessCardApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_virtual_business_card**](VirtualBusinessCardApi.md#archive_virtual_business_card) | **DELETE** /v2/virtualBusinessCard/{id} | Archive Virtual Business Card
[**create_virtual_business_card**](VirtualBusinessCardApi.md#create_virtual_business_card) | **POST** /v2/virtualBusinessCard | Create Virtual Business Card
[**fetch_all_virtual_business_cards**](VirtualBusinessCardApi.md#fetch_all_virtual_business_cards) | **GET** /v2/virtualBusinessCard/all | Get all Virtual Business Cards
[**fetch_virtual_business_card**](VirtualBusinessCardApi.md#fetch_virtual_business_card) | **GET** /v2/virtualBusinessCard/{id} | Get Virtual Business Card
[**fetch_virtual_business_card_requests**](VirtualBusinessCardApi.md#fetch_virtual_business_card_requests) | **GET** /v2/virtualBusinessCard/requests/{id} | Get Virtual Business Card traffic
[**restore_virtual_business_card**](VirtualBusinessCardApi.md#restore_virtual_business_card) | **PATCH** /v2/virtualBusinessCard/{id} | Restore Virtual Business Card
[**update_virtual_business_card**](VirtualBusinessCardApi.md#update_virtual_business_card) | **PUT** /v2/virtualBusinessCard/{id} | Update Virtual Business Card


# **archive_virtual_business_card**
> VirtualBusinessCard archive_virtual_business_card(id)

Archive Virtual Business Card

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
    id = 'id_example' # str | 

    try:
        # Archive Virtual Business Card
        api_response = api_instance.archive_virtual_business_card(id)
        print("The response of VirtualBusinessCardApi->archive_virtual_business_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualBusinessCardApi->archive_virtual_business_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Create Virtual Business Card

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
        # Create Virtual Business Card
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

Get all Virtual Business Cards

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
        # Get all Virtual Business Cards
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

Get Virtual Business Card

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
    id = 'id_example' # str | 

    try:
        # Get Virtual Business Card
        api_response = api_instance.fetch_virtual_business_card(id)
        print("The response of VirtualBusinessCardApi->fetch_virtual_business_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualBusinessCardApi->fetch_virtual_business_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Get Virtual Business Card traffic

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
    id = 'id_example' # str | 

    try:
        # Get Virtual Business Card traffic
        api_response = api_instance.fetch_virtual_business_card_requests(id)
        print("The response of VirtualBusinessCardApi->fetch_virtual_business_card_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualBusinessCardApi->fetch_virtual_business_card_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Restore Virtual Business Card

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
    id = 'id_example' # str | 

    try:
        # Restore Virtual Business Card
        api_response = api_instance.restore_virtual_business_card(id)
        print("The response of VirtualBusinessCardApi->restore_virtual_business_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualBusinessCardApi->restore_virtual_business_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Update Virtual Business Card

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
    id = 'id_example' # str | 
    wt_virtual_business_card_update_params = wallet.WTVirtualBusinessCardUpdateParams() # WTVirtualBusinessCardUpdateParams | 

    try:
        # Update Virtual Business Card
        api_response = api_instance.update_virtual_business_card(id, wt_virtual_business_card_update_params)
        print("The response of VirtualBusinessCardApi->update_virtual_business_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualBusinessCardApi->update_virtual_business_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

