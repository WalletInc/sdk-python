# wallet.CustomerApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_active_vouchers**](CustomerApi.md#fetch_active_vouchers) | **GET** /v2/customer/vouchers/active | Fetch active static vouchers
[**fetch_all_vouchers**](CustomerApi.md#fetch_all_vouchers) | **GET** /v2/customer/vouchers/all | Fetch all static vouchers
[**fetch_expired_vouchers**](CustomerApi.md#fetch_expired_vouchers) | **GET** /v2/customer/vouchers/expired | Fetch expired static vouchers
[**fetch_redeemed_vouchers**](CustomerApi.md#fetch_redeemed_vouchers) | **GET** /v2/customer/vouchers/redeemed | Fetch redeemed static vouchers
[**fetch_refunded_vouchers**](CustomerApi.md#fetch_refunded_vouchers) | **GET** /v2/customer/vouchers/refunded | Fetch refunded static vouchers
[**fetch_upcoming_vouchers**](CustomerApi.md#fetch_upcoming_vouchers) | **GET** /v2/customer/vouchers/upcoming | Fetch upcoming static vouchers
[**fetch_wallet_views_for_session**](CustomerApi.md#fetch_wallet_views_for_session) | **GET** /v2/customer/walletViews/session/{id} | Fetch Wallet Views for Session
[**search_by_member_id**](CustomerApi.md#search_by_member_id) | **POST** /v2/customer/search/memberID | Find members with memberID
[**search_by_phone_number**](CustomerApi.md#search_by_phone_number) | **POST** /v2/customer/search/phoneNumber | Find members with phone number


# **fetch_active_vouchers**
> [StaticVoucher] fetch_active_vouchers()

Fetch active static vouchers

### Example


```python
import time
import wallet
from wallet.api import customer_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.static_voucher import StaticVoucher
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
    api_instance = customer_api.CustomerApi(api_client)
    member_id = "memberID_example" # str |  (optional)
    cell_phone_number = "cellPhoneNumber_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch active static vouchers
        api_response = api_instance.fetch_active_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling CustomerApi->fetch_active_vouchers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | [optional]
 **cell_phone_number** | **str**|  | [optional]

### Return type

[**[StaticVoucher]**](StaticVoucher.md)

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

# **fetch_all_vouchers**
> [StaticVoucher] fetch_all_vouchers()

Fetch all static vouchers

### Example


```python
import time
import wallet
from wallet.api import customer_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.static_voucher import StaticVoucher
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
    api_instance = customer_api.CustomerApi(api_client)
    member_id = "memberID_example" # str |  (optional)
    cell_phone_number = "cellPhoneNumber_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all static vouchers
        api_response = api_instance.fetch_all_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling CustomerApi->fetch_all_vouchers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | [optional]
 **cell_phone_number** | **str**|  | [optional]

### Return type

[**[StaticVoucher]**](StaticVoucher.md)

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

# **fetch_expired_vouchers**
> [StaticVoucher] fetch_expired_vouchers()

Fetch expired static vouchers

### Example


```python
import time
import wallet
from wallet.api import customer_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.static_voucher import StaticVoucher
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
    api_instance = customer_api.CustomerApi(api_client)
    member_id = "memberID_example" # str |  (optional)
    cell_phone_number = "cellPhoneNumber_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch expired static vouchers
        api_response = api_instance.fetch_expired_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling CustomerApi->fetch_expired_vouchers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | [optional]
 **cell_phone_number** | **str**|  | [optional]

### Return type

[**[StaticVoucher]**](StaticVoucher.md)

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

# **fetch_redeemed_vouchers**
> [StaticVoucher] fetch_redeemed_vouchers()

Fetch redeemed static vouchers

### Example


```python
import time
import wallet
from wallet.api import customer_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.static_voucher import StaticVoucher
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
    api_instance = customer_api.CustomerApi(api_client)
    member_id = "memberID_example" # str |  (optional)
    cell_phone_number = "cellPhoneNumber_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch redeemed static vouchers
        api_response = api_instance.fetch_redeemed_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling CustomerApi->fetch_redeemed_vouchers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | [optional]
 **cell_phone_number** | **str**|  | [optional]

### Return type

[**[StaticVoucher]**](StaticVoucher.md)

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

# **fetch_refunded_vouchers**
> [StaticVoucher] fetch_refunded_vouchers()

Fetch refunded static vouchers

### Example


```python
import time
import wallet
from wallet.api import customer_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.static_voucher import StaticVoucher
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
    api_instance = customer_api.CustomerApi(api_client)
    member_id = "memberID_example" # str |  (optional)
    cell_phone_number = "cellPhoneNumber_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch refunded static vouchers
        api_response = api_instance.fetch_refunded_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling CustomerApi->fetch_refunded_vouchers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | [optional]
 **cell_phone_number** | **str**|  | [optional]

### Return type

[**[StaticVoucher]**](StaticVoucher.md)

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

# **fetch_upcoming_vouchers**
> [StaticVoucher] fetch_upcoming_vouchers()

Fetch upcoming static vouchers

### Example


```python
import time
import wallet
from wallet.api import customer_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.static_voucher import StaticVoucher
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
    api_instance = customer_api.CustomerApi(api_client)
    member_id = "memberID_example" # str |  (optional)
    cell_phone_number = "cellPhoneNumber_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch upcoming static vouchers
        api_response = api_instance.fetch_upcoming_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling CustomerApi->fetch_upcoming_vouchers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | [optional]
 **cell_phone_number** | **str**|  | [optional]

### Return type

[**[StaticVoucher]**](StaticVoucher.md)

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

# **fetch_wallet_views_for_session**
> [WalletPageView] fetch_wallet_views_for_session(id)

Fetch Wallet Views for Session

### Example


```python
import time
import wallet
from wallet.api import customer_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wallet_page_view import WalletPageView
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
    api_instance = customer_api.CustomerApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch Wallet Views for Session
        api_response = api_instance.fetch_wallet_views_for_session(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling CustomerApi->fetch_wallet_views_for_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[WalletPageView]**](WalletPageView.md)

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

# **search_by_member_id**
> bool, date, datetime, dict, float, int, list, str, none_type search_by_member_id(wt_customer_search_by_member_id)

Find members with memberID

### Example


```python
import time
import wallet
from wallet.api import customer_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.auth_error import AuthError
from wallet.model.wt_customer_search_by_member_id import WTCustomerSearchByMemberID
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = customer_api.CustomerApi(api_client)
    wt_customer_search_by_member_id = WTCustomerSearchByMemberID(
        member_id="MEM0019",
    ) # WTCustomerSearchByMemberID | 

    # example passing only required values which don't have defaults set
    try:
        # Find members with memberID
        api_response = api_instance.search_by_member_id(wt_customer_search_by_member_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling CustomerApi->search_by_member_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_customer_search_by_member_id** | [**WTCustomerSearchByMemberID**](WTCustomerSearchByMemberID.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **search_by_phone_number**
> bool, date, datetime, dict, float, int, list, str, none_type search_by_phone_number(wt_customer_search_by_phone_number)

Find members with phone number

### Example


```python
import time
import wallet
from wallet.api import customer_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_customer_search_by_phone_number import WTCustomerSearchByPhoneNumber
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
    api_instance = customer_api.CustomerApi(api_client)
    wt_customer_search_by_phone_number = WTCustomerSearchByPhoneNumber(
        phone_number="+1809898989",
    ) # WTCustomerSearchByPhoneNumber | 

    # example passing only required values which don't have defaults set
    try:
        # Find members with phone number
        api_response = api_instance.search_by_phone_number(wt_customer_search_by_phone_number)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling CustomerApi->search_by_phone_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_customer_search_by_phone_number** | [**WTCustomerSearchByPhoneNumber**](WTCustomerSearchByPhoneNumber.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

