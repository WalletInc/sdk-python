# wallet.MembershipTiersApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_membership_tier**](MembershipTiersApi.md#archive_membership_tier) | **DELETE** /v2/membership/tier/{id} | Archive Membership Tier
[**create_membership_tier**](MembershipTiersApi.md#create_membership_tier) | **POST** /v2/membership/tier | Create Membership Tier
[**fetch_all_membership_tiers**](MembershipTiersApi.md#fetch_all_membership_tiers) | **GET** /v2/membership/tier/all | Get all Membership Tiers
[**fetch_all_membership_tiers_with_member_count**](MembershipTiersApi.md#fetch_all_membership_tiers_with_member_count) | **GET** /v2/membership/tier/allWithMemberCount | Get all Membership Tiers with member count
[**fetch_membership_tier_by_id**](MembershipTiersApi.md#fetch_membership_tier_by_id) | **GET** /v2/membership/tier/{id} | Get Membership Tier
[**fetch_membership_tier_history_log**](MembershipTiersApi.md#fetch_membership_tier_history_log) | **POST** /v2/membership/tier/history/log | Get Membership Tier history
[**fetch_membership_tier_redemption_log**](MembershipTiersApi.md#fetch_membership_tier_redemption_log) | **POST** /v2/membership/tier/redemption/log | Get Membership Tier redemption log
[**restore_membership_tier**](MembershipTiersApi.md#restore_membership_tier) | **PATCH** /v2/membership/tier/{id} | Restore Membership Tier
[**update_membership_tier**](MembershipTiersApi.md#update_membership_tier) | **PUT** /v2/membership/tier/{id} | Update Membership Tier


# **archive_membership_tier**
> WTMembershipTier archive_membership_tier(id)

Archive Membership Tier

### Example


```python
import wallet
from wallet.models.wt_membership_tier import WTMembershipTier
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
    api_instance = wallet.MembershipTiersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive Membership Tier
        api_response = api_instance.archive_membership_tier(id)
        print("The response of MembershipTiersApi->archive_membership_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipTiersApi->archive_membership_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMembershipTier**](WTMembershipTier.md)

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

# **create_membership_tier**
> WTMembershipTier create_membership_tier(wt_membership_tier_creation_params)

Create Membership Tier

### Example


```python
import wallet
from wallet.models.wt_membership_tier import WTMembershipTier
from wallet.models.wt_membership_tier_creation_params import WTMembershipTierCreationParams
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
    api_instance = wallet.MembershipTiersApi(api_client)
    wt_membership_tier_creation_params = wallet.WTMembershipTierCreationParams() # WTMembershipTierCreationParams | 

    try:
        # Create Membership Tier
        api_response = api_instance.create_membership_tier(wt_membership_tier_creation_params)
        print("The response of MembershipTiersApi->create_membership_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipTiersApi->create_membership_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_membership_tier_creation_params** | [**WTMembershipTierCreationParams**](WTMembershipTierCreationParams.md)|  | 

### Return type

[**WTMembershipTier**](WTMembershipTier.md)

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

# **fetch_all_membership_tiers**
> List[WTMembershipTier] fetch_all_membership_tiers(is_archive_included=is_archive_included)

Get all Membership Tiers

### Example


```python
import wallet
from wallet.models.wt_membership_tier import WTMembershipTier
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
    api_instance = wallet.MembershipTiersApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all Membership Tiers
        api_response = api_instance.fetch_all_membership_tiers(is_archive_included=is_archive_included)
        print("The response of MembershipTiersApi->fetch_all_membership_tiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipTiersApi->fetch_all_membership_tiers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[WTMembershipTier]**](WTMembershipTier.md)

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

# **fetch_all_membership_tiers_with_member_count**
> List[WTMembershipTierWithMemberCount] fetch_all_membership_tiers_with_member_count(is_archive_included=is_archive_included)

Get all Membership Tiers with member count

### Example


```python
import wallet
from wallet.models.wt_membership_tier_with_member_count import WTMembershipTierWithMemberCount
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
    api_instance = wallet.MembershipTiersApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all Membership Tiers with member count
        api_response = api_instance.fetch_all_membership_tiers_with_member_count(is_archive_included=is_archive_included)
        print("The response of MembershipTiersApi->fetch_all_membership_tiers_with_member_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipTiersApi->fetch_all_membership_tiers_with_member_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[WTMembershipTierWithMemberCount]**](WTMembershipTierWithMemberCount.md)

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

# **fetch_membership_tier_by_id**
> WTMembershipTier fetch_membership_tier_by_id(id)

Get Membership Tier

### Example


```python
import wallet
from wallet.models.wt_membership_tier import WTMembershipTier
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
    api_instance = wallet.MembershipTiersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Membership Tier
        api_response = api_instance.fetch_membership_tier_by_id(id)
        print("The response of MembershipTiersApi->fetch_membership_tier_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipTiersApi->fetch_membership_tier_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMembershipTier**](WTMembershipTier.md)

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

# **fetch_membership_tier_history_log**
> MSMembershipTierHistoryPagination fetch_membership_tier_history_log(pagination_request_with_id_and_without_sort_options)

Get Membership Tier history

### Example


```python
import wallet
from wallet.models.ms_membership_tier_history_pagination import MSMembershipTierHistoryPagination
from wallet.models.pagination_request_with_id_and_without_sort_options import PaginationRequestWithIDAndWithoutSortOptions
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
    api_instance = wallet.MembershipTiersApi(api_client)
    pagination_request_with_id_and_without_sort_options = wallet.PaginationRequestWithIDAndWithoutSortOptions() # PaginationRequestWithIDAndWithoutSortOptions | 

    try:
        # Get Membership Tier history
        api_response = api_instance.fetch_membership_tier_history_log(pagination_request_with_id_and_without_sort_options)
        print("The response of MembershipTiersApi->fetch_membership_tier_history_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipTiersApi->fetch_membership_tier_history_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request_with_id_and_without_sort_options** | [**PaginationRequestWithIDAndWithoutSortOptions**](PaginationRequestWithIDAndWithoutSortOptions.md)|  | 

### Return type

[**MSMembershipTierHistoryPagination**](MSMembershipTierHistoryPagination.md)

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

# **fetch_membership_tier_redemption_log**
> MSMembershipTierRedemptionPagination fetch_membership_tier_redemption_log(pagination_request_with_id_and_without_sort_options)

Get Membership Tier redemption log

### Example


```python
import wallet
from wallet.models.ms_membership_tier_redemption_pagination import MSMembershipTierRedemptionPagination
from wallet.models.pagination_request_with_id_and_without_sort_options import PaginationRequestWithIDAndWithoutSortOptions
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
    api_instance = wallet.MembershipTiersApi(api_client)
    pagination_request_with_id_and_without_sort_options = wallet.PaginationRequestWithIDAndWithoutSortOptions() # PaginationRequestWithIDAndWithoutSortOptions | 

    try:
        # Get Membership Tier redemption log
        api_response = api_instance.fetch_membership_tier_redemption_log(pagination_request_with_id_and_without_sort_options)
        print("The response of MembershipTiersApi->fetch_membership_tier_redemption_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipTiersApi->fetch_membership_tier_redemption_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request_with_id_and_without_sort_options** | [**PaginationRequestWithIDAndWithoutSortOptions**](PaginationRequestWithIDAndWithoutSortOptions.md)|  | 

### Return type

[**MSMembershipTierRedemptionPagination**](MSMembershipTierRedemptionPagination.md)

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

# **restore_membership_tier**
> WTMembershipTier restore_membership_tier(id)

Restore Membership Tier

### Example


```python
import wallet
from wallet.models.wt_membership_tier import WTMembershipTier
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
    api_instance = wallet.MembershipTiersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore Membership Tier
        api_response = api_instance.restore_membership_tier(id)
        print("The response of MembershipTiersApi->restore_membership_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipTiersApi->restore_membership_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMembershipTier**](WTMembershipTier.md)

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

# **update_membership_tier**
> WTMembershipTier update_membership_tier(id, wt_membership_tier_update_params)

Update Membership Tier

### Example


```python
import wallet
from wallet.models.wt_membership_tier import WTMembershipTier
from wallet.models.wt_membership_tier_update_params import WTMembershipTierUpdateParams
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
    api_instance = wallet.MembershipTiersApi(api_client)
    id = 'id_example' # str | 
    wt_membership_tier_update_params = wallet.WTMembershipTierUpdateParams() # WTMembershipTierUpdateParams | 

    try:
        # Update Membership Tier
        api_response = api_instance.update_membership_tier(id, wt_membership_tier_update_params)
        print("The response of MembershipTiersApi->update_membership_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipTiersApi->update_membership_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wt_membership_tier_update_params** | [**WTMembershipTierUpdateParams**](WTMembershipTierUpdateParams.md)|  | 

### Return type

[**WTMembershipTier**](WTMembershipTier.md)

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

