# wallet.InfoGenesisReportsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_ad_credits_redemptions**](InfoGenesisReportsApi.md#count_ad_credits_redemptions) | **POST** /v2/pos/infogenesis/count/adCredits/redemptions | Count redeemed ad credits
[**count_ad_credits_refunds**](InfoGenesisReportsApi.md#count_ad_credits_refunds) | **POST** /v2/pos/infogenesis/count/adCredits/refunds | Count refunded ad credits
[**count_dynamic_voucher_redemptions**](InfoGenesisReportsApi.md#count_dynamic_voucher_redemptions) | **POST** /v2/pos/infogenesis/count/dynamicVoucher/redemptions | Count dynamic voucher redemptions
[**count_dynamic_voucher_refunds**](InfoGenesisReportsApi.md#count_dynamic_voucher_refunds) | **POST** /v2/pos/infogenesis/count/dynamicVoucher/refunds | Count dynamic voucher refunds
[**count_membership_points_redemptions**](InfoGenesisReportsApi.md#count_membership_points_redemptions) | **POST** /v2/pos/infogenesis/count/membershipPoints/redemptions | Count redeemed membership points
[**count_membership_points_refunds**](InfoGenesisReportsApi.md#count_membership_points_refunds) | **POST** /v2/pos/infogenesis/count/membershipPoints/refunds | Count refunded membership points
[**count_membership_tier_redemptions**](InfoGenesisReportsApi.md#count_membership_tier_redemptions) | **POST** /v2/pos/infogenesis/count/membershipTier/redemptions | Count tier redemptions
[**count_membership_tier_refunds**](InfoGenesisReportsApi.md#count_membership_tier_refunds) | **POST** /v2/pos/infogenesis/count/membershipTier/refunds | Count tier refunds
[**count_merchant_credit_redemptions**](InfoGenesisReportsApi.md#count_merchant_credit_redemptions) | **POST** /v2/pos/infogenesis/count/merchantCredit/redemptions | Count redeemed merchant credits
[**count_merchant_credit_refunds**](InfoGenesisReportsApi.md#count_merchant_credit_refunds) | **POST** /v2/pos/infogenesis/count/merchantCredit/refunds | Count refunded merchant credits
[**count_static_voucher_redemptions**](InfoGenesisReportsApi.md#count_static_voucher_redemptions) | **POST** /v2/pos/infogenesis/count/staticVoucher/redemptions | Count static voucher redemptions
[**count_static_voucher_refunds**](InfoGenesisReportsApi.md#count_static_voucher_refunds) | **POST** /v2/pos/infogenesis/count/staticVoucher/refunds | Count static voucher refunds
[**fetch_info_genesis_authorizations**](InfoGenesisReportsApi.md#fetch_info_genesis_authorizations) | **POST** /v2/pos/infogenesis/authorizations | Fetch InfoGenesis authorizations
[**fetch_info_genesis_campaign_data**](InfoGenesisReportsApi.md#fetch_info_genesis_campaign_data) | **POST** /v2/pos/infogenesis/campaign | Fetch campaign information
[**fetch_info_genesis_lookup_requests**](InfoGenesisReportsApi.md#fetch_info_genesis_lookup_requests) | **POST** /v2/pos/infogenesis/requests/lookup | Fetch InfoGenesis lookup requests
[**fetch_info_genesis_lookup_requests_errors**](InfoGenesisReportsApi.md#fetch_info_genesis_lookup_requests_errors) | **POST** /v2/pos/infogenesis/requests/lookup/errors | Fetch InfoGenesis lookup request errors
[**fetch_info_genesis_redeemed_static_vouchers**](InfoGenesisReportsApi.md#fetch_info_genesis_redeemed_static_vouchers) | **POST** /v2/pos/infogenesis/staticVouchers/redeemed | Fetch redeemed static vouchers
[**fetch_info_genesis_redeemed_unique_posting_ids**](InfoGenesisReportsApi.md#fetch_info_genesis_redeemed_unique_posting_ids) | **GET** /v2/pos/infogenesis/postingIDs/redeemed | Fetch redeemed InfoGenesis unique posting IDs
[**fetch_info_genesis_redemptions**](InfoGenesisReportsApi.md#fetch_info_genesis_redemptions) | **POST** /v2/pos/infogenesis/redemptions | Fetch InfoGenesis redemptions
[**fetch_info_genesis_refunded_routing_ids**](InfoGenesisReportsApi.md#fetch_info_genesis_refunded_routing_ids) | **POST** /v2/pos/infogenesis/routingIDs/refunded | Fetch refunded InfoGenesis unique posting IDs
[**fetch_info_genesis_refunded_static_vouchers**](InfoGenesisReportsApi.md#fetch_info_genesis_refunded_static_vouchers) | **POST** /v2/pos/infogenesis/staticVouchers/refunded | Fetch refunded static vouchers
[**fetch_info_genesis_refunds**](InfoGenesisReportsApi.md#fetch_info_genesis_refunds) | **POST** /v2/pos/infogenesis/refunds | Fetch InfoGenesis refunds
[**fetch_info_genesis_request**](InfoGenesisReportsApi.md#fetch_info_genesis_request) | **GET** /v2/pos/infogenesis/request/{transactionID} | Fetch InfoGenesis request with transaction ID
[**fetch_info_genesis_requests**](InfoGenesisReportsApi.md#fetch_info_genesis_requests) | **POST** /v2/pos/infogenesis/requests | Fetch InfoGenesis requests with routing IDs
[**fetch_info_genesis_response_errors**](InfoGenesisReportsApi.md#fetch_info_genesis_response_errors) | **GET** /v2/pos/infogenesis/responses/errors | Fetch InfoGenesis response errors
[**fetch_info_genesis_responses**](InfoGenesisReportsApi.md#fetch_info_genesis_responses) | **POST** /v2/pos/infogenesis/responses | Fetch InfoGenesis responses with routing IDs
[**fetch_info_genesis_transactions_with_unique_posting_ids**](InfoGenesisReportsApi.md#fetch_info_genesis_transactions_with_unique_posting_ids) | **POST** /v2/pos/infogenesis/transactions | Fetch InfoGenesis transactions


# **count_ad_credits_redemptions**
> WTCountResult count_ad_credits_redemptions(wt_info_genesis_record_filter_parameters)

Count redeemed ad credits

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_count_result import WTCountResult
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Count redeemed ad credits
        api_response = api_instance.count_ad_credits_redemptions(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->count_ad_credits_redemptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **count_ad_credits_refunds**
> WTCountResult count_ad_credits_refunds(wt_info_genesis_record_filter_parameters)

Count refunded ad credits

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_count_result import WTCountResult
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Count refunded ad credits
        api_response = api_instance.count_ad_credits_refunds(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->count_ad_credits_refunds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **count_dynamic_voucher_redemptions**
> WTCountResult count_dynamic_voucher_redemptions(wt_info_genesis_record_filter_parameters)

Count dynamic voucher redemptions

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_count_result import WTCountResult
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Count dynamic voucher redemptions
        api_response = api_instance.count_dynamic_voucher_redemptions(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->count_dynamic_voucher_redemptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **count_dynamic_voucher_refunds**
> WTCountResult count_dynamic_voucher_refunds(wt_info_genesis_record_filter_parameters)

Count dynamic voucher refunds

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_count_result import WTCountResult
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Count dynamic voucher refunds
        api_response = api_instance.count_dynamic_voucher_refunds(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->count_dynamic_voucher_refunds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **count_membership_points_redemptions**
> WTCountResult count_membership_points_redemptions(wt_info_genesis_record_filter_parameters)

Count redeemed membership points

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_count_result import WTCountResult
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Count redeemed membership points
        api_response = api_instance.count_membership_points_redemptions(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->count_membership_points_redemptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **count_membership_points_refunds**
> WTCountResult count_membership_points_refunds(wt_info_genesis_record_filter_parameters)

Count refunded membership points

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_count_result import WTCountResult
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Count refunded membership points
        api_response = api_instance.count_membership_points_refunds(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->count_membership_points_refunds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **count_membership_tier_redemptions**
> WTCountResult count_membership_tier_redemptions(wt_info_genesis_record_filter_parameters)

Count tier redemptions

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_count_result import WTCountResult
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Count tier redemptions
        api_response = api_instance.count_membership_tier_redemptions(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->count_membership_tier_redemptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **count_membership_tier_refunds**
> WTCountResult count_membership_tier_refunds(wt_info_genesis_record_filter_parameters)

Count tier refunds

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_count_result import WTCountResult
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Count tier refunds
        api_response = api_instance.count_membership_tier_refunds(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->count_membership_tier_refunds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **count_merchant_credit_redemptions**
> WTCountResult count_merchant_credit_redemptions(wt_info_genesis_record_filter_parameters)

Count redeemed merchant credits

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_count_result import WTCountResult
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Count redeemed merchant credits
        api_response = api_instance.count_merchant_credit_redemptions(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->count_merchant_credit_redemptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **count_merchant_credit_refunds**
> WTCountResult count_merchant_credit_refunds(wt_info_genesis_record_filter_parameters)

Count refunded merchant credits

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_count_result import WTCountResult
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Count refunded merchant credits
        api_response = api_instance.count_merchant_credit_refunds(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->count_merchant_credit_refunds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **count_static_voucher_redemptions**
> WTCountResult count_static_voucher_redemptions(wt_info_genesis_record_filter_parameters)

Count static voucher redemptions

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_count_result import WTCountResult
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Count static voucher redemptions
        api_response = api_instance.count_static_voucher_redemptions(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->count_static_voucher_redemptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **count_static_voucher_refunds**
> WTCountResult count_static_voucher_refunds(wt_info_genesis_record_filter_parameters)

Count static voucher refunds

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_count_result import WTCountResult
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Count static voucher refunds
        api_response = api_instance.count_static_voucher_refunds(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->count_static_voucher_refunds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_info_genesis_authorizations**
> [Request] fetch_info_genesis_authorizations(wt_info_genesis_record_filter_parameters)

Fetch InfoGenesis authorizations

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.request import Request
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch InfoGenesis authorizations
        api_response = api_instance.fetch_info_genesis_authorizations(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_authorizations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**[Request]**](Request.md)

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

# **fetch_info_genesis_campaign_data**
> bool fetch_info_genesis_campaign_data(wt_info_genesis_record_filter_parameters)

Fetch campaign information

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch campaign information
        api_response = api_instance.fetch_info_genesis_campaign_data(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_campaign_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

**bool**

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

# **fetch_info_genesis_lookup_requests**
> [Request] fetch_info_genesis_lookup_requests(wt_info_genesis_record_filter_parameters)

Fetch InfoGenesis lookup requests

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.request import Request
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch InfoGenesis lookup requests
        api_response = api_instance.fetch_info_genesis_lookup_requests(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_lookup_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**[Request]**](Request.md)

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

# **fetch_info_genesis_lookup_requests_errors**
> [Request] fetch_info_genesis_lookup_requests_errors(wt_info_genesis_lookup_request_errors)

Fetch InfoGenesis lookup request errors

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.request import Request
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_info_genesis_lookup_request_errors import WTInfoGenesisLookupRequestErrors
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_lookup_request_errors = WTInfoGenesisLookupRequestErrors(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
        routing_ids=[
            "routing_ids_example",
        ],
    ) # WTInfoGenesisLookupRequestErrors | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch InfoGenesis lookup request errors
        api_response = api_instance.fetch_info_genesis_lookup_requests_errors(wt_info_genesis_lookup_request_errors)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_lookup_requests_errors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_lookup_request_errors** | [**WTInfoGenesisLookupRequestErrors**](WTInfoGenesisLookupRequestErrors.md)|  |

### Return type

[**[Request]**](Request.md)

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

# **fetch_info_genesis_redeemed_static_vouchers**
> [StaticVoucher] fetch_info_genesis_redeemed_static_vouchers(wt_info_genesis_unique_posting_ids)

Fetch redeemed static vouchers

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_info_genesis_unique_posting_ids import WTInfoGenesisUniquePostingIDs
from wallet.model.static_voucher import StaticVoucher
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
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_unique_posting_ids = WTInfoGenesisUniquePostingIDs(
        unique_posting_ids=[
            "unique_posting_ids_example",
        ],
    ) # WTInfoGenesisUniquePostingIDs | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch redeemed static vouchers
        api_response = api_instance.fetch_info_genesis_redeemed_static_vouchers(wt_info_genesis_unique_posting_ids)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_redeemed_static_vouchers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_unique_posting_ids** | [**WTInfoGenesisUniquePostingIDs**](WTInfoGenesisUniquePostingIDs.md)|  |

### Return type

[**[StaticVoucher]**](StaticVoucher.md)

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

# **fetch_info_genesis_redeemed_unique_posting_ids**
> [bool, date, datetime, dict, float, int, list, str, none_type] fetch_info_genesis_redeemed_unique_posting_ids(start_date_time, end_date_time)

Fetch redeemed InfoGenesis unique posting IDs

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
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
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    start_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | 
    end_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch redeemed InfoGenesis unique posting IDs
        api_response = api_instance.fetch_info_genesis_redeemed_unique_posting_ids(start_date_time, end_date_time)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_redeemed_unique_posting_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  |
 **end_date_time** | **datetime**|  |

### Return type

**[bool, date, datetime, dict, float, int, list, str, none_type]**

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

# **fetch_info_genesis_redemptions**
> [Request] fetch_info_genesis_redemptions(wt_info_genesis_record_filter_parameters)

Fetch InfoGenesis redemptions

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.request import Request
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch InfoGenesis redemptions
        api_response = api_instance.fetch_info_genesis_redemptions(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_redemptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**[Request]**](Request.md)

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

# **fetch_info_genesis_refunded_routing_ids**
> [bool, date, datetime, dict, float, int, list, str, none_type] fetch_info_genesis_refunded_routing_ids(start_date_time, end_date_time)

Fetch refunded InfoGenesis unique posting IDs

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
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
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    start_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | 
    end_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch refunded InfoGenesis unique posting IDs
        api_response = api_instance.fetch_info_genesis_refunded_routing_ids(start_date_time, end_date_time)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_refunded_routing_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  |
 **end_date_time** | **datetime**|  |

### Return type

**[bool, date, datetime, dict, float, int, list, str, none_type]**

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

# **fetch_info_genesis_refunded_static_vouchers**
> [StaticVoucher] fetch_info_genesis_refunded_static_vouchers(wt_info_genesis_routing_ids)

Fetch refunded static vouchers

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.static_voucher import StaticVoucher
from wallet.model.auth_error import AuthError
from wallet.model.wt_info_genesis_routing_ids import WTInfoGenesisRoutingIDs
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_routing_ids = WTInfoGenesisRoutingIDs(
        routing_ids=[
            "routing_ids_example",
        ],
    ) # WTInfoGenesisRoutingIDs | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch refunded static vouchers
        api_response = api_instance.fetch_info_genesis_refunded_static_vouchers(wt_info_genesis_routing_ids)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_refunded_static_vouchers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_routing_ids** | [**WTInfoGenesisRoutingIDs**](WTInfoGenesisRoutingIDs.md)|  |

### Return type

[**[StaticVoucher]**](StaticVoucher.md)

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

# **fetch_info_genesis_refunds**
> [Request] fetch_info_genesis_refunds(wt_info_genesis_record_filter_parameters)

Fetch InfoGenesis refunds

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.request import Request
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = WTInfoGenesisRecordFilterParameters(
        start_date_time=dateutil_parser('2022-08-17T18:42:50.713Z'),
        end_date_time=dateutil_parser('2022-08-18T18:42:50.713Z'),
        selected_registers=[
            "selected_registers_example",
        ],
    ) # WTInfoGenesisRecordFilterParameters | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch InfoGenesis refunds
        api_response = api_instance.fetch_info_genesis_refunds(wt_info_genesis_record_filter_parameters)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_refunds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  |

### Return type

[**[Request]**](Request.md)

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

# **fetch_info_genesis_request**
> Request fetch_info_genesis_request(transaction_id)

Fetch InfoGenesis request with transaction ID

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.request import Request
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
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    transaction_id = "transactionID_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch InfoGenesis request with transaction ID
        api_response = api_instance.fetch_info_genesis_request(transaction_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  |

### Return type

[**Request**](Request.md)

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

# **fetch_info_genesis_requests**
> [Request] fetch_info_genesis_requests(wt_info_genesis_routing_ids)

Fetch InfoGenesis requests with routing IDs

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.request import Request
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_info_genesis_routing_ids import WTInfoGenesisRoutingIDs
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_routing_ids = WTInfoGenesisRoutingIDs(
        routing_ids=[
            "routing_ids_example",
        ],
    ) # WTInfoGenesisRoutingIDs | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch InfoGenesis requests with routing IDs
        api_response = api_instance.fetch_info_genesis_requests(wt_info_genesis_routing_ids)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_routing_ids** | [**WTInfoGenesisRoutingIDs**](WTInfoGenesisRoutingIDs.md)|  |

### Return type

[**[Request]**](Request.md)

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

# **fetch_info_genesis_response_errors**
> [Response] fetch_info_genesis_response_errors(start_date_time, end_date_time)

Fetch InfoGenesis response errors

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.response import Response
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
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    start_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | 
    end_date_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch InfoGenesis response errors
        api_response = api_instance.fetch_info_genesis_response_errors(start_date_time, end_date_time)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_response_errors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  |
 **end_date_time** | **datetime**|  |

### Return type

[**[Response]**](Response.md)

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

# **fetch_info_genesis_responses**
> [Response] fetch_info_genesis_responses(wt_info_genesis_routing_ids)

Fetch InfoGenesis responses with routing IDs

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.response import Response
from wallet.model.auth_error import AuthError
from wallet.model.wt_info_genesis_routing_ids import WTInfoGenesisRoutingIDs
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_routing_ids = WTInfoGenesisRoutingIDs(
        routing_ids=[
            "routing_ids_example",
        ],
    ) # WTInfoGenesisRoutingIDs | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch InfoGenesis responses with routing IDs
        api_response = api_instance.fetch_info_genesis_responses(wt_info_genesis_routing_ids)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_responses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_routing_ids** | [**WTInfoGenesisRoutingIDs**](WTInfoGenesisRoutingIDs.md)|  |

### Return type

[**[Response]**](Response.md)

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

# **fetch_info_genesis_transactions_with_unique_posting_ids**
> [Request] fetch_info_genesis_transactions_with_unique_posting_ids(wt_info_genesis_unique_posting_ids)

Fetch InfoGenesis transactions

### Example


```python
import time
import wallet
from wallet.api import info_genesis_reports_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.request import Request
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_info_genesis_unique_posting_ids import WTInfoGenesisUniquePostingIDs
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
    api_instance = info_genesis_reports_api.InfoGenesisReportsApi(api_client)
    wt_info_genesis_unique_posting_ids = WTInfoGenesisUniquePostingIDs(
        unique_posting_ids=[
            "unique_posting_ids_example",
        ],
    ) # WTInfoGenesisUniquePostingIDs | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch InfoGenesis transactions
        api_response = api_instance.fetch_info_genesis_transactions_with_unique_posting_ids(wt_info_genesis_unique_posting_ids)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_transactions_with_unique_posting_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_unique_posting_ids** | [**WTInfoGenesisUniquePostingIDs**](WTInfoGenesisUniquePostingIDs.md)|  |

### Return type

[**[Request]**](Request.md)

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

