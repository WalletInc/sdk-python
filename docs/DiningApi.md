# wallet.DiningApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_dining**](DiningApi.md#archive_dining) | **DELETE** /v2/dining/{id} | Archive dining
[**create_dining**](DiningApi.md#create_dining) | **POST** /v2/dining | Create dining
[**fetch_all_dining**](DiningApi.md#fetch_all_dining) | **GET** /v2/dining/all | Fetch all dining
[**restore_dining**](DiningApi.md#restore_dining) | **PATCH** /v2/dining/{id} | Restore dining
[**update_dining**](DiningApi.md#update_dining) | **PUT** /v2/dining/{id} | Update dining


# **archive_dining**
> Dining archive_dining(id)

Archive dining

### Example


```python
import time
import wallet
from wallet.api import dining_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.dining import Dining
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
    api_instance = dining_api.DiningApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive dining
        api_response = api_instance.archive_dining(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling DiningApi->archive_dining: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Dining**](Dining.md)

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

# **create_dining**
> Dining create_dining(wt_dining_create_params)

Create dining

### Example


```python
import time
import wallet
from wallet.api import dining_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.dining import Dining
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_dining_create_params import WTDiningCreateParams
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
    api_instance = dining_api.DiningApi(api_client)
    wt_dining_create_params = WTDiningCreateParams(
        title="This is the title of the amenity",
        description="This is the description of the amenity",
        displayed_price="$200-$350",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.png",
        additional_info_url="https://your-site.com/restaurants/steak-house",
    ) # WTDiningCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create dining
        api_response = api_instance.create_dining(wt_dining_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling DiningApi->create_dining: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_dining_create_params** | [**WTDiningCreateParams**](WTDiningCreateParams.md)|  |

### Return type

[**Dining**](Dining.md)

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

# **fetch_all_dining**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_dining()

Fetch all dining

### Example


```python
import time
import wallet
from wallet.api import dining_api
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
    api_instance = dining_api.DiningApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all dining
        api_response = api_instance.fetch_all_dining(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling DiningApi->fetch_all_dining: %s\n" % e)
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

# **restore_dining**
> Dining restore_dining(id)

Restore dining

### Example


```python
import time
import wallet
from wallet.api import dining_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.dining import Dining
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
    api_instance = dining_api.DiningApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore dining
        api_response = api_instance.restore_dining(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling DiningApi->restore_dining: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**Dining**](Dining.md)

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

# **update_dining**
> Dining update_dining(id, wt_dining_update_params)

Update dining

### Example


```python
import time
import wallet
from wallet.api import dining_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.dining import Dining
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_dining_update_params import WTDiningUpdateParams
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dining_api.DiningApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_dining_update_params = WTDiningUpdateParams(
        title="This is the title of the amenity",
        description="This is the description of the amenity",
        displayed_price="$200-$350",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.png",
        additional_info_url="https://your-site.com/restaurants/steak-house",
    ) # WTDiningUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update dining
        api_response = api_instance.update_dining(id, wt_dining_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling DiningApi->update_dining: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **wt_dining_update_params** | [**WTDiningUpdateParams**](WTDiningUpdateParams.md)|  |

### Return type

[**Dining**](Dining.md)

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

