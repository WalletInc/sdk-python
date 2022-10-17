# wallet.AdvertisementCreditsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_advertisement_credit**](AdvertisementCreditsApi.md#archive_advertisement_credit) | **DELETE** /v2/payment/advertisementCredit/{id} | Archive ad credit
[**create_advertisement_credit**](AdvertisementCreditsApi.md#create_advertisement_credit) | **POST** /v2/payment/advertisementCredit | Create ad credit
[**fetch_advertisement_credit_by_id**](AdvertisementCreditsApi.md#fetch_advertisement_credit_by_id) | **GET** /v2/payment/advertisementCredit/{id} | Fetch ad credit
[**fetch_advertisement_credit_scans**](AdvertisementCreditsApi.md#fetch_advertisement_credit_scans) | **GET** /v2/payment/advertisementCredit/scans/{id} | Fetch scans
[**fetch_all_advertisement_credits**](AdvertisementCreditsApi.md#fetch_all_advertisement_credits) | **GET** /v2/payment/advertisementCredit/all | Fetch all active ad credits
[**restore_advertisement_credit**](AdvertisementCreditsApi.md#restore_advertisement_credit) | **PATCH** /v2/payment/advertisementCredit/{id} | Restore ad credit
[**update_advertisement_credit**](AdvertisementCreditsApi.md#update_advertisement_credit) | **PUT** /v2/payment/advertisementCredit/{id} | Update ad credit


# **archive_advertisement_credit**
> WTAdvertisementCredit archive_advertisement_credit(id)

Archive ad credit

### Example


```python
import time
import wallet
from wallet.api import advertisement_credits_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_advertisement_credit import WTAdvertisementCredit
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
    api_instance = advertisement_credits_api.AdvertisementCreditsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Archive ad credit
        api_response = api_instance.archive_advertisement_credit(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling AdvertisementCreditsApi->archive_advertisement_credit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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

Create ad credit

### Example


```python
import time
import wallet
from wallet.api import advertisement_credits_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.merchant_not_initialized import MerchantNotInitialized
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_advertisement_credit import WTAdvertisementCredit
from wallet.model.auth_error import AuthError
from wallet.model.wt_advertisement_credit_create_params import WTAdvertisementCreditCreateParams
from wallet.model.duplicate_row_found import DuplicateRowFound
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = advertisement_credits_api.AdvertisementCreditsApi(api_client)
    wt_advertisement_credit_create_params = WTAdvertisementCreditCreateParams(
        title="Ad Credit Title",
        value_type=None,
        payment_design_id=NanoID("C"),
        max_uses=250,
        discount_value=250,
    ) # WTAdvertisementCreditCreateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Create ad credit
        api_response = api_instance.create_advertisement_credit(wt_advertisement_credit_create_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling AdvertisementCreditsApi->create_advertisement_credit: %s\n" % e)
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

# **fetch_advertisement_credit_by_id**
> WTAdvertisementCredit fetch_advertisement_credit_by_id(id)

Fetch ad credit

### Example


```python
import time
import wallet
from wallet.api import advertisement_credits_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_advertisement_credit import WTAdvertisementCredit
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
    api_instance = advertisement_credits_api.AdvertisementCreditsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch ad credit
        api_response = api_instance.fetch_advertisement_credit_by_id(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling AdvertisementCreditsApi->fetch_advertisement_credit_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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
> [WTAdvertisementCreditScan] fetch_advertisement_credit_scans(id)

Fetch scans

### Example


```python
import time
import wallet
from wallet.api import advertisement_credits_api
from wallet.model.wt_advertisement_credit_scan import WTAdvertisementCreditScan
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
    api_instance = advertisement_credits_api.AdvertisementCreditsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch scans
        api_response = api_instance.fetch_advertisement_credit_scans(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling AdvertisementCreditsApi->fetch_advertisement_credit_scans: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

[**[WTAdvertisementCreditScan]**](WTAdvertisementCreditScan.md)

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
> [WTAdvertisementCredit] fetch_all_advertisement_credits()

Fetch all active ad credits

### Example


```python
import time
import wallet
from wallet.api import advertisement_credits_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_advertisement_credit import WTAdvertisementCredit
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
    api_instance = advertisement_credits_api.AdvertisementCreditsApi(api_client)
    is_archive_included = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch all active ad credits
        api_response = api_instance.fetch_all_advertisement_credits(is_archive_included=is_archive_included)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling AdvertisementCreditsApi->fetch_all_advertisement_credits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional]

### Return type

[**[WTAdvertisementCredit]**](WTAdvertisementCredit.md)

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

Restore ad credit

### Example


```python
import time
import wallet
from wallet.api import advertisement_credits_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_advertisement_credit import WTAdvertisementCredit
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
    api_instance = advertisement_credits_api.AdvertisementCreditsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        # Restore ad credit
        api_response = api_instance.restore_advertisement_credit(id)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling AdvertisementCreditsApi->restore_advertisement_credit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

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

Update ad credit

### Example


```python
import time
import wallet
from wallet.api import advertisement_credits_api
from wallet.model.internal_server_error import InternalServerError
from wallet.model.falsum_error import FalsumError
from wallet.model.wt_advertisement_credit import WTAdvertisementCredit
from wallet.model.wt_advertisement_credit_update_params import WTAdvertisementCreditUpdateParams
from wallet.model.foreign_key_does_not_exist import ForeignKeyDoesNotExist
from wallet.model.auth_error import AuthError
from wallet.model.duplicate_row_found import DuplicateRowFound
from pprint import pprint
# Defining the host is optional and defaults to https://api.wall.et
# See configuration.py for a list of all supported configuration parameters.
configuration = wallet.Configuration(
    host = "https://api.wall.et"
)


# Enter a context with an instance of the API client
with wallet.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = advertisement_credits_api.AdvertisementCreditsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | 
    wt_advertisement_credit_update_params = WTAdvertisementCreditUpdateParams(
        title="Ad Credit Title",
        value_type=None,
        payment_design_id=NanoID("C"),
        max_uses=250,
        discount_value=250,
    ) # WTAdvertisementCreditUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        # Update ad credit
        api_response = api_instance.update_advertisement_credit(id, wt_advertisement_credit_update_params)
        pprint(api_response)
    except wallet.ApiException as e:
        print("Exception when calling AdvertisementCreditsApi->update_advertisement_credit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
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

