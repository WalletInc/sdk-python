# wallet.PrizesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_advertisement_credit**](PrizesApi.md#archive_advertisement_credit) | **DELETE** /v2/payment/advertisementCredit/{id} | Archive Prize
[**create_advertisement_credit**](PrizesApi.md#create_advertisement_credit) | **POST** /v2/payment/advertisementCredit | Create Prize
[**create_prize_promotion**](PrizesApi.md#create_prize_promotion) | **POST** /v2/prizePromotions | Create a prize-game promotion Creates one instant-win promotion for the authenticated merchant. Guardrails enforced: purchase-independent trigger only, odds within (0,1], currency-valued prizes belonging to the merchant, total prize-pool value above $500 requires registration attestation, minimum age 18, and only one live promotion per game type.
[**fetch_advertisement_credit_by_id**](PrizesApi.md#fetch_advertisement_credit_by_id) | **GET** /v2/payment/advertisementCredit/{id} | Get Prize
[**fetch_advertisement_credit_scans**](PrizesApi.md#fetch_advertisement_credit_scans) | **GET** /v2/payment/advertisementCredit/scans/{id} | Get Prizes awarded
[**fetch_all_advertisement_credits**](PrizesApi.md#fetch_all_advertisement_credits) | **GET** /v2/payment/advertisementCredit/all | Get all Prizes
[**fetch_prize_promotions**](PrizesApi.md#fetch_prize_promotions) | **GET** /v2/prizePromotions/all | List the merchant&#39;s prize-game promotions
[**restore_advertisement_credit**](PrizesApi.md#restore_advertisement_credit) | **PATCH** /v2/payment/advertisementCredit/{id} | Restore Prize
[**update_advertisement_credit**](PrizesApi.md#update_advertisement_credit) | **PUT** /v2/payment/advertisementCredit/{id} | Update Prize
[**update_prize_promotion**](PrizesApi.md#update_prize_promotion) | **PUT** /v2/prizePromotions/{promotionID} | Update a prize-game promotion Deactivate a promotion or bring its end date forward.


# **archive_advertisement_credit**
> WTAdvertisementCredit archive_advertisement_credit(id)

Archive Prize

### Example


```python
import wallet
from wallet.models.wt_advertisement_credit import WTAdvertisementCredit
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
    api_instance = wallet.PrizesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive Prize
        api_response = api_instance.archive_advertisement_credit(id)
        print("The response of PrizesApi->archive_advertisement_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrizesApi->archive_advertisement_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTAdvertisementCredit**](WTAdvertisementCredit.md)

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

# **create_advertisement_credit**
> WTAdvertisementCredit create_advertisement_credit(wt_advertisement_credit_create_params)

Create Prize

### Example


```python
import wallet
from wallet.models.wt_advertisement_credit import WTAdvertisementCredit
from wallet.models.wt_advertisement_credit_create_params import WTAdvertisementCreditCreateParams
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
    api_instance = wallet.PrizesApi(api_client)
    wt_advertisement_credit_create_params = wallet.WTAdvertisementCreditCreateParams() # WTAdvertisementCreditCreateParams | 

    try:
        # Create Prize
        api_response = api_instance.create_advertisement_credit(wt_advertisement_credit_create_params)
        print("The response of PrizesApi->create_advertisement_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrizesApi->create_advertisement_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_advertisement_credit_create_params** | [**WTAdvertisementCreditCreateParams**](WTAdvertisementCreditCreateParams.md)|  | 

### Return type

[**WTAdvertisementCredit**](WTAdvertisementCredit.md)

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

# **create_prize_promotion**
> WTPrizePromotion create_prize_promotion(wt_prize_promotion_create_params)

Create a prize-game promotion Creates one instant-win promotion for the authenticated merchant. Guardrails enforced: purchase-independent trigger only, odds within (0,1], currency-valued prizes belonging to the merchant, total prize-pool value above $500 requires registration attestation, minimum age 18, and only one live promotion per game type.

### Example


```python
import wallet
from wallet.models.wt_prize_promotion import WTPrizePromotion
from wallet.models.wt_prize_promotion_create_params import WTPrizePromotionCreateParams
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
    api_instance = wallet.PrizesApi(api_client)
    wt_prize_promotion_create_params = wallet.WTPrizePromotionCreateParams() # WTPrizePromotionCreateParams | 

    try:
        # Create a prize-game promotion Creates one instant-win promotion for the authenticated merchant. Guardrails enforced: purchase-independent trigger only, odds within (0,1], currency-valued prizes belonging to the merchant, total prize-pool value above $500 requires registration attestation, minimum age 18, and only one live promotion per game type.
        api_response = api_instance.create_prize_promotion(wt_prize_promotion_create_params)
        print("The response of PrizesApi->create_prize_promotion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrizesApi->create_prize_promotion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_prize_promotion_create_params** | [**WTPrizePromotionCreateParams**](WTPrizePromotionCreateParams.md)|  | 

### Return type

[**WTPrizePromotion**](WTPrizePromotion.md)

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

# **fetch_advertisement_credit_by_id**
> WTAdvertisementCredit fetch_advertisement_credit_by_id(id)

Get Prize

### Example


```python
import wallet
from wallet.models.wt_advertisement_credit import WTAdvertisementCredit
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
    api_instance = wallet.PrizesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Prize
        api_response = api_instance.fetch_advertisement_credit_by_id(id)
        print("The response of PrizesApi->fetch_advertisement_credit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrizesApi->fetch_advertisement_credit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTAdvertisementCredit**](WTAdvertisementCredit.md)

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

# **fetch_advertisement_credit_scans**
> List[WTAdvertisementCreditScan] fetch_advertisement_credit_scans(id)

Get Prizes awarded

### Example


```python
import wallet
from wallet.models.wt_advertisement_credit_scan import WTAdvertisementCreditScan
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
    api_instance = wallet.PrizesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Prizes awarded
        api_response = api_instance.fetch_advertisement_credit_scans(id)
        print("The response of PrizesApi->fetch_advertisement_credit_scans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrizesApi->fetch_advertisement_credit_scans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[WTAdvertisementCreditScan]**](WTAdvertisementCreditScan.md)

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

# **fetch_all_advertisement_credits**
> List[WTAdvertisementCredit] fetch_all_advertisement_credits(is_archive_included=is_archive_included)

Get all Prizes

### Example


```python
import wallet
from wallet.models.wt_advertisement_credit import WTAdvertisementCredit
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
    api_instance = wallet.PrizesApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all Prizes
        api_response = api_instance.fetch_all_advertisement_credits(is_archive_included=is_archive_included)
        print("The response of PrizesApi->fetch_all_advertisement_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrizesApi->fetch_all_advertisement_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[WTAdvertisementCredit]**](WTAdvertisementCredit.md)

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

# **fetch_prize_promotions**
> List[WTPrizePromotion] fetch_prize_promotions()

List the merchant's prize-game promotions

### Example


```python
import wallet
from wallet.models.wt_prize_promotion import WTPrizePromotion
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
    api_instance = wallet.PrizesApi(api_client)

    try:
        # List the merchant's prize-game promotions
        api_response = api_instance.fetch_prize_promotions()
        print("The response of PrizesApi->fetch_prize_promotions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrizesApi->fetch_prize_promotions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[WTPrizePromotion]**](WTPrizePromotion.md)

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

# **restore_advertisement_credit**
> WTAdvertisementCredit restore_advertisement_credit(id)

Restore Prize

### Example


```python
import wallet
from wallet.models.wt_advertisement_credit import WTAdvertisementCredit
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
    api_instance = wallet.PrizesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore Prize
        api_response = api_instance.restore_advertisement_credit(id)
        print("The response of PrizesApi->restore_advertisement_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrizesApi->restore_advertisement_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WTAdvertisementCredit**](WTAdvertisementCredit.md)

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

# **update_advertisement_credit**
> WTAdvertisementCredit update_advertisement_credit(id, wt_advertisement_credit_update_params)

Update Prize

### Example


```python
import wallet
from wallet.models.wt_advertisement_credit import WTAdvertisementCredit
from wallet.models.wt_advertisement_credit_update_params import WTAdvertisementCreditUpdateParams
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
    api_instance = wallet.PrizesApi(api_client)
    id = 'id_example' # str | 
    wt_advertisement_credit_update_params = wallet.WTAdvertisementCreditUpdateParams() # WTAdvertisementCreditUpdateParams | 

    try:
        # Update Prize
        api_response = api_instance.update_advertisement_credit(id, wt_advertisement_credit_update_params)
        print("The response of PrizesApi->update_advertisement_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrizesApi->update_advertisement_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wt_advertisement_credit_update_params** | [**WTAdvertisementCreditUpdateParams**](WTAdvertisementCreditUpdateParams.md)|  | 

### Return type

[**WTAdvertisementCredit**](WTAdvertisementCredit.md)

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

# **update_prize_promotion**
> WTPrizePromotion update_prize_promotion(promotion_id, wt_prize_promotion_update_params)

Update a prize-game promotion Deactivate a promotion or bring its end date forward.

### Example


```python
import wallet
from wallet.models.wt_prize_promotion import WTPrizePromotion
from wallet.models.wt_prize_promotion_update_params import WTPrizePromotionUpdateParams
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
    api_instance = wallet.PrizesApi(api_client)
    promotion_id = 'promotion_id_example' # str | 
    wt_prize_promotion_update_params = wallet.WTPrizePromotionUpdateParams() # WTPrizePromotionUpdateParams | 

    try:
        # Update a prize-game promotion Deactivate a promotion or bring its end date forward.
        api_response = api_instance.update_prize_promotion(promotion_id, wt_prize_promotion_update_params)
        print("The response of PrizesApi->update_prize_promotion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrizesApi->update_prize_promotion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_id** | **str**|  | 
 **wt_prize_promotion_update_params** | [**WTPrizePromotionUpdateParams**](WTPrizePromotionUpdateParams.md)|  | 

### Return type

[**WTPrizePromotion**](WTPrizePromotion.md)

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

