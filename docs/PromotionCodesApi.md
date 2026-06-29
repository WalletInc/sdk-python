# wallet.PromotionCodesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_promo_code**](PromotionCodesApi.md#archive_promo_code) | **DELETE** /v2/promoCodes/{id} | Archive Promotion Code
[**create_promo_code**](PromotionCodesApi.md#create_promo_code) | **POST** /v2/promoCodes | Create Promotion Code
[**fetch_all_promo_codes**](PromotionCodesApi.md#fetch_all_promo_codes) | **GET** /v2/promoCodes/all | Get all Promotion Codes
[**restore_promo_code**](PromotionCodesApi.md#restore_promo_code) | **PATCH** /v2/promoCodes/{id} | Restore Promotion Code
[**update_promo_code**](PromotionCodesApi.md#update_promo_code) | **PUT** /v2/promoCodes/{id} | Update Promotion Code


# **archive_promo_code**
> PromoCode archive_promo_code(id)

Archive Promotion Code

### Example


```python
import wallet
from wallet.models.promo_code import PromoCode
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
    api_instance = wallet.PromotionCodesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive Promotion Code
        api_response = api_instance.archive_promo_code(id)
        print("The response of PromotionCodesApi->archive_promo_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCodesApi->archive_promo_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PromoCode**](PromoCode.md)

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

# **create_promo_code**
> PromoCode create_promo_code(wt_promo_code_create_params)

Create Promotion Code

### Example


```python
import wallet
from wallet.models.promo_code import PromoCode
from wallet.models.wt_promo_code_create_params import WTPromoCodeCreateParams
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
    api_instance = wallet.PromotionCodesApi(api_client)
    wt_promo_code_create_params = wallet.WTPromoCodeCreateParams() # WTPromoCodeCreateParams | 

    try:
        # Create Promotion Code
        api_response = api_instance.create_promo_code(wt_promo_code_create_params)
        print("The response of PromotionCodesApi->create_promo_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCodesApi->create_promo_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_promo_code_create_params** | [**WTPromoCodeCreateParams**](WTPromoCodeCreateParams.md)|  | 

### Return type

[**PromoCode**](PromoCode.md)

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

# **fetch_all_promo_codes**
> object fetch_all_promo_codes(is_archive_included=is_archive_included)

Get all Promotion Codes

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
    api_instance = wallet.PromotionCodesApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Get all Promotion Codes
        api_response = api_instance.fetch_all_promo_codes(is_archive_included=is_archive_included)
        print("The response of PromotionCodesApi->fetch_all_promo_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCodesApi->fetch_all_promo_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

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

# **restore_promo_code**
> PromoCode restore_promo_code(id)

Restore Promotion Code

### Example


```python
import wallet
from wallet.models.promo_code import PromoCode
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
    api_instance = wallet.PromotionCodesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Restore Promotion Code
        api_response = api_instance.restore_promo_code(id)
        print("The response of PromotionCodesApi->restore_promo_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCodesApi->restore_promo_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PromoCode**](PromoCode.md)

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

# **update_promo_code**
> PromoCode update_promo_code(id, wt_promo_code_update_params)

Update Promotion Code

### Example


```python
import wallet
from wallet.models.promo_code import PromoCode
from wallet.models.wt_promo_code_update_params import WTPromoCodeUpdateParams
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
    api_instance = wallet.PromotionCodesApi(api_client)
    id = 'id_example' # str | 
    wt_promo_code_update_params = wallet.WTPromoCodeUpdateParams() # WTPromoCodeUpdateParams | 

    try:
        # Update Promotion Code
        api_response = api_instance.update_promo_code(id, wt_promo_code_update_params)
        print("The response of PromotionCodesApi->update_promo_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCodesApi->update_promo_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wt_promo_code_update_params** | [**WTPromoCodeUpdateParams**](WTPromoCodeUpdateParams.md)|  | 

### Return type

[**PromoCode**](PromoCode.md)

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

