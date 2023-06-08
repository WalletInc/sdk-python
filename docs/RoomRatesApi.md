# wallet.RoomRatesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_room_rate**](RoomRatesApi.md#archive_room_rate) | **DELETE** /v2/roomRates/{id} | Archive room rate
[**create_room_rate**](RoomRatesApi.md#create_room_rate) | **POST** /v2/roomRates | Create room rate
[**fetch_all_room_rates**](RoomRatesApi.md#fetch_all_room_rates) | **GET** /v2/roomRates/all | Fetch all room rates
[**restore_room_rate**](RoomRatesApi.md#restore_room_rate) | **PATCH** /v2/roomRates/{id} | Restore room rate
[**update_room_rate**](RoomRatesApi.md#update_room_rate) | **PUT** /v2/roomRates/{id} | Update room rate


# **archive_room_rate**
> RoomRate archive_room_rate(id)

Archive room rate

### Example


```python
import time
import wallet
from wallet.api import room_rates_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.room_rate import RoomRate
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
    api_instance = room_rates_api.RoomRatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive room rate
        api_response = api_instance.archive_room_rate(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling RoomRatesApi->archive_room_rate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**RoomRate**](RoomRate.md)

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

# **create_room_rate**
> RoomRate create_room_rate(wt_room_rate_create_params)

Create room rate

### Example


```python
import time
import wallet
from wallet.api import room_rates_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.room_rate import RoomRate
from wallet.model.wt_room_rate_create_params import WTRoomRateCreateParams
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
    api_instance = room_rates_api.RoomRatesApi(api_client)
    wt_room_rate_create_params = WTRoomRateCreateParams(
        title="This is the title of the room & rate",
        description="This is the description of the room & rate",
        displayed_price="$200-$350",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.png",
        additional_info_url="https://hotels.com/your-property/king-bedroom",
    ) # WTRoomRateCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create room rate
        api_response = api_instance.create_room_rate(wt_room_rate_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling RoomRatesApi->create_room_rate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_room_rate_create_params** | [**WTRoomRateCreateParams**](WTRoomRateCreateParams.md)|  |

### Return type

[**RoomRate**](RoomRate.md)

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

# **fetch_all_room_rates**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_room_rates()

Fetch all room rates

### Example


```python
import time
import wallet
from wallet.api import room_rates_api
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
    api_instance = room_rates_api.RoomRatesApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all room rates
        api_response = api_instance.fetch_all_room_rates(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling RoomRatesApi->fetch_all_room_rates: %s\n" % e)
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

# **restore_room_rate**
> RoomRate restore_room_rate(id)

Restore room rate

### Example


```python
import time
import wallet
from wallet.api import room_rates_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.room_rate import RoomRate
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
    api_instance = room_rates_api.RoomRatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore room rate
        api_response = api_instance.restore_room_rate(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling RoomRatesApi->restore_room_rate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**RoomRate**](RoomRate.md)

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

# **update_room_rate**
> RoomRate update_room_rate(id, wt_room_rate_update_params)

Update room rate

### Example


```python
import time
import wallet
from wallet.api import room_rates_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.room_rate import RoomRate
from wallet.model.wt_room_rate_update_params import WTRoomRateUpdateParams
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
    api_instance = room_rates_api.RoomRatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_room_rate_update_params = WTRoomRateUpdateParams(
        title="This is the title of the room & rate",
        description="This is the description of the room & rate",
        displayed_price="$200-$350",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.png",
        additional_info_url="https://hotels.com/your-property/king-bedroom",
    ) # WTRoomRateUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update room rate
        api_response = api_instance.update_room_rate(id, wt_room_rate_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling RoomRatesApi->update_room_rate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **wt_room_rate_update_params** | [**WTRoomRateUpdateParams**](WTRoomRateUpdateParams.md)|  |

### Return type

[**RoomRate**](RoomRate.md)

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

