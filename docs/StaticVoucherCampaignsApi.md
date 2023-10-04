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
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.static_voucher_campaign import StaticVoucherCampaign
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
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive static voucher campaign
        api_response = api_instance.archive_static_voucher_campaign(campaign_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->archive_static_voucher_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
> InlineResponse2003 count_vouchers_loaded(campaign_id)

Count loaded vouchers

### Example


```python
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.inline_response2003 import InlineResponse2003
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Count loaded vouchers
        api_response = api_instance.count_vouchers_loaded(campaign_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->count_vouchers_loaded: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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
> InlineResponse2003 count_vouchers_redeemed(campaign_id)

Count redeemed vouchers

### Example


```python
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.inline_response2003 import InlineResponse2003
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Count redeemed vouchers
        api_response = api_instance.count_vouchers_redeemed(campaign_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->count_vouchers_redeemed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.create_static_voucher_campaign import CreateStaticVoucherCampaign
from wallet.model.auth_error import AuthError
from wallet.model.wt_static_voucher_campaign import WTStaticVoucherCampaign
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    create_static_voucher_campaign = CreateStaticVoucherCampaign(
        start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expiration_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        title="This is the title of the news article",
        notes="This is the description of the campaign",
        value_type=None,
        display_value="display_value_example",
        merchants_reference_id="merchants_reference_id_example",
        valid_only_at_pos_register_ids=[
            "valid_only_at_pos_register_ids_example",
        ],
        payment_design_id=NanoID("C"),
        bucket="s3/bucket",
        file_name="offers.csv",
        source_id=4058,
        campaign_group_id=None,
    ) # CreateStaticVoucherCampaign | 

    # example passing only required values which don't have defaults set
    try:
        # Create static voucher campaign
        api_response = api_instance.create_static_voucher_campaign(create_static_voucher_campaign)
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.create_static_voucher_campaign_with_voucher_with_csv import CreateStaticVoucherCampaignWithVoucherWithCSV
from wallet.model.auth_error import AuthError
from wallet.model.wt_static_voucher_campaign import WTStaticVoucherCampaign
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    create_static_voucher_campaign_with_voucher_with_csv = CreateStaticVoucherCampaignWithVoucherWithCSV(
        start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expiration_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        title="This is the title of the news article",
        notes="This is the description of the campaign",
        value_type=None,
        display_value="display_value_example",
        merchants_reference_id="merchants_reference_id_example",
        valid_only_at_pos_register_ids=[
            "valid_only_at_pos_register_ids_example",
        ],
        payment_design_id=NanoID("C"),
        bucket="s3/bucket",
        file_name="offers.csv",
        source_id=4058,
        campaign_group_id=None,
    ) # CreateStaticVoucherCampaignWithVoucherWithCSV | 

    # example passing only required values which don't have defaults set
    try:
        # Import static voucher campaign
        api_response = api_instance.create_static_voucher_campaign_from_csv(create_static_voucher_campaign_with_voucher_with_csv)
        pprint(api_response)
    except wallet.ApiException as e:
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
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_static_voucher_campaign import WTStaticVoucherCampaign
from wallet.model.pick_create_static_voucher_campaign_with_voucher_exclude_keyofcreate_static_voucher_campaign_with_voucher_is_active import PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherIsActive
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    body = PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherIsActive(
        title="This is the title of the news article",
        notes="This is the description of the campaign",
        value_type=None,
        display_value="display_value_example",
        merchants_reference_id="merchants_reference_id_example",
        valid_only_at_pos_register_ids=[
            "valid_only_at_pos_register_ids_example",
        ],
        payment_design_id=NanoID("C"),
        start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expiration_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_id=4058,
        member_id="MEM1001",
        offer_amount_cents=5400,
        cell_phone="+18054052344",
    ) # PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherIsActive | 

    # example passing only required values which don't have defaults set
    try:
        # Create static voucher campaign with voucher
        api_response = api_instance.create_static_voucher_campaign_with_voucher(body)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->create_static_voucher_campaign_with_voucher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherIsActive**](PickCreateStaticVoucherCampaignWithVoucherExcludeKeyofcreateStaticVoucherCampaignWithVoucherIsActive.md)|  |

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
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_static_voucher_campaign import WTStaticVoucherCampaign
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Duplicate static voucher campaign
        api_response = api_instance.duplicate_static_voucher_campaign_by_id(campaign_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->duplicate_static_voucher_campaign_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} fetch_performance_overview(campaign_id)

Fetch performance overview

### Example


```python
import time
import wallet
from wallet.api import static_voucher_campaigns_api
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
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch performance overview
        api_response = api_instance.fetch_performance_overview(campaign_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_performance_overview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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
> ReachPerformanceStats fetch_reach_stats_of_all_static_voucher_campaigns()

Get the reach statistics of all the static voucher campaigns

### Example


```python
import time
import wallet
from wallet.api import static_voucher_campaigns_api
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
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    broadcast_scheduled_start_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    broadcast_scheduled_end_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the reach statistics of all the static voucher campaigns
        api_response = api_instance.fetch_reach_stats_of_all_static_voucher_campaigns(broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)
        pprint(api_response)
    except wallet.ApiException as e:
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
> ReachPerformanceStats fetch_reach_stats_of_individual_static_voucher_campaign(static_voucher_campaign_id)

Get the reach statistics of an individual static voucher campaign

### Example


```python
import time
import wallet
from wallet.api import static_voucher_campaigns_api
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
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    static_voucher_campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    broadcast_scheduled_start_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    broadcast_scheduled_end_at = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the reach statistics of an individual static voucher campaign
        api_response = api_instance.fetch_reach_stats_of_individual_static_voucher_campaign(static_voucher_campaign_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_reach_stats_of_individual_static_voucher_campaign: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the reach statistics of an individual static voucher campaign
        api_response = api_instance.fetch_reach_stats_of_individual_static_voucher_campaign(static_voucher_campaign_id, broadcast_scheduled_start_at=broadcast_scheduled_start_at, broadcast_scheduled_end_at=broadcast_scheduled_end_at)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_reach_stats_of_individual_static_voucher_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **static_voucher_campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_static_voucher_campaign import WTStaticVoucherCampaign
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch static voucher campaign
        api_response = api_instance.fetch_static_voucher_campaign_by_id(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_static_voucher_campaign_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
> [WTStaticVoucherCampaign] fetch_static_voucher_campaigns()

Fetches all static vouchers campaigns

### Example


```python
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_static_voucher_campaign import WTStaticVoucherCampaign
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    is_archive_included = True # bool |  (optional)
    source_id = 3.14 # float |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetches all static vouchers campaigns
        api_response = api_instance.fetch_static_voucher_campaigns(is_archive_included=is_archive_included, source_id=source_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_static_voucher_campaigns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]
 **source_id** | **float**|  | [optional]

### Return type

[**[WTStaticVoucherCampaign]**](WTStaticVoucherCampaign.md)

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
> [WTStaticVoucher] fetch_static_vouchers(campaign_id)

Fetch static vouchers

### Example


```python
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
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
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch static vouchers
        api_response = api_instance.fetch_static_vouchers(campaign_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_static_vouchers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**[WTStaticVoucher]**](WTStaticVoucher.md)

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
> InlineResponse2008 fetch_static_vouchers_page(campaign_id, pagenum, pagesize)

Fetch static vouchers by page

### Example


```python
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.inline_response2008 import InlineResponse2008
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    pagenum = 3.14 # float | 
    pagesize = 3.14 # float | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch static vouchers by page
        api_response = api_instance.fetch_static_vouchers_page(campaign_id, pagenum, pagesize)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_static_vouchers_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **pagenum** | **float**|  |
 **pagesize** | **float**|  |

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

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
> [WTWalletPageView] fetch_views(campaign_id)

Fetch views

### Example


```python
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_wallet_page_view import WTWalletPageView
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
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch views
        api_response = api_instance.fetch_views(campaign_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_views: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**[WTWalletPageView]**](WTWalletPageView.md)

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
> [WTStaticVoucher] fetch_vouchers_redeemed(campaign_id)

Fetch redeemed vouchers

### Example


```python
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
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
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch redeemed vouchers
        api_response = api_instance.fetch_vouchers_redeemed(campaign_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->fetch_vouchers_redeemed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**[WTStaticVoucher]**](WTStaticVoucher.md)

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
> [VSCampaignGeneratedMessage] preview_messages(campaign_id, wt_static_voucher_campaign_preview_messages)

Preview static vouchers. This method has been deprecated. Please use /preview/page/{campaignID} for better performance.

### Example


```python
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_static_voucher_campaign_preview_messages import WTStaticVoucherCampaignPreviewMessages
from wallet.model.vs_campaign_generated_message import VSCampaignGeneratedMessage
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
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_static_voucher_campaign_preview_messages = WTStaticVoucherCampaignPreviewMessages(
        message="Hello [member]",
        locale="en-US",
        timezone="America/New_York",
    ) # WTStaticVoucherCampaignPreviewMessages | 

    # example passing only required values which don't have defaults set
    try:
        # Preview static vouchers. This method has been deprecated. Please use /preview/page/{campaignID} for better performance.
        api_response = api_instance.preview_messages(campaign_id, wt_static_voucher_campaign_preview_messages)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->preview_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **wt_static_voucher_campaign_preview_messages** | [**WTStaticVoucherCampaignPreviewMessages**](WTStaticVoucherCampaignPreviewMessages.md)|  |

### Return type

[**[VSCampaignGeneratedMessage]**](VSCampaignGeneratedMessage.md)

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
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.vs_campaign_generated_message_pagination import VSCampaignGeneratedMessagePagination
from wallet.model.wt_static_voucher_campaign_preview_messages_by_page import WTStaticVoucherCampaignPreviewMessagesByPage
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_static_voucher_campaign_preview_messages_by_page = WTStaticVoucherCampaignPreviewMessagesByPage(
        message="Hello [member]",
        locale="en-US",
        timezone="America/New_York",
        page_num=5,
        page_size=10,
    ) # WTStaticVoucherCampaignPreviewMessagesByPage | 

    # example passing only required values which don't have defaults set
    try:
        # Preview static vouchers by page
        api_response = api_instance.preview_messages_by_page(campaign_id, wt_static_voucher_campaign_preview_messages_by_page)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->preview_messages_by_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.static_voucher_campaign import StaticVoucherCampaign
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
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore static voucher campaign
        api_response = api_instance.restore_static_voucher_campaign(campaign_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->restore_static_voucher_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.static_voucher_campaign_update import StaticVoucherCampaignUpdate
from wallet.model.auth_error import AuthError
from wallet.model.wt_static_voucher_campaign import WTStaticVoucherCampaign
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    static_voucher_campaign_update = StaticVoucherCampaignUpdate(
        start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expiration_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        title="This is the title of the news article",
        notes="This is the description of the campaign",
        value_type=None,
        display_value="display_value_example",
        merchants_reference_id="merchants_reference_id_example",
        valid_only_at_pos_register_ids=[
            "valid_only_at_pos_register_ids_example",
        ],
        payment_design_id=NanoID("C"),
    ) # StaticVoucherCampaignUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update static voucher campaign
        api_response = api_instance.update_static_voucher_campaign(campaign_id, static_voucher_campaign_update)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->update_static_voucher_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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
import time
import wallet
from wallet.api import static_voucher_campaigns_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_static_voucher_campaign import WTStaticVoucherCampaign
from wallet.model.update_static_voucher_campaign_with_voucher import UpdateStaticVoucherCampaignWithVoucher
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = static_voucher_campaigns_api.StaticVoucherCampaignsApi(api_client)
    campaign_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    update_static_voucher_campaign_with_voucher = UpdateStaticVoucherCampaignWithVoucher(
        title="This is the title of the news article",
        notes="This is the description of the campaign",
        value_type=None,
        display_value="display_value_example",
        merchants_reference_id="merchants_reference_id_example",
        valid_only_at_pos_register_ids=[
            "valid_only_at_pos_register_ids_example",
        ],
        payment_design_id=NanoID("C"),
        start_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expiration_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        member_id="MEM1001",
        offer_amount_cents=5400,
        cell_phone="+18054052344",
        voucher_id=None,
    ) # UpdateStaticVoucherCampaignWithVoucher | 

    # example passing only required values which don't have defaults set
    try:
        # Update static voucher campaign with voucher
        api_response = api_instance.update_static_voucher_campaign_with_voucher(campaign_id, update_static_voucher_campaign_with_voucher)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling StaticVoucherCampaignsApi->update_static_voucher_campaign_with_voucher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

