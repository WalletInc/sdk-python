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
import wallet
from wallet.models.wt_member import WTMember
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
    api_instance = wallet.ClubMembersPointsApi(api_client)
    id = None # object | 

    try:
        # Archive member
        api_response = api_instance.archive_member(id)
        print("The response of ClubMembersPointsApi->archive_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersPointsApi->archive_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
import wallet
from wallet.models.wt_member import WTMember
from wallet.models.wt_member_creation_params import WTMemberCreationParams
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
    api_instance = wallet.ClubMembersPointsApi(api_client)
    wt_member_creation_params = wallet.WTMemberCreationParams() # WTMemberCreationParams | 

    try:
        # Create member
        api_response = api_instance.create_member(wt_member_creation_params)
        print("The response of ClubMembersPointsApi->create_member:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.wt_member import WTMember
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
    api_instance = wallet.ClubMembersPointsApi(api_client)
    id = None # object | 

    try:
        # Fetch member
        api_response = api_instance.fetch_member_by_id(id)
        print("The response of ClubMembersPointsApi->fetch_member_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersPointsApi->fetch_member_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
import wallet
from wallet.models.ms_member_history_pagination import MSMemberHistoryPagination
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
    api_instance = wallet.ClubMembersPointsApi(api_client)
    pagination_request_with_id_and_without_sort_options = wallet.PaginationRequestWithIDAndWithoutSortOptions() # PaginationRequestWithIDAndWithoutSortOptions | 

    try:
        # Fetch history
        api_response = api_instance.fetch_member_history_log(pagination_request_with_id_and_without_sort_options)
        print("The response of ClubMembersPointsApi->fetch_member_history_log:\n")
        pprint(api_response)
    except Exception as e:
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
import wallet
from wallet.models.ms_member_redemption_pagination import MSMemberRedemptionPagination
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
    api_instance = wallet.ClubMembersPointsApi(api_client)
    pagination_request_with_id_and_without_sort_options = wallet.PaginationRequestWithIDAndWithoutSortOptions() # PaginationRequestWithIDAndWithoutSortOptions | 

    try:
        # Fetch redemption log
        api_response = api_instance.fetch_member_redemption_log(pagination_request_with_id_and_without_sort_options)
        print("The response of ClubMembersPointsApi->fetch_member_redemption_log:\n")
        pprint(api_response)
    except Exception as e:
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
> List[WTMember] fetch_members_by_page(pagination_request_with_sort_options)

Fetch members by page

### Example


```python
import wallet
from wallet.models.pagination_request_with_sort_options import PaginationRequestWithSortOptions
from wallet.models.wt_member import WTMember
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
    api_instance = wallet.ClubMembersPointsApi(api_client)
    pagination_request_with_sort_options = wallet.PaginationRequestWithSortOptions() # PaginationRequestWithSortOptions | 

    try:
        # Fetch members by page
        api_response = api_instance.fetch_members_by_page(pagination_request_with_sort_options)
        print("The response of ClubMembersPointsApi->fetch_members_by_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersPointsApi->fetch_members_by_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request_with_sort_options** | [**PaginationRequestWithSortOptions**](PaginationRequestWithSortOptions.md)|  | 

### Return type

[**List[WTMember]**](WTMember.md)

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
> FetchMembersCount200Response fetch_members_count()

Count active members

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
    api_instance = wallet.ClubMembersPointsApi(api_client)

    try:
        # Count active members
        api_response = api_instance.fetch_members_count()
        print("The response of ClubMembersPointsApi->fetch_members_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersPointsApi->fetch_members_count: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **restore_member**
> WTMember restore_member(id)

Restore member

### Example


```python
import wallet
from wallet.models.wt_member import WTMember
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
    api_instance = wallet.ClubMembersPointsApi(api_client)
    id = None # object | 

    try:
        # Restore member
        api_response = api_instance.restore_member(id)
        print("The response of ClubMembersPointsApi->restore_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersPointsApi->restore_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
import wallet
from wallet.models.member_search import MemberSearch
from wallet.models.paginated_wt_members import PaginatedWTMembers
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
    api_instance = wallet.ClubMembersPointsApi(api_client)
    member_search = wallet.MemberSearch() # MemberSearch | 

    try:
        # Search for members
        api_response = api_instance.search_members(member_search)
        print("The response of ClubMembersPointsApi->search_members:\n")
        pprint(api_response)
    except Exception as e:
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
> WTMember update_member(id, pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number_or_email_or_birthday)

Update member

### Example


```python
import wallet
from wallet.models.pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number_or_email_or_birthday import PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumberOrEmailOrBirthday
from wallet.models.wt_member import WTMember
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
    api_instance = wallet.ClubMembersPointsApi(api_client)
    id = None # object | 
    pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number_or_email_or_birthday = wallet.PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumberOrEmailOrBirthday() # PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumberOrEmailOrBirthday | 

    try:
        # Update member
        api_response = api_instance.update_member(id, pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number_or_email_or_birthday)
        print("The response of ClubMembersPointsApi->update_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersPointsApi->update_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number_or_email_or_birthday** | [**PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumberOrEmailOrBirthday**](PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumberOrEmailOrBirthday.md)|  | 

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

