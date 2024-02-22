# wallet.PaymentDesignsApi

All URIs are relative to *https://api.wall.et*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_payment_design**](PaymentDesignsApi.md#archive_payment_design) | **DELETE** /v2/payment/design/{id} | Archive payment design
[**create_payment_design**](PaymentDesignsApi.md#create_payment_design) | **POST** /v2/payment/design | Create payment design
[**fetch_all_payment_designs**](PaymentDesignsApi.md#fetch_all_payment_designs) | **GET** /v2/payment/design/all | Fetch all active payment designs
[**fetch_payment_design_by_id**](PaymentDesignsApi.md#fetch_payment_design_by_id) | **GET** /v2/payment/design/{id} | Fetch payment design
[**restore_payment_design**](PaymentDesignsApi.md#restore_payment_design) | **PATCH** /v2/payment/design/{id} | Restore payment design
[**update_payment_design**](PaymentDesignsApi.md#update_payment_design) | **PUT** /v2/payment/design/{id} | Update payment design


# **archive_payment_design**
> WTPaymentDesign archive_payment_design(id)

Archive payment design

### Example


```python
import wallet
from wallet.models.wt_payment_design import WTPaymentDesign
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
    api_instance = wallet.PaymentDesignsApi(api_client)
    id = None # object | 

    try:
        # Archive payment design
        api_response = api_instance.archive_payment_design(id)
        print("The response of PaymentDesignsApi->archive_payment_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentDesignsApi->archive_payment_design: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**WTPaymentDesign**](WTPaymentDesign.md)

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

# **create_payment_design**
> WTPaymentDesign create_payment_design(wt_payment_design_create_params)

Create payment design

### Example


```python
import wallet
from wallet.models.wt_payment_design import WTPaymentDesign
from wallet.models.wt_payment_design_create_params import WTPaymentDesignCreateParams
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
    api_instance = wallet.PaymentDesignsApi(api_client)
    wt_payment_design_create_params = wallet.WTPaymentDesignCreateParams() # WTPaymentDesignCreateParams | 

    try:
        # Create payment design
        api_response = api_instance.create_payment_design(wt_payment_design_create_params)
        print("The response of PaymentDesignsApi->create_payment_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentDesignsApi->create_payment_design: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wt_payment_design_create_params** | [**WTPaymentDesignCreateParams**](WTPaymentDesignCreateParams.md)|  | 

### Return type

[**WTPaymentDesign**](WTPaymentDesign.md)

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

# **fetch_all_payment_designs**
> List[WTPaymentDesign] fetch_all_payment_designs(is_archive_included=is_archive_included)

Fetch all active payment designs

### Example


```python
import wallet
from wallet.models.wt_payment_design import WTPaymentDesign
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
    api_instance = wallet.PaymentDesignsApi(api_client)
    is_archive_included = True # bool |  (optional)

    try:
        # Fetch all active payment designs
        api_response = api_instance.fetch_all_payment_designs(is_archive_included=is_archive_included)
        print("The response of PaymentDesignsApi->fetch_all_payment_designs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentDesignsApi->fetch_all_payment_designs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archive_included** | **bool**|  | [optional] 

### Return type

[**List[WTPaymentDesign]**](WTPaymentDesign.md)

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

# **fetch_payment_design_by_id**
> WTPaymentDesign fetch_payment_design_by_id(id)

Fetch payment design

### Example


```python
import wallet
from wallet.models.wt_payment_design import WTPaymentDesign
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
    api_instance = wallet.PaymentDesignsApi(api_client)
    id = None # object | 

    try:
        # Fetch payment design
        api_response = api_instance.fetch_payment_design_by_id(id)
        print("The response of PaymentDesignsApi->fetch_payment_design_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentDesignsApi->fetch_payment_design_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**WTPaymentDesign**](WTPaymentDesign.md)

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

# **restore_payment_design**
> WTPaymentDesign restore_payment_design(id)

Restore payment design

### Example


```python
import wallet
from wallet.models.wt_payment_design import WTPaymentDesign
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
    api_instance = wallet.PaymentDesignsApi(api_client)
    id = None # object | 

    try:
        # Restore payment design
        api_response = api_instance.restore_payment_design(id)
        print("The response of PaymentDesignsApi->restore_payment_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentDesignsApi->restore_payment_design: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**WTPaymentDesign**](WTPaymentDesign.md)

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

# **update_payment_design**
> WTPaymentDesign update_payment_design(id, wt_payment_design_update_params)

Update payment design

### Example


```python
import wallet
from wallet.models.wt_payment_design import WTPaymentDesign
from wallet.models.wt_payment_design_update_params import WTPaymentDesignUpdateParams
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
    api_instance = wallet.PaymentDesignsApi(api_client)
    id = None # object | 
    wt_payment_design_update_params = wallet.WTPaymentDesignUpdateParams() # WTPaymentDesignUpdateParams | 

    try:
        # Update payment design
        api_response = api_instance.update_payment_design(id, wt_payment_design_update_params)
        print("The response of PaymentDesignsApi->update_payment_design:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentDesignsApi->update_payment_design: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **wt_payment_design_update_params** | [**WTPaymentDesignUpdateParams**](WTPaymentDesignUpdateParams.md)|  | 

### Return type

[**WTPaymentDesign**](WTPaymentDesign.md)

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

