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
import wallet
from wallet.models.wt_count_result import WTCountResult
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Count redeemed ad credits
        api_response = api_instance.count_ad_credits_redemptions(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->count_ad_credits_redemptions:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.wt_count_result import WTCountResult
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Count refunded ad credits
        api_response = api_instance.count_ad_credits_refunds(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->count_ad_credits_refunds:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.wt_count_result import WTCountResult
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Count dynamic voucher redemptions
        api_response = api_instance.count_dynamic_voucher_redemptions(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->count_dynamic_voucher_redemptions:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.wt_count_result import WTCountResult
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Count dynamic voucher refunds
        api_response = api_instance.count_dynamic_voucher_refunds(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->count_dynamic_voucher_refunds:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.wt_count_result import WTCountResult
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Count redeemed membership points
        api_response = api_instance.count_membership_points_redemptions(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->count_membership_points_redemptions:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.wt_count_result import WTCountResult
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Count refunded membership points
        api_response = api_instance.count_membership_points_refunds(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->count_membership_points_refunds:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.wt_count_result import WTCountResult
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Count tier redemptions
        api_response = api_instance.count_membership_tier_redemptions(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->count_membership_tier_redemptions:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.wt_count_result import WTCountResult
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Count tier refunds
        api_response = api_instance.count_membership_tier_refunds(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->count_membership_tier_refunds:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.wt_count_result import WTCountResult
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Count redeemed merchant credits
        api_response = api_instance.count_merchant_credit_redemptions(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->count_merchant_credit_redemptions:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.wt_count_result import WTCountResult
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Count refunded merchant credits
        api_response = api_instance.count_merchant_credit_refunds(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->count_merchant_credit_refunds:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.wt_count_result import WTCountResult
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Count static voucher redemptions
        api_response = api_instance.count_static_voucher_redemptions(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->count_static_voucher_redemptions:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.wt_count_result import WTCountResult
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Count static voucher refunds
        api_response = api_instance.count_static_voucher_refunds(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->count_static_voucher_refunds:\n")
        pprint(api_response)
    except Exception as e:
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
> List[Request] fetch_info_genesis_authorizations(wt_info_genesis_record_filter_parameters)

Fetch InfoGenesis authorizations

### Example


```python
import wallet
from wallet.models.request import Request
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Fetch InfoGenesis authorizations
        api_response = api_instance.fetch_info_genesis_authorizations(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_authorizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_authorizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  | 

### Return type

[**List[Request]**](Request.md)

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
import wallet
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Fetch campaign information
        api_response = api_instance.fetch_info_genesis_campaign_data(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_campaign_data:\n")
        pprint(api_response)
    except Exception as e:
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
> List[Request] fetch_info_genesis_lookup_requests(wt_info_genesis_record_filter_parameters)

Fetch InfoGenesis lookup requests

### Example


```python
import wallet
from wallet.models.request import Request
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Fetch InfoGenesis lookup requests
        api_response = api_instance.fetch_info_genesis_lookup_requests(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_lookup_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_lookup_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  | 

### Return type

[**List[Request]**](Request.md)

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
> List[Request] fetch_info_genesis_lookup_requests_errors(wt_info_genesis_lookup_request_errors)

Fetch InfoGenesis lookup request errors

### Example


```python
import wallet
from wallet.models.request import Request
from wallet.models.wt_info_genesis_lookup_request_errors import WTInfoGenesisLookupRequestErrors
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_lookup_request_errors = wallet.WTInfoGenesisLookupRequestErrors() # WTInfoGenesisLookupRequestErrors | 

    try:
        # Fetch InfoGenesis lookup request errors
        api_response = api_instance.fetch_info_genesis_lookup_requests_errors(wt_info_genesis_lookup_request_errors)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_lookup_requests_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_lookup_requests_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_lookup_request_errors** | [**WTInfoGenesisLookupRequestErrors**](WTInfoGenesisLookupRequestErrors.md)|  | 

### Return type

[**List[Request]**](Request.md)

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
> List[StaticVoucher] fetch_info_genesis_redeemed_static_vouchers(wt_info_genesis_unique_posting_ids)

Fetch redeemed static vouchers

### Example


```python
import wallet
from wallet.models.static_voucher import StaticVoucher
from wallet.models.wt_info_genesis_unique_posting_ids import WTInfoGenesisUniquePostingIDs
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_unique_posting_ids = wallet.WTInfoGenesisUniquePostingIDs() # WTInfoGenesisUniquePostingIDs | 

    try:
        # Fetch redeemed static vouchers
        api_response = api_instance.fetch_info_genesis_redeemed_static_vouchers(wt_info_genesis_unique_posting_ids)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_redeemed_static_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_redeemed_static_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_unique_posting_ids** | [**WTInfoGenesisUniquePostingIDs**](WTInfoGenesisUniquePostingIDs.md)|  | 

### Return type

[**List[StaticVoucher]**](StaticVoucher.md)

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
> List[object] fetch_info_genesis_redeemed_unique_posting_ids(start_date_time, end_date_time)

Fetch redeemed InfoGenesis unique posting IDs

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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Fetch redeemed InfoGenesis unique posting IDs
        api_response = api_instance.fetch_info_genesis_redeemed_unique_posting_ids(start_date_time, end_date_time)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_redeemed_unique_posting_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_redeemed_unique_posting_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

**List[object]**

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
> List[Request] fetch_info_genesis_redemptions(wt_info_genesis_record_filter_parameters)

Fetch InfoGenesis redemptions

### Example


```python
import wallet
from wallet.models.request import Request
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Fetch InfoGenesis redemptions
        api_response = api_instance.fetch_info_genesis_redemptions(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_redemptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_redemptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  | 

### Return type

[**List[Request]**](Request.md)

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
> List[object] fetch_info_genesis_refunded_routing_ids(start_date_time, end_date_time)

Fetch refunded InfoGenesis unique posting IDs

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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Fetch refunded InfoGenesis unique posting IDs
        api_response = api_instance.fetch_info_genesis_refunded_routing_ids(start_date_time, end_date_time)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_refunded_routing_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_refunded_routing_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

**List[object]**

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
> List[StaticVoucher] fetch_info_genesis_refunded_static_vouchers(wt_info_genesis_routing_ids)

Fetch refunded static vouchers

### Example


```python
import wallet
from wallet.models.static_voucher import StaticVoucher
from wallet.models.wt_info_genesis_routing_ids import WTInfoGenesisRoutingIDs
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_routing_ids = wallet.WTInfoGenesisRoutingIDs() # WTInfoGenesisRoutingIDs | 

    try:
        # Fetch refunded static vouchers
        api_response = api_instance.fetch_info_genesis_refunded_static_vouchers(wt_info_genesis_routing_ids)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_refunded_static_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_refunded_static_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_routing_ids** | [**WTInfoGenesisRoutingIDs**](WTInfoGenesisRoutingIDs.md)|  | 

### Return type

[**List[StaticVoucher]**](StaticVoucher.md)

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
> List[Request] fetch_info_genesis_refunds(wt_info_genesis_record_filter_parameters)

Fetch InfoGenesis refunds

### Example


```python
import wallet
from wallet.models.request import Request
from wallet.models.wt_info_genesis_record_filter_parameters import WTInfoGenesisRecordFilterParameters
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_record_filter_parameters = wallet.WTInfoGenesisRecordFilterParameters() # WTInfoGenesisRecordFilterParameters | 

    try:
        # Fetch InfoGenesis refunds
        api_response = api_instance.fetch_info_genesis_refunds(wt_info_genesis_record_filter_parameters)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_refunds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_refunds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_record_filter_parameters** | [**WTInfoGenesisRecordFilterParameters**](WTInfoGenesisRecordFilterParameters.md)|  | 

### Return type

[**List[Request]**](Request.md)

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
import wallet
from wallet.models.request import Request
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    transaction_id = 'transaction_id_example' # str | 

    try:
        # Fetch InfoGenesis request with transaction ID
        api_response = api_instance.fetch_info_genesis_request(transaction_id)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_request:\n")
        pprint(api_response)
    except Exception as e:
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
> List[Request] fetch_info_genesis_requests(wt_info_genesis_routing_ids)

Fetch InfoGenesis requests with routing IDs

### Example


```python
import wallet
from wallet.models.request import Request
from wallet.models.wt_info_genesis_routing_ids import WTInfoGenesisRoutingIDs
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_routing_ids = wallet.WTInfoGenesisRoutingIDs() # WTInfoGenesisRoutingIDs | 

    try:
        # Fetch InfoGenesis requests with routing IDs
        api_response = api_instance.fetch_info_genesis_requests(wt_info_genesis_routing_ids)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_routing_ids** | [**WTInfoGenesisRoutingIDs**](WTInfoGenesisRoutingIDs.md)|  | 

### Return type

[**List[Request]**](Request.md)

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
> List[Response] fetch_info_genesis_response_errors(start_date_time, end_date_time)

Fetch InfoGenesis response errors

### Example


```python
import wallet
from wallet.models.response import Response
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Fetch InfoGenesis response errors
        api_response = api_instance.fetch_info_genesis_response_errors(start_date_time, end_date_time)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_response_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_response_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**List[Response]**](Response.md)

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
> List[Response] fetch_info_genesis_responses(wt_info_genesis_routing_ids)

Fetch InfoGenesis responses with routing IDs

### Example


```python
import wallet
from wallet.models.response import Response
from wallet.models.wt_info_genesis_routing_ids import WTInfoGenesisRoutingIDs
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_routing_ids = wallet.WTInfoGenesisRoutingIDs() # WTInfoGenesisRoutingIDs | 

    try:
        # Fetch InfoGenesis responses with routing IDs
        api_response = api_instance.fetch_info_genesis_responses(wt_info_genesis_routing_ids)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_responses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_responses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_routing_ids** | [**WTInfoGenesisRoutingIDs**](WTInfoGenesisRoutingIDs.md)|  | 

### Return type

[**List[Response]**](Response.md)

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
> List[Request] fetch_info_genesis_transactions_with_unique_posting_ids(wt_info_genesis_unique_posting_ids)

Fetch InfoGenesis transactions

### Example


```python
import wallet
from wallet.models.request import Request
from wallet.models.wt_info_genesis_unique_posting_ids import WTInfoGenesisUniquePostingIDs
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
    api_instance = wallet.InfoGenesisReportsApi(api_client)
    wt_info_genesis_unique_posting_ids = wallet.WTInfoGenesisUniquePostingIDs() # WTInfoGenesisUniquePostingIDs | 

    try:
        # Fetch InfoGenesis transactions
        api_response = api_instance.fetch_info_genesis_transactions_with_unique_posting_ids(wt_info_genesis_unique_posting_ids)
        print("The response of InfoGenesisReportsApi->fetch_info_genesis_transactions_with_unique_posting_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoGenesisReportsApi->fetch_info_genesis_transactions_with_unique_posting_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_info_genesis_unique_posting_ids** | [**WTInfoGenesisUniquePostingIDs**](WTInfoGenesisUniquePostingIDs.md)|  | 

### Return type

[**List[Request]**](Request.md)

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

