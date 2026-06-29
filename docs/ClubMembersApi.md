# wallet.ClubMembersApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_member**](ClubMembersApi.md#archive_member) | **DELETE** /v2/membership/member/{id} | Archive Member
[**create_member**](ClubMembersApi.md#create_member) | **POST** /v2/membership/member | Create Member
[**fetch_member_by_id**](ClubMembersApi.md#fetch_member_by_id) | **GET** /v2/membership/member/{id} | Get Member
[**fetch_member_history_log**](ClubMembersApi.md#fetch_member_history_log) | **POST** /v2/membership/member/history/log | Get Member history
[**fetch_member_redemption_log**](ClubMembersApi.md#fetch_member_redemption_log) | **POST** /v2/membership/member/redemption/log | Get Member redemption log
[**fetch_members_by_page**](ClubMembersApi.md#fetch_members_by_page) | **POST** /v2/membership/member/page | Get Members
[**fetch_members_count**](ClubMembersApi.md#fetch_members_count) | **GET** /v2/membership/member/count | Count Members
[**restore_member**](ClubMembersApi.md#restore_member) | **PATCH** /v2/membership/member/{id} | Restore Member
[**search_members**](ClubMembersApi.md#search_members) | **POST** /v2/membership/member/search | Search for Members
[**update_member**](ClubMembersApi.md#update_member) | **PUT** /v2/membership/member/{id} | Update Member


# **archive_member**
> WTMember archive_member(id)

Archive Member

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
    api_instance = wallet.ClubMembersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive Member
        api_response = api_instance.archive_member(id)
        print("The response of ClubMembersApi->archive_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersApi->archive_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Create Member

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
    api_instance = wallet.ClubMembersApi(api_client)
    wt_member_creation_params = wallet.WTMemberCreationParams() # WTMemberCreationParams | 

    try:
        # Create Member
        api_response = api_instance.create_member(wt_member_creation_params)
        print("The response of ClubMembersApi->create_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersApi->create_member: %s\n" % e)
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

Get Member

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
    api_instance = wallet.ClubMembersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Member
        api_response = api_instance.fetch_member_by_id(id)
        print("The response of ClubMembersApi->fetch_member_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersApi->fetch_member_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Get Member history

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
    api_instance = wallet.ClubMembersApi(api_client)
    pagination_request_with_id_and_without_sort_options = wallet.PaginationRequestWithIDAndWithoutSortOptions() # PaginationRequestWithIDAndWithoutSortOptions | 

    try:
        # Get Member history
        api_response = api_instance.fetch_member_history_log(pagination_request_with_id_and_without_sort_options)
        print("The response of ClubMembersApi->fetch_member_history_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersApi->fetch_member_history_log: %s\n" % e)
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

Get Member redemption log

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
    api_instance = wallet.ClubMembersApi(api_client)
    pagination_request_with_id_and_without_sort_options = wallet.PaginationRequestWithIDAndWithoutSortOptions() # PaginationRequestWithIDAndWithoutSortOptions | 

    try:
        # Get Member redemption log
        api_response = api_instance.fetch_member_redemption_log(pagination_request_with_id_and_without_sort_options)
        print("The response of ClubMembersApi->fetch_member_redemption_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersApi->fetch_member_redemption_log: %s\n" % e)
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

Get Members

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
    api_instance = wallet.ClubMembersApi(api_client)
    pagination_request_with_sort_options = wallet.PaginationRequestWithSortOptions() # PaginationRequestWithSortOptions | 

    try:
        # Get Members
        api_response = api_instance.fetch_members_by_page(pagination_request_with_sort_options)
        print("The response of ClubMembersApi->fetch_members_by_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersApi->fetch_members_by_page: %s\n" % e)
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

Count Members

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
    api_instance = wallet.ClubMembersApi(api_client)

    try:
        # Count Members
        api_response = api_instance.fetch_members_count()
        print("The response of ClubMembersApi->fetch_members_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersApi->fetch_members_count: %s\n" % e)
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

Restore Member

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
    api_instance = wallet.ClubMembersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore Member
        api_response = api_instance.restore_member(id)
        print("The response of ClubMembersApi->restore_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersApi->restore_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

Search for Members

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
    api_instance = wallet.ClubMembersApi(api_client)
    member_search = wallet.MemberSearch() # MemberSearch | 

    try:
        # Search for Members
        api_response = api_instance.search_members(member_search)
        print("The response of ClubMembersApi->search_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersApi->search_members: %s\n" % e)
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

Update Member

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
    api_instance = wallet.ClubMembersApi(api_client)
    id = 'id_example' # str | 
    pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number_or_email_or_birthday = wallet.PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumberOrEmailOrBirthday() # PickWTMemberMemberIDOrFirstNameOrLastNameOrMembershipTierIDOrPointsAccruedOrMobileNumberOrEmailOrBirthday | 

    try:
        # Update Member
        api_response = api_instance.update_member(id, pick_wt_member_member_idor_first_name_or_last_name_or_membership_tier_idor_points_accrued_or_mobile_number_or_email_or_birthday)
        print("The response of ClubMembersApi->update_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubMembersApi->update_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

