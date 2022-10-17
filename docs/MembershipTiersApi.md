# wallet.MembershipTiersApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_membership_tier**](MembershipTiersApi.md#archive_membership_tier) | **DELETE** /v2/membership/tier/{id} | Archive tier
[**create_membership_tier**](MembershipTiersApi.md#create_membership_tier) | **POST** /v2/membership/tier | Create tier
[**fetch_all_membership_tiers**](MembershipTiersApi.md#fetch_all_membership_tiers) | **GET** /v2/membership/tier/all | Fetch all tiers
[**fetch_all_membership_tiers_with_member_count**](MembershipTiersApi.md#fetch_all_membership_tiers_with_member_count) | **GET** /v2/membership/tier/allWithMemberCount | Fetch all tiers with member count
[**fetch_membership_tier_by_id**](MembershipTiersApi.md#fetch_membership_tier_by_id) | **GET** /v2/membership/tier/{id} | Fetch tier
[**fetch_membership_tier_history_log**](MembershipTiersApi.md#fetch_membership_tier_history_log) | **POST** /v2/membership/tier/history/log | Fetch history
[**fetch_membership_tier_redemption_log**](MembershipTiersApi.md#fetch_membership_tier_redemption_log) | **POST** /v2/membership/tier/redemption/log | Fetch redemption log
[**restore_membership_tier**](MembershipTiersApi.md#restore_membership_tier) | **PATCH** /v2/membership/tier/{id} | Restore tier
[**update_membership_tier**](MembershipTiersApi.md#update_membership_tier) | **PUT** /v2/membership/tier/{id} | Update tier


# **archive_membership_tier**
> WTMembershipTier archive_membership_tier(id)

Archive tier

### Example


```python
import time
import wallet
from wallet.api import membership_tiers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_membership_tier import WTMembershipTier
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = membership_tiers_api.MembershipTiersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive tier
        api_response = api_instance.archive_membership_tier(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MembershipTiersApi->archive_membership_tier: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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

Create tier

### Example


```python
import time
import wallet
from wallet.api import membership_tiers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.merchant_not_initialized import MerchantNotInitialized
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_membership_tier import WTMembershipTier
from wallet.model.wt_membership_tier_creation_params import WTMembershipTierCreationParams
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
    api_instance = membership_tiers_api.MembershipTiersApi(api_client)
    wt_membership_tier_creation_params = WTMembershipTierCreationParams(
        tier_number="101",
        tier_name="Gold",
        tier_discount=25,
        tier_design_id=NanoID("C"),
        points_design_id=NanoID("C"),
    ) # WTMembershipTierCreationParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create tier
        api_response = api_instance.create_membership_tier(wt_membership_tier_creation_params)
        pprint(api_response)
    except wallet.ApiException as e:
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
> [WTMembershipTier] fetch_all_membership_tiers()

Fetch all tiers

### Example


```python
import time
import wallet
from wallet.api import membership_tiers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_membership_tier import WTMembershipTier
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = membership_tiers_api.MembershipTiersApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all tiers
        api_response = api_instance.fetch_all_membership_tiers(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MembershipTiersApi->fetch_all_membership_tiers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**[WTMembershipTier]**](WTMembershipTier.md)

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
> [WTMembershipTierWithMemberCount] fetch_all_membership_tiers_with_member_count()

Fetch all tiers with member count

### Example


```python
import time
import wallet
from wallet.api import membership_tiers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_membership_tier_with_member_count import WTMembershipTierWithMemberCount
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = membership_tiers_api.MembershipTiersApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all tiers with member count
        api_response = api_instance.fetch_all_membership_tiers_with_member_count(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MembershipTiersApi->fetch_all_membership_tiers_with_member_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**[WTMembershipTierWithMemberCount]**](WTMembershipTierWithMemberCount.md)

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

Fetch tier

### Example


```python
import time
import wallet
from wallet.api import membership_tiers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_membership_tier import WTMembershipTier
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = membership_tiers_api.MembershipTiersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch tier
        api_response = api_instance.fetch_membership_tier_by_id(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MembershipTiersApi->fetch_membership_tier_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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

Fetch history

### Example


```python
import time
import wallet
from wallet.api import membership_tiers_api
from wallet.model.pagination_request_with_id_and_without_sort_options import PaginationRequestWithIDAndWithoutSortOptions
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.ms_membership_tier_history_pagination import MSMembershipTierHistoryPagination
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
    api_instance = membership_tiers_api.MembershipTiersApi(api_client)
    pagination_request_with_id_and_without_sort_options = PaginationRequestWithIDAndWithoutSortOptions(
        page_size=20,
        page_num=1,
        id=PrefixedNanoID("CMueJDL982Hs"),
    ) # PaginationRequestWithIDAndWithoutSortOptions | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch history
        api_response = api_instance.fetch_membership_tier_history_log(pagination_request_with_id_and_without_sort_options)
        pprint(api_response)
    except wallet.ApiException as e:
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

Fetch redemption log

### Example


```python
import time
import wallet
from wallet.api import membership_tiers_api
from wallet.model.pagination_request_with_id_and_without_sort_options import PaginationRequestWithIDAndWithoutSortOptions
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.ms_membership_tier_redemption_pagination import MSMembershipTierRedemptionPagination
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
    api_instance = membership_tiers_api.MembershipTiersApi(api_client)
    pagination_request_with_id_and_without_sort_options = PaginationRequestWithIDAndWithoutSortOptions(
        page_size=20,
        page_num=1,
        id=PrefixedNanoID("CMueJDL982Hs"),
    ) # PaginationRequestWithIDAndWithoutSortOptions | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch redemption log
        api_response = api_instance.fetch_membership_tier_redemption_log(pagination_request_with_id_and_without_sort_options)
        pprint(api_response)
    except wallet.ApiException as e:
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

Restore tier

### Example


```python
import time
import wallet
from wallet.api import membership_tiers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.prefixed_nano_id import PrefixedNanoID
from wallet.model.auth_error import AuthError
from wallet.model.wt_membership_tier import WTMembershipTier
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = membership_tiers_api.MembershipTiersApi(api_client)
    id = PrefixedNanoID("CMueJDL982Hs") # PrefixedNanoID | 

    # example passing only required values which don't have defaults set
    try:
        # Restore tier
        api_response = api_instance.restore_membership_tier(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MembershipTiersApi->restore_membership_tier: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **PrefixedNanoID**|  |

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

Update tier

### Example


```python
import time
import wallet
from wallet.api import membership_tiers_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.foreign_key_does_not_exist import ForeignKeyDoesNotExist
from wallet.model.auth_error import AuthError
from wallet.model.wt_membership_tier import WTMembershipTier
from wallet.model.duplicate_row_found import DuplicateRowFound
from wallet.model.wt_membership_tier_update_params import WTMembershipTierUpdateParams
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = membership_tiers_api.MembershipTiersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_membership_tier_update_params = WTMembershipTierUpdateParams(
        tier_number="101",
        tier_name="Gold",
        tier_discount=25,
        tier_design_id=NanoID("C"),
        points_design_id=NanoID("C"),
    ) # WTMembershipTierUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update tier
        api_response = api_instance.update_membership_tier(id, wt_membership_tier_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MembershipTiersApi->update_membership_tier: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

