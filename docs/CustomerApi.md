# wallet.CustomerApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_active_vouchers**](CustomerApi.md#fetch_active_vouchers) | **GET** /v2/customer/vouchers/active | Get active static vouchers
[**fetch_all_vouchers**](CustomerApi.md#fetch_all_vouchers) | **GET** /v2/customer/vouchers/all | Get all static vouchers
[**fetch_expired_vouchers**](CustomerApi.md#fetch_expired_vouchers) | **GET** /v2/customer/vouchers/expired | Get expired static vouchers
[**fetch_redeemed_vouchers**](CustomerApi.md#fetch_redeemed_vouchers) | **GET** /v2/customer/vouchers/redeemed | Get redeemed static vouchers
[**fetch_refunded_vouchers**](CustomerApi.md#fetch_refunded_vouchers) | **GET** /v2/customer/vouchers/refunded | Get refunded static vouchers
[**fetch_upcoming_vouchers**](CustomerApi.md#fetch_upcoming_vouchers) | **GET** /v2/customer/vouchers/upcoming | Get upcoming static vouchers
[**fetch_wallet_views_for_session**](CustomerApi.md#fetch_wallet_views_for_session) | **GET** /v2/customer/walletViews/session/{id} | Get Wallet Views for Session
[**search_by_member_id**](CustomerApi.md#search_by_member_id) | **POST** /v2/customer/search/memberID | Find members with memberID
[**search_by_phone_number**](CustomerApi.md#search_by_phone_number) | **POST** /v2/customer/search/phoneNumber | Find members with phone number


# **fetch_active_vouchers**
> List[StaticVoucher] fetch_active_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)

Get active static vouchers

### Example


```python
import wallet
from wallet.models.static_voucher import StaticVoucher
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
    api_instance = wallet.CustomerApi(api_client)
    member_id = 'member_id_example' # str |  (optional)
    cell_phone_number = 'cell_phone_number_example' # str |  (optional)

    try:
        # Get active static vouchers
        api_response = api_instance.fetch_active_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)
        print("The response of CustomerApi->fetch_active_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerApi->fetch_active_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | [optional] 
 **cell_phone_number** | **str**|  | [optional] 

### Return type

[**List[StaticVoucher]**](StaticVoucher.md)

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
> List[StaticVoucher] fetch_all_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)

Get all static vouchers

### Example


```python
import wallet
from wallet.models.static_voucher import StaticVoucher
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
    api_instance = wallet.CustomerApi(api_client)
    member_id = 'member_id_example' # str |  (optional)
    cell_phone_number = 'cell_phone_number_example' # str |  (optional)

    try:
        # Get all static vouchers
        api_response = api_instance.fetch_all_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)
        print("The response of CustomerApi->fetch_all_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerApi->fetch_all_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | [optional] 
 **cell_phone_number** | **str**|  | [optional] 

### Return type

[**List[StaticVoucher]**](StaticVoucher.md)

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
> List[StaticVoucher] fetch_expired_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)

Get expired static vouchers

### Example


```python
import wallet
from wallet.models.static_voucher import StaticVoucher
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
    api_instance = wallet.CustomerApi(api_client)
    member_id = 'member_id_example' # str |  (optional)
    cell_phone_number = 'cell_phone_number_example' # str |  (optional)

    try:
        # Get expired static vouchers
        api_response = api_instance.fetch_expired_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)
        print("The response of CustomerApi->fetch_expired_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerApi->fetch_expired_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | [optional] 
 **cell_phone_number** | **str**|  | [optional] 

### Return type

[**List[StaticVoucher]**](StaticVoucher.md)

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
> List[StaticVoucher] fetch_redeemed_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)

Get redeemed static vouchers

### Example


```python
import wallet
from wallet.models.static_voucher import StaticVoucher
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
    api_instance = wallet.CustomerApi(api_client)
    member_id = 'member_id_example' # str |  (optional)
    cell_phone_number = 'cell_phone_number_example' # str |  (optional)

    try:
        # Get redeemed static vouchers
        api_response = api_instance.fetch_redeemed_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)
        print("The response of CustomerApi->fetch_redeemed_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerApi->fetch_redeemed_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | [optional] 
 **cell_phone_number** | **str**|  | [optional] 

### Return type

[**List[StaticVoucher]**](StaticVoucher.md)

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
> List[StaticVoucher] fetch_refunded_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)

Get refunded static vouchers

### Example


```python
import wallet
from wallet.models.static_voucher import StaticVoucher
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
    api_instance = wallet.CustomerApi(api_client)
    member_id = 'member_id_example' # str |  (optional)
    cell_phone_number = 'cell_phone_number_example' # str |  (optional)

    try:
        # Get refunded static vouchers
        api_response = api_instance.fetch_refunded_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)
        print("The response of CustomerApi->fetch_refunded_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerApi->fetch_refunded_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | [optional] 
 **cell_phone_number** | **str**|  | [optional] 

### Return type

[**List[StaticVoucher]**](StaticVoucher.md)

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
> List[StaticVoucher] fetch_upcoming_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)

Get upcoming static vouchers

### Example


```python
import wallet
from wallet.models.static_voucher import StaticVoucher
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
    api_instance = wallet.CustomerApi(api_client)
    member_id = 'member_id_example' # str |  (optional)
    cell_phone_number = 'cell_phone_number_example' # str |  (optional)

    try:
        # Get upcoming static vouchers
        api_response = api_instance.fetch_upcoming_vouchers(member_id=member_id, cell_phone_number=cell_phone_number)
        print("The response of CustomerApi->fetch_upcoming_vouchers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerApi->fetch_upcoming_vouchers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | [optional] 
 **cell_phone_number** | **str**|  | [optional] 

### Return type

[**List[StaticVoucher]**](StaticVoucher.md)

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
> List[WalletPageView] fetch_wallet_views_for_session(id)

Get Wallet Views for Session

### Example


```python
import wallet
from wallet.models.wallet_page_view import WalletPageView
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
    api_instance = wallet.CustomerApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Wallet Views for Session
        api_response = api_instance.fetch_wallet_views_for_session(id)
        print("The response of CustomerApi->fetch_wallet_views_for_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerApi->fetch_wallet_views_for_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[WalletPageView]**](WalletPageView.md)

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
> object search_by_member_id(wt_customer_search_by_member_id)

Find members with memberID

### Example


```python
import wallet
from wallet.models.wt_customer_search_by_member_id import WTCustomerSearchByMemberID
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
    api_instance = wallet.CustomerApi(api_client)
    wt_customer_search_by_member_id = wallet.WTCustomerSearchByMemberID() # WTCustomerSearchByMemberID | 

    try:
        # Find members with memberID
        api_response = api_instance.search_by_member_id(wt_customer_search_by_member_id)
        print("The response of CustomerApi->search_by_member_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerApi->search_by_member_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_customer_search_by_member_id** | [**WTCustomerSearchByMemberID**](WTCustomerSearchByMemberID.md)|  | 

### Return type

**object**

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
> object search_by_phone_number(wt_customer_search_by_phone_number)

Find members with phone number

### Example


```python
import wallet
from wallet.models.wt_customer_search_by_phone_number import WTCustomerSearchByPhoneNumber
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
    api_instance = wallet.CustomerApi(api_client)
    wt_customer_search_by_phone_number = wallet.WTCustomerSearchByPhoneNumber() # WTCustomerSearchByPhoneNumber | 

    try:
        # Find members with phone number
        api_response = api_instance.search_by_phone_number(wt_customer_search_by_phone_number)
        print("The response of CustomerApi->search_by_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerApi->search_by_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_customer_search_by_phone_number** | [**WTCustomerSearchByPhoneNumber**](WTCustomerSearchByPhoneNumber.md)|  | 

### Return type

**object**

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

