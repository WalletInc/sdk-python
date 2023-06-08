# wallet.GamingApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_gaming**](GamingApi.md#archive_gaming) | **DELETE** /v2/gaming/{id} | Archive gaming
[**create_gaming**](GamingApi.md#create_gaming) | **POST** /v2/gaming | Create gaming
[**fetch_all_gaming**](GamingApi.md#fetch_all_gaming) | **GET** /v2/gaming/all | Fetch all gaming
[**restore_gaming**](GamingApi.md#restore_gaming) | **PATCH** /v2/gaming/{id} | Restore gaming
[**update_gaming**](GamingApi.md#update_gaming) | **PUT** /v2/gaming/{id} | Update gaming


# **archive_gaming**
> Gaming archive_gaming(id)

Archive gaming

### Example


```python
import time
import wallet
from wallet.api import gaming_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.gaming import Gaming
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = gaming_api.GamingApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive gaming
        api_response = api_instance.archive_gaming(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling GamingApi->archive_gaming: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Gaming**](Gaming.md)

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

# **create_gaming**
> Gaming create_gaming(wt_gaming_create_params)

Create gaming

### Example


```python
import time
import wallet
from wallet.api import gaming_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_gaming_create_params import WTGamingCreateParams
from wallet.model.auth_error import AuthError
from wallet.model.gaming import Gaming
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = gaming_api.GamingApi(api_client)
    wt_gaming_create_params = WTGamingCreateParams(
        title="This is the title of the amenity",
        description="This is the description of the amenity",
        displayed_price="$200-$350",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.png",
        additional_info_url="https://your-site.com/games/blackjack",
    ) # WTGamingCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create gaming
        api_response = api_instance.create_gaming(wt_gaming_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling GamingApi->create_gaming: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_gaming_create_params** | [**WTGamingCreateParams**](WTGamingCreateParams.md)|  |

### Return type

[**Gaming**](Gaming.md)

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

# **fetch_all_gaming**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_gaming()

Fetch all gaming

### Example


```python
import time
import wallet
from wallet.api import gaming_api
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
    api_instance = gaming_api.GamingApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all gaming
        api_response = api_instance.fetch_all_gaming(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling GamingApi->fetch_all_gaming: %s\n" % e)
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

# **restore_gaming**
> Gaming restore_gaming(id)

Restore gaming

### Example


```python
import time
import wallet
from wallet.api import gaming_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.gaming import Gaming
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = gaming_api.GamingApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore gaming
        api_response = api_instance.restore_gaming(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling GamingApi->restore_gaming: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Gaming**](Gaming.md)

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

# **update_gaming**
> Gaming update_gaming(id, wt_gaming_update_params)

Update gaming

### Example


```python
import time
import wallet
from wallet.api import gaming_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_gaming_update_params import WTGamingUpdateParams
from wallet.model.auth_error import AuthError
from wallet.model.gaming import Gaming
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = gaming_api.GamingApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_gaming_update_params = WTGamingUpdateParams(
        title="This is the title of the amenity",
        description="This is the description of the amenity",
        displayed_price="$200-$350",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.png",
        additional_info_url="https://your-site.com/games/blackjack",
    ) # WTGamingUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update gaming
        api_response = api_instance.update_gaming(id, wt_gaming_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling GamingApi->update_gaming: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **wt_gaming_update_params** | [**WTGamingUpdateParams**](WTGamingUpdateParams.md)|  |

### Return type

[**Gaming**](Gaming.md)

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

