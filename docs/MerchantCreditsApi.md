# wallet.MerchantCreditsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_merchant_credit**](MerchantCreditsApi.md#archive_merchant_credit) | **DELETE** /v2/payment/merchantcredit/{id} | Archive Merchant Credit
[**create_merchant_credit**](MerchantCreditsApi.md#create_merchant_credit) | **POST** /v2/payment/merchantcredit | Create Merchant Credit
[**fetch_merchant_credit_by_id**](MerchantCreditsApi.md#fetch_merchant_credit_by_id) | **GET** /v2/payment/merchantcredit/{id} | Get Merchant Credit
[**fetch_merchant_credit_count**](MerchantCreditsApi.md#fetch_merchant_credit_count) | **GET** /v2/payment/merchantcredit/count | Count all Merchant Credits
[**fetch_merchant_credit_history_log**](MerchantCreditsApi.md#fetch_merchant_credit_history_log) | **POST** /v2/payment/merchantcredit/history/log | Get history
[**fetch_merchant_credit_redemption_log**](MerchantCreditsApi.md#fetch_merchant_credit_redemption_log) | **POST** /v2/payment/merchantcredit/redemption/log | Get redemption log
[**fetch_merchant_credits_by_page**](MerchantCreditsApi.md#fetch_merchant_credits_by_page) | **POST** /v2/payment/merchantcredit/page | Get Merchant Credits
[**restore_merchant_credit**](MerchantCreditsApi.md#restore_merchant_credit) | **PATCH** /v2/payment/merchantcredit/{id} | Restore Merchant Credit
[**search_merchant_credits**](MerchantCreditsApi.md#search_merchant_credits) | **POST** /v2/payment/merchantcredit/search | Search for Merchant Credits with Member ID
[**update_merchant_credit**](MerchantCreditsApi.md#update_merchant_credit) | **PUT** /v2/payment/merchantcredit/{id} | Update Merchant Credit


# **archive_merchant_credit**
> WTMerchantCredit archive_merchant_credit(id)

Archive Merchant Credit

### Example


```python
import wallet
from wallet.models.wt_merchant_credit import WTMerchantCredit
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
    api_instance = wallet.MerchantCreditsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive Merchant Credit
        api_response = api_instance.archive_merchant_credit(id)
        print("The response of MerchantCreditsApi->archive_merchant_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantCreditsApi->archive_merchant_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMerchantCredit**](WTMerchantCredit.md)

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

# **create_merchant_credit**
> WTMerchantCredit create_merchant_credit(wt_merchant_credit_creation_params)

Create Merchant Credit

### Example


```python
import wallet
from wallet.models.wt_merchant_credit import WTMerchantCredit
from wallet.models.wt_merchant_credit_creation_params import WTMerchantCreditCreationParams
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
    api_instance = wallet.MerchantCreditsApi(api_client)
    wt_merchant_credit_creation_params = wallet.WTMerchantCreditCreationParams() # WTMerchantCreditCreationParams | 

    try:
        # Create Merchant Credit
        api_response = api_instance.create_merchant_credit(wt_merchant_credit_creation_params)
        print("The response of MerchantCreditsApi->create_merchant_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantCreditsApi->create_merchant_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_merchant_credit_creation_params** | [**WTMerchantCreditCreationParams**](WTMerchantCreditCreationParams.md)|  | 

### Return type

[**WTMerchantCredit**](WTMerchantCredit.md)

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

# **fetch_merchant_credit_by_id**
> WTMerchantCredit fetch_merchant_credit_by_id(id)

Get Merchant Credit

### Example


```python
import wallet
from wallet.models.wt_merchant_credit import WTMerchantCredit
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
    api_instance = wallet.MerchantCreditsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Merchant Credit
        api_response = api_instance.fetch_merchant_credit_by_id(id)
        print("The response of MerchantCreditsApi->fetch_merchant_credit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantCreditsApi->fetch_merchant_credit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMerchantCredit**](WTMerchantCredit.md)

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

# **fetch_merchant_credit_count**
> FetchMembersCount200Response fetch_merchant_credit_count()

Count all Merchant Credits

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
    api_instance = wallet.MerchantCreditsApi(api_client)

    try:
        # Count all Merchant Credits
        api_response = api_instance.fetch_merchant_credit_count()
        print("The response of MerchantCreditsApi->fetch_merchant_credit_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantCreditsApi->fetch_merchant_credit_count: %s\n" % e)
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

# **fetch_merchant_credit_history_log**
> MSMerchantCreditHistoryPagination fetch_merchant_credit_history_log(pagination_request_with_id_and_without_sort_options)

Get history

### Example


```python
import wallet
from wallet.models.ms_merchant_credit_history_pagination import MSMerchantCreditHistoryPagination
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
    api_instance = wallet.MerchantCreditsApi(api_client)
    pagination_request_with_id_and_without_sort_options = wallet.PaginationRequestWithIDAndWithoutSortOptions() # PaginationRequestWithIDAndWithoutSortOptions | 

    try:
        # Get history
        api_response = api_instance.fetch_merchant_credit_history_log(pagination_request_with_id_and_without_sort_options)
        print("The response of MerchantCreditsApi->fetch_merchant_credit_history_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantCreditsApi->fetch_merchant_credit_history_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request_with_id_and_without_sort_options** | [**PaginationRequestWithIDAndWithoutSortOptions**](PaginationRequestWithIDAndWithoutSortOptions.md)|  | 

### Return type

[**MSMerchantCreditHistoryPagination**](MSMerchantCreditHistoryPagination.md)

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

# **fetch_merchant_credit_redemption_log**
> MSMerchantCreditRedemptionPagination fetch_merchant_credit_redemption_log(pagination_request_with_id_and_without_sort_options)

Get redemption log

### Example


```python
import wallet
from wallet.models.ms_merchant_credit_redemption_pagination import MSMerchantCreditRedemptionPagination
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
    api_instance = wallet.MerchantCreditsApi(api_client)
    pagination_request_with_id_and_without_sort_options = wallet.PaginationRequestWithIDAndWithoutSortOptions() # PaginationRequestWithIDAndWithoutSortOptions | 

    try:
        # Get redemption log
        api_response = api_instance.fetch_merchant_credit_redemption_log(pagination_request_with_id_and_without_sort_options)
        print("The response of MerchantCreditsApi->fetch_merchant_credit_redemption_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantCreditsApi->fetch_merchant_credit_redemption_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request_with_id_and_without_sort_options** | [**PaginationRequestWithIDAndWithoutSortOptions**](PaginationRequestWithIDAndWithoutSortOptions.md)|  | 

### Return type

[**MSMerchantCreditRedemptionPagination**](MSMerchantCreditRedemptionPagination.md)

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

# **fetch_merchant_credits_by_page**
> List[WTMerchantCredit] fetch_merchant_credits_by_page(pagination_request_with_sort_options)

Get Merchant Credits

### Example


```python
import wallet
from wallet.models.pagination_request_with_sort_options import PaginationRequestWithSortOptions
from wallet.models.wt_merchant_credit import WTMerchantCredit
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
    api_instance = wallet.MerchantCreditsApi(api_client)
    pagination_request_with_sort_options = wallet.PaginationRequestWithSortOptions() # PaginationRequestWithSortOptions | 

    try:
        # Get Merchant Credits
        api_response = api_instance.fetch_merchant_credits_by_page(pagination_request_with_sort_options)
        print("The response of MerchantCreditsApi->fetch_merchant_credits_by_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantCreditsApi->fetch_merchant_credits_by_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request_with_sort_options** | [**PaginationRequestWithSortOptions**](PaginationRequestWithSortOptions.md)|  | 

### Return type

[**List[WTMerchantCredit]**](WTMerchantCredit.md)

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

# **restore_merchant_credit**
> WTMerchantCredit restore_merchant_credit(id)

Restore Merchant Credit

### Example


```python
import wallet
from wallet.models.wt_merchant_credit import WTMerchantCredit
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
    api_instance = wallet.MerchantCreditsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore Merchant Credit
        api_response = api_instance.restore_merchant_credit(id)
        print("The response of MerchantCreditsApi->restore_merchant_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantCreditsApi->restore_merchant_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTMerchantCredit**](WTMerchantCredit.md)

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

# **search_merchant_credits**
> PaginatedWTMerchantCredits search_merchant_credits(merchant_credit_search)

Search for Merchant Credits with Member ID

### Example


```python
import wallet
from wallet.models.merchant_credit_search import MerchantCreditSearch
from wallet.models.paginated_wt_merchant_credits import PaginatedWTMerchantCredits
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
    api_instance = wallet.MerchantCreditsApi(api_client)
    merchant_credit_search = wallet.MerchantCreditSearch() # MerchantCreditSearch | 

    try:
        # Search for Merchant Credits with Member ID
        api_response = api_instance.search_merchant_credits(merchant_credit_search)
        print("The response of MerchantCreditsApi->search_merchant_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantCreditsApi->search_merchant_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_credit_search** | [**MerchantCreditSearch**](MerchantCreditSearch.md)|  | 

### Return type

[**PaginatedWTMerchantCredits**](PaginatedWTMerchantCredits.md)

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

# **update_merchant_credit**
> WTMerchantCredit update_merchant_credit(id, pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number)

Update Merchant Credit

### Example


```python
import wallet
from wallet.models.pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number import PickWTMerchantCreditMemberIDOrCreditAmountOrMobileNumber
from wallet.models.wt_merchant_credit import WTMerchantCredit
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
    api_instance = wallet.MerchantCreditsApi(api_client)
    id = 'id_example' # str | 
    pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number = wallet.PickWTMerchantCreditMemberIDOrCreditAmountOrMobileNumber() # PickWTMerchantCreditMemberIDOrCreditAmountOrMobileNumber | 

    try:
        # Update Merchant Credit
        api_response = api_instance.update_merchant_credit(id, pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number)
        print("The response of MerchantCreditsApi->update_merchant_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantCreditsApi->update_merchant_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number** | [**PickWTMerchantCreditMemberIDOrCreditAmountOrMobileNumber**](PickWTMerchantCreditMemberIDOrCreditAmountOrMobileNumber.md)|  | 

### Return type

[**WTMerchantCredit**](WTMerchantCredit.md)

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

