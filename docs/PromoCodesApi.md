# wallet.PromoCodesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_promo_code**](PromoCodesApi.md#archive_promo_code) | **DELETE** /v2/promoCodes/{id} | Archive promo code
[**create_promo_code**](PromoCodesApi.md#create_promo_code) | **POST** /v2/promoCodes | Create promo code
[**fetch_all_promo_codes**](PromoCodesApi.md#fetch_all_promo_codes) | **GET** /v2/promoCodes/all | Fetch all promo codes
[**restore_promo_code**](PromoCodesApi.md#restore_promo_code) | **PATCH** /v2/promoCodes/{id} | Restore promo code
[**update_promo_code**](PromoCodesApi.md#update_promo_code) | **PUT** /v2/promoCodes/{id} | Update promo code


# **archive_promo_code**
> PromoCode archive_promo_code(id)

Archive promo code

### Example


```python
import time
import wallet
from wallet.api import promo_codes_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.promo_code import PromoCode
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
    api_instance = promo_codes_api.PromoCodesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive promo code
        api_response = api_instance.archive_promo_code(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PromoCodesApi->archive_promo_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import promo_codes_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.promo_code import PromoCode
from wallet.model.auth_error import AuthError
from wallet.model.wt_promo_code_create_params import WTPromoCodeCreateParams
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = promo_codes_api.PromoCodesApi(api_client)
    wt_promo_code_create_params = WTPromoCodeCreateParams(
        title="This is the title of the promo code",
        description="This is the description of the promo code",
        promo_code="XMAS20",
        display_value="20% Off!",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.png",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expiration_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # WTPromoCodeCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create promo code
        api_response = api_instance.create_promo_code(wt_promo_code_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PromoCodesApi->create_promo_code: %s\n" % e)
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
> bool, date, datetime, dict, float, int, list, str, none_type fetch_all_promo_codes()

Fetch all promo codes

### Example


```python
import time
import wallet
from wallet.api import promo_codes_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
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
    api_instance = promo_codes_api.PromoCodesApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all promo codes
        api_response = api_instance.fetch_all_promo_codes(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PromoCodesApi->fetch_all_promo_codes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

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
**401** | Authentication Failed |  -  |
**422** | Validation Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_promo_code**
> PromoCode restore_promo_code(id)

Restore promo code

### Example


```python
import time
import wallet
from wallet.api import promo_codes_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.promo_code import PromoCode
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
    api_instance = promo_codes_api.PromoCodesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore promo code
        api_response = api_instance.restore_promo_code(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PromoCodesApi->restore_promo_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
import time
import wallet
from wallet.api import promo_codes_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.promo_code import PromoCode
from wallet.model.auth_error import AuthError
from wallet.model.wt_promo_code_update_params import WTPromoCodeUpdateParams
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = promo_codes_api.PromoCodesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_promo_code_update_params = WTPromoCodeUpdateParams(
        title="This is the title of the promo code",
        description="This is the description of the promo code",
        promo_code="XMAS20",
        display_value="20% Off!",
        order_number=1,
        media_url="https://wall.et/media/H847Sjudbw.png",
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expiration_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # WTPromoCodeUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update promo code
        api_response = api_instance.update_promo_code(id, wt_promo_code_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling PromoCodesApi->update_promo_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

