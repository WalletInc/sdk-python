# wallet.PrizesApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_advertisement_credit**](PrizesApi.md#archive_advertisement_credit) | **DELETE** /v2/payment/advertisementCredit/{id} | Archive Prize
[**create_advertisement_credit**](PrizesApi.md#create_advertisement_credit) | **POST** /v2/payment/advertisementCredit | Create Prize
[**fetch_advertisement_credit_by_id**](PrizesApi.md#fetch_advertisement_credit_by_id) | **GET** /v2/payment/advertisementCredit/{id} | Get Prize
[**fetch_advertisement_credit_scans**](PrizesApi.md#fetch_advertisement_credit_scans) | **GET** /v2/payment/advertisementCredit/scans/{id} | Get Prizes awarded
[**fetch_all_advertisement_credits**](PrizesApi.md#fetch_all_advertisement_credits) | **GET** /v2/payment/advertisementCredit/all | Get all Prizes
[**restore_advertisement_credit**](PrizesApi.md#restore_advertisement_credit) | **PATCH** /v2/payment/advertisementCredit/{id} | Restore Prize
[**update_advertisement_credit**](PrizesApi.md#update_advertisement_credit) | **PUT** /v2/payment/advertisementCredit/{id} | Update Prize


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

