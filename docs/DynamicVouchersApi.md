# wallet.DynamicVouchersApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dynamic_voucher**](DynamicVouchersApi.md#create_dynamic_voucher) | **POST** /v2/payment/dynamicVoucher | Create dynamic voucher
[**fetch_all_dynamic_vouchers**](DynamicVouchersApi.md#fetch_all_dynamic_vouchers) | **GET** /v2/payment/dynamicVoucher/all | Fetch all active dynamic vouchers
[**fetch_dynamic_voucher_by_id**](DynamicVouchersApi.md#fetch_dynamic_voucher_by_id) | **GET** /v2/payment/dynamicVoucher/{id} | Fetch dynamic voucher
[**fetch_dynamic_voucher_redemptions**](DynamicVouchersApi.md#fetch_dynamic_voucher_redemptions) | **GET** /v2/payment/dynamicVoucher/redemptions/{id} | Fetch redemptions
[**fetch_reach_stats_of_all_dynamic_vouchers**](DynamicVouchersApi.md#fetch_reach_stats_of_all_dynamic_vouchers) | **GET** /v2/payment/dynamicVoucher/reach/all | Get the reach statistics of all the dynamic vouchers
[**fetch_reach_stats_of_individual_dynamic_voucher**](DynamicVouchersApi.md#fetch_reach_stats_of_individual_dynamic_voucher) | **GET** /v2/payment/dynamicVoucher/reach/{dynamicVoucherID} | Get the reach statistics of an individual dynamic voucher
[**save_dynamic_voucher**](DynamicVouchersApi.md#save_dynamic_voucher) | **PUT** /v2/payment/dynamicVoucher/{id} | Update dynamic voucher


# **create_dynamic_voucher**
> WTDynamicVoucher create_dynamic_voucher(wt_dynamic_voucher_create_params)

Create dynamic voucher

### Example


```python
import time
import wallet
from wallet.api import dynamic_vouchers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.merchant_not_initialized import MerchantNotInitialized
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_dynamic_voucher_create_params import WTDynamicVoucherCreateParams
from wallet.model.wt_dynamic_voucher import WTDynamicVoucher
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
    api_instance = dynamic_vouchers_api.DynamicVouchersApi(api_client)
    wt_dynamic_voucher_create_params = WTDynamicVoucherCreateParams(
        title="Thanksgiving Marketing Campaign",
        notes="This is a marketing campaign that needs to be run during the Thanksgiving week",
        payment_design_id=NanoID("C"),
        date_time_start=dateutil_parser('1970-01-01T00:00:00.00Z'),
        date_time_expiration=dateutil_parser('1970-01-01T00:00:00.00Z'),
        starting_value=250,
        max_budget=5000,
        decrease_amount=10,
        frequency=15,
        frequency_type=None,
        decrease_by=3.14,
        decrease_every=3.14,
        is_active=True,
    ) # WTDynamicVoucherCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create dynamic voucher
        api_response = api_instance.create_dynamic_voucher(wt_dynamic_voucher_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
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
> [WTDynamicVoucher] fetch_all_dynamic_vouchers()

Fetch all active dynamic vouchers

### Example


```python
import time
import wallet
from wallet.api import dynamic_vouchers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_dynamic_voucher import WTDynamicVoucher
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
    api_instance = dynamic_vouchers_api.DynamicVouchersApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all active dynamic vouchers
        api_response = api_instance.fetch_all_dynamic_vouchers(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling DynamicVouchersApi->fetch_all_dynamic_vouchers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**[WTDynamicVoucher]**](WTDynamicVoucher.md)

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
import time
import wallet
from wallet.api import dynamic_vouchers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_dynamic_voucher import WTDynamicVoucher
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
    api_instance = dynamic_vouchers_api.DynamicVouchersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch dynamic voucher
        api_response = api_instance.fetch_dynamic_voucher_by_id(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling DynamicVouchersApi->fetch_dynamic_voucher_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
> [WTDynamicVoucherRedemption] fetch_dynamic_voucher_redemptions(id)

Fetch redemptions

### Example


```python
import time
import wallet
from wallet.api import dynamic_vouchers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_dynamic_voucher_redemption import WTDynamicVoucherRedemption
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
    api_instance = dynamic_vouchers_api.DynamicVouchersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch redemptions
        api_response = api_instance.fetch_dynamic_voucher_redemptions(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling DynamicVouchersApi->fetch_dynamic_voucher_redemptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**[WTDynamicVoucherRedemption]**](WTDynamicVoucherRedemption.md)

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
> ReachPerformanceStats fetch_reach_stats_of_all_dynamic_vouchers()

Get the reach statistics of all the dynamic vouchers

### Example


```python
import time
import wallet
from wallet.api import dynamic_vouchers_api
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
    api_instance = dynamic_vouchers_api.DynamicVouchersApi(api_client)
    broadcast_scheduled_start_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    broadcast_scheduled_end_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the reach statistics of all the dynamic vouchers
        api_response = api_instance.fetch_reach_stats_of_all_dynamic_vouchers(broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)
        pprint(api_response)
    except wallet.ApiException as e:
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
> ReachPerformanceStats fetch_reach_stats_of_individual_dynamic_voucher(dynamic_voucher_id)

Get the reach statistics of an individual dynamic voucher

### Example


```python
import time
import wallet
from wallet.api import dynamic_vouchers_api
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
    api_instance = dynamic_vouchers_api.DynamicVouchersApi(api_client)
    dynamic_voucher_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    broadcast_scheduled_start_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    broadcast_scheduled_end_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the reach statistics of an individual dynamic voucher
        api_response = api_instance.fetch_reach_stats_of_individual_dynamic_voucher(dynamic_voucher_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling DynamicVouchersApi->fetch_reach_stats_of_individual_dynamic_voucher: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the reach statistics of an individual dynamic voucher
        api_response = api_instance.fetch_reach_stats_of_individual_dynamic_voucher(dynamic_voucher_id, broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling DynamicVouchersApi->fetch_reach_stats_of_individual_dynamic_voucher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_voucher_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

# **save_dynamic_voucher**
> WTDynamicVoucher save_dynamic_voucher(id, wt_dynamic_voucher_update_params)

Update dynamic voucher

### Example


```python
import time
import wallet
from wallet.api import dynamic_vouchers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.foreign_key_does_not_exist import ForeignKeyDoesNotExist
from wallet.model.wt_dynamic_voucher import WTDynamicVoucher
from wallet.model.auth_error import AuthError
from wallet.model.duplicate_row_found import DuplicateRowFound
from wallet.model.wt_dynamic_voucher_update_params import WTDynamicVoucherUpdateParams
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dynamic_vouchers_api.DynamicVouchersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_dynamic_voucher_update_params = WTDynamicVoucherUpdateParams(
        title="Thanksgiving Marketing Campaign",
        notes="This is a marketing campaign that needs to be run during the Thanksgiving week",
        payment_design_id=NanoID("C"),
        date_time_start=dateutil_parser('1970-01-01T00:00:00.00Z'),
        date_time_expiration=dateutil_parser('1970-01-01T00:00:00.00Z'),
        starting_value=250,
        max_budget=5000,
        decrease_amount=10,
        frequency=15,
        frequency_type=None,
        decrease_by=3.14,
        decrease_every=3.14,
        is_active=True,
    ) # WTDynamicVoucherUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update dynamic voucher
        api_response = api_instance.save_dynamic_voucher(id, wt_dynamic_voucher_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling DynamicVouchersApi->save_dynamic_voucher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

