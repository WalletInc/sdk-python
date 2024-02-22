# wallet.SettingsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_campaigns**](SettingsApi.md#get_active_campaigns) | **GET** /v2/settings/campaigns/active | Get active campaigns
[**get_vouchers_count**](SettingsApi.md#get_vouchers_count) | **GET** /v2/settings/vouchers/count | Get vouchers count


# **get_active_campaigns**
> List[StaticVoucherCampaign] get_active_campaigns()

Get active campaigns

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
    api_instance = wallet.SettingsApi(api_client)

    try:
        # Get active campaigns
        api_response = api_instance.get_active_campaigns()
        print("The response of SettingsApi->get_active_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_active_campaigns: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[StaticVoucherCampaign]**](StaticVoucherCampaign.md)

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

# **get_vouchers_count**
> WTCountResult get_vouchers_count()

Get vouchers count

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
    api_instance = wallet.SettingsApi(api_client)

    try:
        # Get vouchers count
        api_response = api_instance.get_vouchers_count()
        print("The response of SettingsApi->get_vouchers_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_vouchers_count: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

