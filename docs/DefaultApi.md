# wallet.DefaultApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_dynamic_voucher_redeemed**](DefaultApi.md#customers_dynamic_voucher_redeemed) | **POST** /Customers.DynamicVoucher.redeemed | 
[**customers_dynamic_voucher_refunded**](DefaultApi.md#customers_dynamic_voucher_refunded) | **POST** /Customers.DynamicVoucher.refunded | 
[**customers_merchant_credit_redeemed**](DefaultApi.md#customers_merchant_credit_redeemed) | **POST** /Customers.MerchantCredit.redeemed | 
[**customers_merchant_credit_refunded**](DefaultApi.md#customers_merchant_credit_refunded) | **POST** /Customers.MerchantCredit.refunded | 
[**customers_prize_redeemed**](DefaultApi.md#customers_prize_redeemed) | **POST** /Customers.Prize.redeemed | 
[**customers_prize_refunded**](DefaultApi.md#customers_prize_refunded) | **POST** /Customers.Prize.refunded | 
[**customers_static_voucher_redeemed**](DefaultApi.md#customers_static_voucher_redeemed) | **POST** /Customers.StaticVoucher.redeemed | 
[**customers_static_voucher_refunded**](DefaultApi.md#customers_static_voucher_refunded) | **POST** /Customers.StaticVoucher.refunded | 
[**customers_ticket_claimed**](DefaultApi.md#customers_ticket_claimed) | **POST** /Customers.Ticket.claimed | 
[**customers_ticket_redeemed**](DefaultApi.md#customers_ticket_redeemed) | **POST** /Customers.Ticket.redeemed | 
[**customers_ticket_unclaimed**](DefaultApi.md#customers_ticket_unclaimed) | **POST** /Customers.Ticket.unclaimed | 
[**members_points_redeemed**](DefaultApi.md#members_points_redeemed) | **POST** /Members.Points.redeemed | 
[**members_points_refunded**](DefaultApi.md#members_points_refunded) | **POST** /Members.Points.refunded | 
[**members_tier_redeemed**](DefaultApi.md#members_tier_redeemed) | **POST** /Members.Tier.redeemed | 
[**members_tier_refunded**](DefaultApi.md#members_tier_refunded) | **POST** /Members.Tier.refunded | 
[**subscribers_email_opt_in**](DefaultApi.md#subscribers_email_opt_in) | **POST** /Subscribers.Email.opt_in | 
[**subscribers_sms_default_opt_in**](DefaultApi.md#subscribers_sms_default_opt_in) | **POST** /Subscribers.SMS.default_opt_in | 
[**subscribers_sms_keyword_opt_in**](DefaultApi.md#subscribers_sms_keyword_opt_in) | **POST** /Subscribers.SMS.keyword_opt_in | 
[**visitors_authentiation_success**](DefaultApi.md#visitors_authentiation_success) | **POST** /Visitors.Authentiation.success | 
[**visitors_business_card_downloaded**](DefaultApi.md#visitors_business_card_downloaded) | **POST** /Visitors.BusinessCard.downloaded | 
[**visitors_calendar_event_downloaded**](DefaultApi.md#visitors_calendar_event_downloaded) | **POST** /Visitors.CalendarEvent.downloaded | 
[**wallet_platform_add_on_purchased**](DefaultApi.md#wallet_platform_add_on_purchased) | **POST** /WalletPlatform.AddOn.purchased | 
[**wallet_platform_invoice_created**](DefaultApi.md#wallet_platform_invoice_created) | **POST** /WalletPlatform.Invoice.created | 
[**wallet_platform_invoice_paid**](DefaultApi.md#wallet_platform_invoice_paid) | **POST** /WalletPlatform.Invoice.paid | 
[**wallet_platform_ledger_entry_created**](DefaultApi.md#wallet_platform_ledger_entry_created) | **POST** /WalletPlatform.LedgerEntry.created | 
[**wallet_platform_payment_method_added**](DefaultApi.md#wallet_platform_payment_method_added) | **POST** /WalletPlatform.PaymentMethod.added | 
[**wallet_platform_subscription_changed**](DefaultApi.md#wallet_platform_subscription_changed) | **POST** /WalletPlatform.Subscription.changed | 


# **customers_dynamic_voucher_redeemed**
> customers_dynamic_voucher_redeemed(dynamic_voucher=dynamic_voucher)



A customer just redeemed a Dynamic Voucher.

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
    api_instance = wallet.DefaultApi(api_client)
    dynamic_voucher = wallet.DynamicVoucher() # DynamicVoucher |  (optional)

    try:
        api_instance.customers_dynamic_voucher_redeemed(dynamic_voucher=dynamic_voucher)
    except Exception as e:
        print("Exception when calling DefaultApi->customers_dynamic_voucher_redeemed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_voucher** | [**DynamicVoucher**](DynamicVoucher.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_dynamic_voucher_refunded**
> customers_dynamic_voucher_refunded(dynamic_voucher=dynamic_voucher)



A Dynamic Voucher was just refunded to the customer.

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
    api_instance = wallet.DefaultApi(api_client)
    dynamic_voucher = wallet.DynamicVoucher() # DynamicVoucher |  (optional)

    try:
        api_instance.customers_dynamic_voucher_refunded(dynamic_voucher=dynamic_voucher)
    except Exception as e:
        print("Exception when calling DefaultApi->customers_dynamic_voucher_refunded: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_voucher** | [**DynamicVoucher**](DynamicVoucher.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_merchant_credit_redeemed**
> customers_merchant_credit_redeemed(wt_merchant_credit=wt_merchant_credit)



A customer just redeemed some Merchant Credit.

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
    api_instance = wallet.DefaultApi(api_client)
    wt_merchant_credit = wallet.WTMerchantCredit() # WTMerchantCredit |  (optional)

    try:
        api_instance.customers_merchant_credit_redeemed(wt_merchant_credit=wt_merchant_credit)
    except Exception as e:
        print("Exception when calling DefaultApi->customers_merchant_credit_redeemed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_merchant_credit** | [**WTMerchantCredit**](WTMerchantCredit.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_merchant_credit_refunded**
> customers_merchant_credit_refunded(wt_merchant_credit=wt_merchant_credit)



Merchant Credit was just refunded to a customer.

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
    api_instance = wallet.DefaultApi(api_client)
    wt_merchant_credit = wallet.WTMerchantCredit() # WTMerchantCredit |  (optional)

    try:
        api_instance.customers_merchant_credit_refunded(wt_merchant_credit=wt_merchant_credit)
    except Exception as e:
        print("Exception when calling DefaultApi->customers_merchant_credit_refunded: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_merchant_credit** | [**WTMerchantCredit**](WTMerchantCredit.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_prize_redeemed**
> customers_prize_redeemed(advertisement_credit_scan=advertisement_credit_scan)



A customer just redeemed a Prize.

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
    api_instance = wallet.DefaultApi(api_client)
    advertisement_credit_scan = wallet.AdvertisementCreditScan() # AdvertisementCreditScan |  (optional)

    try:
        api_instance.customers_prize_redeemed(advertisement_credit_scan=advertisement_credit_scan)
    except Exception as e:
        print("Exception when calling DefaultApi->customers_prize_redeemed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisement_credit_scan** | [**AdvertisementCreditScan**](AdvertisementCreditScan.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_prize_refunded**
> customers_prize_refunded(advertisement_credit_scan=advertisement_credit_scan)



A Prize was just refunded to the customer.

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
    api_instance = wallet.DefaultApi(api_client)
    advertisement_credit_scan = wallet.AdvertisementCreditScan() # AdvertisementCreditScan |  (optional)

    try:
        api_instance.customers_prize_refunded(advertisement_credit_scan=advertisement_credit_scan)
    except Exception as e:
        print("Exception when calling DefaultApi->customers_prize_refunded: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertisement_credit_scan** | [**AdvertisementCreditScan**](AdvertisementCreditScan.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_static_voucher_redeemed**
> customers_static_voucher_redeemed(static_voucher=static_voucher)



A customer just redeemed a Static Voucher.

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
    api_instance = wallet.DefaultApi(api_client)
    static_voucher = wallet.StaticVoucher() # StaticVoucher |  (optional)

    try:
        api_instance.customers_static_voucher_redeemed(static_voucher=static_voucher)
    except Exception as e:
        print("Exception when calling DefaultApi->customers_static_voucher_redeemed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **static_voucher** | [**StaticVoucher**](StaticVoucher.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_static_voucher_refunded**
> customers_static_voucher_refunded(static_voucher=static_voucher)



A Static Voucher was just refunded to the customer.

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
    api_instance = wallet.DefaultApi(api_client)
    static_voucher = wallet.StaticVoucher() # StaticVoucher |  (optional)

    try:
        api_instance.customers_static_voucher_refunded(static_voucher=static_voucher)
    except Exception as e:
        print("Exception when calling DefaultApi->customers_static_voucher_refunded: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **static_voucher** | [**StaticVoucher**](StaticVoucher.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_ticket_claimed**
> customers_ticket_claimed(ticket=ticket)



A customer just claimed a Ticket.

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
    api_instance = wallet.DefaultApi(api_client)
    ticket = wallet.Ticket() # Ticket |  (optional)

    try:
        api_instance.customers_ticket_claimed(ticket=ticket)
    except Exception as e:
        print("Exception when calling DefaultApi->customers_ticket_claimed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket** | [**Ticket**](Ticket.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_ticket_redeemed**
> customers_ticket_redeemed(ticket=ticket)



A customer just redeemed a Ticket.

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
    api_instance = wallet.DefaultApi(api_client)
    ticket = wallet.Ticket() # Ticket |  (optional)

    try:
        api_instance.customers_ticket_redeemed(ticket=ticket)
    except Exception as e:
        print("Exception when calling DefaultApi->customers_ticket_redeemed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket** | [**Ticket**](Ticket.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_ticket_unclaimed**
> customers_ticket_unclaimed(ticket=ticket)



A customer just unclaimed a Ticket.

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
    api_instance = wallet.DefaultApi(api_client)
    ticket = wallet.Ticket() # Ticket |  (optional)

    try:
        api_instance.customers_ticket_unclaimed(ticket=ticket)
    except Exception as e:
        print("Exception when calling DefaultApi->customers_ticket_unclaimed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket** | [**Ticket**](Ticket.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_points_redeemed**
> members_points_redeemed(member=member)



A member just redeemed some Membership Points.

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
    api_instance = wallet.DefaultApi(api_client)
    member = wallet.Member() # Member |  (optional)

    try:
        api_instance.members_points_redeemed(member=member)
    except Exception as e:
        print("Exception when calling DefaultApi->members_points_redeemed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member** | [**Member**](Member.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_points_refunded**
> members_points_refunded(member=member)



Membership Points were just refunded to a member.

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
    api_instance = wallet.DefaultApi(api_client)
    member = wallet.Member() # Member |  (optional)

    try:
        api_instance.members_points_refunded(member=member)
    except Exception as e:
        print("Exception when calling DefaultApi->members_points_refunded: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member** | [**Member**](Member.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_tier_redeemed**
> members_tier_redeemed(wt_membership_tier=wt_membership_tier)



A member just redeemed a Membership Tier discount.

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
    api_instance = wallet.DefaultApi(api_client)
    wt_membership_tier = wallet.WTMembershipTier() # WTMembershipTier |  (optional)

    try:
        api_instance.members_tier_redeemed(wt_membership_tier=wt_membership_tier)
    except Exception as e:
        print("Exception when calling DefaultApi->members_tier_redeemed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_membership_tier** | [**WTMembershipTier**](WTMembershipTier.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_tier_refunded**
> members_tier_refunded(wt_membership_tier=wt_membership_tier)



A Membership Tier discount was just refunded to a member.

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
    api_instance = wallet.DefaultApi(api_client)
    wt_membership_tier = wallet.WTMembershipTier() # WTMembershipTier |  (optional)

    try:
        api_instance.members_tier_refunded(wt_membership_tier=wt_membership_tier)
    except Exception as e:
        print("Exception when calling DefaultApi->members_tier_refunded: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_membership_tier** | [**WTMembershipTier**](WTMembershipTier.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribers_email_opt_in**
> subscribers_email_opt_in(email_subscriber=email_subscriber)



A new subscriber has opted-in to receive your email communications.

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
    api_instance = wallet.DefaultApi(api_client)
    email_subscriber = wallet.EmailSubscriber() # EmailSubscriber |  (optional)

    try:
        api_instance.subscribers_email_opt_in(email_subscriber=email_subscriber)
    except Exception as e:
        print("Exception when calling DefaultApi->subscribers_email_opt_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_subscriber** | [**EmailSubscriber**](EmailSubscriber.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribers_sms_default_opt_in**
> subscribers_sms_default_opt_in(sms_subscriber=sms_subscriber)



A new subscriber has opted-in to your default SMS/MMS subscriber list.

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
    api_instance = wallet.DefaultApi(api_client)
    sms_subscriber = wallet.SmsSubscriber() # SmsSubscriber |  (optional)

    try:
        api_instance.subscribers_sms_default_opt_in(sms_subscriber=sms_subscriber)
    except Exception as e:
        print("Exception when calling DefaultApi->subscribers_sms_default_opt_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_subscriber** | [**SmsSubscriber**](SmsSubscriber.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribers_sms_keyword_opt_in**
> subscribers_sms_keyword_opt_in(opt_in_list_subscriber=opt_in_list_subscriber)



A new subscriber has opted-in to a specific list / keyword for specialised SMS/MMS communications.

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
    api_instance = wallet.DefaultApi(api_client)
    opt_in_list_subscriber = wallet.OptInListSubscriber() # OptInListSubscriber |  (optional)

    try:
        api_instance.subscribers_sms_keyword_opt_in(opt_in_list_subscriber=opt_in_list_subscriber)
    except Exception as e:
        print("Exception when calling DefaultApi->subscribers_sms_keyword_opt_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opt_in_list_subscriber** | [**OptInListSubscriber**](OptInListSubscriber.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visitors_authentiation_success**
> visitors_authentiation_success()



A visitor successfully authenticated with their mobile phone number and is now a recognized customer.

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
    api_instance = wallet.DefaultApi(api_client)

    try:
        api_instance.visitors_authentiation_success()
    except Exception as e:
        print("Exception when calling DefaultApi->visitors_authentiation_success: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visitors_business_card_downloaded**
> visitors_business_card_downloaded()



A visitor downloaded a Virtual Business Card.

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
    api_instance = wallet.DefaultApi(api_client)

    try:
        api_instance.visitors_business_card_downloaded()
    except Exception as e:
        print("Exception when calling DefaultApi->visitors_business_card_downloaded: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visitors_calendar_event_downloaded**
> visitors_calendar_event_downloaded()



A visitor downloaded a calendar reminder for one of your upcoming events.

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
    api_instance = wallet.DefaultApi(api_client)

    try:
        api_instance.visitors_calendar_event_downloaded()
    except Exception as e:
        print("Exception when calling DefaultApi->visitors_calendar_event_downloaded: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_platform_add_on_purchased**
> wallet_platform_add_on_purchased()



An optional add-on product / service was just purchased.

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
    api_instance = wallet.DefaultApi(api_client)

    try:
        api_instance.wallet_platform_add_on_purchased()
    except Exception as e:
        print("Exception when calling DefaultApi->wallet_platform_add_on_purchased: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_platform_invoice_created**
> wallet_platform_invoice_created()



A new invoice has been generated for your account.

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
    api_instance = wallet.DefaultApi(api_client)

    try:
        api_instance.wallet_platform_invoice_created()
    except Exception as e:
        print("Exception when calling DefaultApi->wallet_platform_invoice_created: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_platform_invoice_paid**
> wallet_platform_invoice_paid()



An invoice has just been paid for your account.

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
    api_instance = wallet.DefaultApi(api_client)

    try:
        api_instance.wallet_platform_invoice_paid()
    except Exception as e:
        print("Exception when calling DefaultApi->wallet_platform_invoice_paid: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_platform_ledger_entry_created**
> wallet_platform_ledger_entry_created(ledger_entry=ledger_entry)



A new ledger entry is created every time a redemption or refund event has occurred.

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
    api_instance = wallet.DefaultApi(api_client)
    ledger_entry = wallet.LedgerEntry() # LedgerEntry |  (optional)

    try:
        api_instance.wallet_platform_ledger_entry_created(ledger_entry=ledger_entry)
    except Exception as e:
        print("Exception when calling DefaultApi->wallet_platform_ledger_entry_created: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger_entry** | [**LedgerEntry**](LedgerEntry.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_platform_payment_method_added**
> wallet_platform_payment_method_added()



The payment method associated with your account has changed.

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
    api_instance = wallet.DefaultApi(api_client)

    try:
        api_instance.wallet_platform_payment_method_added()
    except Exception as e:
        print("Exception when calling DefaultApi->wallet_platform_payment_method_added: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_platform_subscription_changed**
> wallet_platform_subscription_changed()



A change to your billing subscription has been made.

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
    api_instance = wallet.DefaultApi(api_client)

    try:
        api_instance.wallet_platform_subscription_changed()
    except Exception as e:
        print("Exception when calling DefaultApi->wallet_platform_subscription_changed: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a 200 status to indicate that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

