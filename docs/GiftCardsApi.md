# wallet.GiftCardsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claim_gift**](GiftCardsApi.md#claim_gift) | **POST** /giftcards/{giftID}/claim | Claim a gifted card or certificate Claims a gift into the recipient&#39;s wallet (guest-to-guest). For a certificate with the gift-redemption requirement, the claimer must be someone other than the purchaser.
[**create_certificate_deal**](GiftCardsApi.md#create_certificate_deal) | **POST** /giftcards/deals | Create a gift-certificate deal (draft) Creates the discounted \&quot;deal\&quot; template (product/service entitlement, retail + sale price, quantity, validity) as a DRAFT. It is not purchasable until published. Authoring a draft does not require Stripe Connect.
[**fetch_certificate_deal**](GiftCardsApi.md#fetch_certificate_deal) | **GET** /giftcards/deals/{dealID} | Fetch a certificate deal by id
[**fetch_gift**](GiftCardsApi.md#fetch_gift) | **GET** /giftcards/{giftID} | Fetch a gift card or certificate by id
[**publish_certificate_deal**](GiftCardsApi.md#publish_certificate_deal) | **POST** /giftcards/deals/{dealID}/publish | Publish a certificate deal (put it on sale) Flips a draft deal live so guests can buy certificates from it. Requires the merchant&#39;s Stripe Connect account to be active (charges enabled), since a purchase is a direct charge to that account.
[**purchase_certificate_from_deal**](GiftCardsApi.md#purchase_certificate_from_deal) | **POST** /giftcards/deals/{dealID}/purchase | Purchase a certificate from a deal Runs the (mock) Connect direct charge of the deal&#39;s discounted sale price to the merchant, then mints a single-use certificate from the deal. Optionally gifts it to a recipient.
[**purchase_gift_card**](GiftCardsApi.md#purchase_gift_card) | **POST** /giftcards/purchase | Purchase a gift card Runs the (mock) Connect direct charge to the merchant, then issues a funded, reloadable gift card. Optionally gifts it to a recipient. Requires the merchant&#39;s Stripe Connect account to be active (charges enabled).


# **claim_gift**
> object claim_gift(gift_id, wt_gift_claim_request)

Claim a gifted card or certificate Claims a gift into the recipient's wallet (guest-to-guest). For a certificate with the gift-redemption requirement, the claimer must be someone other than the purchaser.

### Example


```python
import wallet
from wallet.models.wt_gift_claim_request import WTGiftClaimRequest
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
    api_instance = wallet.GiftCardsApi(api_client)
    gift_id = 'gift_id_example' # str | 
    wt_gift_claim_request = wallet.WTGiftClaimRequest() # WTGiftClaimRequest | 

    try:
        # Claim a gifted card or certificate Claims a gift into the recipient's wallet (guest-to-guest). For a certificate with the gift-redemption requirement, the claimer must be someone other than the purchaser.
        api_response = api_instance.claim_gift(gift_id, wt_gift_claim_request)
        print("The response of GiftCardsApi->claim_gift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardsApi->claim_gift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_id** | **str**|  | 
 **wt_gift_claim_request** | [**WTGiftClaimRequest**](WTGiftClaimRequest.md)|  | 

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

# **create_certificate_deal**
> object create_certificate_deal(wt_certificate_deal_create_request)

Create a gift-certificate deal (draft) Creates the discounted \"deal\" template (product/service entitlement, retail + sale price, quantity, validity) as a DRAFT. It is not purchasable until published. Authoring a draft does not require Stripe Connect.

### Example


```python
import wallet
from wallet.models.wt_certificate_deal_create_request import WTCertificateDealCreateRequest
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
    api_instance = wallet.GiftCardsApi(api_client)
    wt_certificate_deal_create_request = wallet.WTCertificateDealCreateRequest() # WTCertificateDealCreateRequest | 

    try:
        # Create a gift-certificate deal (draft) Creates the discounted \"deal\" template (product/service entitlement, retail + sale price, quantity, validity) as a DRAFT. It is not purchasable until published. Authoring a draft does not require Stripe Connect.
        api_response = api_instance.create_certificate_deal(wt_certificate_deal_create_request)
        print("The response of GiftCardsApi->create_certificate_deal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardsApi->create_certificate_deal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_certificate_deal_create_request** | [**WTCertificateDealCreateRequest**](WTCertificateDealCreateRequest.md)|  | 

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

# **fetch_certificate_deal**
> object fetch_certificate_deal(deal_id)

Fetch a certificate deal by id

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
    api_instance = wallet.GiftCardsApi(api_client)
    deal_id = 'deal_id_example' # str | 

    try:
        # Fetch a certificate deal by id
        api_response = api_instance.fetch_certificate_deal(deal_id)
        print("The response of GiftCardsApi->fetch_certificate_deal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardsApi->fetch_certificate_deal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deal_id** | **str**|  | 

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
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_gift**
> object fetch_gift(gift_id)

Fetch a gift card or certificate by id

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
    api_instance = wallet.GiftCardsApi(api_client)
    gift_id = 'gift_id_example' # str | 

    try:
        # Fetch a gift card or certificate by id
        api_response = api_instance.fetch_gift(gift_id)
        print("The response of GiftCardsApi->fetch_gift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardsApi->fetch_gift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gift_id** | **str**|  | 

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
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_certificate_deal**
> object publish_certificate_deal(deal_id)

Publish a certificate deal (put it on sale) Flips a draft deal live so guests can buy certificates from it. Requires the merchant's Stripe Connect account to be active (charges enabled), since a purchase is a direct charge to that account.

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
    api_instance = wallet.GiftCardsApi(api_client)
    deal_id = 'deal_id_example' # str | 

    try:
        # Publish a certificate deal (put it on sale) Flips a draft deal live so guests can buy certificates from it. Requires the merchant's Stripe Connect account to be active (charges enabled), since a purchase is a direct charge to that account.
        api_response = api_instance.publish_certificate_deal(deal_id)
        print("The response of GiftCardsApi->publish_certificate_deal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardsApi->publish_certificate_deal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deal_id** | **str**|  | 

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
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_certificate_from_deal**
> object purchase_certificate_from_deal(deal_id, wt_certificate_purchase_request)

Purchase a certificate from a deal Runs the (mock) Connect direct charge of the deal's discounted sale price to the merchant, then mints a single-use certificate from the deal. Optionally gifts it to a recipient.

### Example


```python
import wallet
from wallet.models.wt_certificate_purchase_request import WTCertificatePurchaseRequest
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
    api_instance = wallet.GiftCardsApi(api_client)
    deal_id = 'deal_id_example' # str | 
    wt_certificate_purchase_request = wallet.WTCertificatePurchaseRequest() # WTCertificatePurchaseRequest | 

    try:
        # Purchase a certificate from a deal Runs the (mock) Connect direct charge of the deal's discounted sale price to the merchant, then mints a single-use certificate from the deal. Optionally gifts it to a recipient.
        api_response = api_instance.purchase_certificate_from_deal(deal_id, wt_certificate_purchase_request)
        print("The response of GiftCardsApi->purchase_certificate_from_deal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardsApi->purchase_certificate_from_deal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deal_id** | **str**|  | 
 **wt_certificate_purchase_request** | [**WTCertificatePurchaseRequest**](WTCertificatePurchaseRequest.md)|  | 

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

# **purchase_gift_card**
> object purchase_gift_card(wt_gift_card_purchase_request)

Purchase a gift card Runs the (mock) Connect direct charge to the merchant, then issues a funded, reloadable gift card. Optionally gifts it to a recipient. Requires the merchant's Stripe Connect account to be active (charges enabled).

### Example


```python
import wallet
from wallet.models.wt_gift_card_purchase_request import WTGiftCardPurchaseRequest
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
    api_instance = wallet.GiftCardsApi(api_client)
    wt_gift_card_purchase_request = wallet.WTGiftCardPurchaseRequest() # WTGiftCardPurchaseRequest | 

    try:
        # Purchase a gift card Runs the (mock) Connect direct charge to the merchant, then issues a funded, reloadable gift card. Optionally gifts it to a recipient. Requires the merchant's Stripe Connect account to be active (charges enabled).
        api_response = api_instance.purchase_gift_card(wt_gift_card_purchase_request)
        print("The response of GiftCardsApi->purchase_gift_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GiftCardsApi->purchase_gift_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_gift_card_purchase_request** | [**WTGiftCardPurchaseRequest**](WTGiftCardPurchaseRequest.md)|  | 

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

