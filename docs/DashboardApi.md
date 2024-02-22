# wallet.DashboardApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_dashboard_active_static_voucher_campaigns_count**](DashboardApi.md#fetch_dashboard_active_static_voucher_campaigns_count) | **GET** /v2/dashboard/count/staticVoucherCampaigns/active | Count active static voucher campaigns
[**fetch_dashboard_active_static_vouchers_count**](DashboardApi.md#fetch_dashboard_active_static_vouchers_count) | **GET** /v2/dashboard/count/staticVouchers/active | Count active static vouchers
[**fetch_dashboard_apple_wallet_subscribers_count**](DashboardApi.md#fetch_dashboard_apple_wallet_subscribers_count) | **GET** /v2/dashboard/count/appleWallet/subscribers | Count Apple Wallet Subscribers
[**fetch_dashboard_employees_count**](DashboardApi.md#fetch_dashboard_employees_count) | **GET** /v2/dashboard/count/employees | Count employees
[**fetch_dashboard_members_count**](DashboardApi.md#fetch_dashboard_members_count) | **GET** /v2/dashboard/count/members | Count members
[**fetch_dashboard_membership_tiers_count**](DashboardApi.md#fetch_dashboard_membership_tiers_count) | **GET** /v2/dashboard/count/membershipTiers | Count tiers
[**fetch_dashboard_news_articles_count**](DashboardApi.md#fetch_dashboard_news_articles_count) | **GET** /v2/dashboard/count/newsArticles | Count News Articles
[**fetch_dashboard_opt_in_lists_count**](DashboardApi.md#fetch_dashboard_opt_in_lists_count) | **GET** /v2/dashboard/count/optInLists | Count opt in lists
[**fetch_dashboard_opt_in_sources_count**](DashboardApi.md#fetch_dashboard_opt_in_sources_count) | **GET** /v2/dashboard/count/optInSources | Count opt in sources
[**fetch_dashboard_outbound_sms_count**](DashboardApi.md#fetch_dashboard_outbound_sms_count) | **GET** /v2/dashboard/count/sms/outbound | Count Outbound SMS
[**fetch_dashboard_performances_count**](DashboardApi.md#fetch_dashboard_performances_count) | **GET** /v2/dashboard/count/performances | Count Performances
[**fetch_dashboard_phone_numbers_count**](DashboardApi.md#fetch_dashboard_phone_numbers_count) | **GET** /v2/dashboard/count/phoneNumbers | Count phone numbers
[**fetch_dashboard_pos_machines_count**](DashboardApi.md#fetch_dashboard_pos_machines_count) | **GET** /v2/dashboard/count/pos/machines | Count POS Machines
[**fetch_dashboard_pos_transactions_count**](DashboardApi.md#fetch_dashboard_pos_transactions_count) | **GET** /v2/dashboard/count/pos/transactions | Count POS Transactions
[**fetch_dashboard_redemptions_count**](DashboardApi.md#fetch_dashboard_redemptions_count) | **GET** /v2/dashboard/count/pos/redemptions | Count POS redemptions
[**fetch_dashboard_refunds_count**](DashboardApi.md#fetch_dashboard_refunds_count) | **GET** /v2/dashboard/count/pos/refunds | Count POS refunds
[**fetch_dashboard_wallet_page_views_count**](DashboardApi.md#fetch_dashboard_wallet_page_views_count) | **GET** /v2/dashboard/count/wallet/pageViews | Count Wallet page views
[**fetch_dashboard_widgets_catalog**](DashboardApi.md#fetch_dashboard_widgets_catalog) | **GET** /v2/dashboard/widgets | Fetch widgets catalog


# **fetch_dashboard_active_static_voucher_campaigns_count**
> WTCountResult fetch_dashboard_active_static_voucher_campaigns_count(start_date_time, end_date_time)

Count active static voucher campaigns

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count active static voucher campaigns
        api_response = api_instance.fetch_dashboard_active_static_voucher_campaigns_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_active_static_voucher_campaigns_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_active_static_voucher_campaigns_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_active_static_vouchers_count**
> WTCountResult fetch_dashboard_active_static_vouchers_count(start_date_time, end_date_time)

Count active static vouchers

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count active static vouchers
        api_response = api_instance.fetch_dashboard_active_static_vouchers_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_active_static_vouchers_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_active_static_vouchers_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_apple_wallet_subscribers_count**
> WTCountResult fetch_dashboard_apple_wallet_subscribers_count(start_date_time, end_date_time)

Count Apple Wallet Subscribers

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count Apple Wallet Subscribers
        api_response = api_instance.fetch_dashboard_apple_wallet_subscribers_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_apple_wallet_subscribers_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_apple_wallet_subscribers_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_employees_count**
> WTCountResult fetch_dashboard_employees_count(start_date_time, end_date_time)

Count employees

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count employees
        api_response = api_instance.fetch_dashboard_employees_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_employees_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_employees_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_members_count**
> WTCountResult fetch_dashboard_members_count(start_date_time, end_date_time)

Count members

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count members
        api_response = api_instance.fetch_dashboard_members_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_members_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_members_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_membership_tiers_count**
> WTCountResult fetch_dashboard_membership_tiers_count(start_date_time, end_date_time)

Count tiers

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count tiers
        api_response = api_instance.fetch_dashboard_membership_tiers_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_membership_tiers_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_membership_tiers_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_news_articles_count**
> WTCountResult fetch_dashboard_news_articles_count(start_date_time, end_date_time)

Count News Articles

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count News Articles
        api_response = api_instance.fetch_dashboard_news_articles_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_news_articles_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_news_articles_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_opt_in_lists_count**
> WTCountResult fetch_dashboard_opt_in_lists_count(start_date_time, end_date_time)

Count opt in lists

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count opt in lists
        api_response = api_instance.fetch_dashboard_opt_in_lists_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_opt_in_lists_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_opt_in_lists_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_opt_in_sources_count**
> WTCountResult fetch_dashboard_opt_in_sources_count(start_date_time, end_date_time)

Count opt in sources

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count opt in sources
        api_response = api_instance.fetch_dashboard_opt_in_sources_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_opt_in_sources_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_opt_in_sources_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_outbound_sms_count**
> WTCountResult fetch_dashboard_outbound_sms_count(start_date_time, end_date_time)

Count Outbound SMS

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count Outbound SMS
        api_response = api_instance.fetch_dashboard_outbound_sms_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_outbound_sms_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_outbound_sms_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_performances_count**
> WTCountResult fetch_dashboard_performances_count(start_date_time, end_date_time)

Count Performances

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count Performances
        api_response = api_instance.fetch_dashboard_performances_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_performances_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_performances_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_phone_numbers_count**
> WTCountResult fetch_dashboard_phone_numbers_count(start_date_time, end_date_time)

Count phone numbers

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count phone numbers
        api_response = api_instance.fetch_dashboard_phone_numbers_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_phone_numbers_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_phone_numbers_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_pos_machines_count**
> WTCountResult fetch_dashboard_pos_machines_count(start_date_time, end_date_time)

Count POS Machines

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count POS Machines
        api_response = api_instance.fetch_dashboard_pos_machines_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_pos_machines_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_pos_machines_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_pos_transactions_count**
> WTCountResult fetch_dashboard_pos_transactions_count(start_date_time, end_date_time)

Count POS Transactions

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count POS Transactions
        api_response = api_instance.fetch_dashboard_pos_transactions_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_pos_transactions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_pos_transactions_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_redemptions_count**
> WTCountResult fetch_dashboard_redemptions_count(start_date_time, end_date_time)

Count POS redemptions

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count POS redemptions
        api_response = api_instance.fetch_dashboard_redemptions_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_redemptions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_redemptions_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_refunds_count**
> WTCountResult fetch_dashboard_refunds_count(start_date_time, end_date_time)

Count POS refunds

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        # Count POS refunds
        api_response = api_instance.fetch_dashboard_refunds_count(start_date_time, end_date_time)
        print("The response of DashboardApi->fetch_dashboard_refunds_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_refunds_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_wallet_page_views_count**
> WTCountResult fetch_dashboard_wallet_page_views_count(start_date_time, end_date_time, wallet_object_prefix=wallet_object_prefix)

Count Wallet page views

### Example


```python
import wallet
from wallet.models.wt_count_result import WTCountResult
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
    api_instance = wallet.DashboardApi(api_client)
    start_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    end_date_time = '2013-10-20T19:20:30+01:00' # datetime | 
    wallet_object_prefix = 'wallet_object_prefix_example' # str |  (optional)

    try:
        # Count Wallet page views
        api_response = api_instance.fetch_dashboard_wallet_page_views_count(start_date_time, end_date_time, wallet_object_prefix=wallet_object_prefix)
        print("The response of DashboardApi->fetch_dashboard_wallet_page_views_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_wallet_page_views_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_time** | **datetime**|  | 
 **end_date_time** | **datetime**|  | 
 **wallet_object_prefix** | **str**|  | [optional] 

### Return type

[**WTCountResult**](WTCountResult.md)

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

# **fetch_dashboard_widgets_catalog**
> List[DashboardWidget] fetch_dashboard_widgets_catalog()

Fetch widgets catalog

### Example


```python
import wallet
from wallet.models.dashboard_widget import DashboardWidget
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
    api_instance = wallet.DashboardApi(api_client)

    try:
        # Fetch widgets catalog
        api_response = api_instance.fetch_dashboard_widgets_catalog()
        print("The response of DashboardApi->fetch_dashboard_widgets_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->fetch_dashboard_widgets_catalog: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DashboardWidget]**](DashboardWidget.md)

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

