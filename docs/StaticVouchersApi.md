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
import time
import wallet
from wallet.api import static_vouchers_api
from wallet.model.wt_static_voucher_create_params import WTStaticVoucherCreateParams
from wallet.model.internal_server_error import InternalServerError
from wallet.model.merchant_not_initialized import MerchantNotInitialized
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.duplicate_row_found import DuplicateRowFound
from wallet.model.wt_static_voucher import WTStaticVoucher
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_vouchers_api.StaticVouchersApi(api_client)
    wt_static_voucher_create_params = WTStaticVoucherCreateParams(
        offer_amount_cents=5400,
        member_id="MEM1001",
        cell_phone="+18054052344",
        campaign_id=None,
    ) # WTStaticVoucherCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create static voucher
        api_response = api_instance.create_static_voucher(wt_static_voucher_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import static_vouchers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.foreign_key_does_not_exist import ForeignKeyDoesNotExist
from wallet.model.auth_error import AuthError
from wallet.model.duplicate_row_found import DuplicateRowFound
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_vouchers_api.StaticVouchersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Delete static voucher
        api_response = api_instance.delete_static_voucher(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVouchersApi->delete_static_voucher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
> ReachPerformanceStats fetch_reach_stats_of_all_static_vouchers()

Get the reach statistics of all the static vouchers

### Example


```python
import time
import wallet
from wallet.api import static_vouchers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.reach_performance_stats import ReachPerformanceStats
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_vouchers_api.StaticVouchersApi(api_client)
    broadcast_scheduled_start_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    broadcast_scheduled_end_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the reach statistics of all the static vouchers
        api_response = api_instance.fetch_reach_stats_of_all_static_vouchers(broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)
        pprint(api_response)
    except wallet.ApiException as e:
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
> ReachPerformanceStats fetch_reach_stats_of_individual_static_voucher(static_voucher_id)

Get the reach statistics of an individual static voucher

### Example


```python
import time
import wallet
from wallet.api import static_vouchers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.reach_performance_stats import ReachPerformanceStats
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_vouchers_api.StaticVouchersApi(api_client)
    static_voucher_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    broadcast_scheduled_start_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    broadcast_scheduled_end_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the reach statistics of an individual static voucher
        api_response = api_instance.fetch_reach_stats_of_individual_static_voucher(static_voucher_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVouchersApi->fetch_reach_stats_of_individual_static_voucher: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the reach statistics of an individual static voucher
        api_response = api_instance.fetch_reach_stats_of_individual_static_voucher(static_voucher_id, broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVouchersApi->fetch_reach_stats_of_individual_static_voucher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **static_voucher_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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
import time
import wallet
from wallet.api import static_vouchers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.foreign_key_does_not_exist import ForeignKeyDoesNotExist
from wallet.model.auth_error import AuthError
from wallet.model.wt_static_voucher import WTStaticVoucher
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_vouchers_api.StaticVouchersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch static voucher
        api_response = api_instance.fetch_static_voucher(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVouchersApi->fetch_static_voucher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import static_vouchers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.foreign_key_does_not_exist import ForeignKeyDoesNotExist
from wallet.model.auth_error import AuthError
from wallet.model.wt_static_voucher_update_params import WTStaticVoucherUpdateParams
from wallet.model.duplicate_row_found import DuplicateRowFound
from wallet.model.wt_static_voucher import WTStaticVoucher
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_vouchers_api.StaticVouchersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_static_voucher_update_params = WTStaticVoucherUpdateParams(
        member_id="MEM1001",
        offer_amount_cents=5400,
        cell_phone="+18054052344",
    ) # WTStaticVoucherUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update static voucher
        api_response = api_instance.update_static_voucher(id, wt_static_voucher_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVouchersApi->update_static_voucher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

