# wallet.RoomRatesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_room_rate**](RoomRatesApi.md#archive_room_rate) | **DELETE** /v2/roomRates/{id} | Archive Room &amp; Rate
[**create_room_rate**](RoomRatesApi.md#create_room_rate) | **POST** /v2/roomRates | Create Room &amp; Rate
[**fetch_all_room_rates**](RoomRatesApi.md#fetch_all_room_rates) | **GET** /v2/roomRates/all | Get all Rooms &amp; Rates
[**restore_room_rate**](RoomRatesApi.md#restore_room_rate) | **PATCH** /v2/roomRates/{id} | Restore Room &amp; Rate
[**update_room_rate**](RoomRatesApi.md#update_room_rate) | **PUT** /v2/roomRates/{id} | Update Room &amp; Rate


# **archive_room_rate**
> RoomRate archive_room_rate(id)

Archive Room & Rate

### Example


```python
import wallet
from wallet.models.room_rate import RoomRate
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
    api_instance = wallet.RoomRatesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive Room & Rate
        api_response = api_instance.archive_room_rate(id)
        print("The response of RoomRatesApi->archive_room_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomRatesApi->archive_room_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Create Room & Rate

### Example


```python
import wallet
from wallet.models.room_rate import RoomRate
from wallet.models.wt_room_rate_create_params import WTRoomRateCreateParams
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
    api_instance = wallet.RoomRatesApi(api_client)
    wt_room_rate_create_params = wallet.WTRoomRateCreateParams() # WTRoomRateCreateParams | 

    try:
        # Create Room & Rate
        api_response = api_instance.create_room_rate(wt_room_rate_create_params)
        print("The response of RoomRatesApi->create_room_rate:\n")
        pprint(api_response)
    except Exception as e:
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
> object fetch_all_room_rates(is_archive_included=is_archive_included)

Get all Rooms & Rates

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
    api_instance = wallet.RoomRatesApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all Rooms & Rates
        api_response = api_instance.fetch_all_room_rates(is_archive_included=is_archive_included)
        print("The response of RoomRatesApi->fetch_all_room_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomRatesApi->fetch_all_room_rates: %s\n" % e)
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

# **restore_room_rate**
> RoomRate restore_room_rate(id)

Restore Room & Rate

### Example


```python
import wallet
from wallet.models.room_rate import RoomRate
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
    api_instance = wallet.RoomRatesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore Room & Rate
        api_response = api_instance.restore_room_rate(id)
        print("The response of RoomRatesApi->restore_room_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomRatesApi->restore_room_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Update Room & Rate

### Example


```python
import wallet
from wallet.models.room_rate import RoomRate
from wallet.models.wt_room_rate_update_params import WTRoomRateUpdateParams
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
    api_instance = wallet.RoomRatesApi(api_client)
    id = 'id_example' # str | 
    wt_room_rate_update_params = wallet.WTRoomRateUpdateParams() # WTRoomRateUpdateParams | 

    try:
        # Update Room & Rate
        api_response = api_instance.update_room_rate(id, wt_room_rate_update_params)
        print("The response of RoomRatesApi->update_room_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomRatesApi->update_room_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

