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
    api_instance = wallet.AdvertisementCreditsApi(api_client)
    id = None # object | 

    try:
        # Archive ad credit
        api_response = api_instance.archive_advertisement_credit(id)
        print("The response of AdvertisementCreditsApi->archive_advertisement_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvertisementCreditsApi->archive_advertisement_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
    api_instance = wallet.AdvertisementCreditsApi(api_client)
    wt_advertisement_credit_create_params = wallet.WTAdvertisementCreditCreateParams() # WTAdvertisementCreditCreateParams | 

    try:
        # Create ad credit
        api_response = api_instance.create_advertisement_credit(wt_advertisement_credit_create_params)
        print("The response of AdvertisementCreditsApi->create_advertisement_credit:\n")
        pprint(api_response)
    except Exception as e:
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
    api_instance = wallet.AdvertisementCreditsApi(api_client)
    id = None # object | 

    try:
        # Fetch ad credit
        api_response = api_instance.fetch_advertisement_credit_by_id(id)
        print("The response of AdvertisementCreditsApi->fetch_advertisement_credit_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvertisementCreditsApi->fetch_advertisement_credit_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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

Fetch scans

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
    api_instance = wallet.AdvertisementCreditsApi(api_client)
    id = None # object | 

    try:
        # Fetch scans
        api_response = api_instance.fetch_advertisement_credit_scans(id)
        print("The response of AdvertisementCreditsApi->fetch_advertisement_credit_scans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvertisementCreditsApi->fetch_advertisement_credit_scans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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

Fetch all active ad credits

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
    api_instance = wallet.AdvertisementCreditsApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all active ad credits
        api_response = api_instance.fetch_all_advertisement_credits(is_archive_included=is_archive_included)
        print("The response of AdvertisementCreditsApi->fetch_all_advertisement_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvertisementCreditsApi->fetch_all_advertisement_credits: %s\n" % e)
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

# **restore_advertisement_credit**
> WTAdvertisementCredit restore_advertisement_credit(id)

Restore ad credit

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
    api_instance = wallet.AdvertisementCreditsApi(api_client)
    id = None # object | 

    try:
        # Restore ad credit
        api_response = api_instance.restore_advertisement_credit(id)
        print("The response of AdvertisementCreditsApi->restore_advertisement_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvertisementCreditsApi->restore_advertisement_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

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
    api_instance = wallet.AdvertisementCreditsApi(api_client)
    id = None # object | 
    wt_advertisement_credit_update_params = wallet.WTAdvertisementCreditUpdateParams() # WTAdvertisementCreditUpdateParams | 

    try:
        # Update ad credit
        api_response = api_instance.update_advertisement_credit(id, wt_advertisement_credit_update_params)
        print("The response of AdvertisementCreditsApi->update_advertisement_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvertisementCreditsApi->update_advertisement_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
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

