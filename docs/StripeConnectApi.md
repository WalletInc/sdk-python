# wallet.StripeConnectApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connect_onboarding_link**](StripeConnectApi.md#create_connect_onboarding_link) | **POST** /v2/connect/account/onboarding-link | Create a Stripe Connect onboarding link Creates the merchant&#39;s STANDARD connected account on first call (pass-through model; the merchant owns their Stripe relationship) and returns a hosted onboarding link (single-use, expiring). returnUrl/refreshUrl are validated against the origin allowlist. Not a fund-moving write; 403 when the merchant&#39;s plan does not include Connect ecommerce.
[**fetch_connect_account_status**](StripeConnectApi.md#fetch_connect_account_status) | **GET** /v2/connect/account | Get Stripe Connect account status Observability for Flow B ecommerce: the connected-account id and capability flags for the authenticated merchant, plus the derived onboarding status and the server-side ecommerce eligibility flag. Returns the defined not-started shape (accountId null) rather than 404 when onboarding has not begun.
[**fetch_connect_payments_summary**](StripeConnectApi.md#fetch_connect_payments_summary) | **GET** /v2/connect/payments-summary | Get a read-only Connect payments summary Balances, recent payouts, and recent charges (up to 10 each) for the merchant&#39;s connected account, in Stripe minor units with currency codes. Read-only observability; Wallet is not in the Flow B money path.


# **create_connect_onboarding_link**
> WTConnectOnboardingLinkResponse create_connect_onboarding_link(wt_connect_onboarding_link_request)

Create a Stripe Connect onboarding link Creates the merchant's STANDARD connected account on first call (pass-through model; the merchant owns their Stripe relationship) and returns a hosted onboarding link (single-use, expiring). returnUrl/refreshUrl are validated against the origin allowlist. Not a fund-moving write; 403 when the merchant's plan does not include Connect ecommerce.

### Example


```python
import wallet
from wallet.models.wt_connect_onboarding_link_request import WTConnectOnboardingLinkRequest
from wallet.models.wt_connect_onboarding_link_response import WTConnectOnboardingLinkResponse
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
    api_instance = wallet.StripeConnectApi(api_client)
    wt_connect_onboarding_link_request = wallet.WTConnectOnboardingLinkRequest() # WTConnectOnboardingLinkRequest | 

    try:
        # Create a Stripe Connect onboarding link Creates the merchant's STANDARD connected account on first call (pass-through model; the merchant owns their Stripe relationship) and returns a hosted onboarding link (single-use, expiring). returnUrl/refreshUrl are validated against the origin allowlist. Not a fund-moving write; 403 when the merchant's plan does not include Connect ecommerce.
        api_response = api_instance.create_connect_onboarding_link(wt_connect_onboarding_link_request)
        print("The response of StripeConnectApi->create_connect_onboarding_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeConnectApi->create_connect_onboarding_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_connect_onboarding_link_request** | [**WTConnectOnboardingLinkRequest**](WTConnectOnboardingLinkRequest.md)|  | 

### Return type

[**WTConnectOnboardingLinkResponse**](WTConnectOnboardingLinkResponse.md)

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

# **fetch_connect_account_status**
> WTConnectAccountStatus fetch_connect_account_status()

Get Stripe Connect account status Observability for Flow B ecommerce: the connected-account id and capability flags for the authenticated merchant, plus the derived onboarding status and the server-side ecommerce eligibility flag. Returns the defined not-started shape (accountId null) rather than 404 when onboarding has not begun.

### Example


```python
import wallet
from wallet.models.wt_connect_account_status import WTConnectAccountStatus
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
    api_instance = wallet.StripeConnectApi(api_client)

    try:
        # Get Stripe Connect account status Observability for Flow B ecommerce: the connected-account id and capability flags for the authenticated merchant, plus the derived onboarding status and the server-side ecommerce eligibility flag. Returns the defined not-started shape (accountId null) rather than 404 when onboarding has not begun.
        api_response = api_instance.fetch_connect_account_status()
        print("The response of StripeConnectApi->fetch_connect_account_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeConnectApi->fetch_connect_account_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WTConnectAccountStatus**](WTConnectAccountStatus.md)

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

# **fetch_connect_payments_summary**
> WTConnectPaymentsSummary fetch_connect_payments_summary()

Get a read-only Connect payments summary Balances, recent payouts, and recent charges (up to 10 each) for the merchant's connected account, in Stripe minor units with currency codes. Read-only observability; Wallet is not in the Flow B money path.

### Example


```python
import wallet
from wallet.models.wt_connect_payments_summary import WTConnectPaymentsSummary
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
    api_instance = wallet.StripeConnectApi(api_client)

    try:
        # Get a read-only Connect payments summary Balances, recent payouts, and recent charges (up to 10 each) for the merchant's connected account, in Stripe minor units with currency codes. Read-only observability; Wallet is not in the Flow B money path.
        api_response = api_instance.fetch_connect_payments_summary()
        print("The response of StripeConnectApi->fetch_connect_payments_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeConnectApi->fetch_connect_payments_summary: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WTConnectPaymentsSummary**](WTConnectPaymentsSummary.md)

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

