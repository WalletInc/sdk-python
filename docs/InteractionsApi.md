# wallet.InteractionsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claim_ticket**](InteractionsApi.md#claim_ticket) | **PUT** /wallet/ticket/claim/{id} | Update ticket
[**create_advertisement_credit_scan**](InteractionsApi.md#create_advertisement_credit_scan) | **POST** /wallet/advertisementCredit/scan/{adCreditID} | Create ad credit scan
[**create_employee_v_card**](InteractionsApi.md#create_employee_v_card) | **GET** /wallet/employee/vcard/{id} | Fetch an employee&#39;s VCard
[**create_ics_file**](InteractionsApi.md#create_ics_file) | **GET** /wallet/liveevent/ics/{id} | Fetch ICS for live event
[**create_virtual_business_card_v_card**](InteractionsApi.md#create_virtual_business_card_v_card) | **GET** /wallet/virtualBusinessCard/vCard/{id} | Fetch an employee&#39;s VCard
[**fetch_all_static_vouchers_associated_with_customer_with_voucher_id**](InteractionsApi.md#fetch_all_static_vouchers_associated_with_customer_with_voucher_id) | **GET** /wallet/staticVoucher/all | Fetch a customer&#39;s static vouchers on the basis of a given voucher ID
[**fetch_customer_tickets_with_token**](InteractionsApi.md#fetch_customer_tickets_with_token) | **POST** /wallet/tickets/fetchCustomerTicketsWithToken | Update ticket
[**fetch_dynamic_voucher_with_voucher_id**](InteractionsApi.md#fetch_dynamic_voucher_with_voucher_id) | **GET** /wallet/dynamicVoucher/{voucherID} | Fetch dynamic voucher
[**fetch_member_information**](InteractionsApi.md#fetch_member_information) | **GET** /wallet/member | Fetch member information
[**fetch_static_voucher_with_voucher_id**](InteractionsApi.md#fetch_static_voucher_with_voucher_id) | **GET** /wallet/staticVoucher/{voucherID} | Fetch static voucher
[**fetch_wallet_page_with_token**](InteractionsApi.md#fetch_wallet_page_with_token) | **POST** /wallet/page/token | Fetch page with token NOTE: This route exists because a token can completely change the dataset returned to the client. A simple fetch just logs the token with the request, but a fetchWithToken request can have a very different object returned to the client.
[**fetch_wallet_payment_objects_with_token**](InteractionsApi.md#fetch_wallet_payment_objects_with_token) | **POST** /wallet/paymentObject/token | Fetch payment objects with token NOTE: This route exists because a token can completely change the dataset returned to the client. A simple fetch just logs the token with the request, but a fetchWithToken request can have a very different object returned to the client.
[**find_by_vanity_handle**](InteractionsApi.md#find_by_vanity_handle) | **GET** /wallet/vanityHandle/{handle} | Fetch vanity handle
[**identify_item**](InteractionsApi.md#identify_item) | **GET** /wallet/item/identify/{itemID} | Identify item
[**request_merchant_url_redirect**](InteractionsApi.md#request_merchant_url_redirect) | **POST** /wallet/merchantURL/{itemID} | Request Merchant URL
[**subscribe_email**](InteractionsApi.md#subscribe_email) | **POST** /wallet/subscribeEmail | Create email subscriber
[**subscribe_sms**](InteractionsApi.md#subscribe_sms) | **POST** /wallet/subscribeSms | Create sms subscriber


# **claim_ticket**
> Ticket claim_ticket(id, claim_ticket_request)

Update ticket

### Example


```python
import wallet
from wallet.models.claim_ticket_request import ClaimTicketRequest
from wallet.models.ticket import Ticket
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
    api_instance = wallet.InteractionsApi(api_client)
    id = None # object | 
    claim_ticket_request = wallet.ClaimTicketRequest() # ClaimTicketRequest | 

    try:
        # Update ticket
        api_response = api_instance.claim_ticket(id, claim_ticket_request)
        print("The response of InteractionsApi->claim_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->claim_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **claim_ticket_request** | [**ClaimTicketRequest**](ClaimTicketRequest.md)|  | 

### Return type

[**Ticket**](Ticket.md)

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

# **create_advertisement_credit_scan**
> AdvertisementCreditScan create_advertisement_credit_scan(ad_credit_id)

Create ad credit scan

### Example


```python
import wallet
from wallet.models.advertisement_credit_scan import AdvertisementCreditScan
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
    api_instance = wallet.InteractionsApi(api_client)
    ad_credit_id = None # object | 

    try:
        # Create ad credit scan
        api_response = api_instance.create_advertisement_credit_scan(ad_credit_id)
        print("The response of InteractionsApi->create_advertisement_credit_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->create_advertisement_credit_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ad_credit_id** | [**object**](.md)|  | 

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
import wallet
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
    api_instance = wallet.InteractionsApi(api_client)
    id = None # object | 

    try:
        # Fetch an employee's VCard
        api_response = api_instance.create_employee_v_card(id)
        print("The response of InteractionsApi->create_employee_v_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->create_employee_v_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
> object create_ics_file(id)

Fetch ICS for live event

### Example


```python
import wallet
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
    api_instance = wallet.InteractionsApi(api_client)
    id = None # object | 

    try:
        # Fetch ICS for live event
        api_response = api_instance.create_ics_file(id)
        print("The response of InteractionsApi->create_ics_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->create_ics_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

**object**

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
import wallet
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
    api_instance = wallet.InteractionsApi(api_client)
    id = None # object | 

    try:
        # Fetch an employee's VCard
        api_response = api_instance.create_virtual_business_card_v_card(id)
        print("The response of InteractionsApi->create_virtual_business_card_v_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->create_virtual_business_card_v_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
> List[FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInner] fetch_all_static_vouchers_associated_with_customer_with_voucher_id(voucher_id)

Fetch a customer's static vouchers on the basis of a given voucher ID

### Example


```python
import wallet
from wallet.models.fetch_all_static_vouchers_associated_with_customer_with_voucher_id200_response_inner import FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInner
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
    api_instance = wallet.InteractionsApi(api_client)
    voucher_id = None # object | 

    try:
        # Fetch a customer's static vouchers on the basis of a given voucher ID
        api_response = api_instance.fetch_all_static_vouchers_associated_with_customer_with_voucher_id(voucher_id)
        print("The response of InteractionsApi->fetch_all_static_vouchers_associated_with_customer_with_voucher_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->fetch_all_static_vouchers_associated_with_customer_with_voucher_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_id** | [**object**](.md)|  | 

### Return type

[**List[FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInner]**](FetchAllStaticVouchersAssociatedWithCustomerWithVoucherID200ResponseInner.md)

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

# **fetch_customer_tickets_with_token**
> List[Ticket] fetch_customer_tickets_with_token(fetch_customer_tickets_with_token_request)

Update ticket

### Example


```python
import wallet
from wallet.models.fetch_customer_tickets_with_token_request import FetchCustomerTicketsWithTokenRequest
from wallet.models.ticket import Ticket
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
    api_instance = wallet.InteractionsApi(api_client)
    fetch_customer_tickets_with_token_request = wallet.FetchCustomerTicketsWithTokenRequest() # FetchCustomerTicketsWithTokenRequest | 

    try:
        # Update ticket
        api_response = api_instance.fetch_customer_tickets_with_token(fetch_customer_tickets_with_token_request)
        print("The response of InteractionsApi->fetch_customer_tickets_with_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->fetch_customer_tickets_with_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_customer_tickets_with_token_request** | [**FetchCustomerTicketsWithTokenRequest**](FetchCustomerTicketsWithTokenRequest.md)|  | 

### Return type

[**List[Ticket]**](Ticket.md)

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

# **fetch_dynamic_voucher_with_voucher_id**
> DynamicVoucher fetch_dynamic_voucher_with_voucher_id(voucher_id)

Fetch dynamic voucher

### Example


```python
import wallet
from wallet.models.dynamic_voucher import DynamicVoucher
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
    api_instance = wallet.InteractionsApi(api_client)
    voucher_id = None # object | 

    try:
        # Fetch dynamic voucher
        api_response = api_instance.fetch_dynamic_voucher_with_voucher_id(voucher_id)
        print("The response of InteractionsApi->fetch_dynamic_voucher_with_voucher_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->fetch_dynamic_voucher_with_voucher_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_id** | [**object**](.md)|  | 

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
import wallet
from wallet.models.member import Member
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
    api_instance = wallet.InteractionsApi(api_client)
    member_id = 'member_id_example' # str | 
    merchant_id = 'merchant_id_example' # str | 

    try:
        # Fetch member information
        api_response = api_instance.fetch_member_information(member_id, merchant_id)
        print("The response of InteractionsApi->fetch_member_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->fetch_member_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**|  | 
 **merchant_id** | **str**|  | 

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
    api_instance = wallet.InteractionsApi(api_client)
    voucher_id = None # object | 

    try:
        # Fetch static voucher
        api_response = api_instance.fetch_static_voucher_with_voucher_id(voucher_id)
        print("The response of InteractionsApi->fetch_static_voucher_with_voucher_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->fetch_static_voucher_with_voucher_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voucher_id** | [**object**](.md)|  | 

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
> object fetch_wallet_page_with_token(wt_fetch_wallet_payment_objects_with_token)

Fetch page with token NOTE: This route exists because a token can completely change the dataset returned to the client. A simple fetch just logs the token with the request, but a fetchWithToken request can have a very different object returned to the client.

### Example


```python
import wallet
from wallet.models.wt_fetch_wallet_payment_objects_with_token import WTFetchWalletPaymentObjectsWithToken
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
    api_instance = wallet.InteractionsApi(api_client)
    wt_fetch_wallet_payment_objects_with_token = wallet.WTFetchWalletPaymentObjectsWithToken() # WTFetchWalletPaymentObjectsWithToken | 

    try:
        # Fetch page with token NOTE: This route exists because a token can completely change the dataset returned to the client. A simple fetch just logs the token with the request, but a fetchWithToken request can have a very different object returned to the client.
        api_response = api_instance.fetch_wallet_page_with_token(wt_fetch_wallet_payment_objects_with_token)
        print("The response of InteractionsApi->fetch_wallet_page_with_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->fetch_wallet_page_with_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_fetch_wallet_payment_objects_with_token** | [**WTFetchWalletPaymentObjectsWithToken**](WTFetchWalletPaymentObjectsWithToken.md)|  | 

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
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_wallet_payment_objects_with_token**
> object fetch_wallet_payment_objects_with_token(wt_fetch_wallet_payment_objects_with_token)

Fetch payment objects with token NOTE: This route exists because a token can completely change the dataset returned to the client. A simple fetch just logs the token with the request, but a fetchWithToken request can have a very different object returned to the client.

### Example


```python
import wallet
from wallet.models.wt_fetch_wallet_payment_objects_with_token import WTFetchWalletPaymentObjectsWithToken
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
    api_instance = wallet.InteractionsApi(api_client)
    wt_fetch_wallet_payment_objects_with_token = wallet.WTFetchWalletPaymentObjectsWithToken() # WTFetchWalletPaymentObjectsWithToken | 

    try:
        # Fetch payment objects with token NOTE: This route exists because a token can completely change the dataset returned to the client. A simple fetch just logs the token with the request, but a fetchWithToken request can have a very different object returned to the client.
        api_response = api_instance.fetch_wallet_payment_objects_with_token(wt_fetch_wallet_payment_objects_with_token)
        print("The response of InteractionsApi->fetch_wallet_payment_objects_with_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->fetch_wallet_payment_objects_with_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_fetch_wallet_payment_objects_with_token** | [**WTFetchWalletPaymentObjectsWithToken**](WTFetchWalletPaymentObjectsWithToken.md)|  | 

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
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_vanity_handle**
> WalletConfiguration find_by_vanity_handle(handle)

Fetch vanity handle

### Example


```python
import wallet
from wallet.models.wallet_configuration import WalletConfiguration
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
    api_instance = wallet.InteractionsApi(api_client)
    handle = 'handle_example' # str | 

    try:
        # Fetch vanity handle
        api_response = api_instance.find_by_vanity_handle(handle)
        print("The response of InteractionsApi->find_by_vanity_handle:\n")
        pprint(api_response)
    except Exception as e:
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
> object identify_item(item_id, is_refresh=is_refresh, phone_verification_token=phone_verification_token, referrer=referrer)

Identify item

### Example


```python
import wallet
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
    api_instance = wallet.InteractionsApi(api_client)
    item_id = 'item_id_example' # str | 
    is_refresh = True # bool |  (optional)
    phone_verification_token = 'phone_verification_token_example' # str |  (optional)
    referrer = 'referrer_example' # str |  (optional)

    try:
        # Identify item
        api_response = api_instance.identify_item(item_id, is_refresh=is_refresh, phone_verification_token=phone_verification_token, referrer=referrer)
        print("The response of InteractionsApi->identify_item:\n")
        pprint(api_response)
    except Exception as e:
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

**object**

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
> object request_merchant_url_redirect(item_id, browser_details)

Request Merchant URL

### Example


```python
import wallet
from wallet.models.browser_details import BrowserDetails
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
    api_instance = wallet.InteractionsApi(api_client)
    item_id = 'item_id_example' # str | 
    browser_details = wallet.BrowserDetails() # BrowserDetails | 

    try:
        # Request Merchant URL
        api_response = api_instance.request_merchant_url_redirect(item_id, browser_details)
        print("The response of InteractionsApi->request_merchant_url_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->request_merchant_url_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **browser_details** | [**BrowserDetails**](BrowserDetails.md)|  | 

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
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_email**
> EmailSubscriber subscribe_email(wt_email_subscriber_create_params_wallet_ui)

Create email subscriber

### Example


```python
import wallet
from wallet.models.email_subscriber import EmailSubscriber
from wallet.models.wt_email_subscriber_create_params_wallet_ui import WTEmailSubscriberCreateParamsWalletUI
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
    api_instance = wallet.InteractionsApi(api_client)
    wt_email_subscriber_create_params_wallet_ui = wallet.WTEmailSubscriberCreateParamsWalletUI() # WTEmailSubscriberCreateParamsWalletUI | 

    try:
        # Create email subscriber
        api_response = api_instance.subscribe_email(wt_email_subscriber_create_params_wallet_ui)
        print("The response of InteractionsApi->subscribe_email:\n")
        pprint(api_response)
    except Exception as e:
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

# **subscribe_sms**
> SmsSubscriber subscribe_sms(wt_sms_subscriber_create_params_wallet_ui)

Create sms subscriber

### Example


```python
import wallet
from wallet.models.sms_subscriber import SmsSubscriber
from wallet.models.wt_sms_subscriber_create_params_wallet_ui import WTSmsSubscriberCreateParamsWalletUI
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
    api_instance = wallet.InteractionsApi(api_client)
    wt_sms_subscriber_create_params_wallet_ui = wallet.WTSmsSubscriberCreateParamsWalletUI() # WTSmsSubscriberCreateParamsWalletUI | 

    try:
        # Create sms subscriber
        api_response = api_instance.subscribe_sms(wt_sms_subscriber_create_params_wallet_ui)
        print("The response of InteractionsApi->subscribe_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->subscribe_sms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_sms_subscriber_create_params_wallet_ui** | [**WTSmsSubscriberCreateParamsWalletUI**](WTSmsSubscriberCreateParamsWalletUI.md)|  | 

### Return type

[**SmsSubscriber**](SmsSubscriber.md)

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

