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
import time
import wallet
from wallet.api import virtual_business_card_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.virtual_business_card import VirtualBusinessCard
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
    api_instance = virtual_business_card_api.VirtualBusinessCardApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive VirtualBusinessCard
        api_response = api_instance.archive_virtual_business_card(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling VirtualBusinessCardApi->archive_virtual_business_card: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import virtual_business_card_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.virtual_business_card import VirtualBusinessCard
from wallet.model.wt_virtual_business_card_create_params import WTVirtualBusinessCardCreateParams
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
    api_instance = virtual_business_card_api.VirtualBusinessCardApi(api_client)
    wt_virtual_business_card_create_params = WTVirtualBusinessCardCreateParams(
        first_name="John",
        last_name="Smith",
        email_address="email_address_example",
        designation="designation_example",
        phone_number="+1 (800) 123-4567",
        introduction="John was born into the F&B world. His grandparents owned a restaurant in the 1960s in Lorraine, France. His brother is a chef and his uncle is a famous chef in the U.S. ...",
        instagram="your_IG_handle",
        facebook="page ID or handle",
        you_tube="channel ID or handle",
        twitter="your_handle",
        linked_in="company ID or handle",
        whats_app="WhatsApp number",
        avatar_url="WhatsApp number",
    ) # WTVirtualBusinessCardCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create VirtualBusinessCard
        api_response = api_instance.create_virtual_business_card(wt_virtual_business_card_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
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
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_virtual_business_cards()

Fetch all VirtualBusinessCards

### Example


```python
import time
import wallet
from wallet.api import virtual_business_card_api
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
    api_instance = virtual_business_card_api.VirtualBusinessCardApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all VirtualBusinessCards
        api_response = api_instance.fetch_all_virtual_business_cards(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling VirtualBusinessCardApi->fetch_all_virtual_business_cards: %s\n" % e)
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

# **fetch_virtual_business_card**
> VirtualBusinessCard fetch_virtual_business_card(id)

Fetch virtual business card

### Example


```python
import time
import wallet
from wallet.api import virtual_business_card_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.virtual_business_card import VirtualBusinessCard
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
    api_instance = virtual_business_card_api.VirtualBusinessCardApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch virtual business card
        api_response = api_instance.fetch_virtual_business_card(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling VirtualBusinessCardApi->fetch_virtual_business_card: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
> [WalletPageView] fetch_virtual_business_card_requests(id)

Fetch requests

### Example


```python
import time
import wallet
from wallet.api import virtual_business_card_api
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
    api_instance = virtual_business_card_api.VirtualBusinessCardApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch requests
        api_response = api_instance.fetch_virtual_business_card_requests(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling VirtualBusinessCardApi->fetch_virtual_business_card_requests: %s\n" % e)
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

# **restore_virtual_business_card**
> VirtualBusinessCard restore_virtual_business_card(id)

Restore VirtualBusinessCard

### Example


```python
import time
import wallet
from wallet.api import virtual_business_card_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.virtual_business_card import VirtualBusinessCard
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
    api_instance = virtual_business_card_api.VirtualBusinessCardApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore VirtualBusinessCard
        api_response = api_instance.restore_virtual_business_card(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling VirtualBusinessCardApi->restore_virtual_business_card: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import virtual_business_card_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.virtual_business_card import VirtualBusinessCard
from wallet.model.wt_virtual_business_card_update_params import WTVirtualBusinessCardUpdateParams
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
    api_instance = virtual_business_card_api.VirtualBusinessCardApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_virtual_business_card_update_params = WTVirtualBusinessCardUpdateParams(
        first_name="John",
        last_name="Smith",
        email_address="email_address_example",
        designation="designation_example",
        phone_number="+1 (800) 123-4567",
        introduction="John was born into the F&B world. His grandparents owned a restaurant in the 1960s in Lorraine, France. His brother is a chef and his uncle is a famous chef in the U.S. ...",
        instagram="your_IG_handle",
        facebook="page ID or handle",
        you_tube="channel ID or handle",
        twitter="your_handle",
        linked_in="company ID or handle",
        whats_app="WhatsApp number",
        avatar_url="WhatsApp number",
    ) # WTVirtualBusinessCardUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update VirtualBusinessCard
        api_response = api_instance.update_virtual_business_card(id, wt_virtual_business_card_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling VirtualBusinessCardApi->update_virtual_business_card: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

