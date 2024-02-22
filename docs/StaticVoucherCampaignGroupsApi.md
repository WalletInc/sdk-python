# wallet.StaticVoucherCampaignGroupsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_static_voucher_campaign_groups**](StaticVoucherCampaignGroupsApi.md#fetch_static_voucher_campaign_groups) | **GET** /v2/payment/staticVoucherCampaignGroups/campaigns/{campaignsGroupID} | Fetch all campaigns


# **fetch_static_voucher_campaign_groups**
> object fetch_static_voucher_campaign_groups(campaigns_group_id)

Fetch all campaigns

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
    api_instance = wallet.StaticVoucherCampaignGroupsApi(api_client)
    campaigns_group_id = None # object | 

    try:
        # Fetch all campaigns
        api_response = api_instance.fetch_static_voucher_campaign_groups(campaigns_group_id)
        print("The response of StaticVoucherCampaignGroupsApi->fetch_static_voucher_campaign_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticVoucherCampaignGroupsApi->fetch_static_voucher_campaign_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaigns_group_id** | [**object**](.md)|  | 

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
**409** | Duplicate Row Found |  -  |
**422** | Validation Failed |  -  |
**424** | Foreign Key does not exist |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

