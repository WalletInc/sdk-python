# wallet.ClubMembersPointsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_member**](ClubMembersPointsApi.md#archive_member) | **DELETE** /v2/membership/member/{id} | Archive member
[**create_member**](ClubMembersPointsApi.md#create_member) | **POST** /v2/membership/member | Create member
[**fetch_member_by_id**](ClubMembersPointsApi.md#fetch_member_by_id) | **GET** /v2/membership/member/{id} | Fetch member
[**fetch_member_history_log**](ClubMembersPointsApi.md#fetch_member_history_log) | **POST** /v2/membership/member/history/log | Fetch history
[**fetch_member_redemption_log**](ClubMembersPointsApi.md#fetch_member_redemption_log) | **POST** /v2/membership/member/redemption/log | Fetch redemption log
[**fetch_members_by_page**](ClubMembersPointsApi.md#fetch_members_by_page) | **POST** /v2/membership/member/page | Fetch members by page
[**fetch_members_count**](ClubMembersPointsApi.md#fetch_members_count) | **GET** /v2/membership/member/count | Count active members
[**restore_member**](ClubMembersPointsApi.md#restore_member) | **PATCH** /v2/membership/member/{id} | Restore member
[**search_members**](ClubMembersPointsApi.md#search_members) | **POST** /v2/membership/member/search | Search for members
[**update_member**](ClubMembersPointsApi.md#update_member) | **PUT** /v2/membership/member/{id} | Update member


# **archive_member**
> WTMember archive_member(id)

Archive member

### Example


```python
import time
import wallet
from wallet.api import club_members__points_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_member import WTMember
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = club_members__points_api.ClubMembersPointsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive member
        api_response = api_instance.archive_member(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ClubMembersPointsApi->archive_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**WTMember**](WTMember.md)

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

# **create_member**
> WTMember create_member(wt_member_creation_params)

Create member

### Example


```python
import time
import wallet
from wallet.api import club_members__points_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.merchant_not_initialized import MerchantNotInitialized
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.duplicate_row_found import DuplicateRowFound
from wallet.model.wt_member import WTMember
from wallet.model.wt_member_creation_params import WTMemberCreationParams
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = club_members__points_api.ClubMembersPointsApi(api_client)
    wt_member_creation_params = WTMemberCreationParams(
        first_name="John",
        last_name="Doe",
        membership_tier_id=PrefixedNanoID("CMueJDL982Hs"),
        mobile_number="+18047552674",
        points_accrued=125,
        member_id="1hdue82",
    ) # WTMemberCreationParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create member
        api_response = api_instance.create_member(wt_member_creation_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ClubMembersPointsApi->create_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_member_creation_params** | [**WTMemberCreationParams**](WTMemberCreationParams.md)|  |

### Return type

[**WTMember**](WTMember.md)

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

# **fetch_member_by_id**
> WTMember fetch_member_by_id(id)

Fetch member

### Example


```python
import time
import wallet
from wallet.api import club_members__points_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_member import WTMember
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = club_members__points_api.ClubMembersPointsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch member
        api_response = api_instance.fetch_member_by_id(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ClubMembersPointsApi->fetch_member_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**WTMember**](WTMember.md)

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

# **fetch_member_history_log**
> MSMemberHistoryPagination fetch_member_history_log(pagination_request_with_id_and_without_sort_options)

Fetch history

### Example


```python
import time
import wallet
from wallet.api import club_members__points_api
from wallet.model.pagination_request_with_id_and_without_sort_options import PaginationRequestWithIDAndWithoutSortOptions
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.ms_member_history_pagination import MSMemberHistoryPagination
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = club_members__points_api.ClubMembersPointsApi(api_client)
    pagination_request_with_id_and_without_sort_options = PaginationRequestWithIDAndWithoutSortOptions(
        page_size=20,
        page_num=1,
        id=PrefixedNanoID("CMueJDL982Hs"),
    ) # PaginationRequestWithIDAndWithoutSortOptions | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch history
        api_response = api_instance.fetch_member_history_log(pagination_request_with_id_and_without_sort_options)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ClubMembersPointsApi->fetch_member_history_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request_with_id_and_without_sort_options** | [**PaginationRequestWithIDAndWithoutSortOptions**](PaginationRequestWithIDAndWithoutSortOptions.md)|  |

### Return type

[**MSMemberHistoryPagination**](MSMemberHistoryPagination.md)

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

# **fetch_member_redemption_log**
> MSMemberRedemptionPagination fetch_member_redemption_log(pagination_request_with_id_and_without_sort_options)

Fetch redemption log

### Example


```python
import time
import wallet
from wallet.api import club_members__points_api
from wallet.model.pagination_request_with_id_and_without_sort_options import PaginationRequestWithIDAndWithoutSortOptions
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.ms_member_redemption_pagination import MSMemberRedemptionPagination
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
    api_instance = club_members__points_api.ClubMembersPointsApi(api_client)
    pagination_request_with_id_and_without_sort_options = PaginationRequestWithIDAndWithoutSortOptions(
        page_size=20,
        page_num=1,
        id=PrefixedNanoID("CMueJDL982Hs"),
    ) # PaginationRequestWithIDAndWithoutSortOptions | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch redemption log
        api_response = api_instance.fetch_member_redemption_log(pagination_request_with_id_and_without_sort_options)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ClubMembersPointsApi->fetch_member_redemption_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request_with_id_and_without_sort_options** | [**PaginationRequestWithIDAndWithoutSortOptions**](PaginationRequestWithIDAndWithoutSortOptions.md)|  |

### Return type

[**MSMemberRedemptionPagination**](MSMemberRedemptionPagination.md)

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

# **fetch_members_by_page**
> [WTMember] fetch_members_by_page(pagination_request_with_sort_options)

Fetch members by page

### Example


```python
import time
import wallet
from wallet.api import club_members__points_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.pagination_request_with_sort_options import PaginationRequestWithSortOptions
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_member import WTMember
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = club_members__points_api.ClubMembersPointsApi(api_client)
    pagination_request_with_sort_options = PaginationRequestWithSortOptions(
        is_archive_included=True,
        page_size=20,
        page_num=1,
        sort_key="createdAt",
        sort_order=None,
    ) # PaginationRequestWithSortOptions | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch members by page
        api_response = api_instance.fetch_members_by_page(pagination_request_with_sort_options)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ClubMembersPointsApi->fetch_members_by_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request_with_sort_options** | [**PaginationRequestWithSortOptions**](PaginationRequestWithSortOptions.md)|  |

### Return type

[**[WTMember]**](WTMember.md)

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

# **fetch_members_count**
> InlineResponse2002 fetch_members_count()

Count active members

### Example


```python
import time
import wallet
from wallet.api import club_members__points_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.inline_response2002 import InlineResponse2002
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = club_members__points_api.ClubMembersPointsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Count active members
        api_response = api_instance.fetch_members_count()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ClubMembersPointsApi->fetch_members_count: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **restore_member**
> WTMember restore_member(id)

Restore member

### Example


```python
import time
import wallet
from wallet.api import club_members__points_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_member import WTMember
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = club_members__points_api.ClubMembersPointsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore member
        api_response = api_instance.restore_member(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ClubMembersPointsApi->restore_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**WTMember**](WTMember.md)

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

# **search_members**
> PaginatedWTMembers search_members(member_search)

Search for members

### Example


```python
import time
import wallet
from wallet.api import club_members__points_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.member_search import MemberSearch
from wallet.model.falsum_error import FalsumError
from wallet.model.paginated_wt_members import PaginatedWTMembers
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
    api_instance = club_members__points_api.ClubMembersPointsApi(api_client)
    member_search = MemberSearch(
        is_archive_included=True,
        page_size=20,
        page_num=1,
        sort_order=None,
        sort_key=None,
        search_key=None,
        search_value="MEM001",
    ) # MemberSearch | 

    # example passing only required values which don't have defaults set
    try:
        # Search for members
        api_response = api_instance.search_members(member_search)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ClubMembersPointsApi->search_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_search** | [**MemberSearch**](MemberSearch.md)|  |

### Return type

[**PaginatedWTMembers**](PaginatedWTMembers.md)

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

# **update_member**
> WTMember update_member(id, pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number)

Update member

### Example


```python
import time
import wallet
from wallet.api import club_members__points_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.foreign_key_does_not_exist import ForeignKeyDoesNotExist
from wallet.model.auth_error import AuthError
from wallet.model.pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number import PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumber
from wallet.model.duplicate_row_found import DuplicateRowFound
from wallet.model.wt_member import WTMember
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = club_members__points_api.ClubMembersPointsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number = PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumber(
        member_id="1hdue82",
        first_name="John",
        last_name="Doe",
        membership_tier_id=PrefixedNanoID("CMueJDL982Hs"),
        mobile_number="+18047552674",
        points_accrued=125,
    ) # PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumber | 

    # example passing only required values which don't have defaults set
    try:
        # Update member
        api_response = api_instance.update_member(id, pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling ClubMembersPointsApi->update_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number** | [**PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumber**](PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumber.md)|  |

### Return type

[**WTMember**](WTMember.md)

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

