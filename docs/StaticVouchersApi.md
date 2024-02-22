# wallet.StaticVouchersApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_static_voucher**](StaticVouchersApi.md#create_static_voucher) | **POST** /v2/payment/staticVoucher | Create static voucher
[**delete_static_voucher**](StaticVouchersApi.md#delete_static_voucher) | **DELETE** /v2/payment/staticVoucher/{id} | Delete static voucher
[**fetch_reach_stats_of_all_static_vouchers**](StaticVouchersApi.md#fetch_reach_stats_of_all_static_vouchers) | **GET** /v2/payment/staticVoucher/reach/all | Get the reach statistics of all the static vouchers
[**fetch_reach_stats_of_individual_static_voucher**](StaticVouchersApi.md#fetch_reach_stats_of_individual_static_voucher) | **GET** /v2/payment/staticVoucher/reach/{staticVoucherID} | Get the reach statistics of an individual static voucher
[**fetch_static_voucher**](StaticVouchersApi.md#fetch_static_voucher) | **GET** /v2/payment/staticVoucher/{id} | Fetch static voucher
[**update_static_voucher**](StaticVouchersApi.md#update_static_voucher) | **PUT** /v2/payment/staticVoucher/{id} | Update static voucher


# **create_static_voucher**
> WTStaticVoucher create_static_voucher(wt_static_voucher_create_params)

Create static voucher

### Example


```python
import wallet
from wallet.models.wt_static_voucher import WTStaticVoucher
from wallet.models.wt_static_voucher_create_params import WTStaticVoucherCreateParams
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
    api_instance = wallet.StaticVouchersApi(api_client)
    wt_static_voucher_create_params = wallet.WTStaticVoucherCreateParams() # WTStaticVoucherCreateParams | 

    try:
        # Create static voucher
        api_response = api_instance.create_static_voucher(wt_static_voucher_create_params)
        print("The response of StaticVouchersApi->create_static_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVouchersApi->create_static_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_static_voucher_create_params** | [**WTStaticVoucherCreateParams**](WTStaticVoucherCreateParams.md)|  | 

### Return type

[**WTStaticVoucher**](WTStaticVoucher.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Authentication Failed |  -  |
**409** | Duplicate Row Found |  -  |
**422** | Validation Failed |  -  |
**424** | Merchant Not Initialized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_static_voucher**
> bool delete_static_voucher(id)

Delete static voucher

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
    api_instance = wallet.StaticVouchersApi(api_client)
    id = None # object | 

    try:
        # Delete static voucher
        api_response = api_instance.delete_static_voucher(id)
        print("The response of StaticVouchersApi->delete_static_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVouchersApi->delete_static_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

**bool**

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
**409** | Duplicate Row Found |  -  |
**422** | Validation Failed |  -  |
**424** | Foreign Key does not exist |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_reach_stats_of_all_static_vouchers**
> ReachPerformanceStats fetch_reach_stats_of_all_static_vouchers(broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)

Get the reach statistics of all the static vouchers

### Example


```python
import wallet
from wallet.models.reach_performance_stats import ReachPerformanceStats
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
    api_instance = wallet.StaticVouchersApi(api_client)
    broadcast_scheduled_start_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    broadcast_scheduled_end_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get the reach statistics of all the static vouchers
        api_response = api_instance.fetch_reach_stats_of_all_static_vouchers(broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)
        print("The response of StaticVouchersApi->fetch_reach_stats_of_all_static_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVouchersApi->fetch_reach_stats_of_all_static_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broadcast_scheduled_start_at** | **datetime**|  | [optional] 
 **broadcast_scheduled_end_at** | **datetime**|  | [optional] 

### Return type

[**ReachPerformanceStats**](ReachPerformanceStats.md)

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

# **fetch_reach_stats_of_individual_static_voucher**
> ReachPerformanceStats fetch_reach_stats_of_individual_static_voucher(static_voucher_id, broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)

Get the reach statistics of an individual static voucher

### Example


```python
import wallet
from wallet.models.reach_performance_stats import ReachPerformanceStats
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
    api_instance = wallet.StaticVouchersApi(api_client)
    static_voucher_id = None # object | 
    broadcast_scheduled_start_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    broadcast_scheduled_end_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get the reach statistics of an individual static voucher
        api_response = api_instance.fetch_reach_stats_of_individual_static_voucher(static_voucher_id, broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)
        print("The response of StaticVouchersApi->fetch_reach_stats_of_individual_static_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVouchersApi->fetch_reach_stats_of_individual_static_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **static_voucher_id** | [**object**](.md)|  | 
 **broadcast_scheduled_start_at** | **datetime**|  | [optional] 
 **broadcast_scheduled_end_at** | **datetime**|  | [optional] 

### Return type

[**ReachPerformanceStats**](ReachPerformanceStats.md)

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

# **fetch_static_voucher**
> WTStaticVoucher fetch_static_voucher(id)

Fetch static voucher

### Example


```python
import wallet
from wallet.models.wt_static_voucher import WTStaticVoucher
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
    api_instance = wallet.StaticVouchersApi(api_client)
    id = None # object | 

    try:
        # Fetch static voucher
        api_response = api_instance.fetch_static_voucher(id)
        print("The response of StaticVouchersApi->fetch_static_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVouchersApi->fetch_static_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**WTStaticVoucher**](WTStaticVoucher.md)

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
**424** | Foreign Key does not exist |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_static_voucher**
> WTStaticVoucher update_static_voucher(id, wt_static_voucher_update_params)

Update static voucher

### Example


```python
import wallet
from wallet.models.wt_static_voucher import WTStaticVoucher
from wallet.models.wt_static_voucher_update_params import WTStaticVoucherUpdateParams
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
    api_instance = wallet.StaticVouchersApi(api_client)
    id = None # object | 
    wt_static_voucher_update_params = wallet.WTStaticVoucherUpdateParams() # WTStaticVoucherUpdateParams | 

    try:
        # Update static voucher
        api_response = api_instance.update_static_voucher(id, wt_static_voucher_update_params)
        print("The response of StaticVouchersApi->update_static_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVouchersApi->update_static_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **wt_static_voucher_update_params** | [**WTStaticVoucherUpdateParams**](WTStaticVoucherUpdateParams.md)|  | 

### Return type

[**WTStaticVoucher**](WTStaticVoucher.md)

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
**409** | Duplicate Row Found |  -  |
**422** | Validation Failed |  -  |
**424** | Foreign Key does not exist |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

