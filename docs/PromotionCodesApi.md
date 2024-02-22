# wallet.PromotionCodesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_promo_code**](PromotionCodesApi.md#archive_promo_code) | **DELETE** /v2/promoCodes/{id} | Archive promo code
[**create_promo_code**](PromotionCodesApi.md#create_promo_code) | **POST** /v2/promoCodes | Create promo code
[**fetch_all_promo_codes**](PromotionCodesApi.md#fetch_all_promo_codes) | **GET** /v2/promoCodes/all | Fetch all promo codes
[**restore_promo_code**](PromotionCodesApi.md#restore_promo_code) | **PATCH** /v2/promoCodes/{id} | Restore promo code
[**update_promo_code**](PromotionCodesApi.md#update_promo_code) | **PUT** /v2/promoCodes/{id} | Update promo code


# **archive_promo_code**
> PromoCode archive_promo_code(id)

Archive promo code

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
    id = None # object | 

    try:
        # Archive promo code
        api_response = api_instance.archive_promo_code(id)
        print("The response of PromotionCodesApi->archive_promo_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCodesApi->archive_promo_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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

Create promo code

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
        # Create promo code
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

Fetch all promo codes

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
        # Fetch all promo codes
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

Restore promo code

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
    id = None # object | 

    try:
        # Restore promo code
        api_response = api_instance.restore_promo_code(id)
        print("The response of PromotionCodesApi->restore_promo_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCodesApi->restore_promo_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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

Update promo code

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
    id = None # object | 
    wt_promo_code_update_params = wallet.WTPromoCodeUpdateParams() # WTPromoCodeUpdateParams | 

    try:
        # Update promo code
        api_response = api_instance.update_promo_code(id, wt_promo_code_update_params)
        print("The response of PromotionCodesApi->update_promo_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionCodesApi->update_promo_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
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

