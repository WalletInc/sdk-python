# wallet.DynamicVouchersApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_dynamic_voucher_campaign**](DynamicVouchersApi.md#archive_dynamic_voucher_campaign) | **DELETE** /v2/payment/dynamicVoucher/{campaignID} | Archive dynamic voucher campaign
[**create_dynamic_voucher**](DynamicVouchersApi.md#create_dynamic_voucher) | **POST** /v2/payment/dynamicVoucher | Create dynamic voucher
[**fetch_all_dynamic_vouchers**](DynamicVouchersApi.md#fetch_all_dynamic_vouchers) | **GET** /v2/payment/dynamicVoucher/all | Fetch all active dynamic vouchers
[**fetch_dynamic_voucher_by_id**](DynamicVouchersApi.md#fetch_dynamic_voucher_by_id) | **GET** /v2/payment/dynamicVoucher/{id} | Fetch dynamic voucher
[**fetch_dynamic_voucher_redemptions**](DynamicVouchersApi.md#fetch_dynamic_voucher_redemptions) | **GET** /v2/payment/dynamicVoucher/redemptions/{id} | Fetch redemptions
[**fetch_reach_stats_of_all_dynamic_vouchers**](DynamicVouchersApi.md#fetch_reach_stats_of_all_dynamic_vouchers) | **GET** /v2/payment/dynamicVoucher/reach/all | Get the reach statistics of all the dynamic vouchers
[**fetch_reach_stats_of_individual_dynamic_voucher**](DynamicVouchersApi.md#fetch_reach_stats_of_individual_dynamic_voucher) | **GET** /v2/payment/dynamicVoucher/reach/{dynamicVoucherID} | Get the reach statistics of an individual dynamic voucher
[**restore_dynamic_voucher_campaign**](DynamicVouchersApi.md#restore_dynamic_voucher_campaign) | **PATCH** /v2/payment/dynamicVoucher/{campaignID} | Restore dynamic voucher campaign
[**save_dynamic_voucher**](DynamicVouchersApi.md#save_dynamic_voucher) | **PUT** /v2/payment/dynamicVoucher/{id} | Update dynamic voucher


# **archive_dynamic_voucher_campaign**
> DynamicVoucher archive_dynamic_voucher_campaign(campaign_id)

Archive dynamic voucher campaign

### Example


```python
import wallet
from wallet.models.dynamic_voucher import DynamicVoucher
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
    api_instance = wallet.DynamicVouchersApi(api_client)
    campaign_id = None # object | 

    try:
        # Archive dynamic voucher campaign
        api_response = api_instance.archive_dynamic_voucher_campaign(campaign_id)
        print("The response of DynamicVouchersApi->archive_dynamic_voucher_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicVouchersApi->archive_dynamic_voucher_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 

### Return type

[**DynamicVoucher**](DynamicVoucher.md)

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

# **create_dynamic_voucher**
> WTDynamicVoucher create_dynamic_voucher(wt_dynamic_voucher_create_params)

Create dynamic voucher

### Example


```python
import wallet
from wallet.models.wt_dynamic_voucher import WTDynamicVoucher
from wallet.models.wt_dynamic_voucher_create_params import WTDynamicVoucherCreateParams
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
    api_instance = wallet.DynamicVouchersApi(api_client)
    wt_dynamic_voucher_create_params = wallet.WTDynamicVoucherCreateParams() # WTDynamicVoucherCreateParams | 

    try:
        # Create dynamic voucher
        api_response = api_instance.create_dynamic_voucher(wt_dynamic_voucher_create_params)
        print("The response of DynamicVouchersApi->create_dynamic_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicVouchersApi->create_dynamic_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_dynamic_voucher_create_params** | [**WTDynamicVoucherCreateParams**](WTDynamicVoucherCreateParams.md)|  | 

### Return type

[**WTDynamicVoucher**](WTDynamicVoucher.md)

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

# **fetch_all_dynamic_vouchers**
> List[WTDynamicVoucher] fetch_all_dynamic_vouchers(is_archive_included=is_archive_included)

Fetch all active dynamic vouchers

### Example


```python
import wallet
from wallet.models.wt_dynamic_voucher import WTDynamicVoucher
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
    api_instance = wallet.DynamicVouchersApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all active dynamic vouchers
        api_response = api_instance.fetch_all_dynamic_vouchers(is_archive_included=is_archive_included)
        print("The response of DynamicVouchersApi->fetch_all_dynamic_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicVouchersApi->fetch_all_dynamic_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[WTDynamicVoucher]**](WTDynamicVoucher.md)

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

# **fetch_dynamic_voucher_by_id**
> WTDynamicVoucher fetch_dynamic_voucher_by_id(id)

Fetch dynamic voucher

### Example


```python
import wallet
from wallet.models.wt_dynamic_voucher import WTDynamicVoucher
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
    api_instance = wallet.DynamicVouchersApi(api_client)
    id = None # object | 

    try:
        # Fetch dynamic voucher
        api_response = api_instance.fetch_dynamic_voucher_by_id(id)
        print("The response of DynamicVouchersApi->fetch_dynamic_voucher_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicVouchersApi->fetch_dynamic_voucher_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**WTDynamicVoucher**](WTDynamicVoucher.md)

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

# **fetch_dynamic_voucher_redemptions**
> List[WTDynamicVoucherRedemption] fetch_dynamic_voucher_redemptions(id)

Fetch redemptions

### Example


```python
import wallet
from wallet.models.wt_dynamic_voucher_redemption import WTDynamicVoucherRedemption
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
    api_instance = wallet.DynamicVouchersApi(api_client)
    id = None # object | 

    try:
        # Fetch redemptions
        api_response = api_instance.fetch_dynamic_voucher_redemptions(id)
        print("The response of DynamicVouchersApi->fetch_dynamic_voucher_redemptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicVouchersApi->fetch_dynamic_voucher_redemptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**List[WTDynamicVoucherRedemption]**](WTDynamicVoucherRedemption.md)

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

# **fetch_reach_stats_of_all_dynamic_vouchers**
> ReachPerformanceStats fetch_reach_stats_of_all_dynamic_vouchers(broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)

Get the reach statistics of all the dynamic vouchers

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
    api_instance = wallet.DynamicVouchersApi(api_client)
    broadcast_scheduled_start_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    broadcast_scheduled_end_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get the reach statistics of all the dynamic vouchers
        api_response = api_instance.fetch_reach_stats_of_all_dynamic_vouchers(broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)
        print("The response of DynamicVouchersApi->fetch_reach_stats_of_all_dynamic_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicVouchersApi->fetch_reach_stats_of_all_dynamic_vouchers: %s\n" % e)
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

# **fetch_reach_stats_of_individual_dynamic_voucher**
> ReachPerformanceStats fetch_reach_stats_of_individual_dynamic_voucher(dynamic_voucher_id, broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)

Get the reach statistics of an individual dynamic voucher

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
    api_instance = wallet.DynamicVouchersApi(api_client)
    dynamic_voucher_id = None # object | 
    broadcast_scheduled_start_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    broadcast_scheduled_end_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get the reach statistics of an individual dynamic voucher
        api_response = api_instance.fetch_reach_stats_of_individual_dynamic_voucher(dynamic_voucher_id, broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)
        print("The response of DynamicVouchersApi->fetch_reach_stats_of_individual_dynamic_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicVouchersApi->fetch_reach_stats_of_individual_dynamic_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_voucher_id** | [**object**](.md)|  | 
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

# **restore_dynamic_voucher_campaign**
> DynamicVoucher restore_dynamic_voucher_campaign(campaign_id)

Restore dynamic voucher campaign

### Example


```python
import wallet
from wallet.models.dynamic_voucher import DynamicVoucher
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
    api_instance = wallet.DynamicVouchersApi(api_client)
    campaign_id = None # object | 

    try:
        # Restore dynamic voucher campaign
        api_response = api_instance.restore_dynamic_voucher_campaign(campaign_id)
        print("The response of DynamicVouchersApi->restore_dynamic_voucher_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicVouchersApi->restore_dynamic_voucher_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 

### Return type

[**DynamicVoucher**](DynamicVoucher.md)

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

# **save_dynamic_voucher**
> WTDynamicVoucher save_dynamic_voucher(id, wt_dynamic_voucher_update_params)

Update dynamic voucher

### Example


```python
import wallet
from wallet.models.wt_dynamic_voucher import WTDynamicVoucher
from wallet.models.wt_dynamic_voucher_update_params import WTDynamicVoucherUpdateParams
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
    api_instance = wallet.DynamicVouchersApi(api_client)
    id = None # object | 
    wt_dynamic_voucher_update_params = wallet.WTDynamicVoucherUpdateParams() # WTDynamicVoucherUpdateParams | 

    try:
        # Update dynamic voucher
        api_response = api_instance.save_dynamic_voucher(id, wt_dynamic_voucher_update_params)
        print("The response of DynamicVouchersApi->save_dynamic_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicVouchersApi->save_dynamic_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **wt_dynamic_voucher_update_params** | [**WTDynamicVoucherUpdateParams**](WTDynamicVoucherUpdateParams.md)|  | 

### Return type

[**WTDynamicVoucher**](WTDynamicVoucher.md)

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

