# wallet.LoungeApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_lounge**](LoungeApi.md#archive_lounge) | **DELETE** /v2/lounge/{id} | Archive lounge
[**create_lounge**](LoungeApi.md#create_lounge) | **POST** /v2/lounge | Create lounge
[**fetch_all_lounge**](LoungeApi.md#fetch_all_lounge) | **GET** /v2/lounge/all | Fetch all lounge
[**restore_lounge**](LoungeApi.md#restore_lounge) | **PATCH** /v2/lounge/{id} | Restore lounge
[**update_lounge**](LoungeApi.md#update_lounge) | **PUT** /v2/lounge/{id} | Update lounge


# **archive_lounge**
> Lounge archive_lounge(id)

Archive lounge

### Example


```python
import time
import wallet
from wallet.api import lounge_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.lounge import Lounge
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
    api_instance = lounge_api.LoungeApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive lounge
        api_response = api_instance.archive_lounge(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LoungeApi->archive_lounge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Lounge**](Lounge.md)

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

# **create_lounge**
> Lounge create_lounge(wt_lounge_create_params)

Create lounge

### Example


```python
import time
import wallet
from wallet.api import lounge_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_lounge_create_params import WTLoungeCreateParams
from wallet.model.lounge import Lounge
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
    api_instance = lounge_api.LoungeApi(api_client)
    wt_lounge_create_params = WTLoungeCreateParams(
        title="This is the title of the amenity",
        description="This is the description of the amenity",
        displayed_price="$200-$350",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.png",
        additional_info_url="https://your-site.com/restaurants/steak-house",
    ) # WTLoungeCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create lounge
        api_response = api_instance.create_lounge(wt_lounge_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LoungeApi->create_lounge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_lounge_create_params** | [**WTLoungeCreateParams**](WTLoungeCreateParams.md)|  |

### Return type

[**Lounge**](Lounge.md)

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

# **fetch_all_lounge**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_lounge()

Fetch all lounge

### Example


```python
import time
import wallet
from wallet.api import lounge_api
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
    api_instance = lounge_api.LoungeApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all lounge
        api_response = api_instance.fetch_all_lounge(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LoungeApi->fetch_all_lounge: %s\n" % e)
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

# **restore_lounge**
> Lounge restore_lounge(id)

Restore lounge

### Example


```python
import time
import wallet
from wallet.api import lounge_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.lounge import Lounge
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
    api_instance = lounge_api.LoungeApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore lounge
        api_response = api_instance.restore_lounge(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LoungeApi->restore_lounge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Lounge**](Lounge.md)

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

# **update_lounge**
> Lounge update_lounge(id, wt_lounge_update_params)

Update lounge

### Example


```python
import time
import wallet
from wallet.api import lounge_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_lounge_update_params import WTLoungeUpdateParams
from wallet.model.lounge import Lounge
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
    api_instance = lounge_api.LoungeApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_lounge_update_params = WTLoungeUpdateParams(
        title="This is the title of the amenity",
        description="This is the description of the amenity",
        displayed_price="$200-$350",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.png",
        additional_info_url="https://your-site.com/restaurants/steak-house",
    ) # WTLoungeUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update lounge
        api_response = api_instance.update_lounge(id, wt_lounge_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling LoungeApi->update_lounge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **wt_lounge_update_params** | [**WTLoungeUpdateParams**](WTLoungeUpdateParams.md)|  |

### Return type

[**Lounge**](Lounge.md)

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

