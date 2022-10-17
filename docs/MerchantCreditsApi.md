# wallet.MerchantCreditsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_merchant_credit**](MerchantCreditsApi.md#archive_merchant_credit) | **DELETE** /v2/payment/merchantcredit/{id} | Archive merchant credit
[**create_merchant_credit**](MerchantCreditsApi.md#create_merchant_credit) | **POST** /v2/payment/merchantcredit | Create merchant credit
[**fetch_merchant_credit_by_id**](MerchantCreditsApi.md#fetch_merchant_credit_by_id) | **GET** /v2/payment/merchantcredit/{id} | Fetch merchant credit
[**fetch_merchant_credit_count**](MerchantCreditsApi.md#fetch_merchant_credit_count) | **GET** /v2/payment/merchantcredit/count | Fetch all active merchant credits
[**fetch_merchant_credit_history_log**](MerchantCreditsApi.md#fetch_merchant_credit_history_log) | **POST** /v2/payment/merchantcredit/history/log | Fetch history
[**fetch_merchant_credit_redemption_log**](MerchantCreditsApi.md#fetch_merchant_credit_redemption_log) | **POST** /v2/payment/merchantcredit/redemption/log | Fetch redemption log
[**fetch_merchant_credits_by_page**](MerchantCreditsApi.md#fetch_merchant_credits_by_page) | **POST** /v2/payment/merchantcredit/page | Fetch merchant credits by page
[**restore_merchant_credit**](MerchantCreditsApi.md#restore_merchant_credit) | **PATCH** /v2/payment/merchantcredit/{id} | Restore merchant credit
[**search_merchant_credits**](MerchantCreditsApi.md#search_merchant_credits) | **POST** /v2/payment/merchantcredit/search | Search for merchant credits
[**update_merchant_credit**](MerchantCreditsApi.md#update_merchant_credit) | **PUT** /v2/payment/merchantcredit/{id} | Update merchant credit


# **archive_merchant_credit**
> WTMerchantCredit archive_merchant_credit(id)

Archive merchant credit

### Example


```python
import time
import wallet
from wallet.api import merchant_credits_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_merchant_credit import WTMerchantCredit
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
    api_instance = merchant_credits_api.MerchantCreditsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive merchant credit
        api_response = api_instance.archive_merchant_credit(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantCreditsApi->archive_merchant_credit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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

Create merchant credit

### Example


```python
import time
import wallet
from wallet.api import merchant_credits_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.merchant_not_initialized import MerchantNotInitialized
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_merchant_credit import WTMerchantCredit
from wallet.model.auth_error import AuthError
from wallet.model.wt_merchant_credit_creation_params import WTMerchantCreditCreationParams
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
    api_instance = merchant_credits_api.MerchantCreditsApi(api_client)
    wt_merchant_credit_creation_params = WTMerchantCreditCreationParams(
        mobile_number="+18047552674",
        credit_amount=125,
        member_id="1hdue82",
    ) # WTMerchantCreditCreationParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create merchant credit
        api_response = api_instance.create_merchant_credit(wt_merchant_credit_creation_params)
        pprint(api_response)
    except wallet.ApiException as e:
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

Fetch merchant credit

### Example


```python
import time
import wallet
from wallet.api import merchant_credits_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_merchant_credit import WTMerchantCredit
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
    api_instance = merchant_credits_api.MerchantCreditsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch merchant credit
        api_response = api_instance.fetch_merchant_credit_by_id(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantCreditsApi->fetch_merchant_credit_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
> InlineResponse2002 fetch_merchant_credit_count()

Fetch all active merchant credits

### Example


```python
import time
import wallet
from wallet.api import merchant_credits_api
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
    api_instance = merchant_credits_api.MerchantCreditsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch all active merchant credits
        api_response = api_instance.fetch_merchant_credit_count()
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantCreditsApi->fetch_merchant_credit_count: %s\n" % e)
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

# **fetch_merchant_credit_history_log**
> MSMerchantCreditHistoryPagination fetch_merchant_credit_history_log(pagination_request_with_id_and_without_sort_options)

Fetch history

### Example


```python
import time
import wallet
from wallet.api import merchant_credits_api
from wallet.model.pagination_request_with_id_and_without_sort_options import PaginationRequestWithIDAndWithoutSortOptions
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.ms_merchant_credit_history_pagination import MSMerchantCreditHistoryPagination
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = merchant_credits_api.MerchantCreditsApi(api_client)
    pagination_request_with_id_and_without_sort_options = PaginationRequestWithIDAndWithoutSortOptions(
        page_size=20,
        page_num=1,
        id=PrefixedNanoID("CMueJDL982Hs"),
    ) # PaginationRequestWithIDAndWithoutSortOptions | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch history
        api_response = api_instance.fetch_merchant_credit_history_log(pagination_request_with_id_and_without_sort_options)
        pprint(api_response)
    except wallet.ApiException as e:
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

Fetch redemption log

### Example


```python
import time
import wallet
from wallet.api import merchant_credits_api
from wallet.model.pagination_request_with_id_and_without_sort_options import PaginationRequestWithIDAndWithoutSortOptions
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.ms_merchant_credit_redemption_pagination import MSMerchantCreditRedemptionPagination
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
    api_instance = merchant_credits_api.MerchantCreditsApi(api_client)
    pagination_request_with_id_and_without_sort_options = PaginationRequestWithIDAndWithoutSortOptions(
        page_size=20,
        page_num=1,
        id=PrefixedNanoID("CMueJDL982Hs"),
    ) # PaginationRequestWithIDAndWithoutSortOptions | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch redemption log
        api_response = api_instance.fetch_merchant_credit_redemption_log(pagination_request_with_id_and_without_sort_options)
        pprint(api_response)
    except wallet.ApiException as e:
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
> [WTMerchantCredit] fetch_merchant_credits_by_page(pagination_request_with_sort_options)

Fetch merchant credits by page

### Example


```python
import time
import wallet
from wallet.api import merchant_credits_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.pagination_request_with_sort_options import PaginationRequestWithSortOptions
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_merchant_credit import WTMerchantCredit
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
    api_instance = merchant_credits_api.MerchantCreditsApi(api_client)
    pagination_request_with_sort_options = PaginationRequestWithSortOptions(
        is_archive_included=True,
        page_size=20,
        page_num=1,
        sort_key="createdAt",
        sort_order=None,
    ) # PaginationRequestWithSortOptions | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch merchant credits by page
        api_response = api_instance.fetch_merchant_credits_by_page(pagination_request_with_sort_options)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantCreditsApi->fetch_merchant_credits_by_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request_with_sort_options** | [**PaginationRequestWithSortOptions**](PaginationRequestWithSortOptions.md)|  |

### Return type

[**[WTMerchantCredit]**](WTMerchantCredit.md)

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

Restore merchant credit

### Example


```python
import time
import wallet
from wallet.api import merchant_credits_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_merchant_credit import WTMerchantCredit
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
    api_instance = merchant_credits_api.MerchantCreditsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore merchant credit
        api_response = api_instance.restore_merchant_credit(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantCreditsApi->restore_merchant_credit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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

Search for merchant credits

### Example


```python
import time
import wallet
from wallet.api import merchant_credits_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.merchant_credit_search import MerchantCreditSearch
from wallet.model.auth_error import AuthError
from wallet.model.paginated_wt_merchant_credits import PaginatedWTMerchantCredits
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = merchant_credits_api.MerchantCreditsApi(api_client)
    merchant_credit_search = MerchantCreditSearch(
        is_archive_included=True,
        page_size=20,
        page_num=1,
        key="MEM001",
    ) # MerchantCreditSearch | 

    # example passing only required values which don't have defaults set
    try:
        # Search for merchant credits
        api_response = api_instance.search_merchant_credits(merchant_credit_search)
        pprint(api_response)
    except wallet.ApiException as e:
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

Update merchant credit

### Example


```python
import time
import wallet
from wallet.api import merchant_credits_api
from wallet.model.pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number import PickWTMerchantCreditMemberIDOrCreditAmountOrMobileNumber
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_merchant_credit import WTMerchantCredit
from wallet.model.foreign_key_does_not_exist import ForeignKeyDoesNotExist
from wallet.model.auth_error import AuthError
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
    api_instance = merchant_credits_api.MerchantCreditsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number = PickWTMerchantCreditMemberIDOrCreditAmountOrMobileNumber(
        member_id="1hdue82",
        mobile_number="+18047552674",
        credit_amount=125,
    ) # PickWTMerchantCreditMemberIDOrCreditAmountOrMobileNumber | 

    # example passing only required values which don't have defaults set
    try:
        # Update merchant credit
        api_response = api_instance.update_merchant_credit(id, pick_wt_merchant_credit_member_idor_credit_amount_or_mobile_number)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling MerchantCreditsApi->update_merchant_credit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

