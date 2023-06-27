# wallet.InteractionsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_advertisement_credit_scan**](InteractionsApi.md#create_advertisement_credit_scan) | **POST** /wallet/advertisementCredit/scan/{adCreditID} | Create ad credit scan
[**create_employee_v_card**](InteractionsApi.md#create_employee_v_card) | **GET** /wallet/employee/vcard/{id} | Fetch an employee&#39;s VCard
[**create_ics_file**](InteractionsApi.md#create_ics_file) | **GET** /wallet/liveevent/ics/{id} | Fetch ICS for live event
[**create_virtual_business_card_v_card**](InteractionsApi.md#create_virtual_business_card_v_card) | **GET** /wallet/virtualBusinessCard/vCard/{id} | Fetch an employee&#39;s VCard
[**fetch_all_static_vouchers_associated_with_customer_with_voucher_id**](InteractionsApi.md#fetch_all_static_vouchers_associated_with_customer_with_voucher_id) | **GET** /wallet/staticVoucher/all | Fetch a customer&#39;s static vouchers on the basis of a given voucher ID
[**fetch_dynamic_voucher_with_voucher_id**](InteractionsApi.md#fetch_dynamic_voucher_with_voucher_id) | **GET** /wallet/dynamicVoucher/{voucherID} | Fetch dynamic voucher
[**fetch_member_information**](InteractionsApi.md#fetch_member_information) | **GET** /wallet/member | Fetch member information
[**fetch_static_voucher_with_voucher_id**](InteractionsApi.md#fetch_static_voucher_with_voucher_id) | **GET** /wallet/staticVoucher/{voucherID} | Fetch static voucher
[**fetch_wallet_page_with_token**](InteractionsApi.md#fetch_wallet_page_with_token) | **POST** /wallet/page/token | Fetch page with token NOTE: This route exists because a token can completely change the dataset returned to the client. A simple fetch just logs the token with the request, but a fetchWithToken request can have a very different object returned to the client.
[**fetch_wallet_payment_object_with_token**](InteractionsApi.md#fetch_wallet_payment_object_with_token) | **POST** /wallet/paymentObject/token | Fetch payment object with token NOTE: This route exists because a token can completely change the dataset returned to the client. A simple fetch just logs the token with the request, but a fetchWithToken request can have a very different object returned to the client.
[**find_by_vanity_handle**](InteractionsApi.md#find_by_vanity_handle) | **GET** /wallet/vanityHandle/{handle} | Fetch vanity handle
[**identify_item**](InteractionsApi.md#identify_item) | **GET** /wallet/item/identify/{itemID} | Identify item
[**request_merchant_url_redirect**](InteractionsApi.md#request_merchant_url_redirect) | **POST** /wallet/merchantURL/{itemID} | Identify item
[**subscribe_email**](InteractionsApi.md#subscribe_email) | **POST** /wallet/subscribeEmail | Create email subscriber


# **create_advertisement_credit_scan**
> AdvertisementCreditScan create_advertisement_credit_scan(ad_credit_id)

Create ad credit scan

### Example


```python
import time
import wallet
from wallet.api import interactions_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.advertisement_credit_scan import AdvertisementCreditScan
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interactions_api.InteractionsApi(api_client)
    ad_credit_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Create ad credit scan
        api_response = api_instance.create_advertisement_credit_scan(ad_credit_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->create_advertisement_credit_scan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_credit_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**AdvertisementCreditScan**](AdvertisementCreditScan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee_v_card**
> str create_employee_v_card(id)

Fetch an employee's VCard

### Example


```python
import time
import wallet
from wallet.api import interactions_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interactions_api.InteractionsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch an employee's VCard
        api_response = api_instance.create_employee_v_card(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->create_employee_v_card: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ics_file**
> bool, date, datetime, dict, float, int, list, str, none_type create_ics_file(id)

Fetch ICS for live event

### Example


```python
import time
import wallet
from wallet.api import interactions_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interactions_api.InteractionsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch ICS for live event
        api_response = api_instance.create_ics_file(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->create_ics_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_business_card_v_card**
> str create_virtual_business_card_v_card(id)

Fetch an employee's VCard

### Example


```python
import time
import wallet
from wallet.api import interactions_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interactions_api.InteractionsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch an employee's VCard
        api_response = api_instance.create_virtual_business_card_v_card(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->create_virtual_business_card_v_card: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_all_static_vouchers_associated_with_customer_with_voucher_id**
> [InlineResponse2009] fetch_all_static_vouchers_associated_with_customer_with_voucher_id(voucher_id)

Fetch a customer's static vouchers on the basis of a given voucher ID

### Example


```python
import time
import wallet
from wallet.api import interactions_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.inline_response2009 import InlineResponse2009
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interactions_api.InteractionsApi(api_client)
    voucher_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch a customer's static vouchers on the basis of a given voucher ID
        api_response = api_instance.fetch_all_static_vouchers_associated_with_customer_with_voucher_id(voucher_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->fetch_all_static_vouchers_associated_with_customer_with_voucher_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**[InlineResponse2009]**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_dynamic_voucher_with_voucher_id**
> DynamicVoucher fetch_dynamic_voucher_with_voucher_id(voucher_id)

Fetch dynamic voucher

### Example


```python
import time
import wallet
from wallet.api import interactions_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.dynamic_voucher import DynamicVoucher
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interactions_api.InteractionsApi(api_client)
    voucher_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch dynamic voucher
        api_response = api_instance.fetch_dynamic_voucher_with_voucher_id(voucher_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->fetch_dynamic_voucher_with_voucher_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**DynamicVoucher**](DynamicVoucher.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_member_information**
> Member fetch_member_information(member_id, merchant_id)

Fetch member information

### Example


```python
import time
import wallet
from wallet.api import interactions_api
from wallet.model.member import Member
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.merchant_id import MerchantID
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interactions_api.InteractionsApi(api_client)
    member_id = "memberID_example" # str | 
    merchant_id = MerchantID("C") # MerchantID | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch member information
        api_response = api_instance.fetch_member_information(member_id, merchant_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->fetch_member_information: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  |
 **merchant_id** | **MerchantID**|  |

### Return type

[**Member**](Member.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_static_voucher_with_voucher_id**
> StaticVoucher fetch_static_voucher_with_voucher_id(voucher_id)

Fetch static voucher

### Example


```python
import time
import wallet
from wallet.api import interactions_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.static_voucher import StaticVoucher
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interactions_api.InteractionsApi(api_client)
    voucher_id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch static voucher
        api_response = api_instance.fetch_static_voucher_with_voucher_id(voucher_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->fetch_static_voucher_with_voucher_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**StaticVoucher**](StaticVoucher.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_wallet_page_with_token**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_wallet_page_with_token(wt_fetch_wallet_payment_object_with_token)

Fetch page with token NOTE: This route exists because a token can completely change the dataset returned to the client. A simple fetch just logs the token with the request, but a fetchWithToken request can have a very different object returned to the client.

### Example


```python
import time
import wallet
from wallet.api import interactions_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_fetch_wallet_payment_object_with_token import WTFetchWalletPaymentObjectWithToken
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interactions_api.InteractionsApi(api_client)
    wt_fetch_wallet_payment_object_with_token = WTFetchWalletPaymentObjectWithToken(
        phone_verification_token="nuh787247",
        merchant_id=MerchantID("C"),
        page_type="page_type_example",
        is_refresh=True,
        referrer="https://google.com",
    ) # WTFetchWalletPaymentObjectWithToken | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch page with token NOTE: This route exists because a token can completely change the dataset returned to the client. A simple fetch just logs the token with the request, but a fetchWithToken request can have a very different object returned to the client.
        api_response = api_instance.fetch_wallet_page_with_token(wt_fetch_wallet_payment_object_with_token)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->fetch_wallet_page_with_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_fetch_wallet_payment_object_with_token** | [**WTFetchWalletPaymentObjectWithToken**](WTFetchWalletPaymentObjectWithToken.md)|  |

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
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_wallet_payment_object_with_token**
> bool, date, datetime, dict, float, int, list, str, none_type fetch_wallet_payment_object_with_token(wt_fetch_wallet_payment_object_with_token)

Fetch payment object with token NOTE: This route exists because a token can completely change the dataset returned to the client. A simple fetch just logs the token with the request, but a fetchWithToken request can have a very different object returned to the client.

### Example


```python
import time
import wallet
from wallet.api import interactions_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_fetch_wallet_payment_object_with_token import WTFetchWalletPaymentObjectWithToken
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interactions_api.InteractionsApi(api_client)
    wt_fetch_wallet_payment_object_with_token = WTFetchWalletPaymentObjectWithToken(
        phone_verification_token="nuh787247",
        merchant_id=MerchantID("C"),
        page_type="page_type_example",
        is_refresh=True,
        referrer="https://google.com",
    ) # WTFetchWalletPaymentObjectWithToken | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch payment object with token NOTE: This route exists because a token can completely change the dataset returned to the client. A simple fetch just logs the token with the request, but a fetchWithToken request can have a very different object returned to the client.
        api_response = api_instance.fetch_wallet_payment_object_with_token(wt_fetch_wallet_payment_object_with_token)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->fetch_wallet_payment_object_with_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_fetch_wallet_payment_object_with_token** | [**WTFetchWalletPaymentObjectWithToken**](WTFetchWalletPaymentObjectWithToken.md)|  |

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
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_vanity_handle**
> WalletConfiguration find_by_vanity_handle(handle)

Fetch vanity handle

### Example


```python
import time
import wallet
from wallet.api import interactions_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wallet_configuration import WalletConfiguration
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interactions_api.InteractionsApi(api_client)
    handle = "handle_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch vanity handle
        api_response = api_instance.find_by_vanity_handle(handle)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->find_by_vanity_handle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handle** | **str**|  |

### Return type

[**WalletConfiguration**](WalletConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identify_item**
> bool, date, datetime, dict, float, int, list, str, none_type identify_item(item_id)

Identify item

### Example


```python
import time
import wallet
from wallet.api import interactions_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interactions_api.InteractionsApi(api_client)
    item_id = "itemID_example" # str | 
    is_refresh = True # bool |  (optional)
    phone_verification_token = "phoneVerificationToken_example" # str |  (optional)
    referrer = "referrer_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Identify item
        api_response = api_instance.identify_item(item_id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->identify_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Identify item
        api_response = api_instance.identify_item(item_id, is_refresh=is_refresh, phone_verification_token=phone_verification_token, referrer=referrer)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->identify_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  |
 **is_refresh** | **bool**|  | [optional]
 **phone_verification_token** | **str**|  | [optional]
 **referrer** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_merchant_url_redirect**
> bool, date, datetime, dict, float, int, list, str, none_type request_merchant_url_redirect(item_id, browser_details)

Identify item

### Example


```python
import time
import wallet
from wallet.api import interactions_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.browser_details import BrowserDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interactions_api.InteractionsApi(api_client)
    item_id = "itemID_example" # str | 
    browser_details = BrowserDetails(
        ip="ip_example",
        phone_verification_token="phone_verification_token_example",
        session_id="session_id_example",
        navigator_agent="navigator_agent_example",
        referrer="referrer_example",
    ) # BrowserDetails | 

    # example passing only required values which don't have defaults set
    try:
        # Identify item
        api_response = api_instance.request_merchant_url_redirect(item_id, browser_details)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->request_merchant_url_redirect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  |
 **browser_details** | [**BrowserDetails**](BrowserDetails.md)|  |

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
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_email**
> EmailSubscriber subscribe_email(wt_email_subscriber_create_params_wallet_ui)

Create email subscriber

### Example


```python
import time
import wallet
from wallet.api import interactions_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.email_subscriber import EmailSubscriber
from wallet.model.wt_email_subscriber_create_params_wallet_ui import WTEmailSubscriberCreateParamsWalletUI
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = interactions_api.InteractionsApi(api_client)
    wt_email_subscriber_create_params_wallet_ui = WTEmailSubscriberCreateParamsWalletUI(
        first_name="John",
        last_name="Smith",
        email_address="email_address_example",
        merchant_id=MerchantID("C"),
    ) # WTEmailSubscriberCreateParamsWalletUI | 

    # example passing only required values which don't have defaults set
    try:
        # Create email subscriber
        api_response = api_instance.subscribe_email(wt_email_subscriber_create_params_wallet_ui)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling InteractionsApi->subscribe_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_email_subscriber_create_params_wallet_ui** | [**WTEmailSubscriberCreateParamsWalletUI**](WTEmailSubscriberCreateParamsWalletUI.md)|  |

### Return type

[**EmailSubscriber**](EmailSubscriber.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

