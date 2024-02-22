# wallet.StaticVoucherCampaignsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_static_voucher_campaign**](StaticVoucherCampaignsApi.md#archive_static_voucher_campaign) | **DELETE** /v2/payment/staticVoucherCampaign/{campaignID} | Archive static voucher campaign
[**count_vouchers_loaded**](StaticVoucherCampaignsApi.md#count_vouchers_loaded) | **GET** /v2/payment/staticVoucherCampaign/count/vouchers/loaded/{campaignID} | Count loaded vouchers
[**count_vouchers_redeemed**](StaticVoucherCampaignsApi.md#count_vouchers_redeemed) | **GET** /v2/payment/staticVoucherCampaign/count/vouchers/redeemed/{campaignID} | Count redeemed vouchers
[**create_static_voucher_campaign**](StaticVoucherCampaignsApi.md#create_static_voucher_campaign) | **POST** /v2/payment/staticVoucherCampaign | Create static voucher campaign
[**create_static_voucher_campaign_from_csv**](StaticVoucherCampaignsApi.md#create_static_voucher_campaign_from_csv) | **POST** /v2/payment/staticVoucherCampaign/csv | Import static voucher campaign
[**create_static_voucher_campaign_with_voucher**](StaticVoucherCampaignsApi.md#create_static_voucher_campaign_with_voucher) | **POST** /v2/payment/staticVoucherCampaign/voucher | Create static voucher campaign with voucher
[**duplicate_static_voucher_campaign_by_id**](StaticVoucherCampaignsApi.md#duplicate_static_voucher_campaign_by_id) | **POST** /v2/payment/staticVoucherCampaign/duplicate/{campaignID} | Duplicate static voucher campaign
[**fetch_performance_overview**](StaticVoucherCampaignsApi.md#fetch_performance_overview) | **GET** /v2/payment/staticVoucherCampaign/overview/performance/{campaignID} | Fetch performance overview
[**fetch_reach_stats_of_all_static_voucher_campaigns**](StaticVoucherCampaignsApi.md#fetch_reach_stats_of_all_static_voucher_campaigns) | **GET** /v2/payment/staticVoucherCampaign/reach/all | Get the reach statistics of all the static voucher campaigns
[**fetch_reach_stats_of_individual_static_voucher_campaign**](StaticVoucherCampaignsApi.md#fetch_reach_stats_of_individual_static_voucher_campaign) | **GET** /v2/payment/staticVoucherCampaign/reach/{staticVoucherCampaignID} | Get the reach statistics of an individual static voucher campaign
[**fetch_static_voucher_campaign_by_id**](StaticVoucherCampaignsApi.md#fetch_static_voucher_campaign_by_id) | **GET** /v2/payment/staticVoucherCampaign/{id} | Fetch static voucher campaign
[**fetch_static_voucher_campaigns**](StaticVoucherCampaignsApi.md#fetch_static_voucher_campaigns) | **GET** /v2/payment/staticVoucherCampaign/all | Fetches all static vouchers campaigns
[**fetch_static_vouchers**](StaticVoucherCampaignsApi.md#fetch_static_vouchers) | **GET** /v2/payment/staticVoucherCampaign/staticVouchers/{campaignID} | Fetch static vouchers
[**fetch_static_vouchers_page**](StaticVoucherCampaignsApi.md#fetch_static_vouchers_page) | **GET** /v2/payment/staticVoucherCampaign/staticVouchers/page/{campaignID} | Fetch static vouchers by page
[**fetch_views**](StaticVoucherCampaignsApi.md#fetch_views) | **GET** /v2/payment/staticVoucherCampaign/views/{campaignID} | Fetch views
[**fetch_vouchers_redeemed**](StaticVoucherCampaignsApi.md#fetch_vouchers_redeemed) | **GET** /v2/payment/staticVoucherCampaign/vouchers/redeemed/{campaignID} | Fetch redeemed vouchers
[**preview_messages**](StaticVoucherCampaignsApi.md#preview_messages) | **PUT** /v2/payment/staticVoucherCampaign/preview/{campaignID} | Preview static vouchers. This method has been deprecated. Please use /preview/page/{campaignID} for better performance.
[**preview_messages_by_page**](StaticVoucherCampaignsApi.md#preview_messages_by_page) | **PUT** /v2/payment/staticVoucherCampaign/preview/page/{campaignID} | Preview static vouchers by page
[**restore_static_voucher_campaign**](StaticVoucherCampaignsApi.md#restore_static_voucher_campaign) | **PATCH** /v2/payment/staticVoucherCampaign/{campaignID} | Restore static voucher campaign
[**update_static_voucher_campaign**](StaticVoucherCampaignsApi.md#update_static_voucher_campaign) | **PUT** /v2/payment/staticVoucherCampaign/{campaignID} | Update static voucher campaign
[**update_static_voucher_campaign_with_voucher**](StaticVoucherCampaignsApi.md#update_static_voucher_campaign_with_voucher) | **PUT** /v2/payment/staticVoucherCampaign/voucher/{campaignID} | Update static voucher campaign with voucher


# **archive_static_voucher_campaign**
> StaticVoucherCampaign archive_static_voucher_campaign(campaign_id)

Archive static voucher campaign

### Example


```python
import wallet
from wallet.models.static_voucher_campaign import StaticVoucherCampaign
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # object | 

    try:
        # Archive static voucher campaign
        api_response = api_instance.archive_static_voucher_campaign(campaign_id)
        print("The response of StaticVoucherCampaignsApi->archive_static_voucher_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->archive_static_voucher_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 

### Return type

[**StaticVoucherCampaign**](StaticVoucherCampaign.md)

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

# **count_vouchers_loaded**
> FetchMembersCount200Response count_vouchers_loaded(campaign_id)

Count loaded vouchers

### Example


```python
import wallet
from wallet.models.fetch_members_count200_response import FetchMembersCount200Response
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # object | 

    try:
        # Count loaded vouchers
        api_response = api_instance.count_vouchers_loaded(campaign_id)
        print("The response of StaticVoucherCampaignsApi->count_vouchers_loaded:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->count_vouchers_loaded: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 

### Return type

[**FetchMembersCount200Response**](FetchMembersCount200Response.md)

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

# **count_vouchers_redeemed**
> FetchMembersCount200Response count_vouchers_redeemed(campaign_id)

Count redeemed vouchers

### Example


```python
import wallet
from wallet.models.fetch_members_count200_response import FetchMembersCount200Response
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # object | 

    try:
        # Count redeemed vouchers
        api_response = api_instance.count_vouchers_redeemed(campaign_id)
        print("The response of StaticVoucherCampaignsApi->count_vouchers_redeemed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->count_vouchers_redeemed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 

### Return type

[**FetchMembersCount200Response**](FetchMembersCount200Response.md)

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

# **create_static_voucher_campaign**
> WTStaticVoucherCampaign create_static_voucher_campaign(create_static_voucher_campaign)

Create static voucher campaign

### Example


```python
import wallet
from wallet.models.create_static_voucher_campaign import CreateStaticVoucherCampaign
from wallet.models.wt_static_voucher_campaign import WTStaticVoucherCampaign
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    create_static_voucher_campaign = wallet.CreateStaticVoucherCampaign() # CreateStaticVoucherCampaign | 

    try:
        # Create static voucher campaign
        api_response = api_instance.create_static_voucher_campaign(create_static_voucher_campaign)
        print("The response of StaticVoucherCampaignsApi->create_static_voucher_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->create_static_voucher_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_static_voucher_campaign** | [**CreateStaticVoucherCampaign**](CreateStaticVoucherCampaign.md)|  | 

### Return type

[**WTStaticVoucherCampaign**](WTStaticVoucherCampaign.md)

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

# **create_static_voucher_campaign_from_csv**
> WTStaticVoucherCampaign create_static_voucher_campaign_from_csv(create_static_voucher_campaign_with_voucher_with_csv)

Import static voucher campaign

### Example


```python
import wallet
from wallet.models.create_static_voucher_campaign_with_voucher_with_csv import CreateStaticVoucherCampaignWithVoucherWithCSV
from wallet.models.wt_static_voucher_campaign import WTStaticVoucherCampaign
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    create_static_voucher_campaign_with_voucher_with_csv = wallet.CreateStaticVoucherCampaignWithVoucherWithCSV() # CreateStaticVoucherCampaignWithVoucherWithCSV | 

    try:
        # Import static voucher campaign
        api_response = api_instance.create_static_voucher_campaign_from_csv(create_static_voucher_campaign_with_voucher_with_csv)
        print("The response of StaticVoucherCampaignsApi->create_static_voucher_campaign_from_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->create_static_voucher_campaign_from_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_static_voucher_campaign_with_voucher_with_csv** | [**CreateStaticVoucherCampaignWithVoucherWithCSV**](CreateStaticVoucherCampaignWithVoucherWithCSV.md)|  | 

### Return type

[**WTStaticVoucherCampaign**](WTStaticVoucherCampaign.md)

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

# **create_static_voucher_campaign_with_voucher**
> WTStaticVoucherCampaign create_static_voucher_campaign_with_voucher(body)

Create static voucher campaign with voucher

### Example


```python
import wallet
from wallet.models.pick_create_static_voucher_campaign_with_voucher_exclude_keyofcreate_static_voucher_campaign_with_voucher_is_active import PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherIsActive
from wallet.models.wt_static_voucher_campaign import WTStaticVoucherCampaign
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    body = wallet.PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherIsActive() # PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherIsActive | 

    try:
        # Create static voucher campaign with voucher
        api_response = api_instance.create_static_voucher_campaign_with_voucher(body)
        print("The response of StaticVoucherCampaignsApi->create_static_voucher_campaign_with_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->create_static_voucher_campaign_with_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherIsActive**|  | 

### Return type

[**WTStaticVoucherCampaign**](WTStaticVoucherCampaign.md)

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

# **duplicate_static_voucher_campaign_by_id**
> WTStaticVoucherCampaign duplicate_static_voucher_campaign_by_id(campaign_id)

Duplicate static voucher campaign

### Example


```python
import wallet
from wallet.models.wt_static_voucher_campaign import WTStaticVoucherCampaign
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # object | 

    try:
        # Duplicate static voucher campaign
        api_response = api_instance.duplicate_static_voucher_campaign_by_id(campaign_id)
        print("The response of StaticVoucherCampaignsApi->duplicate_static_voucher_campaign_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->duplicate_static_voucher_campaign_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 

### Return type

[**WTStaticVoucherCampaign**](WTStaticVoucherCampaign.md)

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

# **fetch_performance_overview**
> object fetch_performance_overview(campaign_id)

Fetch performance overview

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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # object | 

    try:
        # Fetch performance overview
        api_response = api_instance.fetch_performance_overview(campaign_id)
        print("The response of StaticVoucherCampaignsApi->fetch_performance_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_performance_overview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 

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

# **fetch_reach_stats_of_all_static_voucher_campaigns**
> ReachPerformanceStats fetch_reach_stats_of_all_static_voucher_campaigns(broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)

Get the reach statistics of all the static voucher campaigns

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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    broadcast_scheduled_start_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    broadcast_scheduled_end_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get the reach statistics of all the static voucher campaigns
        api_response = api_instance.fetch_reach_stats_of_all_static_voucher_campaigns(broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)
        print("The response of StaticVoucherCampaignsApi->fetch_reach_stats_of_all_static_voucher_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_reach_stats_of_all_static_voucher_campaigns: %s\n" % e)
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

# **fetch_reach_stats_of_individual_static_voucher_campaign**
> ReachPerformanceStats fetch_reach_stats_of_individual_static_voucher_campaign(static_voucher_campaign_id, broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)

Get the reach statistics of an individual static voucher campaign

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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    static_voucher_campaign_id = None # object | 
    broadcast_scheduled_start_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    broadcast_scheduled_end_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get the reach statistics of an individual static voucher campaign
        api_response = api_instance.fetch_reach_stats_of_individual_static_voucher_campaign(static_voucher_campaign_id, broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)
        print("The response of StaticVoucherCampaignsApi->fetch_reach_stats_of_individual_static_voucher_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_reach_stats_of_individual_static_voucher_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **static_voucher_campaign_id** | [**object**](.md)|  | 
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

# **fetch_static_voucher_campaign_by_id**
> WTStaticVoucherCampaign fetch_static_voucher_campaign_by_id(id)

Fetch static voucher campaign

### Example


```python
import wallet
from wallet.models.wt_static_voucher_campaign import WTStaticVoucherCampaign
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    id = None # object | 

    try:
        # Fetch static voucher campaign
        api_response = api_instance.fetch_static_voucher_campaign_by_id(id)
        print("The response of StaticVoucherCampaignsApi->fetch_static_voucher_campaign_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_static_voucher_campaign_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**WTStaticVoucherCampaign**](WTStaticVoucherCampaign.md)

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

# **fetch_static_voucher_campaigns**
> List[WTStaticVoucherCampaign] fetch_static_voucher_campaigns(is_archive_included=is_archive_included, source_id=source_id)

Fetches all static vouchers campaigns

### Example


```python
import wallet
from wallet.models.wt_static_voucher_campaign import WTStaticVoucherCampaign
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    is_archive_included = True # bool |  (optional)
    source_id = 3.4 # float |  (optional)

    try:
        # Fetches all static vouchers campaigns
        api_response = api_instance.fetch_static_voucher_campaigns(is_archive_included=is_archive_included, source_id=source_id)
        print("The response of StaticVoucherCampaignsApi->fetch_static_voucher_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_static_voucher_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 
 **source_id** | **float**|  | [optional] 

### Return type

[**List[WTStaticVoucherCampaign]**](WTStaticVoucherCampaign.md)

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

# **fetch_static_vouchers**
> List[WTStaticVoucher] fetch_static_vouchers(campaign_id)

Fetch static vouchers

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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # object | 

    try:
        # Fetch static vouchers
        api_response = api_instance.fetch_static_vouchers(campaign_id)
        print("The response of StaticVoucherCampaignsApi->fetch_static_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_static_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 

### Return type

[**List[WTStaticVoucher]**](WTStaticVoucher.md)

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

# **fetch_static_vouchers_page**
> FetchStaticVouchersPage200Response fetch_static_vouchers_page(campaign_id, pagenum, pagesize)

Fetch static vouchers by page

### Example


```python
import wallet
from wallet.models.fetch_static_vouchers_page200_response import FetchStaticVouchersPage200Response
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # object | 
    pagenum = 3.4 # float | 
    pagesize = 3.4 # float | 

    try:
        # Fetch static vouchers by page
        api_response = api_instance.fetch_static_vouchers_page(campaign_id, pagenum, pagesize)
        print("The response of StaticVoucherCampaignsApi->fetch_static_vouchers_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_static_vouchers_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 
 **pagenum** | **float**|  | 
 **pagesize** | **float**|  | 

### Return type

[**FetchStaticVouchersPage200Response**](FetchStaticVouchersPage200Response.md)

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

# **fetch_views**
> List[WTWalletPageView] fetch_views(campaign_id)

Fetch views

### Example


```python
import wallet
from wallet.models.wt_wallet_page_view import WTWalletPageView
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # object | 

    try:
        # Fetch views
        api_response = api_instance.fetch_views(campaign_id)
        print("The response of StaticVoucherCampaignsApi->fetch_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 

### Return type

[**List[WTWalletPageView]**](WTWalletPageView.md)

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

# **fetch_vouchers_redeemed**
> List[WTStaticVoucher] fetch_vouchers_redeemed(campaign_id)

Fetch redeemed vouchers

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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # object | 

    try:
        # Fetch redeemed vouchers
        api_response = api_instance.fetch_vouchers_redeemed(campaign_id)
        print("The response of StaticVoucherCampaignsApi->fetch_vouchers_redeemed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_vouchers_redeemed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 

### Return type

[**List[WTStaticVoucher]**](WTStaticVoucher.md)

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

# **preview_messages**
> List[VSCampaignGeneratedMessage] preview_messages(campaign_id, wt_static_voucher_campaign_preview_messages)

Preview static vouchers. This method has been deprecated. Please use /preview/page/{campaignID} for better performance.

### Example


```python
import wallet
from wallet.models.vs_campaign_generated_message import VSCampaignGeneratedMessage
from wallet.models.wt_static_voucher_campaign_preview_messages import WTStaticVoucherCampaignPreviewMessages
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # object | 
    wt_static_voucher_campaign_preview_messages = wallet.WTStaticVoucherCampaignPreviewMessages() # WTStaticVoucherCampaignPreviewMessages | 

    try:
        # Preview static vouchers. This method has been deprecated. Please use /preview/page/{campaignID} for better performance.
        api_response = api_instance.preview_messages(campaign_id, wt_static_voucher_campaign_preview_messages)
        print("The response of StaticVoucherCampaignsApi->preview_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->preview_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 
 **wt_static_voucher_campaign_preview_messages** | [**WTStaticVoucherCampaignPreviewMessages**](WTStaticVoucherCampaignPreviewMessages.md)|  | 

### Return type

[**List[VSCampaignGeneratedMessage]**](VSCampaignGeneratedMessage.md)

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

# **preview_messages_by_page**
> VSCampaignGeneratedMessagePagination preview_messages_by_page(campaign_id, wt_static_voucher_campaign_preview_messages_by_page)

Preview static vouchers by page

### Example


```python
import wallet
from wallet.models.vs_campaign_generated_message_pagination import VSCampaignGeneratedMessagePagination
from wallet.models.wt_static_voucher_campaign_preview_messages_by_page import WTStaticVoucherCampaignPreviewMessagesByPage
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # object | 
    wt_static_voucher_campaign_preview_messages_by_page = wallet.WTStaticVoucherCampaignPreviewMessagesByPage() # WTStaticVoucherCampaignPreviewMessagesByPage | 

    try:
        # Preview static vouchers by page
        api_response = api_instance.preview_messages_by_page(campaign_id, wt_static_voucher_campaign_preview_messages_by_page)
        print("The response of StaticVoucherCampaignsApi->preview_messages_by_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->preview_messages_by_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 
 **wt_static_voucher_campaign_preview_messages_by_page** | [**WTStaticVoucherCampaignPreviewMessagesByPage**](WTStaticVoucherCampaignPreviewMessagesByPage.md)|  | 

### Return type

[**VSCampaignGeneratedMessagePagination**](VSCampaignGeneratedMessagePagination.md)

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

# **restore_static_voucher_campaign**
> StaticVoucherCampaign restore_static_voucher_campaign(campaign_id)

Restore static voucher campaign

### Example


```python
import wallet
from wallet.models.static_voucher_campaign import StaticVoucherCampaign
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # object | 

    try:
        # Restore static voucher campaign
        api_response = api_instance.restore_static_voucher_campaign(campaign_id)
        print("The response of StaticVoucherCampaignsApi->restore_static_voucher_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->restore_static_voucher_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 

### Return type

[**StaticVoucherCampaign**](StaticVoucherCampaign.md)

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

# **update_static_voucher_campaign**
> WTStaticVoucherCampaign update_static_voucher_campaign(campaign_id, static_voucher_campaign_update)

Update static voucher campaign

### Example


```python
import wallet
from wallet.models.static_voucher_campaign_update import StaticVoucherCampaignUpdate
from wallet.models.wt_static_voucher_campaign import WTStaticVoucherCampaign
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # object | 
    static_voucher_campaign_update = wallet.StaticVoucherCampaignUpdate() # StaticVoucherCampaignUpdate | 

    try:
        # Update static voucher campaign
        api_response = api_instance.update_static_voucher_campaign(campaign_id, static_voucher_campaign_update)
        print("The response of StaticVoucherCampaignsApi->update_static_voucher_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->update_static_voucher_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 
 **static_voucher_campaign_update** | [**StaticVoucherCampaignUpdate**](StaticVoucherCampaignUpdate.md)|  | 

### Return type

[**WTStaticVoucherCampaign**](WTStaticVoucherCampaign.md)

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

# **update_static_voucher_campaign_with_voucher**
> WTStaticVoucherCampaign update_static_voucher_campaign_with_voucher(campaign_id, update_static_voucher_campaign_with_voucher)

Update static voucher campaign with voucher

### Example


```python
import wallet
from wallet.models.update_static_voucher_campaign_with_voucher import UpdateStaticVoucherCampaignWithVoucher
from wallet.models.wt_static_voucher_campaign import WTStaticVoucherCampaign
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
    api_instance = wallet.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # object | 
    update_static_voucher_campaign_with_voucher = wallet.UpdateStaticVoucherCampaignWithVoucher() # UpdateStaticVoucherCampaignWithVoucher | 

    try:
        # Update static voucher campaign with voucher
        api_response = api_instance.update_static_voucher_campaign_with_voucher(campaign_id, update_static_voucher_campaign_with_voucher)
        print("The response of StaticVoucherCampaignsApi->update_static_voucher_campaign_with_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignsApi->update_static_voucher_campaign_with_voucher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | [**object**](.md)|  | 
 **update_static_voucher_campaign_with_voucher** | [**UpdateStaticVoucherCampaignWithVoucher**](UpdateStaticVoucherCampaignWithVoucher.md)|  | 

### Return type

[**WTStaticVoucherCampaign**](WTStaticVoucherCampaign.md)

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

